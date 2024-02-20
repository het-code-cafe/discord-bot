import discord
from helpers import imgur


async def imgur_command(ctx, search_term: str, emoji: str, color: int = 0x000000):
    img_url, title = imgur.imgur_search(search_term)
    if img_url is not None:
        embed = discord.Embed(title=f"{emoji} {title}", color=color)
        embed.set_image(url=img_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"We konden {search_term} niet vinden op imgur :(")