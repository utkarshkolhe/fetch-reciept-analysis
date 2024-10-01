from etl import extract,transform,load

def performetl(connection,folder_path):
    brands_data,receipts_data,users_data = extract.load_jsons(folder_path)
    reciepts,reciepts_items,users,user_roles,brands,brand_categories = transform.transform_all_json(connection,brands_data,receipts_data,users_data)

    load.load_data_to_postgres(user_roles,"userroles",connection)
    load.load_data_to_postgres(users,"users",connection)
    load.load_data_to_postgres(brand_categories,"brandcategories",connection)
    load.load_data_to_postgres(brands,"brands",connection)
    load.load_data_to_postgres(reciepts,"receipts",connection)
    load.load_data_to_postgres(reciepts_items,"receiptitems",connection)
