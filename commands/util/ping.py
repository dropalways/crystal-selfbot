from discord.ext import commands
import time

class ping(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        self.command_info = {
            "ping": "notch made dis shi"
        }
        
        self.category = "util"
    @commands.command()
    async def ping(self,ctx):
        await ctx.message.delete()

        before = time.monotonic()
        message = await ctx.send("Ping > Pinging...")
        ping = (time.monotonic() - before) * 1000

        await message.edit(content=f"# Pong: {int(ping)} ms")

async def setup(client):
    await client.add_cog(ping(client))

