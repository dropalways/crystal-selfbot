import discord
from discord.ext import commands
import os
import aiohttp

class Command(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "avatar": "sends avatar of the specified user",
        }
        
        self.category = "image"
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            url = self.client.avatar.url
        url = member.display_avatar.url

        saveAs = f"{member.name}_avatar.png"
        saveTo = "data/saved_avatars"
        
        os.makedirs(saveTo, exist_ok=True)
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    file_path = f"{saveTo}/{saveAs}"

                    with open(file_path, "wb") as file:
                        file.write(await response.read())

                    await ctx.send(f"{member.display_avatar.url} - saved to {file_path}")

async def setup(client):
    await client.add_cog(Command(client))