from discord.ext import commands
import requests


class tentacle(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "tentacle": "tentacle shi"
        }
        
        self.category = "image"
    @commands.command()
    async def tentacle(self, ctx):
        await ctx.message.delete()
        request = requests.get("https://nekobot.xyz/api/image?type=tentacle")
        image = request.json()["message"]
        await ctx.send(image)

async def setup(client):
    await client.add_cog(tentacle(client))

