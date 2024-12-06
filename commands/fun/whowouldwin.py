import random
import discord
from discord.ext import commands

class whowouldwin(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "whowouldwin": "who would win this guy or this guy??",
        }
        
        self.category = "fun"
    @commands.command()
    async def whowouldwin(self,ctx,member1,member2):
        await ctx.message.delete()
        whowouldwin = random.randint(1,2)

        if whowouldwin == 1:
            await ctx.send(f"Who would Win? {member1} would win!")
        else:
            await ctx.send(f"Who Would Win? {member2} would win!")
          
async def setup(client):
    await client.add_cog(whowouldwin(client))
