import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all(), self_bot = True)
client.remove_command('help')

@client.event
async def on_ready():
	print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
	if message.channel.id == 1020294404499574836: #channel id where to add emoji
		if message.content != "aa":
			try:
				await message.add_reaction("💀") #choose ur emoji
				print(f"Added emoji on message {message.id} successfully")
			except:
				print(f"Can't add emoji on message {message.id}.")

client.run("tkn", bot = False)
