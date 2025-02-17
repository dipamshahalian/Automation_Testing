import mysql.connector

# Establish connection
con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="Dipam@223133",
    database="mydb"
)

curs = con.cursor()

# Insert data using executemany
# insert_query = """
# INSERT INTO student (first_name, last_name, email, dob, gender, enrollment_date)
# VALUES (%s, %s, %s, %s, %s, NOW())
# """
#
# data = [
#     ('Lewis', 'Hamilton', 'lewis.hamilton@f1.com', '1985-01-07', 'Male'),
#     ('Max', 'Verstappen', 'max.verstappen@f1.com', '1997-09-30', 'Male'),
#     ('Charles', 'Leclerc', 'charles.leclerc@f1.com', '1997-10-16', 'Male'),
#     ('Lando', 'Norris', 'lando.norris@f1.com', '1999-11-13', 'Male'),
#     ('Fernando', 'Alonso', 'fernando.alonso@f1.com', '1981-07-29', 'Male')
# ]
#
# curs.executemany(insert_query, data)
# con.commit()  # Commit the transaction
#
# print("Records inserted successfully!")

# Close the connection
# curs.close()
# con.close()
# print("Done")


import mysql.connector

# Establish connection
con = mysql.connector.connect(host="localhost",port="3306",user="root",password="Dipam@223133",database="mydb"
)

curs = con.cursor()

# Update Max Verstappen's email
update_query = "UPDATE student SET email = 'max33.verstappen@f1.com' WHERE first_name = 'Max' AND last_name = 'Verstappen'"
curs.execute(update_query)
con.commit()
print("Max Verstappen's email updated successfully!")

#  Delete Lando Norris from the table
delete_query = "DELETE FROM student WHERE first_name = 'Lando' AND last_name = 'Norris'"
curs.execute(delete_query)
con.commit()
print("Lando Norris's record deleted successfully!")

# Close the connection
curs.close()
con.close()

