import requests, math, json
cookies = {}

with open("tokens.json", "r") as f:
    cookies = json.load(f)
# print(cookies)

with open("config.json", "r") as f:
    problemid = json.load(f)["problems"]
# print(problemid)

def get(url):
    print("Fetching:", url)
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    if response.status_code != 204:
        posts = response.json()
        return posts
    
def getall():
    probscores = []
    for id in problemid:
        scores = {}
        responses = get(f"https://syoj.org/api/status?page=1&verdict=2,3,5,6,7,8&languages=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27&problem={id}")
        for response in responses["submissions"]:
                scores[response["user"]["displayName"]] = max(response["score"], scores.get(response["user"]["id"], response["score"]))
        for page in range(2, int(math.ceil(int(responses["count"])/20))+1):
            responses = get(f"https://syoj.org/api/status?page={page}&verdict=2,3,5,6,7,8&languages=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27&problem={id}")["submissions"]
            for response in responses:
                scores[response["user"]["displayName"]] = max(response["score"], scores.get(response["user"]["id"], response["score"]))
        probscores.append(scores)
    # print(probscores)
    return probscores