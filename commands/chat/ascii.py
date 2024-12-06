
from discord.ext import commands
import pyfiglet
class ascii(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "ascii": "sends ascii art of the mesage you specified",
        }
        
        self.category = "chat"
    @commands.command()
    async def ascii(self, ctx, message, arg):
        text = pyfiglet.figlet_format(f"{message}", font = arg)
        await ctx.send(f"```{text}```")

        if arg == pyf[1]:
            meow = True           


async def setup(client):
    await client.add_cog(ascii(client))

pyf = pyfiglet.FigletFont.getFonts()

