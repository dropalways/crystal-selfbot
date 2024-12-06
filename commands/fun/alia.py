from discord.ext import commands
import requests
import shutil
import discord
import os

class alia(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "alia": "ali A funny Lmaoooooooooooooooooooooooooo",
        }
        
        self.category = "fun"
    @commands.command()
    async def alia(self, ctx):
        # Erm so basically this code is like fine or whatever, but I want to show u how to download from somewhere else (so it doesn't take up space)
        await ctx.message.delete()
        # This is like when you click on a download button u send a get request (like this)
        song_link = requests.get(
            "https://github.com/ilovebiting/IMAGES/raw/refs/heads/main/alia.mp3", stream=True)
        # And after you click a download button you get a screen asking you what you want to save it as, this is the same thing as that but with text you feel me
        with open("temp/alia.mp3", 'wb') as downloadingSong:
            # For some reason has a warning? always works though ...!
            shutil.copyfileobj(song_link.raw, downloadingSong)
        # this is UR code and u wrote it...
        await ctx.send(file=discord.File("temp/alia.mp3"))
        await ctx.send("listen pls !:ribbon:")
        # Deleting the file here to save space
        os.remove("temp/alia.mp3")

async def setup(client):
    await client.add_cog(alia(client))

