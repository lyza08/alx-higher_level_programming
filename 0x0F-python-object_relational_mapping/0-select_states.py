#!/usr/bin/python3
import MySQLdb

def main(mysql_username, mysql_password, database_name):
  """Lists all states from the database `hbtn_0e_0_usa`.

  Args:
    mysql_username: The username for the MySQL server.
    mysql_password: The password for the MySQL server.
    database_name: The name of the database to connect to.
  """

  # Connect to the MySQL server.
  db = MySQLdb.connect(
      host='localhost',
      port=3306,
      user=mysql_username,
      passwd=mysql_password,
      db=database_name)

  # Create a cursor object.
  cursor = db.cursor()

  # Execute the SQL query to list all states.
  cursor.execute('SELECT * FROM states ORDER BY id ASC')

  # Get the results of the query.
  results = cursor.fetchall()

  # Close the cursor and database connection.
  cursor.close()
  db.close()

  # Print the results.
  for state in results:
    print(state[1])

if __name__ == '__main__':
  # Get the MySQL username, password, and database name from the command line.
  mysql_username = input('Enter the MySQL username: ')
  mysql_password = input('Enter the MySQL password: ')
  database_name = input('Enter the database name: ')

  # List all states from the database.
  main(mysql_username, mysql_password, database_name)
