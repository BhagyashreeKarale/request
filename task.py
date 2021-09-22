import requests
import json
import os.path
def p():
    with open("/home/bhagyashri/Desktop/request/task.json","r") as jf:
        pobj=json.loads(jf.read())
    return pobj
def bubblesort_id():
    pobj=p()
    idlist=[]
    for i in pobj["data"]:
        idlist.append(i["id"])
    max=0
    for i in range(len(idlist)):
        for k in range(len(idlist)-i-1):
            if idlist[k]>idlist[k+1]:
                max=idlist[k]
                idlist[k]=idlist[k+1]
                idlist[k+1]=max
    return idlist
def final(idlist,pobj):
    sr_no=1
    for s in idlist:
        for b in pobj['data']:
            if b["id"]==s:
                print(str(sr_no)+".",b['name'],b["id"])
                sr_no+=1
def main():
    aORd=input("Enter 'a' for ASCENDING ORDER according to the id\nEnter 'd' for DESCENDING ORDER according to the id")
    if aORd=='a' or aORd=='A':
        idlist=bubblesort_id()
        pobj=p()
        final(idlist,pobj)
    elif aORd=='d' or aORd=='D':
        idlist=bubblesort_id()
        pobj=p()
        idlist=idlist[::-1]
        final(idlist,pobj)
    else:
        print("INVALID INPUT")
file_exists=os.path.exists("/home/bhagyashri/Desktop/request/task.json")
r=requests.get("https://join.navgurukul.org/api/partners")
r=r.json()
if file_exists==True:
    main()
else:
    with open("/home/bhagyashri/Desktop/request/task.json","w+") as jf:
        json.dump(r,jf,indent=2)
    main()
