# Calling an API
# API humne abhi samjha kya hote hai. Ab hum ek API ko call kar kar kuch data mangwayenge.

# http://saral.navgurukul.org/api/courses iss link ko open karo. 
# SARAL ke server par yeh data hai, jo hum iss course mei use karenge.
# Abhi ke liye, humei ek bahut simple sa code likhna hai.

# Assignment
# Ab aapko

# - `requests` module use kar kar,
# - [yeh](http://saral.navgurukul.org/api/courses) `API Endpoint` ya `URL` call kar kar
# - yeh data `courses.json` file mei store karna hai.
import requests
import json
response_obj=requests.get("http://saral.navgurukul.org/api/courses")
jsondata=response_obj.json()
with open ("/home/bhagyashri/Desktop/request/courses.json","w") as jsonfile:
    json.dump(jsondata,jsonfile,indent=2)
# Kuch Important Baatein
# call hum functions ke liye bhi use karte hai. 
# functions ko hum call karte hai, kuch arguments dete hai, aur kuch vapas lete hai 
# (jo function return karta hai)
# API ko bhi aap aise function ki tarah soch sakte hai, jo server ne aapko diya hai, 
# use karne ke liye. Aap usse call karoge, kuch arguments doge, 
# aur woh aapko kuch json ya kisi aur format mei data return kar dega
# json sabse commonly used data format hai, jismei server data return karta hai. 
# Pehle xml kaafi popular format tha, data exchange ka

