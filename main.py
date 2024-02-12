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

