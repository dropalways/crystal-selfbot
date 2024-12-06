from discord.ext import commands

class codeblock(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "codeblock": "sends your message in a codeblock",
        }
        
        self.category = "chat"
    @commands.command()
    async def codeblock(self,ctx, message):
        await ctx.message.delete()
        await ctx.send(f"```{message}```")

async def setup(client):
    await client.add_cog(codeblock(client))

