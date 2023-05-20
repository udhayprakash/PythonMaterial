## compiling python files

### To create .pyc/**pycache** files,

    - In command line,

        python -m python_script
        Ex: python -m fibScript

    - In python code,


        import py_compile
        py_compile.compile('fibScript.py')

### To decompile compiled pyc/pyo files to see original code,

    - Installation:

        pip install uncompyle6

    - USAGE:

        uncompyle6 -o . <file-name.pyc>

    - ex:

        uncompyl6 -o . txfile.pyc rxfile.pyc

    - Instead of saving as py file, if you want to see in terminal,

        uncompyle6 <filename.pyc>

## How to profile startup time

    -X importtime: Python’s import profiler

    Python 3.7 introduced the -X importtime option, a specialized profiler that times all imports.
    It prints a table to stderr, summarizing microsecond timing information for each imported module:

    $ python -X importtime -c 'import django'
