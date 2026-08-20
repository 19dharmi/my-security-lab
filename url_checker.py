import requests

def check_url(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"URL: {url}")
        print(f"Status: {response.status_code}")
        print(f"Size: {len(response.text)} bytes")
        print("---")
    except Exception as e:
        print(f"URL: {url}")
        print(f"Error: {e}")
        print("---")

urls = [
    "https://google.com",
    "https://github.com",
    "https://example.com"
]

for url in urls:
    check_url(url)
