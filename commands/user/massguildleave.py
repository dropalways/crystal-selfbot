from discord.ext import commands
import main

class massguildleave(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "massguildleave": "go home"
        }
        
        self.category = "user"
    @commands.command()
    async def massguildleave(self, ctx):
        for guild in self.client.guilds:
            try:
                if guild.id not in main.keepserver:
                    server = self.client.get_guild(guild.id)
                    await server.leave()
            except Exception as exception:
                print(exception)

async def setup(client):
    await client.add_cog(massguildleave(client))
