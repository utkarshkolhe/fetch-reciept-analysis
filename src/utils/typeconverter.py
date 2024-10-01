import datetime
from collections import defaultdict
import datetime

def transformdatkeys(data):
    newdata=[]
    for dat in data:
        newdat=defaultdict(lambda:None)
        for key,value in dat.items():
            # if key=="_id":
            #     print(value)
            newdat[key.lower()]=value
        newdata.append(newdat)
    return newdata
def convert_datatype_in_json(data,colmap):
    data = transformdatkeys(data)
    newdata=[]
    for dp in data:
        newdp=defaultdict(lambda:None)
        for key,value in dp.items():
            new_value=value
            if key not in colmap:
                continue
            if key=="_id":
                try:
                    new_value = value["$oid"]
                except:
                    new_value = value
            elif colmap[key]=="integer":
                new_value = int(value)
            elif colmap[key]=="double precision":
                new_value = float(value)
            elif colmap[key]=="boolean":
                new_value = bool(value)
            elif colmap[key]=="character varying":
                new_value = str(value)
                if len(new_value)>100:
                    print(key,len(new_value))
            elif colmap[key]=="text":
                new_value = str(value)
            elif colmap[key]=="timestamp without time zone":
                # Convert milliseconds to seconds
                timestamp_ms = value["$date"]
                timestamp_s = timestamp_ms / 1000

                # Convert Unix timestamp to datetime object
                new_value = datetime.datetime.fromtimestamp(timestamp_s)
            newdp[key] = new_value
        newdata.append(newdp)
    return newdata
