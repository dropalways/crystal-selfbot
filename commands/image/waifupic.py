from discord.ext import commands
import utils

class waifupic(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "waifupic": "generates a image from the waifu.pics api using the args"
        }
        
        self.category = "image"
    @commands.command()
    async def waifupic(self, ctx, profanity, category):
        await ctx.message.delete()
        if profanity is None:
            await ctx.send("profanity is invalid")
        if category is None:
            await ctx.send("category is invalid")
            
        await ctx.send(utils.waifu_pics(profanity,category))

async def setup(client):
    await client.add_cog(waifupic(client))

