import requests
import discord
from discord.ext import commands
from helpers import imgur

from . import imgur_command


class Animals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["birb", "birdie"])
    async def bird(self, ctx):
        """
        Search a bird on imgur
        """
        await imgur_command(ctx, "bird", "🐦")

    @commands.command(aliases=["newpanda"])
    async def panda(self, ctx):
        """
        Search a panda on imgur
        """
        await imgur_command(ctx, "panda", "🐼")

    @commands.command(aliases=["kwal"])
    async def jellyfish(self, ctx):
        """
        Search a jellyfish on imgur
        """
        await imgur_command(ctx, "jellyfish", "🪼", color=0x03dffc)

    @commands.command(aliases=["wasbeer", "coon"])
    async def raccoon(self, ctx):
        """
        Search a raccoon on imgur
        """
        await imgur_command(ctx, "raccoon", "🦝", color=0x595958)

    @commands.command(aliases=["kikker", "forg"])
    async def forg(self, ctx):
        """
        Search a frog on imgur
        """
        await imgur_command(ctx, "frog", "🐸", color=0x5EDD5F)

    @commands.command(aliases=["katje", "kitty", "cat", "catto"])
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
    async def oldpanda(self, ctx):
        """
        Gets a random panda image from some-random-api.ml
        """
        req = requests.get("https://some-random-api.ml/img/panda").json()
        msg = req["link"]
        embed = discord.Embed(title="🐼 A panda for you!", color=0x000000)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)

    @commands.command(aliases=["doggo", "woof", "hond"])
    async def dog(self, ctx):
        """
        Gets a random dog image from thedogapi.com
        """
        req = requests.get("https://api.thedogapi.com/v1/images/search").json()
        msg = req[0]["url"]
        embed = discord.Embed(title="🐶 Woof! Here's a dog for you!", color=0x8B4513)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)

    @commands.command(aliases=["foxie", "foxxie"])
    async def fox(self, ctx):
        """
        Gets a random fox image from randomfox.ca
        """
        req = requests.get("https://randomfox.ca/floof/").json()
        msg = req["image"]
        embed = discord.Embed(title="🦊 A fox for you!", color=0xFF5733)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)

    @commands.command(aliases=["rabbit"])
    async def bunny(self, ctx):
        """
        Gets a random bunny image from api.bunnies.io
        """
        req = requests.get(
            "https://api.bunnies.io/v2/loop/random/redirect/?media=gif"
        )
        msg = req.url
        embed = discord.Embed(title="🦆 A bunny for you!", color=0x000000)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)

    @commands.command(aliases=["duckie", "quack"])
    async def duck(self, ctx):
        """
        Gets a random duck image from random-d.uk
        """
        req = requests.get("https://random-d.uk/api/v2/random").json()
        msg = req["url"]
        embed = discord.Embed(title="🦆 A duck for you!", color=0x000000)
        embed.set_image(url=msg)
        await ctx.send(embed=embed)

    @commands.command(aliases=["poke", "pkmn", "pokémon", "pokèmon"])
    async def pokemon(self, ctx, *pokemon):
        """
        Gets a random pokemon image from pokeapi.co
        """
        # Search the Pokémon by ID or name
        req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon[0].lower()}").json()

        # Get the species name from the request
        name = req.get("species").get("name").capitalize()

        embed = discord.Embed(
            title=f"🐾 {name} for you!", color=0xFF5733
        )
        embed.add_field(
            name="Name",
            value=name,
            inline=True
        )
        embed.add_field(
            name="Type",
            value=req.get("types")[0].get("type").get("name").title(),
            inline=True,
        )
        embed.add_field(
            name="Health", value=req.get("stats")[0].get("base_stat"), inline=True
        )
        embed.add_field(
            name="Attack", value=req.get("stats")[1].get("base_stat"), inline=True
        )
        embed.add_field(
            name="Defense", value=req.get("stats")[2].get("base_stat"), inline=True
        )
        embed.add_field(
            name="Special Attack",
            value=req.get("stats")[3].get("base_stat"),
            inline=True,
        )
        embed.add_field(
            name="Special Defense",
            value=req.get("stats")[4].get("base_stat"),
            inline=True,
        )
        embed.add_field(
            name="Speed", value=req.get("stats")[5].get("base_stat"), inline=True
        )
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Animals(bot))
