import psycopg2
from psycopg2 import Error

def create_table(connection):
    try:
        cursor = connection.cursor()

        table_names = ['users', 'userroles', 'receipts', 'receiptitems', 'brandcategories']
        valid=True
        # Iterate over the table names and check their existence
        for table_name in table_names:
            # Execute a query to check if the table exists
            cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s);", (table_name,))
            table_exists = cursor.fetchone()[0]
            valid = valid and table_exists

            if table_exists:
                print(f"Table '{table_name}' exists in the database.")
                with open('sql/drop_tables.sql', 'r') as file:
                    create_table_query = file.read()

                # Execute the SQL statement
                cursor.execute(create_table_query)
                connection.commit()
        # Read the SQL query from the file
        with open('sql/table_creation.sql', 'r') as file:
            create_table_query = file.read()

        # Execute the SQL statement
        cursor.execute(create_table_query)
        connection.commit()
        print("Tables created successfully in PostgreSQL ")

    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            return True

        return False
