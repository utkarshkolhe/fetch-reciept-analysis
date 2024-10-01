import psycopg2
from utils import table_info



def load_data_to_postgres(data,tablename, connection):

    colmap=table_info.get_table_columns_and_datatypes(tablename,connection)
        # SQL statement to insert data
    # print(colmap)
    keys = sorted(list(colmap.keys()))
    sql = "INSERT INTO "+tablename+" ("+ ",".join(keys) +") VALUES ("+",".join(["%s"]*len(keys))+")"
    # print(sql)
    # Execute the SQL statement for each row of data
    try:
        cursor = connection.cursor()
        # Assuming a table named 'your_table' with appropriate schema exists
        for row in data:
            try:

                vals =[row[key] for key in keys]
                cursor.execute(sql, tuple(vals))
                connection.commit()
            except Exception as e:
                connection.rollback()
                print("ERROR",row)
                print(e)
        print("Data loaded successfully.")
    except Exception as e:
        connection.rollback()
        print(f"Error loading data to PostgreSQL: {e}")
