import json;

def readJson(json):
    f = open(json, "r");
    data = json.load(f);
    f.close();
    return data;
 