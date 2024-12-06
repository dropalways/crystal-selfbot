from discord.ext import commands
import requests
import nekos
import discord
import shutil
import os

class pat(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "pat": "head pats"
        }
        
        self.category = "image"
    @commands.command()
    # please give me headpats
    async def pat(self, ctx, member: discord.Member = None):
        fortnite = requests.get(nekos.img("pat"), stream=True)
        with open("temp/pat.gif", 'wb') as battlePass:
            # shows error saying it's not going to work for me, but it's fine
            shutil.copyfileobj(fortnite.raw, battlePass)

        await ctx.message.delete()
        if member is None:
            await ctx.send(nekos.img("pat"))
            return
        await ctx.send(f"<@{member.id}>", file=discord.File("temp/pat.gif"))
        os.remove("temp/pat.gif")

async def setup(client):
    await client.add_cog(pat(client))

