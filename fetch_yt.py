import urllib.request
import re

url = "https://www.youtube.com/results?search_query=amoeba+sisters+en+espa%C3%B1ol"
html = urllib.request.urlopen(url).read().decode('utf-8')
video_ids = re.findall(r'\"videoId\":\"(.*?)\"', html)

for vid in set(video_ids):
    print(f"https://www.youtube.com/watch?v={vid}")
