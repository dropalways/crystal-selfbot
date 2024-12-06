from discord.ext import commands
import string
import random

class finderservers(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "findservers": "attempts to finds discord servers"
        }
        
        self.category = "util"
    @commands.command()
    async def findservers(self, ctx):
        await ctx.message.delete()
        server = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        await ctx.send(f'https://discord.gg/{server}')

async def setup(client):
    await client.add_cog(finderservers(client))

