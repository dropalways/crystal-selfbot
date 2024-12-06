from discord.ext import commands
import os,sys
class reboot(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        self.command_info = {
            "reboot": "reboots the bot"
        }
        
        self.category = "util"
    @commands.command()
    async def reboot(self, ctx):
        await ctx.message.delete()
        await ctx.send("# Crystal Selfbot is Rebooting...")
        await os.execv(sys.executable, ['python'] + sys.argv)

async def setup(client):
    await client.add_cog(reboot(client))

