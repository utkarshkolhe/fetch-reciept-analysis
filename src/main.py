import table_creation
import json
from etl import etl
from utils import table_info
import psycopg2
# Read the JSON file
with open("../config/config.json", 'r') as file:
    # Parse the JSON data into a dictionary
    config = json.load(file)

    connection = psycopg2.connect(user=config["user"],
                                  password=config["password"],
                                  host=config["host"],
                                  port=config["port"],
                                  database=config["database"])

    table_creation.create_table(connection)
    connection.commit()
    # print(table_info.get_table_columns_and_datatypes("receipts",connection))
    etl.performetl(connection,"../data/raw_data/")
    connection.close()
    print("PostgreSQL connection is closed")
