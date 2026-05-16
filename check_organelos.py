import urllib.request
import re
import json
import urllib.parse

query = urllib.parse.quote("organelos celulares biología")
url = f"https://www.youtube.com/results?search_query={query}"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')
video_ids = re.findall(r'\"videoId\":\"(.*?)\"', html)

print("Valid videos for organelos:")
count = 0
for vid in list(dict.fromkeys(video_ids)):
    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}"
    try:
        req_o = urllib.request.urlopen(oembed_url)
        data = json.loads(req_o.read().decode('utf-8'))
        print(f"ID: {vid} | Title: {data.get('title')}")
        count += 1
        if count >= 5: break
    except Exception as e:
        pass
