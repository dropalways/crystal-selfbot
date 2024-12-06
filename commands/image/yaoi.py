from discord.ext import commands
import requests

class yaoi(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "yaoi": "gayyyyy"
        }
        
        self.category = "image"
    @commands.command()
    async def yaoi(self, ctx):
        await ctx.message.delete()
        request = requests.get("https://nekobot.xyz/api/image?type=yaoi")
        image = request.json()["message"]
        await ctx.send(image)

async def setup(client):
    await client.add_cog(yaoi(client))

