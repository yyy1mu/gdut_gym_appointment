import json
import hashlib
import requests

data = {
    "indentTime": "2024-10-28 11:41",
    "venueId": 3,
    "orders": [
        {
            "siteId": 15,
            "smallOrders": [
                {
                    "orderTimePeriod": "2024-10-28 14:00-14:30",
                    "orderPrice": 5,
                    "isUnion": False
                }
            ]
        }
    ],
    "isLimit": "0",
    "preOrderDate": "2024-10-27",
    "token": "84982adb394fbcfdb9d88ea3a17ec61e"
}

# Initialize f with venueId, preOrderDate, and isLimit
f = "{}-{}-{}".format(data["venueId"], data["preOrderDate"], data["isLimit"])

# Iterate through orders to append siteId and smallOrders information
for order in data["orders"]:
    f += "-{}".format(order["siteId"])
    for small_order in order["smallOrders"]:
        f += "-{}-{}-{}".format(
            small_order["orderTimePeriod"],
            format(small_order["orderPrice"], ".1f"),  # Format orderPrice to one decimal place
            small_order["isUnion"]
        )

print(f)

# Calculate MD5 hash of f
md5_hash = hashlib.md5(f.encode()).hexdigest()
print("MD5 Hash:", md5_hash)

# Update token in data
data["token"] = md5_hash

print("Updated Data:", data)

# Send POST request
url = "https://cgyd.gdut.edu.cn/test/booking/indent/generate"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Xweb_xhr": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090c11)XWEB/11437",
    "Token": "3OILJYI/gRyKQWoPifNyv4HpQttfvGnyfAN9VWFN1eEG2oNjBcb6SjgMwD8eJ0eqHN1gUnSG2yolPF/avSTbXsIiTUiZpJ0G3iag+zM1M8Txfzct4+Krfl1oDQWjjQN/r1bdIlW94r+hagHDeMA6q2QXos54sD86RnSQ22Ns0XsGsgyOO7b+M3kXIa2CLZUvU0JQQodLoilQtYKVMEYxgJyEsWndXtmn6iO/ySWjmUVPgWCqnMzWC1i/opI1KvcsA2RUeB+bmFDO+jsE1f4loGI7ACsl1WDf+NhmJ2f5YrjMwQqKNcFpDiOQ/cmD19yl6ljyOL3+UBtagLNVguDwOUzkc0okM2fk0Yph2s6wS6dRcbYaf4ADxBi9Gy4qQsf/vOkBY1EB9+0p+I1XAe35vQ==",
    "Content-Type": "application/json",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx27a5b85a92f84a24/86/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive"
}

response = requests.post(url, headers=headers, json=data)
print("Response Status Code:", response.status_code)
print("Response Body:", response.text)
