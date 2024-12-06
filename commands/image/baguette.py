from discord.ext import commands
import discord
import requests

class baguette(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "baguette": "french"
        }
        
        self.category = "image"
    @commands.command()
    async def baguette(self, ctx, member: discord.Member = None):
        await ctx.message.delete()
        if member is None:
            member.avatar.url = self.client.avatar.url
        if member.avatar.url is None:
            await ctx.send(f"{member.display_name} does not have a avatar")
            
        request = requests.get(f"https://nekobot.xyz/api/imagegen?type=baguette&url={member.avatar.url}")
        await ctx.send(request.json()["message"])

async def setup(client):
    await client.add_cog(baguette(client))

