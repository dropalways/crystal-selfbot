from discord.ext import commands
import asyncio 
class abc(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "abc": "says the alphabet",
        }
        
        self.category = "chat"
    @commands.command()
    async def abc(self, ctx):
        await ctx.message.delete()
        TEXT = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z :tada:']
        message = await ctx.send(TEXT[0])
        for _next in TEXT[1:]:
            await message.edit(content=_next)
            await asyncio.sleep(1)

async def setup(client):
    await client.add_cog(abc(client))

