from discord.ext import commands
import random

class coinflip(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "coinflip": "head or tails?",
        }
        
        self.category = "fun"
    @commands.command()
    async def coinflip(self,ctx):
        await ctx.message.delete()
        
        randomint = random.randint(1, 2)
        result = "heads" if randomint == 1 else "tails"
        
        await ctx.send(f"it landed.. on ... {result} !!")

async def setup(client):
    await client.add_cog(coinflip(client))