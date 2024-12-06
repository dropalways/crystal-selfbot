from discord.ext import commands

class massnick(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "massnick": "mass change nicknames in the guild with a specified name.",
        }
        self.category = "admin"

    @commands.command()
    async def massnick(self, ctx, nick=None):
        await ctx.message.delete()
        try:
            members = ctx.guild.members 
            for member in members:
                if member != self.client.user:
                    await member.edit(nick=nick)
        except Exception as e:
            await ctx.send(e)
async def setup(client):
    await client.add_cog(massnick(client))
