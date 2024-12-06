from discord.ext import commands
import discord
import main
class ban(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "ban": "bans a specified member",
        }
        
        self.category = "admin"
    @commands.command()
    async def ban(self, ctx, member: discord.Member = None, reason: str = None):
        await ctx.message.delete()
        try:
            if member is None:
                raise ValueError(f"`Usage: {main.prefix}ban <member> [reason]`")
            if reason is None or reason == "":
                await ctx.guild.ban(member)
                await ctx.send(f"banned {member.name}", delete_after=3, delete_message_seconds=0)
            else:
                await ctx.guild.ban(member, reason=reason, delete_message_seconds=0)
                await ctx.send(f"banned {member.name} for: {reason}", delete_after=3)

        except ValueError as e:
            await ctx.send(str(e), delete_after=main.delete_timer)
        except discord.Forbidden:
            await ctx.send("Missing Permissions.", delete_after=3)
        except discord.NotFound:
            await ctx.send("Member could not be Found.", delete_after=3)

async def setup(client):
    await client.add_cog(ban(client))
