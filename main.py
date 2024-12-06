import sys
sys.dont_write_bytecode = True  # removes that annoying pycache
from discord_webhook.webhook import DiscordWebhook
from dotenv import load_dotenv
import asyncio
from discord.ext import commands, tasks
import pyfiglet
import discord_rpc
import time
import os
from colorama import Fore, Style, init
import discord
import nekos
import utils
import pystyle
import logging
import threading
import json

logging.disable() # removes discord.py logging

config = utils.load_json("config.json")


utils.set_console_title("Crystal Selfbot")

load_dotenv()

token = os.getenv("token")
groq_api_key = os.getenv("groq_api_key")

prefix = config.get("prefix")
massBan_reason = config.get("ban_message")
delete_timer = config.get("delete_timer")
massKick_reason = config.get("kick_message")
shouldrpc = config["rpc"]
client = commands.Bot(command_prefix=prefix, self_bot=True, case_insensitive=True)
client.remove_command("help")

title_lock = threading.Lock()
commandcount = 0
base_titletext = "Crystal Selfbot | Commands: 0 | "
scrolled_title = base_titletext

def set_console_title(title):
    utils.set_console_title(title)

async def scrolling():
    global scrolled_title
    while True:
        with title_lock:
            scrolled_title = scrolled_title[1:] + scrolled_title[0]
            set_console_title(scrolled_title)
        await asyncio.sleep(0.1)

@client.event
async def on_ready():
    print(pystyle.Center.XCenter(f"\n{Fore.WHITE}Logged in as {Fore.LIGHTMAGENTA_EX}{client.user.name}\n{Fore.WHITE}Prefix: {Fore.LIGHTMAGENTA_EX}{prefix}"))

mimiclist = []

@client.event
async def on_message(message):
    if message.author.id in mimiclist:
        await message.reply(message.content)
    if message.author.id == 885651544819781712 and message.content == "plz headpats":
        await message.reply(nekos.img("pat"))
    await client.process_commands(message)

async def load_commands(path="commands"):
    global commandcount, base_titletext, scrolled_title
    base_dir = os.path.dirname(os.path.abspath(__file__))
    commands_path = os.path.join(base_dir, path)

    for root, dirs, files in os.walk(commands_path):
        for file in files:
            if file.endswith('.py'):
                module = os.path.join(root, file).replace("/", ".").replace("\\", ".")
                module = module[:-3]  # Strip the .py extension
                module = module[module.index("commands"):]  # Make sure the path starts from "commands"
                
                try:
                    commandcount += 1
                    with title_lock:
                        base_titletext = f"Crystal Selfbot | Commands: {commandcount} | "
                        scrolled_title = base_titletext
                    await client.load_extension(module)
                except Exception as e:
                    print(f"Failed to load command {module}!\n{e}")  # Debug line

@tasks.loop(seconds=15)
async def update_rpc():
    if shouldrpc:
        start = time.time()
        discord_rpc.update_presence(
            state="Crystal Selfbot",
            details="By nuptunia, always and nautiaa",
            start_timestamp=start,
            large_image_key="default"
        )
        discord_rpc.update_connection()
        discord_rpc.run_callbacks()

def start_scrolling_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(scrolling())
    loop.run_forever()

async def main():
    try:
        pystyle.Cursor.HideCursor()
        logo = pyfiglet.figlet_format("Crystal Selfbot", font="Big")
        
        print(pystyle.Colorate.Color(pystyle.Colors.pink, pystyle.Center.XCenter(logo), True))
    except:
        pass

    await load_commands()
    await client.start(token)

if __name__ == "__main__":
    
        
    print(groq_api_key)
    scrolling_thread = threading.Thread(target=start_scrolling_thread, daemon=True)
    scrolling_thread.start()

    # Start the RPC task
    if shouldrpc:
        update_rpc.start()

    utils.clear_console()
    
    if token is None:
        print("no token in .env please put your discord token in .env")
        sys.exit(0)
        
    if groq_api_key is None or groq_api_key == "":
        print("no groq api key in .env airespond wont work")
        

    asyncio.run(main())
