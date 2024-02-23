import discord
from helpers import imgur

DISCORD_COLORS = {
    'blurple': 0x5865F2,
    'green': 0x57F287,
    'yellow': 0xFEE75C,
    'fuchsia': 0xEB459E,
    'red': 0xED4245,
    'grey': 0x4a4c51
}


async def imgur_command(ctx, search_term: str, emoji: str, color: int = 0x000000):
    img_url, title = imgur.imgur_search(search_term)
    if img_url is not None:
        embed = discord.Embed(title=f"{emoji} {title}", color=color)
        embed.set_image(url=img_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"We konden {search_term} niet vinden op imgur :(")