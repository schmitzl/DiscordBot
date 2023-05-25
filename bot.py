# bot.py
import os
import discord
import random

TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if random.random() <= 0.25:
        num_i = random.randint(1, 10)
        response = "N" + "i" * num_i + "ce!!"

        await message.channel.send(response)


client.run(TOKEN)
