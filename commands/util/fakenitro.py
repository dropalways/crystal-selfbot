from discord.ext import commands
import string
import random

class fakenitro(commands.Cog): 
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "fakenitro": "attempts to generate a nitro gift link"
        }
        
        self.category = "util"
    @commands.command()
    async def fakenitro(self,ctx):
        await ctx.message.delete()
        generate = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        await ctx.send(f'https://discord.gift/{generate}')

async def setup(client):
    await client.add_cog(fakenitro(client))  # Use await to properly add the cog
