from discord.ext import commands

class textchannel(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "textchannel": "creats a text channel with the specified name",
        }
        
        self.category = "admin"
    @commands.command()
    async def textchannel(self, ctx, arg):
        await ctx.message.delete()
        await ctx.guild.create_text_channel(arg)

async def setup(client):
    await client.add_cog(textchannel(client))

