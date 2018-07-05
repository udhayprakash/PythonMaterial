with open('mydata.csv', 'rb') as file_handler:
    csv_file_data = file_handler.read()
    print 'Content in the csv file:'
    print csv_file_data
        
    file_handler.close()