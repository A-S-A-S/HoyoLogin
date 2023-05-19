import json
import requests
from requests.exceptions import HTTPError
import http.cookies


# Constants
with open('tokens.json') as file:
    USERS_COOKIES = json.load(file)
GI_URL = "https://sg-hk4e-api.hoyolab.com/event/sol/sign?act_id=e202102251931481"
HSR_URL = "https://sg-public-api.hoyolab.com/event/luna/os/sign?act_id=e202303301540311"

def parseCookie(USERS_COOKIES):
    parsed_cookies = {}
    for user, cookie_string in USERS_COOKIES.items():
        cookie = http.cookies.SimpleCookie()
        cookie.load(cookie_string)
        parsed_cookies[user] = {name: cookie[name].value for name in cookie}
    return parsed_cookies

def getAccountInfo(cookies):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47",
        "Referer": "https://act.hoyolab.com",
        "Accept-Encoding": "gzip, deflate, br",
    }

    try:
        response = requests.get("https://api-account-os.hoyolab.com/auth/api/getUserAccountInfoByLToken", headers=headers, cookies=cookies)
        return response.json()
    except Exception as e:
        return e

def ClaimReward(cookies, URI):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ja-JP,ja;q=0.5",
        "Content-Type": "application/json;charset=utf-8",
        "Connection": "keep-alive"
    }

    params = (("lang", "en-us"),)

    try:
        response = requests.post(URI, headers=headers, params=params, cookies=cookies)
        return response.json()
    except Exception as e:
        return e

if __name__ == "__main__":
    parsed_cookies = parseCookie(USERS_COOKIES)
    for user, cookie in parsed_cookies.items():
        print(f"Processing user: {user}")
        result = getAccountInfo(cookie)
        print(result)

        print("Claiming rewards from GI")
        result = ClaimReward(cookie, GI_URL)
        print(result)

        print("Claiming rewards from HSR")
        result = ClaimReward(cookie, HSR_URL)
        print(result)
