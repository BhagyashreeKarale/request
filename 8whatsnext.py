# What's next?
# Yeh bahut basic sa introduction tha API and JSON ka. Par iss mei kaafi saare fundamentals covered the. 
# Aap acche se samjhe kaise server, API, JSON jaisi saari cheezein aapas mei interlinked hai.

# Jab aap login karte hai, toh aap ko server authenticate karta hai. 
# Phir jab aap koi bhi request karte hai, toh aap batate hai, 
# aap wohi ho jisne thodi der pehle login kiya tha. Yeh sab karne ke liye aap headers ka use karte ho. 
# Unn sab cheezo ka hum API - Part 2 mei focus karenge.

# Aise hi humne abhi bahut simple get requests use ki hai, aage hum post request use bhi karenge, 
# aur sahi se dono tarah ki requests mei difference bhi pata karenge.

# Tab tak aap yeh features integrate kar sakte ho, apne code mei, jisse ki woh aur behetar ho jaye:

# 1 - Up Navigation Jaise hi user up likhe, toh aap usko peechli wali menu par le jao. 
# Matlab agar woh exercises ki list par hai, toh courses ki list dikha kar, usse waha se proceed karao, 
# etc.

# 2 - Previous Navigation Jaise hi user 'p' likhe, toh usse previous exercise ka content dikhao

# 3 - Next Navigation Jaise hi user 'n' likhe, toh usse next exercise ka content dikhao

# 4 - DRY - Don't repeat yourself Dekho kaha kaha aap apne code ko aap repeat kar rahe ho. 
# Kya aap repetitions avoid kar sakte ho - functions, etc. use kar kar?

# navigation=input("Enter 'up' for previous menu\nEnter 'p' for previous navigation\nEnter 'n' for next navigation")
# if navigation=="up":
import requests
import json
import os.path
#all courses
def up():
    with open ("/home/bhagyashri/Desktop/request/courses.json","r") as jsonfile:
        p=json.loads(jsonfile.read())
        index=97
        sr_no=1
        for i in p:
            print(chr(index).upper(),".",i,":")
            sr_no=1
            for values in p[i]:
                print(sr_no,".",values["name"])
                sr_no+=1
            print()
            index+=1
    return(p)
file_exists=os.path.exists("/home/bhagyashri/Desktop/request/courses.json")
if file_exists==True:
    pobj=up()
else:
    response_obj=requests.get("http://saral.navgurukul.org/api/courses")
    jsondata=response_obj.json()
    with open ("/home/bhagyashri/Desktop/request/courses.json","w") as jsonfile:
        json.dump(jsondata,jsonfile,indent=2)
    pobj=up()
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
    print("Exercises under the selected course are:")
    sr_no=1
    for i in pobj["data"]:
        print(str(sr_no)+".",i["name"])
        if len(i["childExercises"])!=0:
            index=97
            for k in i["childExercises"]:
                print("  ",chr(index)+".",k["name"])
                index+=1
        sr_no+=1
        print()

else:
    with open(file_name,"w") as jsonfile_ofspecified:
        json.dump(json_content_ofspecified,jsonfile_ofspecified ,indent=2)
    with open(file_name,"r") as jsonfile_ofspecified:
        pobj=json.loads(jsonfile_ofspecified.read())
    print("Exercises under the selected course are:")
    sr_no=1
    for i in pobj["data"]:
        print(str(sr_no)+".",i["name"])
        if len(i["childExercises"])!=0:
            index=97
            for k in i["childExercises"]:
                print("  ",chr(index)+".",k["name"])
                index+=1
        sr_no+=1
        print()
#user specified exeercise content under the user specified course 
def loop():
    selected_exercise_srno=input("Enter serial number of the exercise you want to visit:\n (Enter 'up' if you want to return to the courses menu)\n")
    if selected_exercise_srno=="up":
        up()
        loop()
    else:
        return(int(selected_exercise_srno))
selected_exercise_srno=loop()
def exercisecontent(selected_exercise_srno):
    sr_no=1
    for d in pobj["data"]:
        if sr_no==selected_exercise_srno:
            print("Exercise name:",d["name"])
            print("Content under "+str(d["name"])+":")
            response_obj=requests.get(url+id+"/exercise/getBySlug?slug="+str(d["slug"]))
            jsondata=response_obj.json()
            print(jsondata)
        sr_no+=1
def NP(selected_exercise_srno):
    with open(file_name,"r") as jsonfile_ofspecified:
        pobj=json.loads(jsonfile_ofspecified.read())
    count=len(pobj["data"])
    if selected_exercise_srno==1:
        exercisecontent(selected_exercise_srno)
        only_n=input("Enter 'n' for next\n")
        if only_n=="n" or only_n=="N":
            selected_exercise_srno+=1
            NP(selected_exercise_srno)
        else:
            print("This is the first page")
    elif selected_exercise_srno>1 and selected_exercise_srno<count:
        exercisecontent(selected_exercise_srno)
        nORp=input("Enter 'n' for next\nEnter 'p' for previous\n")
        if nORp=="n" or nORp=="N":
            selected_exercise_srno+=1
            NP(selected_exercise_srno)
        else:
            NP(selected_exercise_srno-1)
    elif selected_exercise_srno==count:
        exercisecontent(selected_exercise_srno)
        only_p=input("Enter 'p' for previous\n")
        if only_p=="p" or only_p=="P":
            NP(selected_exercise_srno-1)
        else:
            print("This was the last page")
                
    else:
        print("Invalid option selected")
NP(selected_exercise_srno)
