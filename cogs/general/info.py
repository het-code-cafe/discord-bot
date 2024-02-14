import discord, asyncio, os, inspect
from discord.ext import commands
from collections import defaultdict

class DynamicHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, *, page: int = 1):
        """
        Display help for all commands in the bot.
        Use the page parameter to switch between sections.
        """

        # Organize commands by sections and categories
        sections = self._organize_commands()
        section_names = list(sections.keys())
        total_sections = len(section_names)

        # Adjust page number to be within bounds
        page = max(1, min(page, total_sections)) - 1
        section_name = section_names[page]
        categories = sections[section_name]

        # Create embed for the current section
        embed = self._create_section_embed(section_name, categories, page, total_sections)
        msg = await ctx.send(embed=embed)

        # Add navigation reactions if there are multiple sections
        if total_sections > 1:
            await msg.add_reaction("◀️")
            await msg.add_reaction("▶️")

        # Reaction handling for navigation with automatic deletion after timeout
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"] and reaction.message.id == msg.id

        try:
            while True:
                reaction, user = await asyncio.wait_for(self.bot.wait_for("reaction_add", check=check), timeout=120.0)
                if str(reaction.emoji) == "◀️" and page > 0:
                    page -= 1
                elif str(reaction.emoji) == "▶️" and page < total_sections - 1:
                    page += 1
                else:
                    await reaction.remove(user)
                    continue

                section_name = section_names[page]
                categories = sections[section_name]
                new_embed = self._create_section_embed(section_name, categories, page, total_sections, ctx.guild)
                await msg.edit(embed=new_embed)
                await msg.clear_reactions()
                if total_sections > 1:
                    await msg.add_reaction("◀️")
                    await msg.add_reaction("▶️")
        except asyncio.TimeoutError:
            await msg.clear_reactions()  # Optionally clear reactions first
            await msg.delete()  # Delete the message after the timeout
        except Exception as e:
            # Handle other exceptions, such as bot lacking permissions, if necessary
            await ctx.send("An error occurred, please try again later.")
            await msg.delete()  # Ensure message is deleted in case of other exceptions

        # Reaction handling for navigation
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"] and reaction.message.id == msg.id

        while True:
            try:
                reaction, user = await self.bot.wait_for("reaction_add", timeout=60.0, check=check)
            except:
                break  # Timeout or other exception

            if str(reaction.emoji) == "◀️" and page > 0:
                page -= 1
            elif str(reaction.emoji) == "▶️" and page < total_sections - 1:
                page += 1
            else:
                await reaction.remove(user)
                continue

            section_name = section_names[page]
            categories = sections[section_name]
            new_embed = self._create_section_embed(section_name, categories, page, total_sections)
            await msg.edit(embed=new_embed)
            await msg.clear_reactions()
            if total_sections > 1:
                await msg.add_reaction("◀️")
                await msg.add_reaction("▶️")

    def _organize_commands(self):
        """Organize commands by sections and categories based on cog file paths."""
        sections = defaultdict(lambda: defaultdict(list))
        for command in self.bot.commands:
            if not command.cog:
                continue  # Ignore commands not part of a cog
            cog_path = inspect.getfile(command.cog.__class__)
            # Extract section and category from cog_path, you might need to adjust this logic
            section = os.path.basename(os.path.dirname(cog_path))
            category = os.path.splitext(os.path.basename(cog_path))[0]
            sections[section][category].append(command)
        return sections

    def _create_section_embed(self, section_name, categories, page, total_sections):
        """Create an embed for a specific section, listing categories and commands with placeholder arguments."""
        embed = discord.Embed(title=f"Help: {section_name.capitalize()}", description=f"Page {page + 1} of {total_sections}", color=0x00ff00)
        for category, commands in categories.items():
            commands_list = "\n".join([self._format_command_usage(cmd) for cmd in commands])
            embed.add_field(name=category.capitalize(), value=commands_list or "No commands available", inline=True)
        return embed

    def _format_command_usage(self, command):
        """Format a command's usage string with placeholder arguments."""
        # If the command has defined usage, use it directly
        if command.usage:
            usage = f"{os.getenv('PREFIX')}{command.name} {command.usage}"
        else:
            # Attempt to generate usage based on the command's signature
            params = inspect.signature(command.callback).parameters.values()
            param_list = [f"<{param.name}>" for param in params if param.name != "self" and param.name != "ctx" and param.default is param.empty]
            usage = f"{os.getenv('PREFIX')}{command.name} {' '.join(param_list)}"
        
        return f"`{usage}`: {command.short_doc}"

async def setup(bot):
    await bot.add_cog(DynamicHelp(bot))
