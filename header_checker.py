import requests

def check_headers(url):
    response = requests.get(url)
    
    print("\n=== Header Security Check ===")
    print("URL: " + url)
    print("Status: " + str(response.status_code))
    print("\n--- Security Headers ---")
    
    headers_to_check = [
        "x-frame-options",
        "content-security-policy",
        "x-xss-protection",
        "strict-transport-security",
        "server"
    ]
    
    for header in headers_to_check:
        if header in response.headers:
            print("✓ " + header + ": " + response.headers[header])
        else:
            print("✗ MISSING: " + header)

url = input("Enter URL to check: ")
check_headers(url)
