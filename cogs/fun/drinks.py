import discord, requests
from discord.ext import commands

from cogs.fun import imgur_command


class Drinks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["monster energy"])
    async def monster(self, ctx):
        """
        Search monster energy on imgur
        """
        await imgur_command(ctx, "monster energy", "⚡", color=0x7CB701)

    @commands.command(aliases=["bakkie", "coffee"])
    async def koffie(self, ctx):
        """
        Get a random coffee image from coffee.alexflipnote.dev
        """
        req = requests.get("https://coffee.alexflipnote.dev/random.json").json()
        msg = req["file"]
        embed = discord.Embed(title="☕ A coffee for you!", color=0x8B4513)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)

    @commands.command(aliases=["beer","pils"])
    async def bier(self, ctx):
        """
        Get a random picture of a beer
        """
        await imgur_command(ctx, "beer", "🍺", color=0xF28E1C)

async def setup(bot):
    await bot.add_cog(Drinks(bot))
