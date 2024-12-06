from discord.ext import commands
import random
import requests

class httpduck(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "httpduck": "quack"
        }
        
        self.category = "image"
    @commands.command()
    async def httpduck(self, ctx):
        while True:
            code = random.choice(range(100, 500))
            url = f"https://random-d.uk/api/http/{code}.jpg"
            response = requests.head(url)
            if response.status_code == 200:
                await ctx.send(url)
                break

async def setup(client):
    await client.add_cog(httpduck(client))
