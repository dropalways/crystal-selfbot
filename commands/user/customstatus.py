from discord.ext import commands
import discord
import main
class customstatus(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "customstatus": "changes your discord presence to custom ones"
        }
        
        self.category = "user"
    @commands.command()
    async def customstatus(self, ctx, arg, message):
        await ctx.message.delete()

        if arg == "help":
            if message == "help":
                    await ctx.send("```Crystal Selfbot - Custom Status - Help```")
                    await ctx.send(f"```Playing (usage: {main.prefix}customstatus playing [""Details""] ) info: Sets a playing status.```")
                    await ctx.send(f"```listening (usage: {main.prefix}customstatus listening [""Details""] ) info: Sets a listening status.```")
                    await ctx.send(f"```watching (usage: {main.prefix}customstatus watching [""Details""] ) info: Sets a watching status.```")
                    await ctx.send(f"```Streaming (usage: {main.prefix}customstatus streaming [""Details""] ) info: Sets a streaming status.```")

        if arg == "playing":
            await self.client.change_presence(activity=discord.Game(name=message))
        if arg == "listening":
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message))  
        if arg == "watching":
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=message))
        if arg == "streaming":
            await ctx.send("# Streaming Status Set!")
            await self.client.change_presence(activity = discord.Streaming(
            name = message, url = "https://twitch.tv/crystalselfbot")) 
            # if anyone of u can fix this that wud be amazing! listening and watching statuses dont work and the error i get is 
            # discord.ext.commands.errors.CommandInvokeError: Command raised an exception: TypeError: MessageToDict() got an unexpected keyword argument 'including_default_value_fields'

async def setup(client):
    await client.add_cog(customstatus(client))
