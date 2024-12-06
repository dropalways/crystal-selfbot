from discord.ext import commands
import discord
import main

class nick(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "nick": "change your nickname",
        }
        
        self.category = "user"

    @commands.command()
    async def nick(self, ctx, nick: str = None, member: discord.Member = None):
        await ctx.message.delete()
        
        reset_nick = nick is None
        
        if member is None:
            member = ctx.author

        try:
            if reset_nick:
                await member.edit(nick=None)
                await ctx.send(f"""```ansi
[1;2mCrystal Selfbot - Nickname[0m
> [2;35mReset nickname![0m```""", delete_after=15)
            else:
                await member.edit(nick=nick)
                await ctx.send(f"""```ansi
[1;2mCrystal Selfbot - Nickname[0m
> [2;35mSet nickanme to {nick}![0m```""", delete_after=15)
            
            
        except discord.Forbidden:
            await ctx.send("No Permissions to change nickname!", delete_after=3) 
            print("Missing reqired Permissions.")
    

async def setup(client):
    await client.add_cog(nick(client))

    

