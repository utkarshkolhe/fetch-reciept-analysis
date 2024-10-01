from utils import typeconverter
from utils import table_info
from utils import common_functions
from datetime import datetime
import json
def convert_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert to ISO 8601 format
    raise TypeError(f"Type {type(obj)} not serializable")

def removeDuplicates(data):
    unique_list = []
    seen = set()
    for item in data:
        # Convert each dictionary to a JSON string
        json_str = json.dumps(item, default=convert_datetime,sort_keys=True)
        if json_str not in seen:
            unique_list.append(item)
            seen.add(json_str)
    return unique_list
def seperateRecieptItems(receipts_data):
    new_reciepts=[]
    new_reciepts_items=[]

    for reciept in receipts_data:
        recipetid = reciept["_id"]["$oid"]
        if "rewardsReceiptItemList" in reciept:
            for item in reciept["rewardsReceiptItemList"]:
                newitem = item.copy()
                newitem["recieptID"] = recipetid
                newitem["_id"]=common_functions.generate_random_string()
                new_reciepts_items.append(newitem)
        newreciept = reciept.copy()
        if "rewardsReceiptItemList" in newreciept:
            del newreciept["rewardsReceiptItemList"]
        new_reciepts.append(newreciept)
    return new_reciepts,new_reciepts_items
def seperateUsersAndUserRolels(data):
    userrolemap={}
    counter=1
    for i in range(len(data)):
        dat = data[i]
        if "role" in dat:
            if dat["role"] not in userrolemap:
                userrolemap[dat["role"]]=counter
                counter+=1
            data[i]["roleid"] =userrolemap[dat["role"]]
    userroles=[]
    for key,value in userrolemap.items():
        userroles.append({"_id":value,
    "role":key})
    return data,userroles

def seperateBrandAndBrandCategories(data):
    categorymap={}
    categorycodemap={}
    counter=1
    for i in range(len(data)):
        dat = data[i]
        if "category" in dat:
            if dat["category"] not in categorymap:
                categorymap[dat["category"]]=counter
                if "categoryCode" in dat:
                    categorycodemap[dat["category"]]=dat["categoryCode"]
                counter+=1
            data[i]["catid"] =categorymap[dat["category"]]
    brandcategories=[]
    for key,value in categorymap.items():
        categorycode=""
        if key in categorycodemap:
            categorycode=categorycodemap[key]
        brandcategories.append({"_id":value,
    "category":key,"categoryCode":categorycode})
    return data,brandcategories

def fillBrandIDs(reciepts_items,brands):
    # barcodeIdMap={}
    brandcodeIdMap={}
    # print("##########################")
    # print(brands[0])
    # print(reciepts_items[0])
    for brand in brands:
        if 'brandcode' in brand and brand['brandcode'] not in brandcodeIdMap:
            brandcodeIdMap[brand['brandcode']]=brand['_id']
    print(brandcodeIdMap)
    new_reciepts_items=[]
    mapped=0
    for reciepts_item in reciepts_items:
        if 'brandCode' in reciepts_item and reciepts_item['brandCode'] in brandcodeIdMap:
            reciepts_item['brandID']=brandcodeIdMap[reciepts_item['brandCode']]
            mapped+=1
            # print(reciepts_item)
        new_reciepts_items.append(reciepts_item)
    print("Mapped",mapped)
    return new_reciepts_items

def transform_all_json(connection,brands_data,receipts_data,users_data):

    reciepts,reciepts_items = seperateRecieptItems(receipts_data)
    users,user_roles = seperateUsersAndUserRolels(users_data)
    brands,brand_categories = seperateBrandAndBrandCategories(brands_data)




    colmap=table_info.get_table_columns_and_datatypes("users",connection)
    users = typeconverter.convert_datatype_in_json(users,colmap)
    # print("Users",colmap)
    # print("==========================")

    colmap=table_info.get_table_columns_and_datatypes("userroles",connection)
    user_roles = typeconverter.convert_datatype_in_json(user_roles,colmap)
    # print("UserRoles",colmap)
    # print("==========================")

    colmap=table_info.get_table_columns_and_datatypes("brands",connection)
    brands = typeconverter.convert_datatype_in_json(brands,colmap)
    # print("Brands",colmap)
    # print("==========================")

    colmap=table_info.get_table_columns_and_datatypes("brandcategories",connection)
    brand_categories = typeconverter.convert_datatype_in_json(brand_categories,colmap)
    # print("BrandCategories",colmap)
    # print("==========================")


    reciepts_items =fillBrandIDs(reciepts_items,brands)

    colmap=table_info.get_table_columns_and_datatypes("receipts",connection)
    reciepts = typeconverter.convert_datatype_in_json(reciepts,colmap)
    # print("Reciepts",colmap)
    # print("==========================")

    colmap=table_info.get_table_columns_and_datatypes("receiptitems",connection)
    reciepts_items = typeconverter.convert_datatype_in_json(reciepts_items,colmap)
    # print("RecieptsItems",colmap)
    # print("==========================")



    # new_reciepts_items = typeconverter.convert_datatype_in_json(new_reciepts_items,colmap)
    # users_data = typeconverter.convert_datatype_in_json(users_data)
    return removeDuplicates(reciepts),removeDuplicates(reciepts_items),removeDuplicates(users),removeDuplicates(user_roles),removeDuplicates(brands),removeDuplicates(brand_categories)
