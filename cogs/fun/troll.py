import discord
from discord.ext import commands

from cogs.fun import imgur_command


class Troll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["rick", "rr"])
    async def rickroll(self, ctx):
        """
            Get rickrolled.
        """
        embed = discord.Embed(title="🎵 Never gonna give you up! 🎵", color=0xFF5733)
        embed.set_image(
            url="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTRlYmszeTZ0dHg5ejg5OG14N28weDZpbDE0enh2emJtNnpscWVoZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ju7l5y9osyymQ/giphy.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def mock(self, ctx, *text):
        """
            Get mocked thru mockingspongebob.org
        """
        arg = "_".join(text)
        embed = discord.Embed(title="You got mocked!", color=0xFF5733)
        embed.set_image(url=f"https://mockingspongebob.org/{arg}.jpg")
        await ctx.send(embed=embed)

    @commands.command(aliases=["shit","schijt","drol"])
    async def poep(self, ctx):
        """
            Sends a random picture of shit
        """
        await imgur_command(ctx, "shit", "💩", color=0x8B4513)

async def setup(bot):
    await bot.add_cog(Troll(bot))
