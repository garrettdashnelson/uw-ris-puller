uw-ris-puller
=============

This is a simple Python script that allows you to generate a RIS citation file for every item you currently have checked out from the UW-Madison libraries, for use in citations manager like Papers, BibTeX, or Zotero. Currently this is not a native feature in the library catalog.

## Usage

*  Using any web browser, log in to your library account and navigate to your list of charged items. Save the source of this file as `charged.html` in the script directory.
*  Execute `python puller.py` and you should get a sequence of RIS files dumped out to your script directory.

## Limitations and future improvements

*  The script will pull items which you currently have requested in addition to those already charged
*  The library system's RIS files are not always very clean. Many are missing the PY (published year) field.
*  For citation-management purposes, it may be useful to strip the authors' DOB from the RIS files.