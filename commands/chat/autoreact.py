from discord.ext import commands
import discord
# super dangerous
# ! ! ! ! ! ! ! ! silly code ahead ! ! ! ! ! ! ! !

class autoreaction(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.target_member=None
        self.reaction=None
        self.command_info = {
            "autoreact": "automatically reacts to the person specified",
        }
        
        self.category = "chat"

    @commands.command()
    async def autoreact(self,ctx, arg=None, emoji=None, member: discord.Member=None):
        self.target_member = member
        self.reaction_emoji = emoji
        # await ctx.send(f"Reacting to {member} with {emoji}.")
        

        if arg == "react":
            self.target_member = member
            self.reaction_emoji = emoji
            # await ctx.send(f"Reacting to {member} with {emoji}.")
            await ctx.send(
                f"""```ansi
[1;2mCrystal Selfbot - Auto React[0m
> [2;35mAuto React: ON[0m
```""",delete_after=15)     
        if arg == "off":
            self.target_member = None
            self.reaction_emoji = None
            await ctx.send(
                f"""```ansi
[1;2mCrystal Selfbot - Auto React[0m
> [2;35mAuto React: OFF[0m
```""",delete_after=15)     
             
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.target_member:
            if self.reaction_emoji:
                await message.add_reaction(self.reaction_emoji)
async def setup(client):
    await client.add_cog(autoreaction(client))
