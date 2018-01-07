
import aiohttp # Web requests, gonna need it.
import json # Kitsu's API uses JSON
import urllib # url encoding

class Anime:
    def __init__(self, id, attributes):
        self.id = id
        self.attributes = attributes

class KitsuAPI:
    'A wrapper for the kitsu.io api by ry00001'
    def __init__(self):
        pass

    async def get_anime(self, name:str):
        with aiohttp.ClientSession() as sesh:
            urlencoded = urllib.parse.quote(name)
            async with sesh.get(f'http://kitsu.io/api/edge/anime?filter[text]={urlencoded}') as req:
                req = await req.json(content_type=None)
                return req['data']
            sesh.close()
