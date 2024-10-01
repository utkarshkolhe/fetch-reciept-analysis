import gzip
import json


def extract_json_from_gzip(file_path):
    try:
        with gzip.open(file_path, 'rt') as f:
            json_data = []
            for line in f:
                json_obj = json.loads(line)
                json_data.append(json_obj)
            return json_data
    except Exception as e:
        try:
            data = []
            with gzip.open(file_path, 'rt', encoding='utf-8') as f2:
                firstline=True
                for line in f2:
                    if firstline:
                        firstline=False
                        line =line[line.find('{'):]
                    try:
                        data.append(json.loads(line))
                    except:
                        print(line)
            return data
        except Exception as e:
            print(line)
            print(f"Error reading JSON from {file_path}: {e}")
            return None

def load_jsons(folder_path):
    brands_data = extract_json_from_gzip(folder_path+"/brands.json.gz")
    receipts_data = extract_json_from_gzip(folder_path+"/receipts.json.gz")
    users_data = extract_json_from_gzip(folder_path+"/users.json.gz")
    return brands_data,receipts_data,users_data
