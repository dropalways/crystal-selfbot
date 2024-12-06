from discord.ext import commands

class voicechannel(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "voicechannel": "creates a voice channel",
        }
        
        self.category = "admin"
    @commands.command()
    async def voicechannel(self, ctx, arg):
        await ctx.message.delete()
        await ctx.guild.create_voice_channel(arg)

async def setup(client):
    await client.add_cog(voicechannel(client))

