import discord
from discord.ext import commands

from cogs.system import MOD_LOG_CHANNEL
from helpers.CCProfanityFilter import CCProfanityFilter


class Moderation(commands.Cog):

    def __init__(self, bot):
        self._bot: commands.Bot = bot
        self._filter: CCProfanityFilter = CCProfanityFilter()
        self._logchannel = None

        # Create a task to initialize the logging channel separately,
        # since the bot needs to request the channel asynchronously
        self._bot.loop.create_task(self.init_log(MOD_LOG_CHANNEL))

    async def init_log(self, channel_id: int):
        """
            Voor we moderatie kunnen loggen hebben we het juiste kanaal nodig,
            maar dit is een actie die we moeten afwachten.
        """
        # Fetch the channel asynchronously
        self._logchannel = await self._bot.fetch_channel(channel_id)

    @commands.Cog.listener()
    async def on_message(self, message):
        """
            Removes messages that contain forbidden content
        """
        # Ignore messages that were sent in the logging channel
        if message.channel == self._logchannel:
            return

        if self._filter.forbidden(message.content):
            await message.delete()
            await message.channel.send(f"{message.author.mention}, dat mag je niet zeggen!")
            await self._logchannel.send(f"Bot removed a message from {message.author}.\n"
                                        f"Message: {message.content}")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """
            Kick a member from the server
        """
        await member.kick(reason=reason)
        embed = discord.Embed(title="You have been kicked!", color=0xFF5733).\
            add_field(name="Reason", value=reason)
        await member.send(embed=embed)
        embed = discord.Embed(title="Member kicked!", color=0xFF5733)\
            .add_field(name="Member", value=member)\
            .add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)
        await self._logchannel.send(f"Bot has kicked {member.display_name}.\n"
                                    f"Reason: {reason}")

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
        await self._logchannel.send(f"Bot has banned member {member.display_name}\n"
                                    f"Reason: {reason}")

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
        await self._logchannel.send(f"Bot has given member {member.display_name} a timeout.\n"
                                    f"Reason: {reason}")


async def setup(bot):
    await bot.add_cog(Moderation(bot))
