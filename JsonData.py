import requests, json

URL = "https://ht.mdex.com/tokenlist.json"

add_new = [
    {
        "name": "JOIN",
        "address": "0x1D9Fd228adda1975e376AFA6B73e35Ee6c2Cf9ae",
        "symbol": "JOIN",
        "decimals": 18,
        "chainId": 128,
        "logoURI": "https://raw.githubusercontent.com/longbaby1101/JoinData/master/logo.png"
    }
]


def getJsonData():
    jd = requests.get(URL)
    JSON_DATA = jd.json()
    JSON_DATA["name"] = "JoinSwap token List"
    JSON_DATA["tokens"].extend(add_new)
    with open("JoinData.json", "w") as f:
        f.write(json.dumps(JSON_DATA))


if __name__ == '__main__':
    getJsonData()
