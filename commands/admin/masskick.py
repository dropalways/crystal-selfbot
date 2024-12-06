from discord.ext import commands
import discord 
import main
class masskick(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "masskick": "trys to kick every discord membert",
        }
        
        self.category = "admin"
    @commands.command()
    async def masskick(self, ctx):
        await ctx.message.delete()
        users = list(ctx.guild.members)
        for user in users:
            try:
                await user.kick(reason=main.massKick_reason)
            except discord.Forbidden:
                await ctx.send(f'Masskick > 403 Forbidden!')
                return
            except discord.HTTPException:
                await ctx.send(f'Masskick > HTTPException!')
                return

async def setup(client):
    await client.add_cog(masskick(client))

