import os
from datetime import datetime
from zipfile import ZipFile


def zipdir(path, zip):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip.write(os.path.join(root, file))


if __name__ == '__main__':
    # set file name and time of creation
    today = datetime.now()
    dir_name = os.environ.get('TEMP', None)  # update path
    print 'dir_name', dir_name
    file_name = dir_name + os.sep + 'zipper_' + today.strftime('%Y.%m.%d_h%H%M') + '.zip'
    print 'file_name', file_name

    # Zipping work
    zipfile = ZipFile(file_name, 'w')
    zipdir(dir_name, zipfile)
    zipfile.close()
