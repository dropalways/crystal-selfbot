from discord.ext import commands
import discord
class masschannel(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "masschannel": "creates a specified amount of channels with the name being specified",
        }
        
        self.category = "admin"
    @commands.command()
    async def masschannel(self, ctx, count: int = None, name: str = None):
        await ctx.message.delete()

        if count == None or count == 0:
            await ctx.send("please add a numba", delete_after=3)
            return

        if name == None:
            await ctx.send("please add a name", delete_after=3)
            return

        for _ in range(int(count)):
            try:
                await ctx.guild.create_text_channel(name=f"{name}")

            except discord.Forbidden:
                await ctx.send("Missing required permissions <3")
                break

async def setup(client):
    await client.add_cog(masschannel(client))

