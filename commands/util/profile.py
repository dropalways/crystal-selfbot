from discord.ext import commands
import main
import discord
import requests
class profile(commands.Cog):
    def __init__(self, client):
        self.client = client
        
        self.command_info = {
            "profile": "gives you information about a users profile"
        }
        
        self.category = "util"
    @commands.command()
    async def profile(self,ctx, member: discord.Member = None):
        if member is None:
            member = self.client.id
        else:
            brooke = member.id
        url = f'https://discord.com/api/v9/users/{brooke}/profile'
        print(f"user id = {brooke}")

        headers = {"accept": "/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en-CH;q=0.9,en-GB;q=0.8",
        "authorization": main.token,
        "content-length": "0",
        "origin": "https://discord.com",
        "referer": "https://discord.com/channels/@me",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.669 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "hu",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42NjkiLCJvc192ZXJzaW9uIjoiMTAuMC4xOTA0MyIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzMwOTgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        rq = requests.get(url, headers=headers)
        print(f"request = {rq}")

        if rq.status_code == 200:
            # parsing the json data
            try:
                data = rq.json()

                # searching for only the name and bio
                user_profile = data.get("user", {})
                if user_profile:
                    user_info = (
                        f"`Display Name: {user_profile.get('global_name', 'N/A```')}\n"
                        f"`name: {user_profile.get('username', 'N/A`')}\n"
                        f"`about: {user_profile.get('bio', 'N/A`')}\n"
                        f"`Pronouns: {user_profile.get('pronouns', 'N/A`')}\n"
                        f"`Profile Color Accent: {user_profile.get('accent_color', 'N/A`')}\n"
                        f"`https://cdn.discordapp.com/avatars/{brooke}/{user_profile.get('avatar', 'N/A')}.webp?size=96`"
                    )
                    await ctx.send(f"info :\n{user_info}")
            except ValueError as e:
                ctx.send(rq)

async def setup(client):
    await client.add_cog(profile(client))
