import requests

def check_cookies(url):
    response = requests.get(url)
    
    print("\n=== Cookie Security Check ===")
    print("URL: " + url)
    
    if response.cookies:
        for cookie in response.cookies:
            print("\nCookie name: " + cookie.name)
            print("Value: " + cookie.value[:20] + "...")
            print("HttpOnly: " + str(cookie.has_nonstandard_attr('HttpOnly')))
            print("Secure: " + str(cookie.secure))
    else:
        print("No cookies found")

url = input("Enter URL: ")
check_cookies(url)
