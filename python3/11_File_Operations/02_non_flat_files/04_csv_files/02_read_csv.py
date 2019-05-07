
with open('mydata.csv', 'r') as file_handler:
    csv_file_data = file_handler.readlines()
    print('Content in the csv file:')
    print(csv_file_data)

    print() 
    employee_names = []
    for eachLine in csv_file_data[1:]:
        # print eachLine, type(eachLine)
        # print eachLine.split(',')
        print(eachLine.split(',')[0])
        employee_names.append(eachLine.split(',')[0])
    
    print('Employee names:', employee_names)
    file_handler.close()