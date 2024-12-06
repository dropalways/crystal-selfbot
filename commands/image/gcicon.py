from discord.ext import commands
import discord
class gcicon(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "gcicon": "sends the icon of the groupchat"
        }
        
        self.category = "image"
    @commands.command()
    async def gcicon(self, ctx):
        await ctx.message.delete()
        if isinstance(ctx.channel, discord.GroupChannel):
            icon = ctx.channel.icon.url
            if icon is None:
                await ctx.send("this groupchat does not have an icon")
            else:
                await ctx.send(icon)
        else:
            await ctx.send("you cant use gcicon in a non group chat")

async def setup(client):
    await client.add_cog(gcicon(client))

