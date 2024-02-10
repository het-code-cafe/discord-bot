import discord
from discord.ext import commands

class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """
        Sends a welcome message when a member joins the server
        """
        channel = member.guild.system_channel
        if channel is not None:
            embed = discord.Embed(
                title="Welkom bij Code-Cafe!",
                description=f"Leuk dat je er bent {member.mention}! 👋",
                color=discord.Color.green()
            )
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Welcomer(bot))