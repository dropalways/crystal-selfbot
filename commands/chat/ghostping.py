from discord.ext import commands

class ghostping(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "ghostping": "just deletes the message",
        }
        
        self.category = "chat"
    @commands.command()
    async def ghostping(self, ctx):
        await ctx.message.delete()


async def setup(client):
    await client.add_cog(ghostping(client))
