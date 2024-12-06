from discord.ext import commands
import asyncio
import main
### dangerous codes ahead ### 
afkmessage = main.config.get("afk_message")

class afk(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.afkx = None  

    async def listener(self, ctx):
        while True:
            try:
                def check(msg):
                    return msg.mentions and self.client.user in msg.mentions

                message = await self.client.wait_for('message', timeout=10, check=check)
                await message.channel.send(
            f"""```ansi
[1;2mAFK[0m
> [2;35m{afkmessage}[0m
            ```""")            
            except asyncio.TimeoutError:
                pass

    @commands.command()
    async def afk(self, ctx, arg):
        if arg == "on":
            if self.afkx is None:  
                await ctx.message.delete()
            await ctx.send(
                f"""```ansi
[1;2mCrystal Selfbot - AFK[0m
> [2;35mAFK is now ON[0m
```""",delete_after=25)                
            self.afkx = asyncio.create_task(self.listener(ctx))

        elif arg == "off":
            if self.afkx is not None:  
                self.afkx.cancel()
                self.afkx = None
                await ctx.message.delete()
            await ctx.send(
                f"""```ansi
[1;2mCrystal Selfbot - AFK[0m
> [2;35mAFK is now OFF[0m
```""",delete_after=25)
async def setup(client):
    await client.add_cog(afk(client))
