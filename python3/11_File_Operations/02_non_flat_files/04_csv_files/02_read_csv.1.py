
with open('sampleCSVFile.csv', 'r') as file_handler:
    csv_file_data = file_handler.read()
    print(('Content in the csv file:\n',csv_file_data))
    file_handler.close()