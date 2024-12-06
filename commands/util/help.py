from discord.ext import commands
import main

class help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "help": "shows this command"
        }
        
        self.category = "util"
    
    
    @commands.command()
    async def help(self, ctx, category: str = None):
        help_message = ""
        displayed_categories = set()
    
        if category is None:
            help_message = f"""```ansi
[1;2m[0m[2;35m[0m[1;2mCrystal Selfbot[0m\n"""
            for cog_name, cog in self.client.cogs.items():
                if hasattr(cog, 'command_info') and cog.category not in displayed_categories:
                    displayed_categories.add(cog.category)
                    help_message += f"[0m> [2;35m{cog.category}[0m < [2;37m([2;37m{main.prefix}help {cog.category}[0m)\n"
        else:
            found_category = False
            for cog_name, cog in self.client.cogs.items():
                if hasattr(cog, 'command_info') and cog.category.lower() == category.lower():
                    found_category = True
                    help_message = f"""```ansi
[1;2m[0m[2;35m[0m[1;2mCrystal Selfbot[0m\n"""
                    break
            
            if found_category:
                for cog_name, cog in self.client.cogs.items():
                    if hasattr(cog, 'command_info') and cog.category.lower() == category.lower():
                        for command_name, description in cog.command_info.items():
                            help_message += f"[0m> [2;35m{command_name}[0m < [2;37m{description}\n"
            else:
                help_message = f"No commands found for category '{category}'. Make sure you've entered the correct category name."
        await ctx.send(help_message + "```")

async def setup(client):
    await client.add_cog(help(client))
