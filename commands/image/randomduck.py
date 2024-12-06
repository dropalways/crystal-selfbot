from discord.ext import commands
import random
import string
class randomduck(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "randomduck": "quack"
        }
        
        self.category = "image"
    @commands.command()
    async def randomduck(self, ctx):
        # its like this because the command doesnt send the duck
        url = f"https://random-d.uk/api/randomimg?t={''.join(random.choices(string.digits, k=13))}"  # = 13 strings
        await ctx.send(url)
                

async def setup(client):
    await client.add_cog(randomduck(client))
