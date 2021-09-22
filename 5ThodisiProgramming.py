# Thodi si Programming!
# What we have done so far
# requests use kar ke courses download kar liye
# aur user ko aapne ek list of courses bhi dikha di
# Aage kya karna hai?
# user koi bhi ek course select karega iske liye user,
# uss course ke saamne likha hua number input karega

# agar aap dhyaan se dekhenge toh, yeh number
# course ki jo list aapko json se milegi
# uss list ke `index` ki tarah hoga, jaise aapne
# KBC game mei shayad kiya hoga

# ussi json ko use kar kar, ab aap, uss course ke
# corresponding jo `id` stored hai, `json` mei,
# woh aap dhoondh sakte hai

# yeh `id` print karo. yehi `id` hum agle part mei use karenge.
import requests
import json
with open("/home/bhagyashri/Desktop/request/courses.json","r") as jsonfile:
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
selection=int(input("Enter seriel number of the course you want to explore:\n"))
for i in pobj:
    sr_no=1
    for values in pobj[i]:
        if sr_no==selection:
            print("name of the selected course is:",values["name"])
            print("ID of the selected course is:",values["id"])
        sr_no+=1
