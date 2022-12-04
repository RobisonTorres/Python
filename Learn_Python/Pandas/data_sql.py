import pypyodbc as odbc
import pandas as pd
print('Working with SQL data.')
print()

conn = odbc.connect(

    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-KPEHRJT\SQLEXPRESS;"
    "Database=Northwind;"
    "Trusted_Connection=yes;"
    "uid=Robison Torres;"
)

my_cursor = conn.cursor()
my_cursor.execute('Select * From Products;')

my_result = my_cursor.fetchall()
# print(my_result)

# for x in my_result:  To show all the info.
#     print(x)

my_data_sql = pd.DataFrame(my_result)
print(my_data_sql.to_string())
print(my_data_sql.describe())

