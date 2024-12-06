from discord.ext import commands
import discord
import main
class kick(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "kick": "kicks a specified member",
        }
        
        self.category = "admin"
    @commands.command()
    async def kick(self, ctx, member: discord.Member=None, reason: str = None):
        await ctx.message.delete()
        try:
            if member is None:
                raise ValueError(f"`Usage: {main.prefix}kick <member> [reason]`")
                if reason is None or reason == "":
                    await ctx.guild.kick(member)
                    await ctx.send(f"kicked {member.name}", delete_after=main.delete_timer)
                else:
                    await ctx.guild.kick(member, reason=reason)
                    await ctx.send(f"kicked {member.name} for: {reason}", delete_after=main.delete_timer)
        except ValueError as e:
            await ctx.send(str(e), delete_after=main.delete_timer)
        except discord.Forbidden:
            await ctx.send("Missing Permissions", delete_after=3)
        except discord.NotFound:
            await ctx.send("Member could not be Found.", delete_after=3)
        except Exception as e:
           print(f"An error occurred: {e}")

async def setup(client):
    await client.add_cog(kick(client))

