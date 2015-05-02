# Manifestos

A Git repository containing UK party political manifestos in open data formats.

## Progress (2015 manifestos)

Manifesto    | Source | Markdown | Images
-------------|--------|----------|-------
conservative | ✓ |  | 
green        | ✓ |  | 
labour       | ✓ | ✓ | ✓
libdem       | ✓ |  | 
plaid        | ✓ |  | 
snp          | ✓ |  | 
ukip         | ✓ |  | 

## About this fork

In March 2015 I started working on a project to automatically convert PDF
manifesto documents into more open data formats and to make them available for
reading, searching and linking-to in a single place, with particular focus on
the 2015 UK general election. I've got some of the way there with
[manifestos.org.uk](http://manifestos.org.uk), but the amount of variety in
source documents has made fully-automated parsing and conversion very difficult.

I recently heard about [Sym Roe's](https://github.com/symroe)
[DemocracyClub/manifestos](https://github.com/DemocracyClub/manifestos)
repository and decided that it offered a great solution: Use a Github repo as an
extra level of indirection. This repo will contain the original PDFs and open
format versions of the manifesto documents and the transformation from the
former to the latter can be collaborative and open in its own right.

While the original repo contained the source of a django web app with similar
functions to [manifestos.org.uk](http://manifestos.org.uk), this repo just
contains the manifesto documents. I think this de-coupling is useful and will
hopefully encourage the development of other apps which make use of this
dataset.

## Contact

[@maxspencer](https://twitter.com/maxspencer)