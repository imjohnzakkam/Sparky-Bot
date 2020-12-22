import discord
from discord.ext import commands
import asyncio
import random
import os
## Setup Client
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix= '=', intents = intents)



## Load Cogs
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension("cogs.{}".format(filename.replace('.py','').strip()))


## On Ready
@client.event
async def on_ready():
	print("Bot is Ready")
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='your commands'))


## On Member Join
@client.event
async def on_member_join(member):
	print(f'{member} has joined our kitchen named {member.guild}!')



## On Member Remove
@client.event
async def on_member_remove(member):
	print(f'{member} has left our named {member.guild}!')


#Add Your Bot Token
token = "YOURBOTTOKEN"


client.run(token)