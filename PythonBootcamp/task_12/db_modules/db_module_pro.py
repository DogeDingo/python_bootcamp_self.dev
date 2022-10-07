import json
import psycopg2

def read_jsonfile(name_jsonfile):
    file_json = open(name_jsonfile)
    data_members = json.load(file_json)
    members = data_members["selfdev_members"]
    members_list = []
    [members_list.append(tuple(x.values())) for x in members]
    return members_list
