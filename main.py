import random

import discord
from discord.ext import commands
import requests as r 
import os


PREFIX = "!"
BANNED_WORDS = [
	"pizza hawaii",
	"pizza hawai",
	"scriptie",
	"mark rutte",
	"marc rutte",
	"hugo de jonge"
]

UNFORGIVABLE_WORDS = [
	"lord of the rings was eigenlijk niet zo'n goede film",
	"crucio", 
	"ava kedavra",
	"emacs is beter dan vim"
]

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(intents=intents, command_prefix=PREFIX)

@client.event
async def on_ready():
	print(f"Logged in as {client.user}")

@client.command()
async def hoi(context):
	await context.message.reply("Hallo!")

@client.command()
async def kat(context):
	req = r.get("https://api.thecatapi.com/v1/images/search")
	res = req.json()
	msg = res[0]["url"]
	if msg.endswith(".gif"):
		await context.message.reply(f"You have been blessed with a cat gif 🙏 {msg}")
		return	
	await context.message.reply(msg)

@client.command()
async def panda(context):
    req = r.get("https://some-random-api.ml/img/panda/")
    res = req.json()
    await context.message.reply(res["link"])

@client.command()
async def woof(context):
    req = r.get("https://random.dog/woof.json")
    res = req.json()
    await context.message.reply(res["url"])

@client.command()
async def bird(context):
    req = r.get("https://some-random-api.ml/img/birb/")
    res = req.json()
    await context.message.reply(res["link"])

@client.command()
async def fox(context):
    req = r.get("https://randomfox.ca/floof/")
    res = req.json()
    await context.message.reply(res["image"])

@client.command()
async def duck(context):
    req = r.get("https://random-d.uk/api/random")
    res = req.json()
    await context.message.reply(res["url"])

@client.command()
async def bunny(context):
	media_type = "gif" if random.random() < 0.5 else "mp4"
	url = f"https://api.bunnies.io/v2/loop/random/redirect/?media={media_type}"
	response = r.get(url)
	await context.message.reply(response.url)

@client.command()
async def koffie(context):
	req = r.get("https://coffee.alexflipnote.dev/random.json")
	res = req.json()
	await context.message.reply(res["file"])

@client.command()
async def testban(context, user: discord.Member):
	if context.message.author.top_role.name == "Moderator":
		await context.message.channel.send("Yeet!")
		await user.ban()
	else: 
		await context.message.reply("UNAUTHORIZED")

@client.command()
async def mock(context, *argument):
	arg = "_".join(argument)
	await context.message.reply(f"https://mockingspongebob.org/{arg}.jpg")

@client.command()
async def poke(context, argument):
	msg = ""

	req = r.get(f"https://pokeapi.co/api/v2/pokemon/{argument}")
	res = req.json()

	msg += f"{res['name'].title()}:\n"

	types = res["types"]

	for tp in types:
		msg += f"Type {tp['slot']}: {tp['type']['name'].title()}\n"

	stats = res["stats"]

	for st in stats:
		msg += f"{st['stat']['name'].title()}: {st['base_stat']}\n"

	await context.message.reply(msg)

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
	
@client.event
async def on_member_join(member):
	guild = member.guild
	if guild.system_channel is not None:
		res = f"Welkom {member.mention} in de {guild.name} server!"
		await guild.system_channel.send(res)

@client.event
async def on_message(message):
	if message.author.id == client.user.id:
		return

	for word in BANNED_WORDS:
		if word in message.content.lower():
			await message.delete()

	for word in UNFORGIVABLE_WORDS:
		if word in message.content.lower():
			await message.delete()
			await message.channel.send("Yeet!")
			await message.author.ban()
	
	await client.process_commands(message) 


client.run(os.getenv("TOKEN"))
