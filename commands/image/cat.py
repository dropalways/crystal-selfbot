from discord.ext import commands
import nekos

class cat(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "cat": "sends a random cat"
        }
        
        self.category = "image"
    @commands.command()
    async def cat(self, ctx):
        await ctx.message.delete()
        await ctx.send(nekos.cat())

async def setup(client):
    await client.add_cog(cat(client))

