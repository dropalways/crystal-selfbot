from discord.ext import commands
import discord
class role(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "role": "adds the role you specified to the member you specified",
        }
        
        self.category = "admin"
    @commands.command()
    # add a role to a user haha
    async def role(ctx, member: discord.Member, role: discord.Role, *, reason="never question me again..."):
        await ctx.message.delete()
        try:
            # add roles to friends.
            await member.add_roles(role, reason=reason, atomic=True)

            # Send a confirmation message
            await ctx.send(f"role has been added to {member.mention}")
            await ctx.message.delete()
        except discord.Forbidden:
            # from the docs cus I was there lol "Forbidden – You do not have permissions to add these roles."
            await ctx.send("Missing required permissions <3")

async def setup(client):
    await client.add_cog(role(client))

