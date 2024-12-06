from discord.ext import commands
import main
class mimic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mimic(self, ctx, *, arg=None):
        await ctx.message.delete()
        self.command_info = {
            "mimic": "add someone to the mimic list",
        }
        
        self.category = "chat"
        if arg == "list":
            if main.mimiclist:
                mimic_ids = [f"<@{member_id}>" for member_id in main.mimiclist]
                await ctx.send(f"current mimic list: {', '.join(mimic_ids)}", delete_after=5)
            else:
                await ctx.send("the mimic list is empty.", delete_after=3)
            return

        if arg == "clear":
            main.mimiclist.clear()
            await ctx.send("mimic list cleared!", delete_after=3)
            return

        member = None
        if ctx.message.mentions:
            member = ctx.message.mentions[0]

        if member is None:
            await ctx.send("please mention someone! silly", delete_after=3)
            return

        if member.id in main.mimiclist:
            await ctx.send(f"removing <@{member.id}> from the mimic list", delete_after=3)
            main.mimiclist.remove(member.id)
            return

        # If the member is not in the mimic list, add them
        await ctx.send(f"added <@{member.id}> to the mimic list", delete_after=3)
        main.mimiclist.append(member.id)

async def setup(client):
    await client.add_cog(mimic(client))

