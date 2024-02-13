import discord
from discord.ext import commands

class ForbiddenFilter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.banned_scentences = ["lord of the rings was eigenlijk niet zo'n goede film", "crucio", "ava kedavra", "emacs is beter dan vim"]
        self.forbidden_words = ["kanker", "kut", "neger", "pizza hawaii", "scriptie", "rutte", "de jonge"]

    @commands.Cog.listener()
    async def on_message(self, message):
        """
            Deletes or Bans based off the condition
        """
        if any(word in message.content for word in self.banned_scentences):
            await message.delete()
            await message.channel.send(f"Yeet!")
            await message.author.ban(reason="Banned for saying a forbidden sentence")
        if any(word in message.content for word in self.forbidden_words):
            await message.delete()
            await message.channel.send(f"{message.author.mention} je mag dit woord niet gebruiken!")
        

async def setup(bot):
    await bot.add_cog(ForbiddenFilter(bot))