#!usr/bin/env python
# Similarly, UNZIPPING A ZIP FILE
import zipfile


def unzip(zip_file, outdir):
    """
    Unzip a given 'zip_file' into the output directory 'outdir'.
    """
    zf = zipfile.ZipFile(zip_file, "r")
    zf.extractall(outdir)
