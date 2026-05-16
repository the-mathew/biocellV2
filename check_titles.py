import urllib.request
import re
import json

url = "https://www.youtube.com/results?search_query=amoeba+sisters+en+espa%C3%B1ol"
html = urllib.request.urlopen(url).read().decode('utf-8')
video_ids = re.findall(r'\"videoId\":\"(.*?)\"', html)

print("Valid videos:")
for vid in list(set(video_ids))[0:10]:
    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}"
    try:
        req = urllib.request.urlopen(oembed_url)
        data = json.loads(req.read().decode('utf-8'))
        print(f"ID: {vid} | Title: {data.get('title')}")
    except Exception as e:
        pass
