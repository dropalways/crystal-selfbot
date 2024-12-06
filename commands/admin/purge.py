from discord.ext import commands
import discord
class purge(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "purge": "deletes the amount of messages of the specified amount",
        }
        
        self.category = "admin"
    @commands.command()
    async def purge(self, ctx, count=None):
        await ctx.message.delete()

        if count == None or count == 0:
            await ctx.send("please add a numba", delete_after=3)
            return

        async for message in ctx.channel.history(limit=int(count)):
            try:
                await message.delete()
            except discord.Forbidden:
                await ctx.send("Missing required permissions <3")
                break

async def setup(client):
    await client.add_cog(purge(client))

