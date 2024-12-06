from discord.ext import commands
import requests


class thigh(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "thigh": "i love thighs please crush my skull"
        }
        
        self.category = "image"
    @commands.command()
    async def thigh(self, ctx):
        await ctx.message.delete()
        request = requests.get("https://nekobot.xyz/api/image?type=thigh")
        image = request.json()["message"]
        await ctx.send(image)

async def setup(client):
    await client.add_cog(thigh(client))

