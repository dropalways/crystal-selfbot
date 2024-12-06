from discord.ext import commands
import os

class cmd(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "opencmd": "opens command prompt",
        }        
        self.category = "util"

    @commands.command()
    async def cmd(self, ctx):
        await ctx.message.delete()
        await ctx.send(
                f"""```ansi
[1;2mCrystal Selfbot - Command Prompt[0m
> [2;35mOpened Command Prompt window![0m
```""",delete_after=15)            
        os.system(f'start "" "C:\\Windows\\system32\\cmd.exe"')
async def setup(client):
    await client.add_cog(cmd(client))

