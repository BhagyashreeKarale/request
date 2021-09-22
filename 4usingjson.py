# Using JSON
# Jo code humne likha tha, requests library kar kar, courses download karne ke liye, uss code mei yeh changes karo.

# Abhi tak woh code kya karta hai?
# requests module use kar kar, courses ka API Endpoint ya URL call kar kar, data courses.json file mei store karta hai.

# Ab aapko kya karna hai?
# - `courses.json` file padh kar
# - aapko iss object ko ek json argument mei load karna hai
# - uss json object ko parse kar kar
# - aapko saare courses ki list print karni hai, jaise
# - 1. Introduction to Javascript
# - 2. Getting Started
# - 3. Implementing PickleDB - DB - Part I
# - ...
# - ...
# - n. Web Scraping 101
# Yeh karne se pehle aap apne code mei ek chota sa change karo, ki
# check karo ki agar (if) `courses.json` pehle se exist karti hai,
# toh aap dobara API call mat karo. isse aap debugging fast kar paoge. 
# API call sirf tab karo, jab `courses.json` file exist nahikarti
# isse aap fast debugging kar paoge, nahi toh baar baar aapko API call khatam hone ka wait karna padega.
import json
import requests
import os.path
file_exists=os.path.exists("/home/bhagyashri/Desktop/request/courses.json")
if file_exists==True:
    with open ("/home/bhagyashri/Desktop/request/courses.json","r") as jsonfile:
        pobj=json.loads(jsonfile.read())
        index=97
        sr_1=1
        for i in pobj:
            print(chr(index).upper(),".",i,":")
            sr_no=1
            for values in pobj[i]:
                print(sr_no,".",values["name"])
                sr_no+=1
            print()
            index+=1
else:
    response_obj=requests.get("http://saral.navgurukul.org/api/courses")
    jsondata=response_obj.json()
    with open ("/home/bhagyashri/Desktop/request/courses.json","w") as jsonfile:
        json.dump(jsondata,jsonfile,indent=2)
    with open ("/home/bhagyashri/Desktop/request/courses.json","r") as jsonfile:
        pobj=json.loads(jsonfile.read())
        index=97
        sr_1=1
        for i in pobj:
            print(chr(index).upper(),".",i,":")
            sr_no=1
            for values in pobj[i]:
                print(sr_no,".",values["name"])
                sr_no+=1
            print()
            index+=1
