from discord.ext import commands
import random
import requests

class httpcat(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "httpcat": "meow"
        }
        
        self.category = "image"
    @commands.command()
    async def httpcat(self, ctx):
        while True:
            code = random.choice(range(100, 599))
            url = f"https://http.cat/{code}.jpg"
            response = requests.head(url)
            if response.status_code == 200:
                await ctx.send(url)
                break

async def setup(client):
    await client.add_cog(httpcat(client))
