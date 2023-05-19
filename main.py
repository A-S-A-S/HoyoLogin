import json
import requests

# Constants
with open('tokens.json') as file:
    USERS_COOKIES = json.load(file)
GI_URL = "https://sg-hk4e-api.hoyolab.com/event/sol/sign?act_id=e202102251931481"
HSR_URL = "https://sg-public-api.hoyolab.com/event/luna/os/sign?act_id=e202303301540311"

# Create a session for HTTP requests
session = requests.Session()

# Debug function to test access
def getAccountInfo(cookies):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
        "Referer": "https://act.hoyolab.com",
        "Accept-Encoding": "gzip, deflate, br",
    }

    try:
        response = session.get("https://api-account-os.hoyolab.com/auth/api/getUserAccountInfoByLToken", headers=headers, cookies=cookies)
        return response.json()
    except requests.exceptions.RequestException as e:
        return str(e)

# The only function you need
def claimReward(cookies, URI):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ja-JP,ja;q=0.5",
        "Content-Type": "application/json;charset=utf-8",
        "Connection": "keep-alive"
    }

    try:
        response = session.post(URI, headers=headers, cookies=cookies)
        return response.json()
    except requests.exceptions.RequestException as e:
        return str(e)

if __name__ == "__main__":
    for user, cookie_string in USERS_COOKIES.items():
        print(f"Processing user: {user}")
        cookies = requests.utils.cookiejar_from_dict({user: cookie_string})

        print("Claiming rewards from GI")
        result = claimReward(cookies, GI_URL)
        print(result)

        print("Claiming rewards from HSR")
        result = claimReward(cookies, HSR_URL)
        print(result)
