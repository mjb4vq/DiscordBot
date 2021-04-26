import discord
import os
import random
from stayawake import stay_awake

bot = discord.Client()

@bot.event
async def on_ready():
  print("We have logged on as {0.user}".format(bot))

@bot.event
async def on_message(message):
  print("Received message")
  if message.author == bot.user:
    return
  if message.content.startswith("hi"):
    await message.channel.send("hi right on back")
  else:
    await message.channel.send("why don't you greet me?")

stay_awake()
bot.run(os.getenv('TOKEN'))