
import discord

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


bot.run("MTA0MDYyMzk0NDI5NTc5NjgxNg.GuTjvK.q_GSQcrZCxTQuUVaq7M70qBsOws528haR6EiPw")