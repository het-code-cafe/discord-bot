import discord
from discord.ext import commands

class AutoMod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.banned_words = ["kanker", "kut", "neger"]

    @commands.Cog.listener()
    async def on_message(self, message):
        """
            Deletes a message if it contains a banned word
        """
        if any(word in message.content for word in self.banned_words):
            await message.delete()

def setup(bot):
    bot.add_cog(AutoMod(bot))