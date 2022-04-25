import pyodbc
from pandas import cut

con = pyodbc.connect("DRIVER={SQL Server};server=localhost;database=hr1;uid=sa;pwd=sa")
cur = con.cursor()
cur.execute("select emp_code, emp_name, sum(gross_pas) gross_pay from employee_master")
for row in cur:
    print(row.emp_code + "," + row.emp_name)
    # print(row[0] + "," + row[1])

cur.close()
con.close()
