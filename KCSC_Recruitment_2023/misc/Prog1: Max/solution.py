from pwn import *

def is_valid_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return not stack

def solve_challenge(io):
    for round_num in range(1, 102):
        data = io.recvline().decode()
        log.info(f"Received: {data.strip()}")

        answer = "yes" if is_valid_parentheses(data) else "no"
        log.info(f"Sending answer: {answer}")
        io.sendline(answer)

        result = io.recvline().strip().decode()
        log.info(f"Result: {result}")


def main():
    host = '103.162.14.116'
    port = 14003
    io = remote(host, port)
    data = io.recvline().decode()
    while "I will give you the flag after 100 rounds :D" not in data:
        data = io.recvline().decode()
    solve_challenge(io)

    io.close()

if __name__ == "__main__":
    main()
