from discord.ext import commands    
import main
class category(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "category": "creates a category with the name specified",
        }
        
        self.category = "admin"
    @commands.command()
    async def category(self, ctx, arg: str =None):
        try:
            if arg is None: 
                raise ValueError(f"`Usage: {main.prefix}category <name>`")                
            await ctx.message.delete()
            await ctx.guild.create_category(arg)

        except ValueError as e:
            await ctx.send(str(e), delete_after=main.delete_timer)

async def setup(client):
    await client.add_cog(category(client))
