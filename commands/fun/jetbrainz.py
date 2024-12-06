from discord.ext import commands

class jetbrainz(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "jetbrainz": "I C she Lion giving others jet Brainz I just gotta Rider Along",
        }
        
        self.category = "fun"
    @commands.command()
    async def jetbrainz(self,ctx):
        await ctx.send("I C she Lion giving others jet Brainz I just gotta Rider Along")

async def setup(client):
    await client.add_cog(jetbrainz(client))
