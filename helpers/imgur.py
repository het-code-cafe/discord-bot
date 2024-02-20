import os
import random

import requests as r


def imgur_search(search_query='panda') -> tuple | None:
    headers = {'Authorization': 'Client-ID {}'.format(os.getenv('IMGUR_CLIENT_ID'))}
    url = 'https://api.imgur.com/3/gallery/search/top/?q=' + search_query
    response = r.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        imgs = []
        for item in data['data']:
            if 'link' in item and 'title' in item:
                if 'i.imgur.com' in item['link']:  # Embed url, post url will fail the image
                    imgs.append((item['link'], item['title']))
        return random.choice(imgs) if imgs else None
    return None
