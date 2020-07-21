To create .pyc/__pycache__ files, 
    In command line,
          python -m python_script
      Ex: python -m fibScript

In python code, 
    import py_compile
    py_compile.compile('fibScript.py')   


To decompile compiled pyc/pyo files to see original code, 
    Installation:
        pip install uncompyle6
    
    USAGE:
        uncompyle6 -o . <file-name.pyc> 
    ex:
        uncompyl6 -o . txfile.pyc rxfile.pyc

    Instead of saving as py file, if you want to see in terminal,
         uncompyle6 <filename.pyc>