import subprocess
import argparse
import os
import os.path


def pdftk_burst(source_path, output_dir):
    '''Uses pdftk to split the pages of the source PDF document.'''
    # Remove the rightmost extension from the source file name
    source_name_no_ext = os.path.basename(source_path).rsplit('.', 1)[0]
    output_name_template = source_name_no_ext + '-page-%d.pdf'
    try:
        subprocess.check_call(
            [
                'pdftk', source_path, 'burst',
                'output', os.path.join(output_dir, output_name_template)
            ]
        )
    except subprocess.CalledProcessError as e:
        self.stderr.write('An error occurred whilst running pdftk\n')
        raise SystemExit
    except FileNotFoundError:
        self.stderr.write('Could not find pdftk command\n')
        raise SystemExit


def mogrify(target_files, width=None, density=300, format='png'):
    '''Use ImageMagick's mogrify to resize and convert images.'''
    args = [
        'mogrify',
        '-background', 'white',
        '-alpha', 'Remove',
        '+antialias',
        '-density', str(density),
        '-format', format
    ]

    if width is not None:
        args += ['-resize', str(width)]

    args += ['--', target_files]

    try:
        subprocess.check_call(args)
    except subprocess.CalledProcessError as e:
        sys.stderr.write('An error occurred whilst running mogrify\n')
        raise SystemExit
    except FileNotFoundError:
        sys.stderr.write('Could not find mogrify command')
        raise SystemExit


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='split the pages of a PDF and render them as PNGs')
    parser.add_argument(
        'source',
        help='source PDF document')
    parser.add_argument(
        'width', type=int,
        help='list of widths of output PNGs to produce'
    )
    parser.add_argument(
        '-o', '--output-directory', metavar='PATH', default='./pages',
        help='output directory, default is ./pages'
    )
    args = parser.parse_args()

    # Ensure that source exists
    if not os.path.isfile(args.source):
        self.stderr.write(args.source + ' does not exist or is not a file')
        raise SystemExit

    # Ensure output directory exists
    os.makedirs(args.output_directory, exist_ok=True)

    # Split into separate PDFs
    pdftk_burst(args.source, args.output_directory)

    # Convert them to PNGs
    targets = os.path.join(args.output_directory, '*.pdf')
    mogrify(targets, width=args.width)
