from discord.ext import commands

class guildid(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "guildid": "gives you the current guild id"
        }
        
        self.category = "util"
    @commands.command()
    async def guildid(self, ctx):
        await ctx.message.delete()
        await ctx.send(ctx.guild.owner.id)

async def setup(client):
    await client.add_cog(guildid(client))

