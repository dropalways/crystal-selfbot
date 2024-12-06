from discord.ext import commands
import requests
class iplookup(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "iplookup": "gives you information about a ip"
        }
        
        self.category = "util"

    @commands.command()
    async def iplookup(self,ctx, ip):
        url = f'http://ip-api.com/json/{ip}'

        headers = {"accept": "/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en-CH;q=0.9,en-GB;q=0.8",
        "content-length": "0",
        "origin": "https://whatismyipaddress.com",
        "referer": "https://whatismyipaddress.com/ip/",
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
                print(f"data: {data}")
                if data:
                    ipinfo_ = (
                        f"`ip: {data.get('query', 'N/A')}`\n"
                        f"`status: {data.get('status', 'N/A')}`\n"
                        f"`city: {data.get('city', 'N/A')}`\n"
                        f"`country: {data.get('country', 'N/A')}`\n"
                        f"`countrycode: {data.get('countryCode', 'N/A')}`\n"
                        f"`region: {data.get('region', 'N/A')}`\n"
                        f"`isp: {data.get('isp', 'N/A')}`\n"



                    )
                    await ctx.send(f"> Crystal Selfbot:\n{ipinfo_}")
            except ValueError as e:
                ctx.send(rq)

async def setup(client):
    await client.add_cog(iplookup(client))

