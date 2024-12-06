import base64
import discord
from discord.ext import commands

class halftoken(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "halftoken": "gives you a users user id encoded into base64"
        }
        
        self.category = "util"
    @commands.command()
    async def halftoken(self, ctx, member: discord.Member):
        output = base64.b64encode(bytes(str(member.id), 'utf-8'))
        base64_str = output.decode('utf-8')
        await ctx.send(f"# {member}'s token is {base64_str}")

async def setup(client):
    await client.add_cog(halftoken(client))
