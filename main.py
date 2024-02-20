import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

"""

	In a soon-to-be-implemented update, the bot will overwrite the default help command with a custom one. 
	This will allow for a more custom help command that will be able to display the 
	help command in a more user-friendly way.

"""


class CCBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        super().__init__(
            command_prefix=os.getenv("PREFIX"),
            intents=intents
        )

        self.remove_command("help")

    async def setup_hook(self):
        for folder in os.listdir("./cogs"):
            if folder == "__pycache__" or folder == ".git" or folder == "docker":
                continue
            print(f"-----------------------------\n[>>] Loading {folder}'s cogs\n-----------------------------")
            for filename in os.listdir(f"./cogs/{folder}"):
                # Skip initialization files
                if filename.endswith("__init__.py"):
                    continue

                if filename.endswith(".py"):
                    try:
                        await self.load_extension(f"cogs.{folder}.{filename[:-3]}")
                        print(f"[+] {filename} loaded")
                    except Exception as e:
                        print(f"[-] {filename} failed to load\n[->]{e}")


os.system('cls' if os.name == 'nt' else 'clear')
print("Code-Café's Discord bot is starting...")
CCBot().run(os.getenv("TOKEN"))
