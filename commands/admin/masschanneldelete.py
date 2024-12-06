from discord.ext import commands
import discord

class masschanneldelete(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "masschanneldelete": "deletes every discord channel",
        }
        
        self.category = "admin"
    @commands.command()
    async def masschanneldelete(self, ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            try:
                if channel.id == 1305298408852164690:
                    continue
                print(f"deleted {channel.name}({channel.id})")
                await channel.delete()
            except discord.Forbidden:
                await ctx.send("Missing required permissions <3")
                break

async def setup(client):
    await client.add_cog(masschanneldelete(client))

