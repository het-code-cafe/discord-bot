import random

import discord, asyncio, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = commands.Bot(command_prefix=os.getenv("PREFIX"), intents=discord.Intents.all())
client.remove_command("help")

"""

	In a soon-to-be-implemted update, the bot will overwrite the default help command with a custom one. 
	This will allow for a more custom help command that will be able to display the help command in a more user-friendly way.

"""

async def load_cogs():
    for folder in os.listdir("./cogs"):
        if folder == "__pycache__" or folder == ".git" or folder == "docker":
            continue
        print(f"-----------------------------\n[>>] Loading {folder}'s cogs\n-----------------------------")
        for filename in os.listdir(f"./cogs/{folder}"):
            if filename.endswith(".py"):
                try:
                    await client.load_extension(f"cogs.{folder}.{filename[:-3]}")
                    print(f"[+] {filename} loaded")
                except Exception as e:
                    print(f"[-] {filename} failed to load\n[->]{e}")

async def main():
    async with client:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Code-Café's Discord bot is starting...")
        await load_cogs()

asyncio.run(main())

@client.command()
async def newpanda(context):
	res: tuple | None = _imgur_search("panda")
	if res is not None:
		img, title = res
		await context.message.channel.send(title)
		await context.message.reply(img)

@client.command()
async def monsterenergy(context):
	res: tuple | None = _imgur_search("monster energy")
	if res is not None:
		img, title = res
		await context.message.channel.send(title)
		await context.message.reply(img)

def _imgur_search(search_query='panda') -> tuple | None:
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
	
