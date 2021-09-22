# Dekho, Dekho - Slug aaya hai!
# Ab aap yeh link - 
# http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json open karein. 
# Aise link ko use kar kar, aap kisi particular exercise ka content nikal sakte hai.

# Yeh karne ke liye teen steps honge:

# 1 - Sabse pehle aap user se input loge, ki user kaunsi exercise ka content dekhna chahta hai 
# 2 - User se input lekar, aap corresponding exercise ka slug nikaloge 
# 3 - Yeh slug aur purana course_id use kar kar, aap uppar wale jaisa URL call karoge

# Slug Nikalne ke liye hints
# Pehle toh aap yeh samjhiye, slug nikalna normal programming hai, 
# iska requests se kuch khaas lena dena nahi hai.

# Jaise hi user input karega, toh aap ko dekhna padega, ki woh parent exercise hai, child exercise.

# Phir aap yeh process repeat karna:

# - Aap kuch select karna, aur manually list mei se uski `slug` dhoondhna.
# - Yeh aap 5 se 10 baar karo.
# - Yeh karte karte observe karo, ki aap slug kaise nikal rahe ho.
# - Aap ussi karne ke tareeke ki - ek user story likho.
# - Uss user story ko code mei badalne ki koshish karo
# Aise kar kar shayad aap soch pao, ki kaise user ki selection ke basis par aap usse koi 
# slug recommend kar sakte ho.
import requests
import json
import os.path

#all courses
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

#specified course
selection=int(input("Enter seriel number of the course you want to explore:\n"))
for i in pobj:
    sr_no=1
    for values in pobj[i]:
        if sr_no==selection:
            print("name of the selected course is:",values["name"])
            print("ID of the selected course is:",values["id"])
            id=values["id"]
        sr_no+=1

#exercises under the user specified course
url="http://saral.navgurukul.org/api/courses/"
userspecifiedurl=requests.get(url+id+"/exercises")
json_content_ofspecified=userspecifiedurl.json()
file_name="/home/bhagyashri/Desktop/request/exercises_"+str(id)+".json"
file_exists=os.path.exists(file_name)
if file_exists==True:
    with open(file_name,"r") as jsonfile_ofspecified:
        pobj=json.loads(jsonfile_ofspecified.read())
    sr_no=1
    print("Exercises under the selected course are:")
    for i in pobj["data"]:
            print(str(sr_no)+".",i["name"])
            sr_no+=1

else:
    with open(file_name,"w") as jsonfile_ofspecified:
        json.dump(json_content_ofspecified,jsonfile_ofspecified ,indent=2)
    with open(file_name,"r") as jsonfile_ofspecified:
        pobj=json.loads(jsonfile_ofspecified.read())
    sr_no=1
    print("Exercises under the selected course are:")
    for i in pobj["data"]:
            print(str(sr_no)+".",i["name"])
            sr_no+=1

#user specified exeercise content under the user specified course 
selected_exercise_srno=int(input("Enter serial number of the exercise you want to visit:"))
sr_no=1
for d in pobj["data"]:
    if sr_no==selected_exercise_srno:
        print("Selected exercise name:",d["name"])
        print("Content under "+str(d["name"])+":")
        response_obj=requests.get(url+id+"/exercise/getBySlug?slug="+str(d["slug"]))
        jsondata=response_obj.json()
        print(jsondata)
    sr_no+=1

