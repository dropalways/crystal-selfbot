import json
import requests
import shutil
import ctypes
import requests
import os
def load_json(jsonfile):
    with open(jsonfile) as f:
        return json.load(f)

def set_console_title(title):
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except:
        pass
    
def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')    


def waifu_pics(profanity: str = "sfw", category: str=None):
    profanity_list = ["nsfw", "sfw"]
    nsfw_list = ["waifu", "neko", "trap", "blowjob"]
    sfw_list = [
    "waifu",
    "neko",
    "shinobu",
    "megumin",
    "bully",
    "cuddle",
    "cry",
    "hug",
    "awoo",
    "kiss",
    "lick",
    "pat",
    "smug",
    "bonk",
    "yeet",
    "blush",
    "smile",
    "wave",
    "highfive",
    "handhold",
    "nom",
    "bite",
    "glomp",
    "slap",
    "kill",
    "kick",
    "happy",
    "wink",
    "poke",
    "dance",
    "cringe"
    ]

    if profanity not in profanity_list:  
        return f"Invalid profanity {profanity_list}"
    
    if category not in nsfw_list and profanity == "nsfw":
        return f"Invalid category {nsfw_list}"
    
    if category not in sfw_list and profanity == "sfw":
        return f"Invalid category {sfw_list}"
    
    request = requests.get(f"https://api.waifu.pics/{profanity}/{category}")
    match request.status_code:
        case 404:
            if profanity == "nsfw":
                return f"Error: Category '{category}' not found. {nsfw_list}"
            else:
                return f"Error: Category '{category}' not found. {sfw_list}"
        case 500:
            return f"Error: Category '{category}' internal server error."
        case 200:
            return request.json()["url"]
        case 429:
            return f"Error: Rate limit exceeded. Please wait for {request.headers['Retry-After']} seconds."
        case _:
            return "niggers"
