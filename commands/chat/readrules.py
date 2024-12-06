from discord.ext import commands
import asyncio
class readrules(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "readrules": "read the rules man",
        }
        
        self.category = "chat"
    @commands.command()
    async def readrules(self, ctx):
        await ctx.message.delete()

        readrules = ['read', 'the', 'rules', 'read the', 'read the rules', 'READ',
                    'THE', 'RULES', '# READ', '# THE', '# RULES', '# READ THE FUCKING RULES']

        message = await ctx.send(readrules[0])

        for _next in readrules[1:]:
            await message.edit(content=_next)
            await asyncio.sleep(1)

async def setup(client):
    await client.add_cog(readrules(client))

