from pwn import *

host = "103.162.14.116"
port = 14005
r = remote(host, port)
count = 0
while True:
    count = count+1
    data = r.recvuntil("n = ")
    n = int(r.recvline().strip())

  
    def calculate_a_n(n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            return n * calculate_a_n(n - 1)
        else:
            return n + calculate_a_n(n - 1)
    result = calculate_a_n(n)
    r.sendline(str(result))
    response = r.recvuntil("\n").strip()
    print(f"Challenge: n = {n}")
    print(f"Response: {response.decode()}\n")
    if count ==100:
       response = r.recvuntil("\n").strip()

       print(f"Response: {response.decode()}\n")
r.close()
