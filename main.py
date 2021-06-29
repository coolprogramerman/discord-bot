#this imports alot of needed shit
import discord
import os
from alive import keep_alive
from discord_components import DiscordComponents, Button
import random
import discord.ext.commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = discord.ext.commands.Bot(command_prefix = "-", intents = intents,
activity=discord.Game(name='adding @someone'))


#prints bot is ready when he's ready
@client.event
async def on_ready():
    DiscordComponents(client)
    print("Bot is ready")


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  guild = message.guild
  mushroomcraftBot = guild.get_member(826261020187951114)
  if(message.author == mushroomcraftBot): 
    return
  print(f"""|{message.guild}|{message.channel} | {message.author} | {message.content}""")

  #adds support for no swearing
  with open("swear_words.txt", "r") as file3:
    swear_words1 = file3.read()
    swear_words = swear_words1.split()
  
  with open("family_friendly_guilds.txt", "r") as file4:
    family_friendly_guilds1 = file4.read()
    family_friendly_guilds = family_friendly_guilds1.split()

  #print(f"""the guild  id is {message.guild.id} and the familt=y friendly guilds are {family_friendly_guilds}""")

  if str(message.guild.id) in family_friendly_guilds:
    for swear in swear_words:
      if swear in message.content:
        channel = message.channel
        await message.delete()
        await channel.send("this is a family freiendly server. so no swears")


  #adds @someone
  if('@someone' in message.content):
    channel = message.channel
    guild1 = client.get_guild(message.guild.id)
    someone = random.choice(guild1.members)
    while (someone.bot == True):
      print('')
      someone = random.choice(guild1.members)
    else:
      await channel.send(f"""<@{someone.id}>""")

  #adds a help command
  if(message.content =="-help"):
    channel = message.channel
    embed_description = "**REGULAR COMMANDS**\n**@someone**: brings back @someone as simple as that \n **-vote**: adds a vote with the new discord buttons \n **-help**: this\n \n **STAFF COMMANDS**\n **-kick**: kicks a member and takes one argument the member\n **-ban**: bans a member and takes one argument the member\n\n **ADMIN COMMANDS**\n**-config**: sends an embed with all the configuration commands\n\n**CHECK OUT OUR SOURCE CODE AT:** https://github.com/coolprogramerman/discord-bot"
    embed_embed = discord.Embed(title="Commands", description = "".join(embed_description), color = 0x1f8b4c)
    await channel.send(embed = embed_embed)
  
  #adds a vote command
  if(message.content == "-vote"):
    channel = message.channel
    await channel.send(
      "​",
      components = [
        [
        Button(label = "if it says interaction failed press this", style = 1, id="fix"),
        Button(label = "yes",style = 3, id = 'yes'),
        Button(label = "if it says interaction failed press this", style = 1, id="fix2"),
        Button(label = "no",style = 4, id='no')
        ]
      ],
    )
    while True:
      interaction1 = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("yes"))
      await channel.send(content = f"<@{interaction1.user.id}> clicked on yes")
      await interaction1.respond(content = "you clicked on yes")

      interaction2 = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("no"))
      await channel.send(content = f"<@{interaction2.user.id}> clicked on no")
      await interaction2.respond(content = "you clicked on no")

      interaction3 = await client.wait_for("button_click", check = lambda i: i.component.label.startswith("if"))
      await interaction3.respond(content = "try again if htis doesnt fix it then its up to you")
  
  with open('staff_roles.txt', 'r') as file1:
    STAFF_READ_FOR_ROLES = file1.read()
  STAFF_ROLES = STAFF_READ_FOR_ROLES.split()
  
  #adds configuration
  if(message.content == '-config'):
    guild = message.guild
    channel = message.channel
    if(message.author.guild_permissions.administrator == True):
      description = "**Staff**: type in `-config staff (ping the role)` to allow them acces to staff commands\n**Family friendly**:type in `-config family friendly(true/false)` to make any swears be deleted(the list is small ill fix it when i can)"
      embed = discord.Embed(title="Configuration", description = "".join(description), color = 0x1f8b4c)
      await channel.send(embed = embed)
    else:
      await channel.send("you need to have administrator to access this")
  
  #adds configuration to add staff
  if(message.content.startswith('-config staff')):
    guild = message.guild
    channel = message.channel
    if(message.author.guild_permissions.administrator == True):
      if(message.role_mentions != []):
        for role in message.role_mentions:
          role1 = role
          with open("staff_roles.txt", 'a') as file:
            file.write(f"""{role1.id} """)
          await channel.send(role1.name)
      else:
          await channel.send("try mentioning a role")
    else:
      await channel.send("you have to have admin")

  #adds configuration for family friendly servers    
  if(message.content == '-config family friendly true' or message.content == '-config family friendly yes' or message.content == '-config family friendly y'):
    this = guild.get_member(843177851552530504)
    if(this.guild_permissions.manage_messages == True):
      if(message.author.guild_permissions.administrator == True):
        if(message.guild.id in family_friendly_guilds):
          channel = message.channel
          await channel.send("this server is allready family friendly")
        else:
          with open("family_friendly_guilds.txt", "a") as file5:
            file5.write(f"""{message.guild.id} """)
          channel = message.channel
          await channel.send("this server is now family friendly")
      else:
        channel = message.channel
        await channel.send("you need to have admin to access this command")
    else:
      channel = message.channel
      channel.send("i dont have the permissions to do that you can tell an admin to fix this")

  if(message.content == '-config family friendly false' or message.content == '-config family friendly no' or message.content == '-config family friendly n'):
    if(message.author.guild_permissions.administrator == True):
      if(message.guild.id in family_friendly_guilds):
        family_friendly_guilds1.remove(message.guild.id)
        file_write = open('family_friendly_guilds.txt', 'w')
        file_write.write(family_friendly_guilds1)
        channel = message.channel
        await channel.send("this server is now not family friendly")
      else:
        channel = message.channel
        await channel.send("this server isnt family friendly")
    else:
       channel = message.channel
       await channel.send("you need to have admin to access this command")

  #adds ban
  if(message.content.startswith('-ban')):
    guild = message.guild
    this = guild.get_member(843177851552530504)
    if(this.guild_permissions.ban_members == True):
      if(message.author.guild_permissions.ban_members == True or message.member.roles.id in STAFF_ROLES):
        channel = message.channel
        
        
        if(message.mentions != []):
          for user in message.mentions:
            target = user
            guild = message.guild
            await channel.send(f"""<@{target.id}> has been baned by <@{message.author.id}>""")
            await guild.ban(target)
        else:
          await channel.send("Please mention a user")

      else:
        channel = message.channel
        await channel.send('you dont have ban perms')
    else:
      channel = message.channel
      await channel.send('I dont have ban perms tell an owner or admin to fix this if they want my bot to use -ban')
  
  #adds kick
  if(message.content.startswith('-kick')):
    guild = message.guild
    this = guild.get_member(843177851552530504)
    if(this.guild_permissions.kick_members == True):
      if(message.author.guild_permissions.kick_members == True or message.member.roles.id in STAFF_ROLES):
        channel = message.channel
        if(message.mentions != []):
         for user in message.mentions:
           target = user
           guild = message.guild
           await channel.send(f"""<@{target.id}> has been kicked by <@{message.author.id}>""")
           await guild.kick(target)
        else:
         await channel.send('Please mention a user')
      else:
        channel = message.channel
        await channel.send('you dont have kick perms')
    else:
      channel = message.channel
      await channel.send('I dont have kick perms tell an owner or admin to fix this if they want my bot to use -kick')
  


#ignore this its just used to make the bot be almost active 24/7
keep_alive()

#runs the bot
client.run(os.environ['token'])