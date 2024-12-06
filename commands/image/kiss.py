from discord.ext import commands
import requests
import nekos
import discord
import shutil
import os

class kiss(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "kiss": "mwah"
        }
        
        self.category = "image"
    @commands.command()
    # i neeed a k kk isss.....
    async def kiss(self, ctx, member: discord.Member = None):
        fortnite = requests.get(nekos.img("kiss"), stream=True)
        with open("temp/kiss.gif", 'wb') as battlePass:
            shutil.copyfileobj(fortnite.raw, battlePass)

        await ctx.message.delete()
        if member is None:
            await ctx.send(nekos.img("kiss"))
            return
        await ctx.send(f"<@{member.id}>", file=discord.File("temp/kiss.gif"))
        os.remove("temp/kiss.gif")

async def setup(client):
    await client.add_cog(kiss(client))

