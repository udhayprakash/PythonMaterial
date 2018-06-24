with open('mydata.csv', 'wb') as fh:
    # csv header
    fh.write('Name, position, location\n')
    # csv body 
    fh.write('Madhavi,Sr. developer,texas\n')
    fh.write('udhay,developer,hyderabad\n')
    fh.write('prakash,Architect,ontario\n')
    fh.close()