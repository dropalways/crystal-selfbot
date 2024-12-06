from discord.ext import commands
import main
import sys
class currentconfig(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "currentconfig": "displays your current config"
        }
        
        self.category = "util"
    @commands.command()
    async def currentconfig(self, ctx):
        await ctx.message.delete()
        await ctx.send("`Config.json`")
        await ctx.send(f"`Prefix: {main.prefix}`", delete_after=10)
        await ctx.send(f"`RPC: {main.shouldrpc}`", delete_after=10)
        await ctx.send(f"`Mass Mention Size: {main.batch_sizecfg}`", delete_after=10)
        await ctx.send(f"`Mass Ban Reason: {main.massBan_reason}`", delete_after=10)
        await ctx.send(f"`Mass Kick Reason: {main.massKick_reason}`", delete_after=10)
        await ctx.send(f"```Python Version: {sys.version}```", delete_after=10)

async def setup(client):
    await client.add_cog(currentconfig(client))

