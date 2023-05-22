## File Types

    1) Binary files (files with some encoding)
        Document files: .pdf, .doc, .xls etc.
        Image files: .png, .jpg, .gif, .bmp etc.
        Video files: .mp4, .3gp, .mkv, .avi etc.
        Audio files: .mp3, .wav, .mka, .aac etc.
        Database files: .mdb, .accde, .frm, .sqlite etc.
        Archive files: .zip, .rar, .iso, .7z etc.
        Executable files: .exe, .dll, .class etc.

    2) Text files (files without encoding)
        Web standards: html, XML, CSS, JSON etc.
        Source code: c, app, js, py, java etc.
        Documents: txt, tex, RTF etc.
        Tabular data: csv, tsv etc.
        Configuration: ini, cfg, reg etc.

## File Operations

    Open
    Read
    Write
    Close

    Rename
    Delete

## File operation Modes

    'r' – Read Mode:            Read mode is used only to read data from the file.
    'w' – Write Mode:           This mode is used when you want to write data into the file or modify it.
                                Remember write mode overwrites the data present in the file.
    'a' – Append Mode:          Append mode is used to append data to the file.
                                Remember data will be appended at the end of the file pointer.
    'r+' – Read or Write Mode:  This mode is used when we want to write or read the data from the same file.
    'a+' – Append or Read Mode: This mode is used when we want to read data from the file or append the data into the same file.

same file modes, when working with binary files

    'wb' – Open a file for write only mode in the binary format.
    'rb' – Open a file for the read-only mode in the binary format.
    'ab' – Open a file for appending only mode in the binary format.
    'rb+' – Open a file for read and write only mode in the binary format.
    'ab+' – Open a file for appending and read-only mode in the binary format.

## Encoding in Files

Different machines have different encoding format as shown below.

    Microsoft Windows OS uses 'cp1252' encoding format by default.
    Linux or Unix OS uses 'utf-8' encoding format by default.
    Apple's MAC OS uses 'utf-8' or 'utf-16' encoding format by default.

## Python File Methods

    Function	Explanation
    --------------------------------------------------------------------------
    open()	        To open a file
    close()	        Close an open file
    fileno()	    Returns an integer number of the file
    read(n)	        Reads ‘n’ characters from the file till end of the file
    readable()	    Returns true if the file is readable
    readline()	    Read and return one line from the file
    readlines()	    Reads and returns all the lines from the file
    seek(offset)	Change the cursor position by bytes as specified by the offset
    seekable()	    Returns true if the file supports random access
    tell()	        Returns the current file location
    writable()	    Returns true if the file is writable
    write()	        Writes a string of data to the file
    writelines()	Writes a list of data to the file
    --------------------------------------------------------------------------


    Cursor Positioning Methods
    	seek() method in Python is used to change the cursor to a specific position.
    	tell() method in Python prints the current position of our cursor.


    Truncating a File
    	- to truncate a file to a given size
    	file = open('myfile.txt', 'w')
    	file.truncate(20)
    	file.close()
