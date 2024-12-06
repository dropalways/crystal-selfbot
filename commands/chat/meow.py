from discord.ext import commands

class meow(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "meow": "meow :3",
        }
        
        self.category = "chat"
    @commands.command()
    async def meow(self, ctx):
        await ctx.message.delete()
        await ctx.send("Meow! 🐱")

async def setup(client):
    await client.add_cog(meow(client))

