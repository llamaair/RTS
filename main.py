import discord
import asyncio
import random
import datetime
import time
import string
from discord.ext import commands
from discord.ext import tasks
import os
import json
from discord.ext.commands import check
from dotenv import load_dotenv

#---------------------------#
#NAME: FetchBot
#Status: Working
#Version: 3.0.0
#Creator: Marc13 and Raxeemo
#---------------------------#
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
intents = discord.Intents.all()

client = discord.Bot(intents=intents, help_command=None)


#Defining startup
@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="/help"))
    global startTime
    startTime = time.time()

@client.command(description="Ping!")
async def pong(ctx):
  await ctx.respond('Pong! {0}'.format(round(client.latency, 1)))

client.run(TOKEN)
