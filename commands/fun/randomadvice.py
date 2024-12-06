from discord.ext import commands
import random
import requests

class randomadvice(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "randomadvice": "gives you random advice",
        }
        
        self.category = "fun"
    @commands.command()
    async def randomadvice(self, ctx):
        max_retries = 5 
        for _ in range(max_retries): 
            number = random.randint(1, 200) # 1 to 200 because random advice is only dat!
            url = f"https://api.adviceslip.com/advice/{number}"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                advice = data.get("slip", {}).get("advice")
                if advice:
                    await ctx.send(f"Advice #{number}: {advice}")
                    return

async def setup(client):
    await client.add_cog(randomadvice(client))
