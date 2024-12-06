from discord.ext import commands
import requests

class UrbanDictionary(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "urbandictonary": "gives you a description of the specified word",
        }
        
        self.category = "fun"

    @commands.command()
    async def urbandictionary(self, ctx, *, word):
        url = f'https://api.urbandictionary.com/v0/define?term={word}'

        headers = {
            "accept": "/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en-CH;q=0.9,en-GB;q=0.8",
            "content-length": "0",
            "origin": "google.com",
            "referer": "google.com",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.669 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "hu",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42NjkiLCJvc192ZXJzaW9uIjoiMTAuMC4xOTA0MyIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoxMzMwOTgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }

        get = requests.get(url, headers=headers)
        print(f"request = {get}")

        if get.status_code == 200:
            try:
                data = get.json()
                if data and "list" in data and len(data["list"]) > 0:
                    entry = data["list"][0]
                    urbandictionary = (
                    f"Definition: `{entry.get('definition', 'N/A')}`\n"
                    f"`Example: {entry.get('example', 'N/A')}`\n"
                    f"`Word: {word}`\n"
                    f"`Thumbs Up: {entry.get('thumbs_up', 0)}`\n"
                    f"`Thumbs Down: {entry.get('thumbs_down', 0)}`\n"
                    f"`Permalink: {entry.get('permalink', 'N/A')}`\n"
                    f"`Written On: {entry.get('written_on', 'N/A')}`\n"
                    f"`Author: {entry.get('author', 'N/A')}`"
                    )
                    await ctx.send(f"> Urban Dictionary:\n{urbandictionary}")
                else:
                    await ctx.send(f"No results found for `{word}`.")
            except ValueError as e:
                await ctx.send(f"An error occurred while parsing the response: {e}")
        else:
            await ctx.send(f"Error: Received status code {get.status_code}.")

async def setup(client):
    await client.add_cog(UrbanDictionary(client))
