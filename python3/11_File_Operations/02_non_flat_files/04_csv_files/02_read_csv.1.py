
with open('sampleCSVFile.csv', 'r') as file_handler:
    csv_file_data = file_handler.read()
    print('Content in the csv file:\n',csv_file_data)

    for each_line in csv_file_data.split('\n')[1:]:
        print(each_line.split(',')[0])
    file_handler.close()