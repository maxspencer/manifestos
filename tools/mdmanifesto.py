import argparse
import sys
import subprocess
import tempfile

import refiner.input.pdftohtml
import refiner.core
import refiner.columns


def pdftohtml_parse(pdf_path):
    '''Run pdftohtml on an input PDF document and parse the output.

    Returns a refiner.input.InputDocument instance.

    '''
    try:
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.xml') as xml_file:
            args = ['pdftohtml', '-xml', pdf_path, xml_file.name]
            subprocess.check_call(args, stdout=subprocess.DEVNULL)
            xml = xml_file.read()
        return refiner.input.pdftohtml.parse(xml)
    except subprocess.CalledProcessError:
        sys.stderr.write('An error occurred whilst running pdftohtml\n')
        raise SystemExit
    except FileNotFoundError:
        sys.stderr.write('Could not find pdftohtml command\n')
        raise SystemExit


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pdf', help='source PDF document')
    parser.add_argument(
        '-r', '--roi', type=float, nargs=4,
        help='region of interest (expressed as proportions of page width and height)'
    )
    parser.add_argument(
        '-i', '--ignore', help='comma-separated list of pages to ignore the contents of'
    )
    parser.add_argument(
        '-s', '--max-line-sep', type=float,
        default=refiner.core.DEFAULT_MAX_LINE_SEP,
        help='max. separation allowed between lines of same paragraph (expressed as a proportion of line height'
    )
    parser.add_argument(
        '-c', '--min-column-width', type=float,
        default=refiner.columns.DEFAULT_SMALLEST_COL,
        help='min. column width (expressed as a proportion of the text width)'
    )
    args = parser.parse_args()

    # Additional processing of arguments
    if args.ignore:
        ignore = [int(n) for n in args.ignore.split(',')]
    else:
        ignore = []

    # Processing:
    input_document = pdftohtml_parse(args.pdf)
    refined_document = refiner.core.refine(
        input_document,
        roi=args.roi,
        ignore=ignore, # Using ignore not args.ignore directly here
        max_line_sep=args.max_line_sep,
        smallest_col=args.min_column_width
    )
    for page in refined_document.page_list:
        print('<span class="page" id="page-{}">\n'.format(page.number))
        #to_print = []
        for content in page.contents:
            try:
                print('{} {}'.format('#' * content.level, content.string))
            except AttributeError:
                # Not a heading
                print(content.string)
            print()
        print('</span>')
    

