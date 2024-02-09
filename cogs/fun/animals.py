import discord, requests, random
from discord.ext import commands

class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kat(self, ctx):
        """
            Gets a random cat image from thecatapi.com
        """
        req = requests.get("https://api.thecatapi.com/v1/images/search").json()
        msg = req[0]["url"]
        embed = discord.Embed(title="🐱 Meow! Here's a cat for you!", color=0xFF5733)
        if msg.endswith(".gif"):
            embed.description = "You have been blessed with a cat gif! 🙏"
            embed.set_image(url=msg)
        else:
            embed.set_image(url=msg)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def panda(self, ctx):
        """
            Gets a random panda image from some-random-api.ml
        """
        req = requests.get("https://some-random-api.ml/img/panda").json()
        msg = req["link"]
        embed = discord.Embed(title="🐼 A panda for you!", color=0x000000)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)
        
    @commands.command(aliases=["doggo", "woof"])
    async def dog(self, ctx):
        """
            Gets a random dog image from thedogapi.com
        """
        req = requests.get("https://api.thedogapi.com/v1/images/search").json()
        msg = req[0]["url"]
        embed = discord.Embed(title="🐶 Woof! Here's a dog for you!", color=0x8B4513)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def fox(self, ctx):
        """
            Gets a random fox image from randomfox.ca
        """
        req = requests.get("https://randomfox.ca/floof/").json()
        msg = req["image"]
        embed = discord.Embed(title="🦊 A fox for you!", color=0xFF5733)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def bird(self, ctx):
        """
            Gets a random bird image from some-random-api.ml
        """
        req = requests.get("https://some-random-api.ml/img/birb").json()
        msg = req["link"]
        embed = discord.Embed(title="🐦 A bird for you!", color=0x000000)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def bunny(self, ctx):
        """
            Gets a random bunny image from api.bunnies.io
        """
        media_type = "gif" if random.random() < 0.5 else "mp4"
        req = requests.get(f"https://api.bunnies.io/v2/loop/random/redirect/?media={media_type}")
        msg = req.url
        embed = discord.Embed(title="🦆 A bunny for you!", color=0x000000)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def duck(self, ctx):
        """
            Gets a random duck image from random-d.uk
        """
        req = requests.get("https://random-d.uk/api/v2/random").json()
        msg = req["url"]
        embed = discord.Embed(title="🦆 A duck for you!", color=0x000000)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Animals(bot))
