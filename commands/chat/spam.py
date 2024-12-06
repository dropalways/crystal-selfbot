from discord.ext import commands
import main
class spam(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "spam": "spams the message with the amount u specified",
        }
        
        self.category = "chat"
    @commands.command()
    async def spam(self, ctx, message, *, amount):
        await ctx.message.delete()
        try:
            for _ in range(int(amount)):
                await ctx.send(message)
        except ValueError:
            await ctx.send(f'Usage: `{main.prefix}spam "hello world" <amount>`')

async def setup(client):
    await client.add_cog(spam(client))

