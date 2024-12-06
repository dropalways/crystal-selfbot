from discord.ext import commands
import requests

class trap(commands.Cog):
    def __init__(self, client):
        self.client = client
        descripton  = "niggerz"
        self.command_info = {
            "trap": "EVEN MORE GAY"
        }
        
        self.category = "image"
    @commands.command()
    async def trap(self, ctx):
        await ctx.message.delete()
        request = requests.get("https://api.waifu.pics/nsfw/trap")
        image = request.json()["url"]
        await ctx.send(image)

async def setup(client):
    await client.add_cog(trap(client))

