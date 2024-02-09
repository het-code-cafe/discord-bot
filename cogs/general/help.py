import discord, json
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = json.load(open('config/help.json'))

    @commands.command()
    async def help(self, ctx, pagenum=0):
        pagetitle = list(self.db)[pagenum]
        embed = self._create_embed(pagetitle, pagenum, ctx.guild.icon)
        msg = await ctx.send(embed=embed)
        await self._add_navigation_reactions(msg)

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=69, check=self._check_reaction(ctx))
            except:
                try:
                    await msg.clear_reactions()
                    break
                except:
                    break
            else:
                if str(reaction.emoji) == "◀️":
                    if not pagenum == 0:
                        pagenum -= 1
                        pagetitle = list(self.db)[pagenum]
                        embed = self._create_embed(pagetitle, pagenum, ctx.guild.icon)
                        await msg.edit(embed=embed)
                        await self._remove_reaction(reaction, user)
                        # Add back ▶️ if not on max page
                        if pagenum < len(self.db) - 1:
                            await msg.add_reaction("▶️")
                    else:
                        await self._remove_reaction(reaction, user)
                elif str(reaction.emoji) == "▶️":
                    if not pagenum == len(self.db) - 1:
                        pagenum += 1
                        pagetitle = list(self.db)[pagenum]
                        embed = self._create_embed(pagetitle, pagenum, ctx.guild.icon)
                        await msg.edit(embed=embed)
                        await self._remove_reaction(reaction, user)
                        # Add back ◀️ if not on min page
                        if pagenum > 0:
                            await msg.add_reaction("◀️")
                    else:
                        await self._remove_reaction(reaction, user)

    async def _add_navigation_reactions(self, message):
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

    async def _remove_reaction(self, reaction, user):
        try:
            await reaction.remove(user)
        except:
            pass

    def _check_reaction(self, ctx):
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        return check

    def _create_embed(self, title, pagenum, guild_icon):
        embed = discord.Embed(title=title, color=0x00ff00)
        for key, val in self.db[title].items():
            embed.add_field(name=self.bot.command_prefix + key, value=val, inline=False)
        embed.set_footer(text=f"Page {pagenum+1}/{len(self.db)}")
        embed.set_thumbnail(url=guild_icon)
        return embed

async def setup(bot):
    await bot.add_cog(Help(bot))
