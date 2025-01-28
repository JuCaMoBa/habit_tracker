# This file contains the class DBConnection which is used to connect to the database and execute queries.
# It is used as a context manager in the database.py file.
# The __enter__ method is used to establish a connection to the database and return the connection object.
# The __exit__ method is used to commit the transaction if no exception has occurred, otherwise rollback the transaction.
# The __exit__ method also closes the cursor and connection objects.

# Importing the required modules

class DBConnection:
    def __enter__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()
            print
            self.cursor.close()
            self.connection.close()
        
        

   