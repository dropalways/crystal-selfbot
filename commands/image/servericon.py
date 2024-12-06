from discord.ext import commands

class servericon(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "servericon": "sends the icon of the server the command was executed in"
        }
        
        self.category = "image"
    @commands.command()
    async def servericon(self, ctx):
        await ctx.message.delete()

        icon = ctx.guild.icon

        if icon is None:
            await ctx.send("server has no icon")
        else:
            await ctx.send(icon.url)

async def setup(client):
    await client.add_cog(servericon(client))

