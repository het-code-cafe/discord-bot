import random, os
import requests as r

def imgur_search(search_query='panda') -> tuple | None:
    headers = {'Authorization': 'Client-ID ' + os.getenv('IMGUR_API_KEY')}
    url = 'https://api.imgur.com/3/gallery/search/top/?q=' + search_query
    response = r.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        imgs = []
        for item in data['data']:
            if 'link' in item and 'title' in item:
                imgs.append((item['link'], item['title']))
        return random.choice(imgs) if imgs else None
    return None
	
