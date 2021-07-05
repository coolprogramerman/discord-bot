import discord
import random
from replit import db
import discord.ext.commands
import asyncio

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = discord.ext.commands.Bot(command_prefix = "-", intents = intents)


@client.event
async def on_message(message):
  if(message.content.startswith('-rob')):
     random_num = random.randrange(1, 10)
     list_of_words = message.content.split()
     user = str(message.author.id)
     keys = db.keys()
     #theese are errors
     if(f"rob_{str(message.mentions[0].id)}" not in keys):
             
     if(message.mentions[0].id == message.author.id):
        channel = message.channel
        await channel.send('you cant rob yourself')
        return

client.run(os.environ['token'])