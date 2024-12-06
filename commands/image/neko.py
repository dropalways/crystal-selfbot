from discord.ext import commands
import utils
import main
class neko(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "neko": "cute neko girls"
        }
        
        self.category = "image"
    @commands.command()
    async def neko(self, ctx, arg):
        await ctx.message.delete()
        if arg is None:
            image = utils.waifu_pics(profanity="sfw", category="neko")
        elif arg == "nsfw":
            image = utils.waifu_pics(profanity="nsfw", category="neko")
        elif arg == "sfw":
            image = utils.waifu_pics(profanity="sfw", category="neko")
        else:
            ctx.send(f"invalid argument usage: `{main.prefix}neko nsfw/sfw`")
            
        await ctx.send(image)

async def setup(client):
    await client.add_cog(neko(client))

