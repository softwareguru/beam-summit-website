import requests
import json
import re

API_URL = "https://sessionize.com/api/v2/ezuter2b/view/all"

res = requests.get(API_URL)

json_data = json.loads(res.text)

speakers = {}

def clean_name(name):
  regex = re.compile('[^a-zA-Z]')
  res = regex.sub('', name)

  return res.lower()


# Speakers
for i, s in enumerate(json_data['speakers']):
  new_key = clean_name(s['fullName'])

  speakers[new_key] = {}
  speakers[new_key]['bio'] = s['bio']
  speakers[new_key]['id'] = new_key
  speakers[new_key]['title'] = s['tagLine']
  speakers[new_key]['company'] = s['tagLine']
  speakers[new_key]['order'] = i
  speakers[new_key]['photoUrl'] = s['profilePicture']
  speakers[new_key]['name'] = s['fullName']
  speakers[new_key]['featured'] = True
  speakers[new_key]['socials'] = []
  for l in s['links']:
    to_add = {}
    to_add['name'] = l['title']
    to_add['link'] = l['url']
    to_add['icon'] = l['title'].lower()
    speakers[new_key]['socials'].append(to_add)

with open('sessionize_speakers.json', 'w') as f:
  f.write(json.dumps(speakers))


