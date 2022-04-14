import base64
import json


for i in range(604):
    with open("page{}.png".format(i+1), "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            print(b64_string)
    if i == 0 :
        with open("quran_page.json", "rb") as jsonFile:
            string1 = json.load(jsonFile)
            string1["data"][i]["page"] = str(b64_string)
            print(string1["data"][i]["page"])
    else:
            with open("quran_index.json", "rb") as qi:
                string1 = json.load(qi)
                string1["data"][i]["page"] = str(b64_string)
                print(string1["data"][i]["page"])
    with open("quran_index.json" ,"w") as qJson:
        json.dump(string1 , qJson) 
    