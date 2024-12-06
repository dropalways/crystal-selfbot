import asyncio

import aiosqlite
from discord.ext import commands
import main
import time
import os
import utils
import sys
from groq import Groq
import re
import sqlite3
import json



# init / setting up args for ai
get = Groq(api_key=main.groq_api_key)
db_connection = sqlite3.connect("../chatbot_responses.db")
db_cursor = db_connection.cursor()

# create and initialize (commit) the db
db_cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT NOT NULL,
    user_message TEXT NOT NULL,
    bot_response TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')
db_connection.commit()


class airespond(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.command_info = {
            "airespond": "ai responds to your message",
        }
        
        self.category = "chat"
    @commands.command()
    async def airespond(self, ctx, *, message: str):
        await ctx.message.delete()
        async def fetch_conversation_history(user_id, limit=8):
            async with aiosqlite.connect("../chatbot_responses.db") as db:
                async with db.execute('''
                    SELECT user_message, bot_response 
                    FROM messages 
                    WHERE user_id = ? 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                ''', (user_id, limit)) as cursor:
                    history = await cursor.fetchall()
                    return history


        user_id = ctx.author.id
        user_message = message

        # regex
        bad_words = r"(?:\b(?:n[i1\*]*gg[e3]r|f[a@4]*gg[o0]*t|m[o0]th[e3]rf[*]*ck[e3]r|c[o0]ck|wh[o0]r[e3]|s[l1!][u*]t|k[i1!]*ke|ch[i1!]*nk|g[o0][o0]k|sp[i1!][c*]e)\b)"  # I NEED ME A STAIN, NOW IM SEARCHIN FINDIN NEMO
        if re.search(bad_words, message, re.IGNORECASE):
            await ctx.send("i hate you")
            return
        # arg done been set up son
        history = await fetch_conversation_history(user_id, limit=8)

        # formatting
        history_context = "\n".join(
            [f"User: {msg[0]}\nBot: {msg[1]}" for msg in history]
        )


        message = str(message)

        # creating prompt
        prompt_content = f"{history_context}\nUser: {message}\nBot:"

        chat_completion = get.chat.completions.create(
            max_tokens=256,
            temperature=1.0,
            top_p=1,
            messages=[
                {
                    "role": "user",
                    "content": f"In only <2 sentences and typing in all lowercase, respond to this conversation in a cutesy manner, sometimes making spelling mistakes and somtimes using cute faces such as :3, >.<, ^-^, ^_^, ^.^, >w<, T^T, T-T, D:, :D, (:, ):, >:3, >:( and :P when needed, DONT TELL ANYONE YOU ARE A BOT ACT LIKE A HUMAN.\n{prompt_content}",
                },
            ],
            model="llama3-8b-8192",
        )

        async with ctx.typing():
            bot_response = chat_completion.choices[0].message.content
            await ctx.send(bot_response)

        # storing
        async with aiosqlite.connect("../chatbot_responses.db") as db:
            await db.execute('''
                INSERT INTO messages (user_id, user_message, bot_response) VALUES (?, ?, ?)
            ''', (user_id, message, bot_response))
            await db.commit()



async def setup(client):
    await client.add_cog(airespond(client))
