from discord.ext import commands

class test(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        self.command_info = {
            "test": "test command"
        }
        
        self.category = "util"
        
    @commands.command()
    async def test(self, ctx):
        print("test working")
        await ctx.message.delete()

async def setup(client):
    await client.add_cog(test(client))

