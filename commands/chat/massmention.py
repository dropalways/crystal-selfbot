from discord.ext import commands
import discord

class massmention(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "massmention": "attempts to mention the entire server",
        }
        
        self.category = "chat"
    @commands.command()
    async def massmention(self, ctx, arg):
        await ctx.message.delete()
        try:
            arg = int(arg)
        except ValueError:
            await ctx.send("invalid batch size")
            return
        if arg <= 0:
            await ctx.send("batch size gotta be bigger than 0")
            return
        batch_size = arg
        batch = []
        members = [member for member in ctx.guild.members if not member.bot]
        for member in members:
            if member.id == self.client.user.id:
                continue
            batch.append(f"<@{member.id}>")
            
            if len(batch) >= batch_size or len(" ".join(batch)) > 2000:
                try:
                    await ctx.send(" ".join(batch))
                except discord.errors.HTTPException as e:
                    if "exceeds the mention limit" in str(e):
                        await ctx.send("flagged automod #DTC")
                        return
                    else:
                        print(f"error: {e}")
                    break
                
                batch = []

        if batch:
            try:
                await ctx.send(" ".join(batch))
            except discord.errors.HTTPException as e:
                if "exceeds the mention limit" in str(e):
                    await ctx.send("flagged automod")
                else:
                    print(f"error: {e}")

async def setup(client):
    await client.add_cog(massmention(client))

