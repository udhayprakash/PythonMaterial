import csv

with open('names.csv', 'wt', newline='') as csvfile:
    # csv header
    header_names = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, 
                      fieldnames=header_names)
    writer.writeheader()

    # csv body
    writer.writerow({'first_name': 'udhay', 
                     'last_name': 'prakash'})
    writer.writerow({'first_name': 'Madhavi', 
                    'last_name': 'm'})
    writer.writerow({'first_name': 'john', 
                    'last_name': 'hasten'})

    csvfile.close()
