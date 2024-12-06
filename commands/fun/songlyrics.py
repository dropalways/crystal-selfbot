from discord.ext import commands
import requests

class songlyrics(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "songlyrics": "gives you lyrics of the artist and the song",
        }
        
        self.category = "fun"
    @commands.command()
    async def songlyrics(self, ctx, artist, song):
        url = f'https://api.lyrics.ovh/v1/{artist}/{song}'

        headers = {
            "accept": "/",
            "Content-Type":"application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.669 Chrome/91.0.4472.164 Electron/13.6.6 Safari/537.36",
        }

        get = requests.get(url, headers=headers)
        print(f"request = {get}")

        if get.status_code == 200:
                data = get.json()
                if data:
                    getdata_ = (
                    f"'Lyrics:' ```{data.get('lyrics', 'N/A')}```\n"
                    f"`Request: {song} by {artist})'`\n"
                    )
                    await ctx.send(f"> Crystal Selfbot > Song Lyrics API:\n{getdata_}")

async def setup(client):
    await client.add_cog(songlyrics(client))
