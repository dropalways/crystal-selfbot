from discord.ext import commands

class serverbanner(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "serverbanner": "servericon but instead of icon its banner"
        }
        
        self.category = "image"
    @commands.command()
    async def serverbanner(self, ctx):
        await ctx.message.delete()

        banner = ctx.guild.banner

        if banner is None:
            await ctx.send("server has no banner")
        else:
            await ctx.send(banner.url)

async def setup(client):
    await client.add_cog(serverbanner(client))

