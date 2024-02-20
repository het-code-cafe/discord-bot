from discord.ext import commands


class ErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send(f"An error occurred: {error.original}")
        # Handle other errors or re-raise them if not handled
        else:
            raise error


async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))
