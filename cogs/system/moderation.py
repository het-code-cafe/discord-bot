import discord
from discord.ext import commands

from helpers.CCProfanityFilter import CCProfanityFilter


class Moderation(commands.Cog):
    def __init__(self, bot):
        self._bot = bot
        self._filter = CCProfanityFilter()

    @commands.Cog.listener()
    async def on_message(self, message):
        """
            Deletes or Bans based off the condition
        """
        if self._filter.forbidden(message.content):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, dat mag je niet zeggen!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
            Kick a member from the server
        """
        await member.kick(reason=reason)
        embed = discord.Embed(title="You have been kicked!", color=0xFF5733)
        embed.add_field(name="Reason", value=reason)
        await member.send(embed=embed)
        embed = discord.Embed(title="Member kicked!", color=0xFF5733)
        embed.add_field(name="Member", value=member)
        embed.add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """
            Ban a member from the server
        """
        await member.ban(reason=reason)
        embed = discord.Embed(title="You have been banned!", color=0xFF5733)
        embed.add_field(name="Reason", value=reason)
        await member.send(embed=embed)
        embed = discord.Embed(title="Member banned!", color=0xFF5733)
        embed.add_field(name="Member", value=member)
        embed.add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def timeout(self, ctx, member: discord.Member, *, reason=None):
        """
            Timeout a member from the server
        """
        await member.timeout(reason=reason)
        embed = discord.Embed(title="You have been timed out!", color=0xFF5733)
        embed.add_field(name="Reason", value=reason)
        await member.send(embed=embed)
        embed = discord.Embed(title="Member timed out!", color=0xFF5733)
        embed.add_field(name="Member", value=member)
        embed.add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Moderation(bot))
