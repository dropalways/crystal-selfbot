from discord.ext import commands
import requests
import main

main.config = main.utils.load_json("config.json")
whois_apiKey = main.config.get("whois_api_key")

class whois(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "domainwhois": "uses the whois api to lookup a domain/ip"
        }
        
        self.category = "util"
    @commands.command()
    async def whois(self,ctx, domain):
        url = f'https://api.ip2whois.com/v2?key={whois_apiKey}&domain={domain}'
        headers = {"accept": "/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en-CH;q=0.9,en-GB;q=0.8",
        "content-length": "0",
        "origin": "https://google.com",
        "referer": "https://google.com",
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
                    whoisinfo_ = (
                        f"`domain: {data.get('domain', 'N/A')}`\n"
                        f"`domain id: {data.get('domain_id', 'N/A')}`\n"
                        f"`status: {data.get('status', 'N/A')}`\n"
                        f"`creation date: {data.get('create_date', 'N/A')}`\n"
                        f"`update date: {data.get('update_date', 'N/A')}`\n"
                        f"`expire date: {data.get('expire_date', 'N/A')}`\n"
                        f"`domain age: {data.get('domain_age', 'N/A')}`\n"
                        f"`whois server: {data.get('whois_server', 'N/A')}`\n"
                        f"`iana id: {data.get('iana_id', 'N/A')}`\n"
                        f"`name: {data.get('name', 'N/A')}`\n"
                        f"`registrar url: {data.get('url', 'N/A')}`\n"
                    )
                    await ctx.send(f"> Whois:\n{whoisinfo_}")
            except ValueError as e:
                await ctx.send(rq)

async def setup(client):
    await client.add_cog(whois(client))

