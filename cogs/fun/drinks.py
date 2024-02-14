import discord, requests, random
from discord.ext import commands
from helpers import imgur


class Drinks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

    @commands.command(aliases=["monster"])
    async def monsterenergy(self, ctx):
        """
        Get a random monster energy image from imgur
        """
        res: tuple | None = imgur.imgur_search("monster energy")
        if res is not None:
            img, title = res
            embed = discord.Embed(title=f"🤮 {title} ", color=0x8B4513)
            embed.set_image(url=img)
            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Drinks(bot))
