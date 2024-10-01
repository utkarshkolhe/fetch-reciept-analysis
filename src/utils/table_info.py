import psycopg2

def get_table_columns_and_datatypes(table_name,connection):

    cursor = connection.cursor()

    # Query to retrieve column information
    query = """
    SELECT column_name, data_type
    FROM information_schema.columns
    WHERE table_name = %s
    """

    cursor.execute(query, (table_name,))
    columns = cursor.fetchall()

    colmap={}
    for key,value in columns:
        colmap[key]=value

    return colmap
