from discord.ext import commands
import discord
import re
from datetime import timedelta

class timeout(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "timeout": "timeouts the user you mentioned with the time",
        }
        
        self.category = "admin"
    @commands.command()
    async def timeout(self, ctx, member: discord.Member, duration: str):
        await ctx.message.delete()
        duration_pattern = re.match(r'(\d+)(s|m|h|d)', duration)
        
        if not duration_pattern:
            await ctx.send("invalid duration format only '10s', '30m', '2h', or '7d' are supported")
            return

        time_value, time_unit = duration_pattern.groups()
        time_value = int(time_value)

        if time_unit == 's':
            timeout_duration = time_value
        elif time_unit == 'm':
            timeout_duration = time_value * 60
        elif time_unit == 'h':
            timeout_duration = time_value * 60 * 60
        elif time_unit == 'd':
            timeout_duration = time_value * 60 * 60 * 24

        timeout_end = discord.utils.utcnow() + timedelta(seconds=timeout_duration)

        # Convert the timeout end time to a Unix timestamp
        timeout_timestamp = int(timeout_end.timestamp())

        try:
            await member.timeout(timeout_end)
            await ctx.send(f"{member.mention} has been timed out for {duration} they will be untimed out <t:{timeout_timestamp}:R>")
        except discord.Forbidden:
            await ctx.send("no perms")
        except discord.NotFound:
            await ctx.send("member not found")
        except Exception as e:
           print(f"An error occurred: {e}")
            
        

async def setup(client):
    await client.add_cog(timeout(client))

