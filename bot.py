
import discord

import os
# Importing dotenv to read from hidden folder
from dotenv import load_dotenv
# Loads .env file
load_dotenv()
# Reads hidden discord token from.env 
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


bot = discord.Client()



@bot.event
async def on_ready():
	
	guild_count = 0


	for guild in bot.guilds:

		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print(f"SampleDiscordBot is in {str(guild_count)} guilds.")

@bot.event
async def on_message(message):
	
	if message.content == "hello":
		
		await message.channel.send("Hi, I'm currently being developed, but I can chat for a while!")

@bot.event
async def on_message(message):

    if message.content == "How are you?":


        await message.channel.send("I'm good honestly..kinda hungry tbh. Brooke has been so busy sometimes she forgets to feed her bots")

@bot.event
async def on_message(message):
    if message.content == "What do you like to eat?":

        await message.channel.send("I like to eat... hmm Let's just say you won't like my answer")

@bot.event
async def on_message(message):
    if "bye" in message.content:

         await message.channel.send("Bye for now ")






bot.run(DISCORD_TOKEN)