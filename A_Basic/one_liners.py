"""
TO start a local http server,
    # Python 2
    python -m SimpleHTTPServer 8080

    # Python 3
    python -m http.server 8080

To pretty print a json from terminal quickly, 
    cat file.json | python -m json.tool

To profile a python script,
    python -m cProfile my_script.py

To convert csv to json quickly,
    python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
"""
