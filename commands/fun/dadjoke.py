from discord.ext import commands
import requests

class dadjoke(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "dadjoke": "HAHAH DAD JOKE 😂",
        }
        
        self.category = "fun"
    @commands.command()
    async def dadjoke(self, ctx):
        await ctx.message.delete()
        max_retries = 5
        for _ in range(max_retries):
            url = "https://icanhazdadjoke.com/" # it limk!!!!!!
            response = requests.get(url, headers={"Accept": "application/json"})

            if response.status_code == 200:
                joke = response.json().get("joke")
                await ctx.send(joke)
                return

async def setup(client):
    await client.add_cog(dadjoke(client))
