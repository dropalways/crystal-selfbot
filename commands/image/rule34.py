from aiorule34 import rule34get as r34get
from discord.ext import commands

class rule34(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "rule34": "generates a image from the rule34 api"
        }
        
        self.category = "image"        
    @commands.command()
    async def rule34(self, ctx, theme, character):
        await ctx.message.delete()

        async for post in r34get([f'{theme}',f'{character}']):
            await ctx.send(post.url)
            return

async def setup(client):
    await client.add_cog(rule34(client))
