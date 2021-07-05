#this imports alot of needed shit
import discord
import os
from alive import keep_alive
from discord_components import DiscordComponents, Button
import random
from replit import db
import time
from discord.ext import commands
#import asyncio



intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix ="-", intents = intents,
activity=discord.Game(name='-help|Watching 7 chats'))

#prints bot is ready when he's ready
@client.event
async def on_ready():
    DiscordComponents(client)
    print("Bot is ready")
#     guild = client.get_guild(850875538280546344)
#     channel1 = 859037617868636230
#     channel = guild.get_channel(channel1)
#     embed_description = "**Added 8 commands**:-servers,-balance,-give,-beg,-rob,-shop,-buy,-delete,servers\n **invite my bot at**: https://discord.com/oauth2/authorize?client_id=843177851552530504&permissions=8&scope=bot"
#     embed1 = discord.Embed(title="UPDATE", description = "".join(embed_description), color = 0x1f8b4c)
#     await channel.send(embed = embed1)

first_num = ''
second_num = "" 
is_on_button = 'first'
result = 0

@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  member = payload.member
  guild_id = payload.guild_id
  guild = client.get_guild(guild_id)
  if(message_id == 860945122312060978):
    if(payload.emoji.name == "🎮"):
       role = discord.utils.get(guild.roles,name="gamer")
       await member.add_roles(role)
  if(message_id == 860945124510269460):
       if(payload.emoji.name == "💻"):
        role = discord.utils.get(guild.roles,name="programer")
        await member.add_roles(role)   
  if(message_id == 860945128042397707):
      if(payload.emoji.name == "🎨"):
        role = discord.utils.get(guild.roles,name="artist")
        await member.add_roles(role) 
  if(message_id == 860945131879530497):
      if(payload.emoji.name == "✏️"):
        role = discord.utils.get(guild.roles,name="animator")
        await member.add_roles(role)
  if(message_id == 860945137563861002):
      if(payload.emoji.id == 860938579424706590):
        role = discord.utils.get(guild.roles,name="firefox")
        await member.add_roles(role)
  if(message_id == 860945143893065758):
      if(payload.emoji.id == 860939107240116264):
        role = discord.utils.get(guild.roles,name="chrome")
        await member.add_roles(role)
  if(message_id == 860945375840698368):
      if(payload.emoji.id == 860939455958876181):
        role = discord.utils.get(guild.roles,name="edge")
        await member.add_roles(role)        

# 🐍      
    
          

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  guild = message.guild
  if(guild != None):
     mushroomcraftBot = guild.get_member(843232491964071946)
     if(message.author == mushroomcraftBot): 
       return  
  print(f"""|{message.guild}|{message.channel} | {message.author} | {message.content}""")
  db['728641142874308740'] = 69000000000000000
  db['717070380795428866'] = -690000000
  #adds support for no swearing
  with open("swear_words.txt", "r") as file3:
    swear_words1 = file3.read()
    swear_words = swear_words1.split()
  
  with open("family_friendly_guilds.txt", "r") as file4:
    family_friendly_guilds1 = file4.read()
    family_friendly_guilds = family_friendly_guilds1.split()

  

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
      return

  #adds a help command
  if(message.content =="-help"):
    channel = message.channel
    embed_description = "**REGULAR COMMANDS**\n**@someone** **-vote** **-whois** **-dm** **-servers**\n**CURRENCY COMMANDS**\n **-balance** **-give** **-beg** **-rob** **-shop** **-buy** \n**STAFF COMMANDS**\n **-kick** **-ban** **-delete**\n **ADMIN COMMANDS**\n**-config**\n\n**CHECK OUT OUR SOURCE CODE AT:** https://github.com/coolprogramerman/discord-bot"
    embed_embed = discord.Embed(title="Commands", description = "".join(embed_description), color = 0x1f8b4c)
    await channel.send(embed = embed_embed, components = [Button(label = 'vote', style = 5, url="https://discordbotlist.com/bots/someone-bot")])
    return
  
  #adds a vote command
  if(message.content == "-vote"):
    channel = message.channel
    await channel.send(
      "​",
      components = [     
        Button(label = "Vote!",style = 5, url = 'https://discordbotlist.com/bots/someone-bot')
      ]
    )
    
  
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
      return
    else:
      await channel.send("you need to have administrator to access this")
      return
  
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
          return
      else:
          await channel.send("try mentioning a role")
          return
    else:
      await channel.send("you have to have admin")
      return

  #adds configuration for family friendly servers    
  if(message.content == '-config family friendly true' or message.content == '-config family friendly yes' or message.content == '-config family friendly y'):
    this = guild.get_member(843177851552530504)
    if(this.guild_permissions.manage_messages == True):
      if(message.author.guild_permissions.administrator == True):
        if(message.guild.id in family_friendly_guilds):
          channel = message.channel
          await channel.send("this server is allready family friendly")
          return
        else:
          with open("family_friendly_guilds.txt", "a") as file5:
            file5.write(f"""{message.guild.id} """)
          channel = message.channel
          await channel.send("this server is now family friendly")
          return
      else:
        channel = message.channel
        await channel.send("you need to have admin to access this command")
        return
    else:
      channel = message.channel
      channel.send("i dont have the permissions to do that you can tell an admin to fix this")
      return

  if(message.content == '-config family friendly false' or message.content == '-config family friendly no' or message.content == '-config family friendly n'):
    if(message.author.guild_permissions.administrator == True):
      if(str(message.guild.id) in family_friendly_guilds):
        family_friendly_guilds.remove(str(message.guild.id))
        family_friendly_guilds2 = " "
        family_friendly_guilds3 = family_friendly_guilds2.join(family_friendly_guilds)
        file_write = open('family_friendly_guilds.txt', 'w')
        file_write.write(family_friendly_guilds3)
        channel = message.channel
        await channel.send("this server is now not family friendly")
        return
      else:
        channel = message.channel
        await channel.send("this server isnt family friendly")
        return
    else:
       channel = message.channel
       await channel.send("you need to have admin to access this command")
       return

  #adds ban
  if(message.content.startswith('-ban')):
    guild = message.guild
    this = guild.get_member(843177851552530504)
    if(this.guild_permissions.ban_members == True):
      if(message.author.guild_permissions.ban_members == True or message.author.roles.id in STAFF_ROLES):
        channel = message.channel
        
        
        if(message.mentions != []):
          for user in message.mentions:
            target = user
            guild = message.guild
            await channel.send(f"""<@{target.id}> has been baned by <@{message.author.id}>""")
            await guild.ban(target)
            return
        else:
          await channel.send("Please mention a user")
          return

      else:
        channel = message.channel
        await channel.send('you dont have ban perms')
        return
    else:
      channel = message.channel
      await channel.send('I dont have ban perms tell an owner or admin to fix this if they want my bot to use -ban')
      return
  
  #adds kick
  if(message.content.startswith('-kick')):
    guild = message.guild
    this = guild.get_member(843177851552530504)
    if(this.guild_permissions.kick_members == True):
      if(message.author.guild_permissions.kick_members == True or message.author.roles.id in STAFF_ROLES):
        channel = message.channel
        if(message.mentions != []):
         for user in message.mentions:
           target = user
           guild = message.guild
           await channel.send(f"""<@{target.id}> has been kicked by <@{message.author.id}>""")
           await guild.kick(target)
           return
        else:
         await channel.send('Please mention a user')
         return
      else:
        channel = message.channel
        await channel.send('you dont have kick perms')
        return
    else:
      channel = message.channel
      await channel.send('I dont have kick perms tell an owner or admin to fix this if they want my bot to use -kick')
      return
  
  #adds whois
  if(message.content.startswith('-whois')):
    for user in message.mentions:
      user1 = user
      channel = message.channel
      embed_description1 = f"""**Joined server at**:\n{user1.joined_at}\n**Made account at**: \n{user1.created_at}\n**Username**:\n{user1.name}\n**User id**:\n{user1.id}\n**Status**:\n{user1.status}\n**Status on web(if the same as status that means theyre on web)**:\n{user1.web_status}\n**Is mobile**:\n{user1.is_on_mobile()}\n**Is a bot**:\n{user1.bot}\n**Is playin game**:\n{user1.activity}""" 
      embed_embed1 = discord.Embed(title="Who is", description = "".join(embed_description1), color = 0x1f8b4c)
      avatar = user1.avatar_url
      embed_embed1.set_thumbnail(url = avatar)
      await channel.send(embed = embed_embed1)
    for channels in message.channel_mentions:
      channel = channels
      if (channel.last_message == None):
        embed_description2 = f"""**Made channel at**: \n{channel.created_at}\n**Name**:\n{channel.name}\n**Is nsfw**:\n{channel.is_nsfw()}"""  
      else:
        embed_description2 = f"""**Made channel at**: \n{channel.created_at}\n**Last message** \n`{channel} | {channel.last_message.author} | {channel.last_message.content}`\n**Name**:\n{channel.name}\n**Is nsfw**:\n{channel.is_nsfw()}""" 
      embed_embed2 = discord.Embed(title="Who is", description = "".join(embed_description2), color = 0x1f8b4c)
      channel3 = message.channel
      await channel3.send(embed = embed_embed2)
  
  #adds support for gifs
  if(message.content.startswith('-gif')):
    gif = message.content
    gif2 = gif.split()
    if gif2 == ['-gif']:
      channel = message.channel
      await channel.send("please provide a url")
      return
    if 'http' not in gif:
      channel = message.channel
      await channel.send("please provide a valid url")
      return
    
    gif = gif.split(" ", 1)[1]
    channel = message.channel
    await channel.send(gif)    
  
  #adds support for checking your money in currency
  if(message.content == '-balance'):
    channel = message.channel
    user = str(message.author.id)
    keys = db.keys()
    if(user not in keys):
      db[user] = "0"
    embed_description5 = f"""Your balance is {db[user]}"""
    embed_embed5 = discord.Embed(title="Balance", description = "".join(embed_description5), color = 0x1f8b4c)
    await channel.send(embed = embed_embed5) 

  #adds support for giving money
  if(message.content.startswith('-give')):
    list_of_words = message.content.split()
    user = str(message.author.id)
    keys = db.keys()
    #theese are errors
    if(message.mentions[0].id == message.author.id):
      channel = message.channel
      await channel.send('you cant give money to yourself')
      return

    if(len(list_of_words) != 3):
      channel = message.channel
      await channel.send('please provide the correct ammount of parameters')
      return
    if(message.mentions == []):
      channel = message.channel
      await channel.send('please mention a user')
      return
    if(list_of_words[2].isdigit() == False):
      channel = message.channel
      await channel.send('please use a number')
      return
    if(user not in keys):
       db[user] = "0"
       channel = message.channel
       await channel.send('insuffiecent funds')
       return
    if(int(db[user]) < int(list_of_words[2])):
      channel = message.channel
      await channel.send('insuffiecent funds')
      return
    #this is when there are no errors  
    user_recieving = str(message.mentions[0].id)
    if(user_recieving not in keys):
      db[user_recieving] = "0"                 
    
    my_money = db[user]
    their_money = db[user_recieving]
    
    db[user] = str(int(my_money) - int(list_of_words[2]))
    db[user_recieving] = str(int(their_money) + int(list_of_words[2]))
    money_given = list_of_words[2]
    embed_description4 = f"""gave {money_given} to <@{user_recieving}>"""
    embed_embed4 = discord.Embed(title="gave money", description = "".join(embed_description4), color = 0x1f8b4c)
    channel = message.channel
    await channel.send(embed = embed_embed4)
        
  #adds support for beging
  if(message.content == '-beg'):
    random_num = random.randrange(1, 1000)
    embed_description3 = f"""you got {random_num}"""
    embed_embed3 = discord.Embed(title="you begged noob", description = "".join(embed_description3), color = 0x1f8b4c)
    channel = message.channel
    await channel.send(embed = embed_embed3)
    user = str(message.author.id)
    keys = db.keys()
    if(user not in keys):
      db[user] = "0" 
    my_money = db[user]
    db[user] = str(int(my_money) + random_num)
  
  #adds support for robbing
  if(message.content.startswith('-rob')):
     random_num = random.randrange(1, 10)
     list_of_words = message.content.split()
     user = str(message.author.id)
     keys = db.keys()
     #theese are errors
     if(message.mentions == []):
        channel = message.channel
        await channel.send('please mention a user')
        return
     if(message.mentions[0].id == message.author.id):
       channel = message.channel
       await channel.send('you cant rob yourself')
       return
     if(len(list_of_words) != 2):
       channel = message.channel
       await channel.send('please provide the correct ammount of parameters')
       return  
     user_recieving = str(message.mentions[0].id)
     if(user_recieving not in keys):
       db[user_recieving] = "0"
       embed_description6 = "ayo why tf are you stealing money from a poor person i think i should remove your money"
       embed_embed6 = discord.Embed(title="try someone else", description = "".join(embed_description6), color = 0x1f8b4c)
       channel = message.channel
       await channel.send(embed = embed_embed6)
       return
     their_money = db[user_recieving]
     if(int(their_money) < 1):
       embed_description6 = "ayo why tf are you stealing money from a poor person i think i should remove your money"
       embed_embed6 = discord.Embed(title="try someone else", description = "".join(embed_description6), color = 0x1f8b4c)
       channel = message.channel
       await channel.send(embed = embed_embed6)
       return  
     #there are no errors if we made it to here
     if(random_num < 9):
       embed_description7 = "you tried to steal the money but somebody told you to gtfo or their gonna call the police and they let their pitbull dog at you so you had to escape"
       embed_embed7 = discord.Embed(title="try amother time", description = "".join(embed_description7), color = 0x1f8b4c)
       channel = message.channel
       await channel.send(embed = embed_embed7)
       return
     my_money = db[user]
     their_money = db[user_recieving]
     random_num2 = random.randrange(0, int(their_money))
     my_money = str(int(my_money) + random_num2)
     their_money = str(int(their_money) - random_num2)
     db[user] = my_money
     db[user_recieving] = their_money
     embed_description8 = f"""ayo you robbed <@{user_recieving}> and got {random_num2}"""
     embed_embed8 = discord.Embed(title="sucks to be the one who got robbed", description = "".join(embed_description8), color = 0x1f8b4c)
     channel = message.channel
     await channel.send(embed = embed_embed8)

  #adds shops
  if(message.content.startswith('-shop')):
     list_of_words = message.content.split()
     del list_of_words[0]
     if(list_of_words == []):
       embed_description9 = "PC price: 5000 description: u can do lots of things with the pc\n"
       embed2 = discord.Embed(title='shop', description = "".join(embed_description9), color = 0x1f8b4c)
       channel = message.channel
       the_message = await channel.send(embed = embed2)
       #shop = embed2.title
       #await the_message.add_reaction('⬅️')
       #await the_message.add_reaction('➡️')
     if(list_of_words == ['pc']):  
       embed_description9 = "PC price: 5000 description: u can do lots of things with the pc\n"
       embed2 = discord.Embed(title='PC', description = "".join(embed_description9), color = 0x1f8b4c)
       embed2.set_image(url = 'https://www.wikihow.com/images/9/92/Draw-a-Computer-Step-10.jpg')
       channel = message.channel
       await channel.send(embed = embed2)


  #adds support for dming
  if(message.content.startswith('-dm')):
    list_of_words = message.content.split()
    if(message.mentions == []):
      channel = message.channel
      await channel.send('please mention a user')
      return  
    if(len(list_of_words) < 3):
      channel = message.channel
      await channel.send('please provide the correct ammount of parameters')
      return
    user1 = message.mentions[0].id
    user = client.get_user(user1)
    del list_of_words[0]
    del list_of_words[0]
    words1 = ""
    words = ""
    for i in list_of_words:
      words1=words1+i
               
    for i in list_of_words:
      words=words+i+" "
    await user.send(words)

  
  #adds the pc
  if(message.content.startswith('-pc')):
     user = str(message.author.id)
     keys = db.keys()
     pc = 'pc_' + user
     channel = message.channel
     if(pc in keys):     
       list_of_words = message.content.split()
       del list_of_words[0]
       if(list_of_words == []):
        description13 = "**-hack**: hacks someone\n**-calculator**: brings up a calculator"
        embed3 = discord.Embed(title = 'Commands for pc', description = "".join(description13))
        await channel.send(embed = embed3)     
        return
       if(list_of_words[0] == "hack"):
        if(message.mentions == []):
           channel = message.channel
           await channel.send('Please mention a user')
           return
        for mention in message.mentions:
           channel = message.channel                
           the_message = await channel.send(f"Hacking <@{mention.id}>")
           time.sleep(3)
           await the_message.edit('hacked their discord account\nemail:troller@troll.com\npassword:LeEpikTroll123')         
           time.sleep(3)
           await the_message.edit('grabbed their ip\n127.0.0.1')         
           time.sleep(3)
           await the_message.edit('they have the port 69 open hosting a minecraft server')
           time.sleep(3)
           await the_message.edit('Done')
       if(list_of_words[0] == 'calculator'):
        description14 = ""
        global author
        author = message.author
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
        await channel.send(embed = embed4, components = [
         [
           Button(emoji = '1️⃣',style = 1, id = '1'),
           Button(emoji = "2️⃣",style = 1, id='2'),
           Button(emoji = '3️⃣',style = 1, id = '3'),
           Button(emoji = '➕',style = 1, id = '+')
         ],
         [
           Button(emoji = '4️⃣',style = 1, id = '4'),
           Button(emoji = "5️⃣",style = 1, id='5'),
           Button(emoji = '6️⃣',style = 1, id = '6'),
           Button(emoji = '➖',style = 1, id = '-')
         ],
         [
           Button(emoji = '7️⃣',style = 1, id = '7'),
           Button(emoji = '8️⃣',style = 1, id = '8'),
           Button(emoji = '9️⃣',style = 1, id = '9'),
           Button(emoji = '➗',style = 1, id = '/')
         ],
         [
           Button(label = '=',style = 2, id = '='),
           Button(emoji = '0️⃣',style = 1, id = '0'),
           Button(label = ' ',style = 2, disabled = True),
           Button(emoji = '✖️',style = 1, id = '*')      
         ]
        ]
        )
        

     else:
        await channel.send('you need to buy the pc')      
  
  if(message.content.startswith('-buy')):
     channel = message.channel
     user = str(message.author.id)
     keys = db.keys()     
     list_of_words = message.content.split()
     del list_of_words[0]
     if(list_of_words[0] == "pc"):
      pc = 'pc_' + user       
      if(user not in keys):
        db[user] = "0"
        await channel.send('you dont have enough money lol poor')
        return
      if(int(db[user]) < 5000):
        await channel.send('you dont have enough money lol poor')
        return       
      if(pc in keys):
        await channel.send('you allready have it lol')
        return
      db[pc] = 'true'
      money = db[user]
      db[user] = str(int(money) - 5000)
      await channel.send('you bought a pc')  



  if(message.content.startswith('-delete')):
     has_staff = False     
     for role in message.author.roles:       
      if role.id in STAFF_ROLES:     
        has_staff = True       
     if(message.author.guild_permissions.manage_messages == True or has_staff == True):
       ammount1 = message.content.split()
       del ammount1[0]
       channel = message.channel
       if(ammount1[0].isdigit() == False):
        channel = message.channel
        await channel.send('please use a number')
        return
       ammount = int(ammount1[0])
       value = 1
       async for message1 in channel.history(limit=ammount+1):
        await message1.delete()
        value = value + 1
       if(value == ammount + 2):
        await channel.send(f"deleted {str(ammount)}")      
     else:
       channel = message.channel
       await channel.send('You dont have the perms')          
       
  
  if(message.content == '-servers'):
    channel = message.channel
    await channel.send(f"Im connected to {len(client.guilds)} servers theese are the servers:")
    for server in client.guilds:
      await channel.send(server.name)
        
  
  #always keep this at end in case of spam
  if(guild != None):
    if(str(message.guild.id) in family_friendly_guilds):
      for swear in swear_words:
        if swear in message.content:
          channel = message.channel
          await message.delete()
          await channel.send("this is a family friendly server. so no swears")


#makes there be a message when the bot joins a guild
@client.event
async def on_guild_join(guild):
  for channel in guild.text_channels:
    if channel.permissions_for(guild.me).send_messages:
      embed_description = "Hello and thanks for inviting me\ni would reccomend you start with -help so you know what my bot does"
      embed1 = discord.Embed(title="Hello", description = "".join(embed_description), color = 0x1f8b4c)
      await channel.send(embed = embed1)
      break


@client.event
async def on_member_join(member):
  guild = client.get_guild(860921535228280902)
  if(guild == member.guild):
    channel = client.get_channel(860922949678530581)
    await channel.send(f"hello <@{member.id}> welcome to our server please read the <#860922902009479168> and follow them, and after that go get yourself some roles at <#860922981194399804>")
    role = discord.utils.get(guild.roles,name="Member")
    await member.add_roles(role)

@client.event
async def on_button_click(interaction):
   d = interaction.raw_data['d']
   data = d['data']
   id = data.get('custom_id')
   message = interaction.message
   global is_on_button
   global first_num
   global second_num       
   global operation
   embed4 = discord.Embed()
   if(id == '1'):
     await interaction.respond(content = 'you pressed on 1')
     if is_on_button == None:
       is_on_button = 'first'
     if(is_on_button == 'first'):
       first_num = first_num + '1'
       description14 = f"{first_num}"
       embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
       second_num = second_num + '1'
       description14 = f"{first_num} {operation} {second_num}"
       embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
   
   if(id == '2'):
     await interaction.respond(content = 'you pressed on 2')
     if is_on_button == None:
       is_on_button = 'first'
     if(is_on_button == 'first'):
        first_num = first_num + '2'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
        second_num = second_num + '2'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
   if(id == '3'):
     await interaction.respond(content = 'you pressed on 3')
     if is_on_button == None:
        is_on_button = 'first'
     if(is_on_button == 'first'):
        first_num = first_num + '3'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
        second_num = second_num + '3'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
   if(id == '4'):
     await interaction.respond(content = 'you pressed on 4')
     if is_on_button == None:
        is_on_button = 'first'
     if(is_on_button == 'first'):
        first_num = first_num + '4'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
        second_num = second_num + '4'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))

   if(id == '5'):
     await interaction.respond(content = 'you pressed on 5')
     if is_on_button == None:
        is_on_button = 'first'
     if(is_on_button == 'first'):
        first_num = first_num + '5'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
        second_num = second_num + '5'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
   if(id == '6'):
     await interaction.respond(content = 'you pressed on 6')
     if is_on_button == None:
        is_on_button = 'first'
     if(is_on_button == 'first'):
        first_num = first_num + '6'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
        second_num = second_num + '6'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
   if(id == '7'):
     await interaction.respond(content = 'you pressed on 7')
     if is_on_button == None:
        is_on_button = 'first'
     if(is_on_button == 'first'):
        first_num = first_num + '7'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
        second_num = second_num + '7'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))                
   if(id == '8'):
     await interaction.respond(content = 'you pressed on 8')
     if is_on_button == None:
        is_on_button = 'first'
     if(is_on_button == 'first'):
        first_num = first_num + '8'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
        second_num = second_num + '8'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14)) 
   if(id == '9'):
     await interaction.respond(content = 'you pressed on 9')
     if is_on_button == None:
        is_on_button = 'first'
     if(is_on_button == 'first'):
        first_num = first_num + '9'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
     if(is_on_button == 'second'):
        second_num = second_num + '9'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
   if(id == '0'):
      await interaction.respond(content = 'you pressed on 0')
      if is_on_button == None:
        is_on_button = 'first'
      if(is_on_button == 'first'):
        first_num = first_num + '0'
        description14 = f"{first_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
      if(is_on_button == 'second'):
        second_num = second_num + '0'
        description14 = f"{first_num} {operation} {second_num}"
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
   if(id == '+'):
      if(is_on_button == 'first'):
        is_on_button = 'second'
        await interaction.respond(content = 'you pressed +')
        operation = '+'
      else:
        await interaction.respond(content = 'you can only give 2 arguments')
   if(id == '-'):
     if(is_on_button == 'first'):
        is_on_button = 'second'
        await interaction.respond(content = 'you pressed -')
        operation = '-'
     else:
        await interaction.respond(content = 'you can only give 2 arguments')                    
   if(id == '*'):
     if(is_on_button == 'first'):
        is_on_button = 'second'
        await interaction.respond(content = 'you pressed *')
        operation = '*'
     else:
        await interaction.respond(content = 'you can only give 2 arguments')          
   if(id == '/'):
     if(is_on_button == 'first'):
        is_on_button = 'second'
        await interaction.respond(content = 'you pressed /')
        operation = '/'
     else:
        await interaction.respond(content = 'you can only give 2 arguments')

   if(id == 'CE'):
     description14 = ''
     operation = None
     first_num = ''
     second_num = ''
     is_on_button = 'first'
     await interaction.respond(content = 'the screen is cleared')
     embed4 = discord.Embed(title = 'calculator', description = "".join(description14))      
     
   if(id == '='):
      if(operation == '/' and second_num == '0'):
        description14 = "ERROR : cannot divide by zero"
        await interaction.respond(content = 'the screen is cleared')
        embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
        return     
      if(operation == '+'):     
        equals = str(int(first_num) + int(second_num))     
      if(operation == '-'):     
        equals = str(int(first_num) - int(second_num))     
      if(operation == '/'):     
        equals = str(int(first_num) / int(second_num))
      if(operation == '*'):     
        equals = str(int(first_num) * int(second_num))        
      
      description14 = str(f"{first_num} {operation} {second_num} = {equals}")
      await interaction.respond(content = 'done')
      embed4 = discord.Embed(title = 'calculator', description = "".join(description14))
      operation = None
      first_num = ''
      second_num = ''
      is_on_button = 'first'
   if(id == '1' or id == '2' or id == '3' or id == '3' or id == '4' or id == '5' or id == '6' or id == '7' or id == '8' or id == '9' or id == '0' or id == '=' or id == 'CE' or id == '/' or id == '*' or id == '-' or id == '+'):
     await message.edit(embed = embed4, components = [
     [
      Button(emoji = '1️⃣',style = 1, id = '1'),
      Button(emoji = "2️⃣",style = 1, id='2'),
      Button(emoji = '3️⃣',style = 1, id = '3'),
      Button(emoji = '➕',style = 1, id = '+')
     ],
     [
      Button(emoji = '4️⃣',style = 1, id = '4'),
      Button(emoji = "5️⃣",style = 1, id='5'),
      Button(emoji = '6️⃣',style = 1, id = '6'),
      Button(emoji = '➖',style = 1, id = '-')
     ],
     [
      Button(emoji = '7️⃣',style = 1, id = '7'),
      Button(emoji = '8️⃣',style = 1, id = '8'),
      Button(emoji = '9️⃣',style = 1, id = '9'),
      Button(emoji = '➗',style = 1, id = '/')
     ],
     [
      Button(label = '=',style = 2, id = '='),
      Button(emoji = '0️⃣',style = 1, id = '0'),
      Button(label = 'Clear',style = 2, id = 'CE'),
      Button(emoji = '✖️',style = 1, id = '*')      
     ]
   ])

#ignore this its just used to make the bot be almost active 24/7
keep_alive()
#runs the bot
client.run(os.environ['token'])