"""IMPORTANT: PLEASE INSTALL THE FOLLOWING BEFORE RUNNING:"""
#pip install PyNaCl - voice channel sync
#pip install Discord - main discord files
#pip install pillow - for image manipulation

# © Copyright @Justice - Discord 2021

import keep_alive

import discord #main discord file
from discord.ext import commands, tasks #secondary discord file
from discord.utils import get
import os #for env file
import requests #requests

import json #json reader
import random #random generator
import aiohttp #to search the web

import time #time commands
from datetime import datetime

import asyncio

from PIL import Image as image #imagine manipulation
from PIL import ImageFont, ImageDraw
from io import BytesIO #image manipulation
import pyfiglet

import aiofiles

import akinator as ak

api_key = "23d8f873ed81b457f85c31512d6b87ed"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

import praw

from alexa_reply import reply

import pycountry
import fruit_stand


reddit = praw.Reddit(
  client_id = "JMP4Sf57faZZBZAMU2aicQ", 
  client_secret = "VRb33wE3ZSJO0SIXFG0FNXngQuX3Xw", 
  username = "Justice--06", 
  password = "Blackpanther06.", 
  user_agent = "Celeste")

subreddit = reddit.subreddit("memes")
all_subs = []
upvote_count = []
top = subreddit.top(limit = 100)

for submission in top:
  all_subs.append(submission)
  upvote_count.append(submission.score)

subreddit = reddit.subreddit("dankmemes")
top = subreddit.top(limit = 100)

for submission in top:
  all_subs.append(submission)
  upvote_count.append(submission.score)

subreddit = reddit.subreddit("Showerthoughts")
shower_thoughts = []
upvote_st = []
top = subreddit.top(limit = 100)

for submission in top:
  shower_thoughts.append(submission)
  upvote_st.append(submission.score)

subreddit = reddit.subreddit("foxes")
foxes123456 = []
upvote_fox = []
top = subreddit.top(limit = 100)

for submission in top:
  foxes123456.append(submission)
  upvote_fox.append(submission.score)

subreddit = reddit.subreddit("dogpictures")
dogs123456 = []
upvote_dog = []
top = subreddit.top(limit = 100)

for submission in top:
  dogs123456.append(submission)
  upvote_dog.append(submission.score)


subreddit = reddit.subreddit("catpictures")
cats = []
upvote_cat = []
top = subreddit.top(limit = 100)

for submission in top:
  cats.append(submission)
  upvote_cat.append(submission.score)

subreddit = reddit.subreddit("wholesomememes")
wholesome1 = []
upvote_wholesome = []
top = subreddit.top(limit = 100)

for submission in top:
  wholesome1.append(submission)
  upvote_wholesome.append(submission.score)

def message_prefixes_custom(guild):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  
  return prefixes[str(guild.id)]

countries = []
fruits = []

def get_prefix(client, message):
  with open("prefixes.json", "r") as f:
    prefixes = json.load(f)
  
  return prefixes[str(message.guild.id)]

intents = discord.Intents.all()
intents.members = True

def prefix_for_celeste(client,message):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    if prefixes[str(message.guild.id)] != None:
      return prefixes[str(message.guild.id)]

    else:
      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

      prefixes[str(message.guild.id)] = "//"

      with open("prefixes.json", "w") as f:
          json.dump(prefixes,f)

      return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix = prefix_for_celeste, intents=intents)
client.remove_command('help')
client.sniped_messages = {}
client.ticket_configs = {}

autoresponses = {}

colors = [0xFF0000, 0xED471B, 0x32FF00, 0x00FFF0, 0x00FF8B, 0x006CFF, 0x113D79, 0x250C66, 0x9173DF, 0xDB18C6, 0x4F7B89, 0x88DAF5, 0x1E8917, 0x1E8917,  0xDA1111, 0xFF0097, 0x4D1067, 0x4D7BB2, 0x29887F, 0x43ED96, 0x43ED96, 0xB28CC7]
ball_answers = ["Yes", "Maybe", "No", "Definetly not", "Ask again","For sure", "Not clear", "If I tell you now, your future will be hunted."]

def color_picker():
  color = random.choice(colors)
  return color

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return (quote) 




@client.event
async def on_guild_join(guild):


    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "//"

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)











@client.event
async def on_ready():
  # for emoji in client.emojis:
  #       print("Name:", emoji.name + ",", "ID:", emoji.id)
  current_time = datetime.now().strftime("%H:%M:%S")
  print("--------------------------------------------------------------------------")
  print("Current Time =", current_time) 
  await client.change_presence(activity=discord.Streaming(name=f'', url='https://www.youtube.com/watch?v=6AviDjR9mmo&ab_channel=NationalGeographic'))

  async with aiofiles.open("ticket_configs.txt", mode="a") as temp:
        pass

  async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            client.ticket_configs[int(data[0])] = [int(data[1]), int(data[2]), int(data[3])]

  for fruit in fruit_stand.shopping_list(n=100):
    if "," in fruit or " " in fruit or "-" in fruit or "Açaí" in fruit:
      pass
    elif len(fruit) <= 5:
      fruits.append(fruit)
    else:
      pass

  for country in pycountry.countries:
      if "," in country.name or " " in country.name or "-" in country.name:
        pass
      elif len(country.name) <= 5:
        countries.append(country.name)
      else:
        pass

  print("{0.user} has logged in and is ready to go!".format(client))
  activeservers = client.guilds
  for guild in activeservers:
    print(f"{guild.name}: {guild.id}: {guild.member_count}")
  # toleave = client.get_guild(807854126691254272)
  # await toleave.leave()

async def ch_pr():
  await client.wait_until_ready()

  member_count = 0
  for guild in client.guilds:
    for member in guild.members:
      member_count += 1

  statuses = ["www.celeste.gq", f"on {len(client.guilds)} servers", "the moon 🌙‎ ‎", f"//help", f"for {member_count} members"]

  while not client.is_closed():
    status = random.choice(statuses)

    await client.change_presence(activity=discord.Streaming(name=status, url='https://www.youtube.com/watch?v=6AviDjR9mmo&ab_channel=NationalGeographic'))

    await asyncio.sleep(10)



snipe_message_author = {}
snipe_message_content = {}
snipe_message_time = {}
snipe_message_author_url = {}




@client.event
async def on_message(message):

  if client.user == message.author:
    return

  if message.channel.type is discord.ChannelType.private:
    return

  if "celeste" in message.channel.name:
    try:
      msg = message.content.lower()
      sentence = reply(msg, client.user.name, "Justice#0514")
      await message.reply(sentence, mention_author = False)
    except:
      sentence = "Sorry, my chatbot feature is currently under maintenence. Please try again later."
      await message.reply(sentence, mention_author = False)

  if message.mentions:
    if "<@!818651306641326121>" in message.content:

            with open("prefixes.json", "r") as f:
                prefixes = json.load(f)

            pre = prefixes[str(message.guild.id)] 
            color=color_picker()
            embed = discord.Embed(title = f"{message.guild.name}'s Prefix:", description = f"My prefix for this server is: **{message_prefixes_custom(message.guild)}**\nYou can change my prefix using `{message_prefixes_custom(message.guild)}prefix [new_prefix]`", color=color, timestamp=datetime.utcnow())
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png")
            await message.channel.send(embed=embed)
            


    id_of_user_mention = str(message.mentions[0].id)
    with open('afk.json') as f:
      afk = json.load(f)
    tryer = afk.get(id_of_user_mention, None)
    if tryer != None:
      color=color_picker()
      embed = discord.Embed(title = "AFK!", description = f"<@{id_of_user_mention}> has gone afk!\n\n**Reason:** {tryer}", color=color)
      await message.channel.send(embed=embed)

  if message.author.id != 818651306641326121:
    with open('atr.json') as f:
      atr = json.load(f)

    with open('att.json') as f:
      att = json.load(f)

    values = atr.keys()
    for value in values:
      if value in message.content and atr.get(message.content) == message.guild.name:
        returning_value = att.get(message.content, None)
        if returning_value != None:
          await message.channel.send(returning_value)
        else:
          pass
        
  if "<@818651306641326121>" in message.content and message.author.id != 818651306641326121:
      color = color_picker()
      embed = discord.Embed(title = "Prefix:", description = f"The prefix for this server is {message_prefixes_custom(ctx.message.guild)}.", color=color)
      await message.channel.send(embed=embed)
    
  await client.process_commands(message)





@client.command()
@commands.has_permissions(administrator = True)
async def prefix(ctx, prefix = None):
  color = color_picker()
  if prefix == None:
    embed = discord.Embed(title = "Error!", description = f"Please enter a prefix for Celeste! For example:\n`{message_prefixes_custom(ctx.message.guild)}prefix +`", color=color)
    await ctx.send(embed=embed)
    return

  with open("prefixes.json", "r") as f:
      prefixes = json.load(f)

  prefixes[str(ctx.guild.id)] = prefix

  with open("prefixes.json", "w") as f:
      json.dump(prefixes,f)    

  embed = discord.Embed(title = "Success!", description = f"The new prefix for {ctx.message.guild.name} is now `{prefix}`", color=color)
  await ctx.send(embed=embed)

#autoresponses
@client.command()
@commands.has_permissions(ban_members = True)
async def ar(ctx, *ar):
  count = 0
  response = ""
  trigger = ""
  while ar[count] != "&":
    response += ar[count]
    response += " "
    count += 1
  response = response[:-1]
  count += 1
  while count < len(ar):
    trigger += ar[count]
    trigger += " "
    count += 1
  trigger = trigger[:-1]


  with open('atr.json') as f:
    atr = json.load(f)

  with open('att.json') as f:
    att = json.load(f)


  tester = atr.get(response, None)
  tester2 = att.get(response, None)
  if tester == None or tester2 == None or tester2 != trigger:
    atr[response] = ctx.guild.name
    att[response] = trigger
    color = color_picker()
    embed = discord.Embed(title = "Added!", description = f"The autoresponse *{response}* has been added with the trigger *{trigger}*.", color=color)
    await ctx.send(embed=embed)
  else:
    del atr[response]
    del att[response]
    color = color_picker()
    embed = discord.Embed(title = "Removed!", description = f"The autoresponse *{response}* has been removed with the trigger *{trigger}*.", color=color)
    await ctx.send(embed=embed)


  with open('atr.json', 'w') as f:
    json.dump(atr, f)
  with open('att.json', 'w') as f:
    json.dump(att, f)


@client.event
async def on_message_delete(message):
      if message.author.id != 818651306641326121:
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        snipe_message_time[message.channel.id] = message.created_at
        snipe_message_author_url[message.channel.id] = message.author.avatar_url

edit_snipe_message_author = {}
edit_snipe_before_message_content = {}
edit_snipe_after_message_content = {}
edit_snipe_message_time = {}
edit_snipe_message_author_url = {}

@client.event
async def on_message_edit(message_before, message_after):
      if message_before.author.id != 818651306641326121 and message_after.author.id != 818651306641326121:
        edit_snipe_message_author[message_before.channel.id] = message_before.author
        edit_snipe_before_message_content[message_before.channel.id] = message_before.content
        edit_snipe_after_message_content[message_before.channel.id] = message_after.content
        edit_snipe_message_time[message_before.channel.id] = message_after.created_at
        edit_snipe_message_author_url[message_before.channel.id] = message_after.author.avatar_url
      else:
        return



global reminder_count
with open('reminder_count.json') as f:
    reminderc = json.load(f)
reminder_count= reminderc.get("Count")


@tasks.loop(seconds = 1)
async def reminders_function():
  global reminder_count
  with open('reminder_count.json') as f:
    reminderc = json.load(f)
  reminder_count= reminderc.get("Count")
  reminder_count += 1
  reminderc["Count"] = reminder_count

  with open('reminders.json') as f:
    reminders = json.load(f)
  with open('reminder_reason.json') as f:
    reminder_reason = json.load(f)
  with open('reminder_time.json') as f:
    reminder_time = json.load(f)
  with open('reminder_url.json') as f:
    reminder_url = json.load(f)


  check = reminders.get(str(reminder_count))
  if check == None:
    pass
  else:
    color = color_picker()
    embed = discord.Embed(title = "Reminder!", description = f"**Reason**: {reminder_reason.get(str(reminder_count))} \n **Time:** {reminder_time.get(str(reminder_count))}\n\n**[Jump to Message]({reminder_url.get(str(reminder_count))})**", color = color)

    user = await client.fetch_user(int(check))
    await discord.DMChannel.send(user, embed=embed)

    del reminders[str(reminder_count)]
    del reminder_reason[str(reminder_count)]
    del reminder_time[str(reminder_count)]
    del reminder_url[str(reminder_count)]

    with open('reminders.json', 'w') as f:
      json.dump(reminders, f)
    with open('reminder_reason.json', 'w') as f:
      json.dump(reminder_reason, f)
    with open('reminder_time.json', 'w') as f:
      json.dump(reminder_time, f)
    with open('reminder_url.json', 'w') as f:
      json.dump(reminder_url, f)


  with open('tempban.json') as f:
    tempban = json.load(f)
  with open('tempban_reason.json') as f:
    tempban_reason = json.load(f)
  check = tempban.get(str(reminder_count))
  if check == None:
    pass
  else:
    guildz = None
    for guild in client.guilds:
      try:
        user = await client.fetch_user(int(check))
        await guild.unban(user)
        guildz = guild
        link = await guildz.create_invite(max_age = 0)
        color = color_picker()
        embed = discord.Embed(title = "Unbanned!", description = "You have been unbanned! Don't make the same mistake twice!\n\n**Reason**: " + tempban_reason.get(str(reminder_count)) + "\n\nServer Invite: \n" + link, color = color)
        await discord.DMChannel.send(user, embed=embed)
      except:
        pass
    del tempban[str(reminder_count)]
    del tempban_reason[str(reminder_count)]

    with open('tempban.json', 'w') as f:
      json.dump(tempban, f)
    with open('tempban_reason.json', 'w') as f:
      json.dump(tempban_reason, f)

  with open('tempmute.json') as f:
      tempmute = json.load(f)
  with open('tempmute_reason.json') as f:
      tempmute_reason = json.load(f)
  with open('tempmute_role.json') as f:
      tempmute_role = json.load(f)

  check = tempmute.get(str(reminder_count))
  if check == None:
    pass
  else:
    user = await client.fetch_user(int(check))
    guild_id = tempmute_role.get(str(reminder_count))
    guild = client.get_guild(int(guild_id))
    mute_role = discord.utils.get(guild.roles, name = "MUTE")
    async for user in guild.fetch_members(limit=None):
      if user.id == int(check):
        await user.remove_roles(mute_role)
    color = color_picker()
    embed = discord.Embed(title = "Unmuted!", description = "You have been unmuted! Don't make the same mistake twice!\n**Reason**: " + tempmute_reason.get(str(reminder_count)), color = color)
    await discord.DMChannel.send(user, embed=embed)

    del tempmute[str(reminder_count)]
    del tempmute_reason[str(reminder_count)]
    del tempmute_role[str(reminder_count)]
    

    with open('tempmute.json', 'w') as f:
      json.dump(tempmute, f)
    with open('tempmute_reason.json', 'w') as f:
      json.dump(tempmute_reason, f)
    with open('tempmute_role.json', 'w') as f:
      json.dump(tempmute_role, f)
  
  with open('reminder_count.json', 'w') as f:
      json.dump(reminderc, f)



  with open('giveaway.json', 'r') as f:
      gawjson = json.load(f)

  gaw = gawjson.get(str(reminder_count), None)

  if gaw != None:
    guild = client.get_guild(int(gaw[4]))
    channel = guild.get_channel(int(gaw[1]))
    new_gaw_msg = await channel.fetch_message(int(gaw[0]))

    users = await new_gaw_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    color = color_picker()

    await channel.send(f"🎉 🎉 🎉  {winner.mention} won the giveaway hosted by <@{gaw[2]}> for **{gaw[3]}**! 🎉 🎉 🎉")

    embed = discord.Embed(title="🎉 Giveaway Over! 🎉", description=f"Your giveaway for *{gaw[3]}* has ended.\n**Winner:** {winner.mention}", color=color, url = new_gaw_msg.jump_url)

    embed1 = discord.Embed(title="🎉 Giveaway Over! 🎉", description=f"**Hosted By:** <@{gaw[2]}>\n**Prize:** {gaw[3]}\n\n**Winner:** {winner.mention}", color=color)
    await new_gaw_msg.edit(embed=embed1)
    for user in guild.members:
      if user.id == int(gaw[2]):
        author = user
    await author.send(embed=embed)

  

#tempban
@client.command(aliases=["tempban"])
 
@commands.has_permissions(ban_members = True)
async def tban(ctx, member: discord.Member = None, days = None, hours = None, minutes = None, seconds = None, *, reason = None):
  try:
    with open('tempban.json') as f:
      tempban = json.load(f)
    with open('tempban_reason.json') as f:
      tempban_reason = json.load(f)
    if member == None or days == None or hours == None or minutes == None or seconds == None:
      color = color_picker()
      embed = discord.Embed(title = "Error!", description = f"Please temp-ban using the following convention:\n\n`d` - Days │ `h` - Hours │ `m` - Minutes │ `s` - Seconds\n\nFor example: `{message_prefixes_custom(ctx.message.guild)}tban @user 4d 6h 7m 3s [reason]` or `{message_prefixes_custom(ctx.message.guild)}tban @user 0d 2h 0m 3s [reason]`", color = color)
      await ctx.send(embed=embed)
      return
    if ctx.message.author == member:
      color = color_picker()
      embed = discord.Embed(
        title = "Request Declined.",
        description = "You can't ban yourself!",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if reason == None:
        reason = "Not specified."

    days_list = []
    hours_list = []
    minutes_list = []
    seconds_list = []

    days_list.append(int(days.split("d")[0]))
    hours_list.append(int(hours.split("h")[0]))
    minutes_list.append(int(minutes.split("m")[0]))
    seconds_list.append(int(seconds.split("s")[0]))

    words = ""
    if days_list[-1] != 0:
      words += str(days_list[-1]) + " days "
    if hours_list[-1] != 0:
      words += str(hours_list[-1]) + " hours "
    if minutes_list[-1] != 0:
      words += str(minutes_list[-1]) + " minutes "
    if seconds_list[-1] != 0:
      words += str(seconds_list[-1]) + " seconds "

    if words == "":
      words = "0 seconds"

    total = days_list[-1] * 86400 + hours_list[-1] * 3600 + minutes_list[-1] * 60 + seconds_list[-1] + reminder_count + 5

    link = await ctx.channel.create_invite(max_age = 0)

    color = color_picker()
    embed = discord.Embed(
          title = "You have been Banned.",
          description = "You have been temporarily banned for " + reason + "\n\n**Time:** " + words + "\n\n**Invite:** " + str(link),
          color=color
    )
    await member.send(embed=embed)

    await member.ban(reason = reason)


    tempban[total] = member.id
    tempban_reason[total] = reason

    with open('tempban.json', 'w') as f:
      json.dump(tempban, f)
    with open('tempban_reason.json', 'w') as f:
      json.dump(tempban_reason, f)

    color = color_picker()
    embed = discord.Embed(
          title = "Reqeust Accepted.",
          description = str(member.mention) + " has been banned for " + reason + "\n\n**Time:** " + words,
          color=color
    )
    await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You either do not have banning permissions, or the member could not be found. If either of these are not the case, I do not have a high enough role to ban that member.",
      color=color
    )
    await ctx.send(embed=embed)


#channel edit
@client.command(aliases=['channeledit', 'editchannel', 'editc'])
 
@commands.has_permissions(manage_channels=True)
async def cedit(ctx, channel = None, *, name = None):
  try:
    if name == None or channel == None:
      color = color_picker()
      embed = discord.Embed(
        title = "Request Declined.",
        description = "Please enter a channel to change and a new channel name.",
        color=color
      )
      await ctx.send(embed=embed)
      return
    color = color_picker()
    channel = discord.utils.get(ctx.guild.channels, name=channel)
    if channel == None: 
      color = color_picker()
      embed = discord.Embed(
        title = "Request Declined.",
        description = "That is not a valid channel.",
        color=color
      )
      await ctx.send(embed=embed)
      return
    old_name = channel.name
    await channel.edit(name=name)
    color = color_picker()
    embed = discord.Embed(
        title = "Request Accepted.",
        description = f"The channel <#{channel.id}> has been changed from {old_name} to {name}",
        color=color
    )
    await ctx.send(embed=embed)
    return
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "Make sure you enter the channel name, and not mention the channel. If this still doesnt work, you either do not have manage channels permissions, or the channel could not be found.",
      color=color
    )
    await ctx.send(embed=embed)


#tempmute
@client.command(aliases=["tempmute"])
 
@commands.has_permissions(ban_members = True)
async def tmute(ctx, member: discord.Member = None, days = None, hours = None, minutes = None, seconds = None, *, reason = None):
  try:
    global reminder_count
    with open('tempmute.json') as f:
      tempmute = json.load(f)
    with open('tempmute_reason.json') as f:
      tempmute_reason = json.load(f)
    with open('tempmute_role.json') as f:
      tempmute_role = json.load(f)


    if member == None or days == None or hours == None or minutes == None or seconds == None:
      color = color_picker()
      embed = discord.Embed(title = "Error!", description = f"Please temp-mute using the following convention:\n\n`d` - Days │ `h` - Hours │ `m` - Minutes │ `s` - Seconds\n\nFor example: `{message_prefixes_custom(ctx.message.guild)}tmute @user 4d 6h 7m 3s [reason]` or `{message_prefixes_custom(ctx.message.guild)}tmute @user 0d 2h 0m 3s [reason]`", color = color)
      await ctx.send(embed=embed)
      return
    if ctx.message.author == member:
      color = color_picker()
      embed = discord.Embed(
        title = "Request Declined.",
        description = "You can't mute yourself!",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if reason == None:
        reason = "Not specified."

    days_list = []
    hours_list = []
    minutes_list = []
    seconds_list = []

    days_list.append(int(days.split("d")[0]))
    hours_list.append(int(hours.split("h")[0]))
    minutes_list.append(int(minutes.split("m")[0]))
    seconds_list.append(int(seconds.split("s")[0]))

    words = ""
    if days_list[-1] != 0:
      words += str(days_list[-1]) + " days "
    if hours_list[-1] != 0:
      words += str(hours_list[-1]) + " hours "
    if minutes_list[-1] != 0:
      words += str(minutes_list[-1]) + " minutes "
    if seconds_list[-1] != 0:
      words += str(seconds_list[-1]) + " seconds "

    total = days_list[-1] * 86400 + hours_list[-1] * 3600 + minutes_list[-1] * 60 + seconds_list[-1] + reminder_count + 5

    if words == "":
      words = "0 seconds"

    guild = ctx.guild
    mute_role = discord.utils.get(guild.roles, name = "MUTE")
    if mute_role == None:
      color = color_picker()
      embed = discord.Embed(
            title = "Error!",
            description = f"Be sure to creat a role called `'MUTE'` first!",
            color=color
      )
      await ctx.send(embed=embed)
      return

    await member.add_roles(mute_role)
    color = color_picker()
    embed = discord.Embed(
      title = "Muted!",
      description = f"{member} has been muted for {words}.",
      color=color
    )
    await ctx.send(embed=embed)
    color = color_picker()
    embed2 = discord.Embed(
      title = "Muted!",
      description = f"**Reason: **{reason}\n**Time: **{words}",
      color=color
    )
    await member.send(embed=embed2)

    tempmute[total] = member.id
    tempmute_reason[total] = reason
    tempmute_role[total] = ctx.guild.id


    with open('tempmute.json', 'w') as f:
      json.dump(tempmute, f)
    with open('tempmute_reason.json', 'w') as f:
      json.dump(tempmute_reason, f)
    with open('tempmute_role.json', 'w') as f:
      json.dump(tempmute_role, f)

  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You either do not have banning permissions, or the member could not be found.",
      color=color
    )
    await ctx.send(embed=embed)


@client.command()
 
@commands.has_permissions(manage_roles = True)
async def crole(ctx, *, role = None):
  try:
    if role == None:
      color = color_picker()
      embed = discord.Embed(
          title = "Request Declined.",
          description = "Please specify a role name.",
          color=color
      )
      await ctx.send(embed=embed)
      return
    guild = ctx.guild
    await guild.create_role(name=role)
    color = color_picker()
    roles = discord.utils.get(guild.roles, name = role)
    embed = discord.Embed(
          title = "Created!",
          description = f"The role {roles.mention} has been created by {ctx.author.mention}!",
          color=color
    )
    await ctx.send(embed=embed)
    return
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You do not have manage role permissions. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)





@client.event
async def on_raw_reaction_add(payload):
    if payload.member.id != client.user.id and str(payload.emoji) == u"\U0001F3AB":
        msg_id, channel_id, category_id = client.ticket_configs[payload.guild_id]

        if payload.message_id == msg_id:
            guild = client.get_guild(payload.guild_id)

            for category in guild.categories:
                if category.id == category_id:
                    break

            channel = guild.get_channel(channel_id)

            for channels in guild.text_channels:
              if str(f"ticket-{payload.member.display_name.lower()}") in str(channels.name):
                color = color_picker()
                embed = discord.Embed(
                  title = "Request Declined.",
                  description = "You already have an open ticket! Close that first to continue.",
                  color=color,
                  timestamp=datetime.utcnow()
                )
                embed.set_thumbnail(url="https://static.clubs.nfl.com/image/private/f_auto/seahawks/lfsa1vgeuehu7fhof2xs")
                await payload.member.send(embed=embed)
                message = await channel.fetch_message(msg_id)
                await message.remove_reaction(payload.emoji, payload.member)
                return

            ticket_channel = await category.create_text_channel(f"ticket-{payload.member.display_name}", topic=f"A ticket for {payload.member.display_name}.", permission_synced=True)
            
            await ticket_channel.set_permissions(payload.member, read_messages=True, send_messages=True)

            message = await channel.fetch_message(msg_id)
            await message.remove_reaction(payload.emoji, payload.member)

            color = color_picker()
            embed = discord.Embed(
                  title = "Welcome!",
                  description = f"{payload.member.mention} Thank you for creating a ticket! Please wait, a staff member will be with you shortly. To cancel the ticket, just react to the lock below.",
                  color=color
            )
            embed.set_thumbnail(url="https://static.clubs.nfl.com/image/private/f_auto/seahawks/lfsa1vgeuehu7fhof2xs")
            embed_msg = await ticket_channel.send(embed=embed)
            await embed_msg.add_reaction('🔒')

            def reaction_check(reaction, user):
              return user.id != 818651306641326121 and str(reaction.emoji) == '🔒'

            try:
                result = await client.wait_for('reaction_add', check = reaction_check)

            except asyncio.TimeoutError:
                await ticket_channel.delete()

            else:
                await ticket_channel.delete()

@client.command(manage_channels=True, aliases=["ticket"])
 
async def config_ticket(ctx, msg: discord.Message=None, category: discord.CategoryChannel=None):
  try:
    if msg is None or category is None:
        color = color_picker()
        embed = discord.Embed(
          title = "Request Declined.",
          description = f"Please specify a message id and a category id for tickets.\nFor example: `{message_prefixes_custom(ctx.message.guild)}config_ticket [message_id] [category_id]`",
          color=color
        )
        await ctx.send(embed=embed)
        return

    client.ticket_configs[ctx.guild.id] = [msg.id, msg.channel.id, category.id] # this resets the configuration

    async with aiofiles.open("ticket_configs.txt", mode="r") as file:
        data = await file.readlines()

    async with aiofiles.open("ticket_configs.txt", mode="w") as file:
        await file.write(f"{ctx.guild.id} {msg.id} {msg.channel.id} {category.id}\n")

        for line in data:
            if int(line.split(" ")[0]) != ctx.guild.id:
                await file.write(line)
                
    await msg.add_reaction(u"\U0001F3AB")
    color = color_picker()
    embed = discord.Embed(
          title = "Success",
          description = f"The ticket system has been configured! Feel free to test it out, and release it!",
          color=color
    )
    await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You do not have manage channels permissions. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)

hack_password = ["WWpBEWhv$sB@T2KYQ0XYeBA#$I^wcpUOH%nV!XJJf$2LGFsGQK", "IfHackedIntoPleaseSellBackAccountFor10Bucks", "aluezmsjidoxucyvbtnqw102938465/][.;',|``", "thisisagoodpassword", "memorysux", "imnotsingle", "imstillsingle:("]
hack_yt = ["Peppa Pig", "TheOdd1sOut", "JaidenAnimations", "Mr. Beast", "Milad Mirg", "Tech for Old People"]
hack_wanted = ["Stealing apple sauce from an old woman", "Parking in handicap spots", "Forging autographs", "Hurting a teacher's feelings", "Liking math", "Liking school", "Liking KPOP", "Liking cdramas", "Hating sports"]

@client.command()
 
async def hack(ctx, member: discord.Member = None):
  global hack_yt
  global hack_password
  global hack_wanted
  if member == None:
    member = ctx.author
  msg = await ctx.send(f"Hacking {member.mention}...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Retreiving Medical Records...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Contacting Local Police Department...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Scrapping school records and transcripts... ({random.randint(5, 9)} F's)")
  await asyncio.sleep(1)
  await msg.edit(content=f"Listing user on the black market (3 sold, 1 in stock)...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Most recent youtube video: {random.choice(hack_yt)}...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Bank Account Pin: {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}")
  await asyncio.sleep(1)
  await msg.edit(content=f"Discord Password: {random.choice(hack_password)}...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Injecting Virus: JSON Asyncio virus injected, initiating launch and deployment sequence...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Wanted For: {random.choice(hack_wanted)}...")
  await asyncio.sleep(1)
  await msg.edit(content=f"IP Address: {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}.{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}.{random.randint(0, 9)}.{random.randint(0, 9)} ...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Social Security Number: {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}...")
  await asyncio.sleep(1)
  await msg.edit(content=f"Hack Complete!")
  


@client.command()
 
async def guess(ctx):
    color = color_picker()
    embed = discord.Embed(title="Let's Begin!", description = "Celeste is ready to guess your character!", color = color)
    embed.add_field(name='Here are my commands: ', value = '`y = YES, n = NO, p = Probably, b = BACK`', inline = True)
    embed.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    await ctx.send(embed=embed)
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in ["y", "n","p","b"]
    try:
        aki = ak.Akinator()
        q = aki.start_game()
        while aki.progression <= 80:
            color = color_picker()
            embed = discord.Embed(title="Question:", description = f"{q}\n\nYour answer: `y / n / p / b`", color = color)
            await ctx.send(embed=embed)
            try:
              msg = await client.wait_for("message", check = lambda message: message.author == ctx.author, timeout = 30)
              e = discord.Embed(title="Error!", description = f"That was the first question! There is no question to go back to.", color = color)
              if msg.content.lower() == "b":
                  try:
                      q=aki.back()
                  except ak.CantGoBackAnyFurther:
                      await ctx.send(embed=e)
                      continue
              else:
                  try:
                      q = aki.answer(msg.content.lower())
                  except ak.InvalidAnswerError as er:
                      er = discord.Embed(title="Error!", description = f"An invalid answer was provided.", color = color)
                      await ctx.send(embed=er)
                      continue
            except:
              too_long = discord.Embed(title="Error!", description = f"{ctx.author.mention} took too long to respond! Game over.", color = color)
              await ctx.send(embed=embed)
              return
        aki.win()
        color = color_picker()
        final = discord.Embed(title = "My Guess:", description = f"It's {aki.first_guess['name']}! Was I correct? `(y / n)`\t", color=color)
        final.set_thumbnail(url=aki.first_guess['absolute_picture_path'])
        await ctx.send(embed=final)
        try:
          while True:
            correct = await client.wait_for("message", check = lambda message: message.author == ctx.author, timeout = 30)
            if correct.content.lower() == "y":
                color = color_picker()
                answer = discord.Embed(title = "Awesome!", description = f"It was fun playing with you! Play again soon!", color=color)
                await ctx.send(embed=answer)
                return
            elif correct.content.lower() == "n":
                color = color_picker()
                answer = discord.Embed(title = "Maybe Next Time!", description = f"It was fun playing with you! Play again soon!", color=color)
                await ctx.send(embed=answer)
                return
        except:
          too_long = discord.Embed(title="Error!", description = f"{ctx.author.mention} took too long to respond! Game over.", color = color)
          await ctx.send(embed=too_long)
          return

    except Exception as e:
        await ctx.send(e)
  








#remind
@client.command()
 
async def remind(ctx, days = None, hours = None, minutes = None, seconds = None, *, reason = None):
  with open('reminders.json') as f:
    reminders = json.load(f)
  with open('reminder_reason.json') as f:
    reminder_reason = json.load(f)
  with open('reminder_time.json') as f:
    reminder_time = json.load(f)
  with open('reminder_url.json') as f:
    reminder_url = json.load(f)



  if days == None or hours == None or minutes == None or seconds == None:
    color = color_picker()
    embed = discord.Embed(title = "Error!", description = "Please set reminders using the following convention:\n\n`d` - Days │ `h` - Hours │ `m` - Minutes │ `s` - Seconds\n\nFor example: `4d 6h 7m 3s [reason]` or `0d 2h 0m 3s [reason]`", color = color)
    await ctx.send(embed=embed)
    return
  try:
    if reason == None:
      reason = "Not specified."

    days_list = []
    hours_list = []
    minutes_list = []
    seconds_list = []

    days_list.append(int(days.split("d")[0]))
    hours_list.append(int(hours.split("h")[0]))
    minutes_list.append(int(minutes.split("m")[0]))
    seconds_list.append(int(seconds.split("s")[0]))

    words = ""
    if days_list[-1] != 0:
      words += str(days_list[-1]) + " days "
    if hours_list[-1] != 0:
      words += str(hours_list[-1]) + " hours "
    if minutes_list[-1] != 0:
      words += str(minutes_list[-1]) + " minutes "
    if seconds_list[-1] != 0:
      words += str(seconds_list[-1]) + " seconds "

    if words == "":
      words = "0 seconds"


    global reminder_count
    total = str(days_list[-1] * 86400 + hours_list[-1] * 3600 + minutes_list[-1] * 60 + seconds_list[-1] + reminder_count)
    reminders[total] = ctx.author.id
    reminder_time[total] = words
    reminder_url[total] = ctx.message.jump_url
    reminder_reason[total] = reason
    color = color_picker()
    embed = discord.Embed(title = "Reminder Set!", description = f"**Time:** {words}\n\n**Reason:** {reason}", color = color)
    embed.set_thumbnail(url='https://cdn.iconscout.com/icon/free/png-256/reminder-1605719-1361068.png')
    await ctx.send(embed = embed)


    with open('reminders.json', 'w') as f:
      json.dump(reminders, f)
    with open('reminder_reason.json', 'w') as f:
      json.dump(reminder_reason, f)
    with open('reminder_time.json', 'w') as f:
      json.dump(reminder_time, f)
    with open('reminder_url.json', 'w') as f:
      json.dump(reminder_url, f)

  except:
    color = color_picker()
    embed = discord.Embed(title = "Error!", description = "Please set reminders using the following convention:\n\n`d` - Days │ `h` - Hours │ `m` - Minutes │ `s` - Seconds\n\nFor example: `4d 6h 7m 3s` or `0d 2h 0m 3s`", color = color)
    await ctx.send(embed=embed)
    return

#autoresponse check
@client.command(aliases=["arc", "autoresponsecheck"])
 
async def archeck(ctx):
  with open('atr.json') as f:
    atr = json.load(f)

  with open('att.json') as f:
    att = json.load(f)

  send = ""
  num = 1
  for key in atr.keys():
    if atr[key] == ctx.guild.name:
      addable = "\n**" + str(num) + ") Trigger:** *" + key + "* ︱ **Response:** *" + att.get(key) + "*\n"
      send += addable
      num += 1
  if send == "":
    send += "None Added."
  color = color_picker()
  embed = discord.Embed(title = "Autoresponses:", description = send, color = color)
  await ctx.send(embed = embed)


#afk
@client.command()
 
async def afk(ctx, *, reason = None):
  if reason == None:
    reason = "None Given."
  color=color_picker()
  embed = discord.Embed(title = "AFK!", description = f"{ctx.author.mention} has gone afk.\n\n**Reason:** {reason}", color=color)

  with open('afk.json') as f:
    afk = json.load(f)

  afk[ctx.author.id] = reason

  with open("afk.json", "w") as f:
    json.dump(afk, f)

  await ctx.send(embed=embed)
  try:
    prev = ctx.author.name
    prev = "[AFK]" + prev
    await ctx.author.edit(nick=prev)
  except:
    pass

#unafk
@client.command()
 
async def unafk(ctx):
  with open('afk.json', 'r') as f:
    afk = json.load(f)

  alpha = afk.get(str(ctx.author.id), None)
  if alpha != None:
    del afk[str(ctx.author.id)]

    with open("afk.json", "w") as f:
      json.dump(afk, f)

    color=color_picker()
    embed = discord.Embed(title = "Welcome Back!", description = f"Your AFK status has been removed! To go back to AFK mode, try `{message_prefixes_custom(ctx.message.guild)} afk [reason]`", color=color)
    try:
      await ctx.author.edit(nick=ctx.author.name)
    except:
      pass
    await ctx.send(embed=embed)
    return

  elif alpha == None:
    color=color_picker()
    embed = discord.Embed(title = "Error!", description = f"You never went afk! To go AFK, try `{message_prefixes_custom(ctx.message.guild)} afk [reason]`", color=color)
    await ctx.send(embed=embed)
  

#ascii
@client.command()
 
async def ascii(ctx, *, arg = None):
  if arg == None:
    color = color_picker()
    embed = discord.Embed(title = "Error!", description = f"Make sure you enter something to convert!", color=color)
    await ctx.send(embed=embed)
    return
  ascii_banner = pyfiglet.figlet_format(arg)
  await ctx.send("```" + ascii_banner + "```")




@client.command()
 
async def suggest(ctx, *, description):
    await ctx.message.delete()
    color = color_picker()
    embed = discord.Embed(title='Suggestion:', description=f"**Suggestion:** {description}", color=color, timestamp=datetime.utcnow())
    embed.set_footer(text=f"Suggested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_thumbnail(url="https://cdn1.iconfinder.com/data/icons/business-and-finance-flat-4/128/Suggestion_idea_business_giving_light_bulb_hand-512.png")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('⬆️')
    await msg.add_reaction('⬇️')





#user info
@client.command(name="info", aliases=["memberinfo", "userinfo", "ui", "mi", "profile"])
 
async def info(ctx, target: discord.Member = None):
        if target == None:
          target = ctx.author
        else:
          target = target

        roles = []
        for role in target.roles:
          if role.name.lower() != '@everyone':
            roles.append(role)
        
        role_amt = int(len(roles))
        if role_amt < 0:
          role_amt = 0

        description = f"**Roles ({role_amt}):** "
        description += " | ".join([role.mention for role in roles])
        
        
        if description == f"**Roles ({role_amt}):** ":
          description = f"**Roles ({role_amt}):** None"
        
        color = color_picker()

        totalInvites = 0
        for i in await ctx.guild.invites():
          if i.inviter == ctx.author:
            totalInvites += i.uses

        totalInvites = str(totalInvites) + " invites"

        embed = discord.Embed(title=f"User Information for {target.name.title()}",
                      description = description,
                      color = color,
                      timestamp=datetime.utcnow())
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=target.avatar_url)

        fields = [("Name:", str(target), True),
                  ("** **", "** **", True),
                  ("ID:", str(target.id) + "       _ _        ", True),
                  ("Bot:", target.bot, True),
                  ("** **", "** **", True),
                  ("Invites:", str(totalInvites), True),
                  ("Created At:", target.created_at.strftime("%m/%d/%Y %-I:%M %p"), True),
                  ("** **", "** **", True),
                  ("Joined At:", target.joined_at.strftime("%m/%d/%Y %-I:%M %p"), True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        

        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in target.guild_permissions if p[1]])
        # embed.add_field(name="Guild Permissions", value=perm_string, inline=True)
        # embed.add_field(name="** **", value="** **", inline=True)
        # embed.add_field(name="Join Position", value=str(ctx.guild.members.index(target)), inline=True)
        embed.add_field(name="Top Role:", value=target.top_role, inline=True)
        embed.add_field(name="** **", value="** **", inline=True)
        embed.add_field(name="Discriminator:",value="#" + str(target.discriminator), inline=True)
        embed.add_field(name="Current Status:", value=str(target.status).title(), inline=True)
        embed.add_field(name="** **", value="** **", inline=True)
        embed.add_field(name="Join Position:", value=str(int(ctx.guild.members.index(target) + 1)), inline=True)
        # embed.add_field(name="Current Activity:", value=f"{str(target.activity.type).title().split('.')[1]} {target.activity.name}" if target.activity is not None else "None", inline=True)

        await ctx.send(embed=embed)


@client.command(aliases=["climate"])
 
async def weather(ctx, *, city: str = None):
  color = color_picker()
  if city == None:
    embed = discord.Embed(title = f"Error!", description = f"You never entered a city's name! Try again.", color=color)
    await ctx.send(embed=embed)
    return
  city_name = city.title()
  complete_url = base_url + "appid=" + api_key + "&q=" + city_name
  response = requests.get(complete_url)
  x = response.json()
  channel = ctx.message.channel
  if x["cod"] != "404":
      color = color_picker()
      y = x["main"]
      current_temperature = y["temp"]
      current_temperature_celsiuis = str(round(current_temperature - 273.15))
      current_pressure = y["pressure"]
      current_humidity = y["humidity"]
      z = x["weather"]
      weather_description = z[0]["description"]
      weather_description = z[0]["description"]
      embed = discord.Embed(title=f"Weather in {city_name}:",
                        color=color,
                        timestamp=ctx.message.created_at,)
      embed.add_field(name="Descripition", value=f"{weather_description.title()}", inline=False)
      embed.add_field(name="Temperature(C)", value=f"{str(int(current_temperature_celsiuis)*9/5 + 32)}°F", inline=False)
      embed.add_field(name="Humidity(%)", value=f"{current_humidity}%", inline=False)
      embed.add_field(name="Atmospheric Pressure(hPa)", value=f"{current_pressure}hPa", inline=False)
      embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
      embed.set_footer(text=f"Requested by {ctx.author.name}")
      await channel.send(embed=embed)
      return
  else:
    embed = discord.Embed(title = f"Error!", description = f"Sorry, but I couldn't find that city! Try again.", color=color)
    await ctx.send(embed=embed)
    return

#poll
@client.command(aliases=["opinion"])
 
async def poll(ctx, *, question = None):
  color = color_picker()
  if question == None:
    embed = discord.Embed(title = f"Error!", description = f"You never entered a question! Try again.", color=color)
    await ctx.send(embed=embed)
    return
  await ctx.message.delete()
  color = color_picker()
  embed = discord.Embed(title = f"{question}", description = f"Poll from {ctx.author.mention}\n\n:white_check_mark: ⇾ Yes ︱ ❎ ⇾ No", color=color)
  message = await ctx.send(embed=embed)
  await message.add_reaction('✅')
  await message.add_reaction('❎')

#guilds
@client.command(aliases=["servers", "guild", "server"])
 
async def guilds(ctx):
  color = color_picker()
  embed = discord.Embed(title = f"Celeste Server Count!", description = f"Celeste is in {len(client.guilds)} servers!", color=color)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png")
  await ctx.send(embed=embed)

#snipe
@client.command(name = 'snipe')
 
async def snipe(ctx):
    channel = ctx.channel
    try: 
        color = color_picker()
        em = discord.Embed(title = f"**Message deleted in #{channel.name}:**", description = snipe_message_content[channel.id], color=color).set_author(name=snipe_message_author[channel.id], icon_url=snipe_message_author_url[channel.id])
        em.timestamp = snipe_message_time[channel.id]
        await ctx.send(embed = em)
    except: 
        color = color_picker()
        embed = discord.Embed(title = "Error!", description = f"There are no new messages to snipe in #{channel}.", color=color)
        await ctx.send(embed=embed)

#esnipe
@client.command(aliases=['editsnipe'])
 
async def esnipe(ctx):
    channel = ctx.channel
    try: 
        color = color_picker()
        em = discord.Embed(title = f"**Message edited in #{channel.name}:**", description = f"**Before:** {edit_snipe_before_message_content.get(channel.id)}\n**After: **{edit_snipe_after_message_content.get(channel.id)}", color=color).set_author(name=edit_snipe_message_author[channel.id], icon_url=edit_snipe_message_author_url[channel.id])
        em.timestamp = edit_snipe_message_time[channel.id]
        await ctx.send(embed = em)
    except: 
        color = color_picker()
        embed = discord.Embed(title = "Error!", description = f"There are no new messages to esnipe in #{channel}.", color=color)
        await ctx.send(embed=embed)

#say
@client.command()
 
async def say(ctx, *, say = None):
  if say == None:
    say = f"What should I say {ctx.author.name}?"
  await ctx.send(say)



#8 ball
@client.command(aliases=['8ball', 'ball'])
 
async def magicball(ctx, *, arg = None):
  color = color_picker()
  try:
    if arg == "" or arg == None:
      embed = discord.Embed(title = "Error!",description = "Make sure you enter a question for the 8 ball!",color=color
      )
      await ctx.send(embed=embed)
      return
    x = random.randint(0, len(ball_answers))
    embed = discord.Embed(
      title = ball_answers[x],
      description = None,
      color=color
    )
    if x == 0:
      embed.set_image(url = "https://cdn.discordapp.com/attachments/766158371820666940/821642869248884736/8_ball_ahsoka.png")
    elif x == 1:
      embed.set_image(url = 'https://cdn.discordapp.com/attachments/766158371820666940/821642857500508240/8_ball_ahsoka_2.png')
    elif x == 2:
      embed.set_image(url = "https://cdn.discordapp.com/attachments/766158371820666940/821642855541637140/8_ball_ahsoka_1.png")
    elif x == 3:
      embed.set_image(url = "https://cdn.discordapp.com/attachments/766158371820666940/821642860302565426/8_ball_ahsoka_4.png")
    elif x == 4:
      embed.set_image(url = "https://cdn.discordapp.com/attachments/766158371820666940/821642861547749426/8_ball_ahsoka_5.png")
    elif x == 5:
      embed.set_image(url = "https://cdn.discordapp.com/attachments/766158371820666940/821642863297167360/8_ball_ahsoka_6.png")
    elif x == 6:
      embed.set_image(url = "https://cdn.discordapp.com/attachments/766158371820666940/821642864727293982/8_ball_ahsoka_7.png")
    elif x == 7:
      embed.set_image(url = "https://cdn.discordapp.com/attachments/766158371820666940/821642867885211708/8_ball_ahsoka_9.png")
    await ctx.send(embed=embed)
  except:
    embed = discord.Embed(title = "Error!",description = "Make sure you enter a question for the 8 ball!",color=color
    )
    await ctx.send(embed=embed)

#gif
@client.command()
async def gif(ctx, *, arg = None):
  try:
    search = arg
    color = color_picker()
    embed = discord.Embed(title = "Here's a gif about " + arg + "!", color=color)
    session = aiohttp.ClientSession()

    if search == 'random':
        response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=7cJQGpUz7Gjp5PvQDmB4q8NwI5ZmO6Jn')
        data = json.loads(await response.text())
        embed.set_image(url=data['data']['images']['original']['url'])
    else:
        search.replace(' ', '+')
        response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=7cJQGpUz7Gjp5PvQDmB4q8NwI5ZmO6Jn&limit=10')
        data = json.loads(await response.text())
        gif_choice = random.randint(0, 9)
        embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

    await session.close()
    await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(title = "Error!", description = f"Make sure you enter the topic of the gif you want to search!\nFor example: `{message_prefixes_custom(ctx.message.guild)}gif celeste`", color=color)
    await ctx.send(embed=embed)





#hug
@client.command()
async def hug(ctx, member: discord.Member = None):
  color = color_picker()
  if member == None:
    embed = discord.Embed(title = f"Huh?!", description = f"Who do you want to hug? Please mention them like this: `{message_prefixes_custom(ctx.message.guild)}hug @user`", color=color)
    await ctx.send(embed=embed)
    return
  elif member == ctx.author:
    member = "themselves"
  else:
    member = member.name

  embed = discord.Embed(title = f"{ctx.author.name} hugs {member}!", color=color)
  session = aiohttp.ClientSession()
  search = "anime+hug"
  response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=7cJQGpUz7Gjp5PvQDmB4q8NwI5ZmO6Jn&limit=10')
  data = json.loads(await response.text())
  gif_choice = random.randint(0, 9)
  embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

  await session.close()
  await ctx.send(embed=embed)


#kiss
@client.command()
async def kiss(ctx, member: discord.Member = None):
  color = color_picker()
  if member == None:
    embed = discord.Embed(title = f"Huh?!", description = f"Who do you want to kiss? Please mention them like this: `{message_prefixes_custom(ctx.message.guild)}kiss @user`", color=color)
    await ctx.send(embed=embed)
    return
  elif member == ctx.author:
    member = "themselves"
  else:
    member = member.name

  embed = discord.Embed(title = f"{ctx.author.name} kisses {member}!", color=color)
  session = aiohttp.ClientSession()
  search = "anime+kiss"
  response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=7cJQGpUz7Gjp5PvQDmB4q8NwI5ZmO6Jn&limit=10')
  data = json.loads(await response.text())
  gif_choice = random.randint(0, 9)
  embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

  await session.close()
  await ctx.send(embed=embed)


#cuddle
@client.command()
async def cuddle(ctx, member: discord.Member = None):
  color = color_picker()
  if member == None:
    embed = discord.Embed(title = f"Huh?!", description = f"Who do you want to cuddle? Please mention them like this: `{message_prefixes_custom(ctx.message.guild)}cuddle @user`", color=color)
    await ctx.send(embed=embed)
    return
  elif member == ctx.author:
    member = "themselves"
  else:
    member = member.name

  embed = discord.Embed(title = f"{ctx.author.name} cuddles {member}!", color=color)
  session = aiohttp.ClientSession()
  search = "anime+cuddle"
  response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=7cJQGpUz7Gjp5PvQDmB4q8NwI5ZmO6Jn&limit=10')
  data = json.loads(await response.text())
  gif_choice = random.randint(0, 9)
  embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

  await session.close()
  await ctx.send(embed=embed)


#comic
@client.command()
 
async def comic(ctx):
  color = color_picker()
  latest = requests.get('https://xkcd.com/info.0.json').json()
  num = random.randint(1, latest['num'])
  comic = requests.get('https://xkcd.com/' + str(num) + '/info.0.json').json()
  embed = discord.Embed(
    title = "Here's something fun!",
    description = '_' + comic['alt'] + '_',
    color=color
  )
  embed.set_image(url = comic['img'])
  await ctx.send(embed=embed)

#dadjoke
@client.command()
 
async def dadjoke(ctx):
  color = color_picker()
  joke = requests.get('https://icanhazdadjoke.com', headers={"Accept": "text/plain"}).text
  embed = discord.Embed(title="Here's a joke, from me to you!", description=joke, color=color)
  await ctx.send(embed=embed)

  
  


#ping
@client.command()
 
async def ping(ctx):
  ping = client.latency
  color = color_picker()
  embed = discord.Embed(title="Ping Latency:", description=str(int(ping * 1000)) + " ms", color=color)
  await ctx.send(embed=embed)

#purge
@client.command()
 
@commands.has_permissions(manage_messages = True)
async def purge(ctx, arg = None):
  try:
    if arg == None:
      await ctx.send("Please specify the number of messages I should delete!")
      return
    z = int(arg)
    await ctx.channel.purge(limit=int(z + 1))
    x = await ctx.send("Purging " + str(z) + " messages...")
    time.sleep(1)
    msg = await ctx.channel.fetch_message(x.id)
    await msg.delete() 
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You do not have manage messages permissions.",
      color=color
    )
    await ctx.send(embed=embed)
  

#inspire
@client.command()
 
async def inspire(ctx):
  quote = get_quote()
  author = quote.split("-", 1)[1]
  quote_true = quote.split("-", 1)[0]
  color = color_picker()
  embed = discord.Embed(
    title = author + ":",
    description = quote_true,
    color=color
  )
  await ctx.send(embed=embed)

#roll
@client.command()
 
async def roll(ctx, *arg):
  try:
    global num1
    num1 = []
    global cute
    cute = ""
    global num2
    num2 = []
    for word in arg:
      cute += word
    if cute == "":
      num1.append(1)
      num1.append(6)
    else:
      for word in arg:
        num1.append(word.split("-"))
      for num in num1:
        for number in num:
          num2.append(int(number))
    range1 = int(num2[0])
    range2 = int(num2[-1])
    global x
    x = random.randint(range1, range2)
    global tester
    tester = 1
    while tester < len(num2) - 1:
      if x == num2[tester]:
        x = random.randint(range1, range2)
        tester = 1
      else:
        tester += 1
    color = color_picker()
    embed = discord.Embed(
      title = "Here's what you rolled:",
      description = 'You rolled a ' + str(x) + '!',
      color=color
    )
    await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Error!",
      description = f'Make sure you typed the command right! Try `{message_prefixes_custom(ctx.message.guild)}help_fun` for more help.',
      color=color
    )
    await ctx.send(embed=embed)


#bans a user with a reason
@client.command()
 
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
  try:
    if ctx.message.author == member:
      color = color_picker()
      embed = discord.Embed(
        title = "Request Declined.",
        description = "You can't ban yourself!",
        color=color
      )
      await ctx.send(embed=embed)
    elif reason == None:
      reason = "violating server rules."
      await member.ban(reason = reason)
      color = color_picker()
      embed = discord.Embed(
        title = "Reqeust Accepted.",
        description = str(member) + " has been banned for " + reason,
        color=color
      )
      await ctx.send(embed=embed)
    else:
      await member.ban(reason = reason)
      color = color_picker()
      embed = discord.Embed(
        title = "Reqeust Accepted.",
        description = str(member) + " has been banned for " + reason,
        color=color
      )
      await ctx.send(embed=embed)

  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You either do not have banning permissions, or the member could not be found.",
      color=color
    )
    await ctx.send(embed=embed)

#kicks a user with a reason
@client.command()
 
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
  try:
    if ctx.message.author == member:
      color = color_picker()
      embed = discord.Embed(
        title = "Request Declined.",
        description = "You can't kick yourself!",
        color=color
      )
      await ctx.send(embed=embed)
    elif reason == None:
      reason = "violating server rules."
      await member.kick(reason = reason)
      color = color_picker()
      embed = discord.Embed(
        title = "Reqeust Accepted.",
        description = str(member) + " has been kicked for " + reason,
        color=color
      )
      await ctx.send(embed=embed)
    else:
      await member.kick(reason = reason)
      color = color_picker()
      embed = discord.Embed(
        title = "Reqeust Accepted.",
        description = str(member) + " has been kicked for " + reason,
        color=color
      )
      await ctx.send(embed=embed)

  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You either do not have kicking permissions, or the member could not be found.",
      color=color
    )
    await ctx.send(embed=embed)

#unbans a user
@client.command()
 
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
  try:
    banned_users = await ctx.guild.bans()
    
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user
      
      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        color = color_picker()
        embed = discord.Embed(
          title = "Request Accepted.",
          description = f"Unbanned: {user.mention}",
          color=color
        )
        await ctx.send(embed=embed)
      
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You either do not have unbanning permissions, or the member could not be found.",
      color=color
    )
    await ctx.send(embed=embed)

# #prefix
# @client.command()
# @commands.has_permissions(administrator = True)
# async def prefix(ctx, prefix):
#   try:
#     with open("prefixes.json", "r") as f:
#       prefixes = json.load(f)

#     prefixes[str(ctx.guild.id)] = prefix

#     with open("prefixes.json", "w") as f:
#       json.dump(prefixes, f)

#     message_prefixes_custom(ctx.message.guild) = prefix
#     color = color_picker()
#     embed = discord.Embed(
#       title = "Request Accepted.",
#       description = "My prefix has been changed to **" + str(prefix) + "**",
#       color=color
#     )
#     await ctx.send(embed=embed)
#   except:
#     color = color_picker()
#     embed = discord.Embed(
#       title = "Request Declined.",
#       description = "You do not have admin permissions. Nice try.",
#       color=color
#     )
#     await ctx.send(embed=embed)

# @client.command()
 
# async def prefix(ctx):
#   color = color_picker()
#   embed = discord.Embed(
#       title = "Request Declined.",
#       description = "As of now, only the owner (<@760949977903398923>) can change the prefix. This will soon be fixed. Sorry for the inconvenience. Please contact <@760949977903398923>for more information. ",
#       color=color
#   )
#   embed.set_thumbnail(
#       url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
#   )
#   await ctx.send(embed=embed)

#mock
@client.command()
 
async def mock(ctx, *arg):
  return_msg = ""
  msg = ctx.message.content.split(message_prefixes_custom(ctx.message.guild) + "mock", 1)[1]
  for letter in msg:
    x = random.randint(1,2)
    if x == 1:
      return_msg += letter.upper()
    elif x == 2:
      return_msg += letter.lower()
  await ctx.send(return_msg)

#meme
@client.command()
 
async def meme(ctx):
  global all_subs
  global upvote_count
  random_sub = random.choice(all_subs)
  index_for_meme = all_subs.index(random_sub)
  up_vote_count = upvote_count[index_for_meme]
  name = random_sub.title
  url = random_sub.url
  color=color_picker()
  embed = discord.Embed(title = name, url = f"https://www.reddit.com{random_sub.permalink})", color = color)
  embed.set_image(url = url)
  parsed_date = datetime.utcfromtimestamp(random_sub.created_utc)
  year = parsed_date.year
  month = parsed_date.month
  day = parsed_date.day
  embed.set_footer(text=f"Author: {random_sub.author} ︱ Date: {month}/{day}/{year} ︱ 👍  {up_vote_count}")
  await ctx.send(embed=embed)


#wholesome
@client.command(aliases=['whlsm'])
 
async def wholesome(ctx):
  global wholesome1
  global upvote_wholesome
  random_sub = random.choice(wholesome1)
  index_for_meme = wholesome1.index(random_sub)
  up_vote_count = upvote_wholesome[index_for_meme]
  name = random_sub.title
  url = random_sub.url
  color=color_picker()
  embed = discord.Embed(title = name, url = f"https://www.reddit.com{random_sub.permalink})", color = color)
  embed.set_image(url = url)
  parsed_date = datetime.utcfromtimestamp(random_sub.created_utc)
  year = parsed_date.year
  month = parsed_date.month
  day = parsed_date.day
  embed.set_footer(text=f"Author: {random_sub.author} ︱ Date: {month}/{day}/{year} ︱ 👍  {up_vote_count}")
  await ctx.send(embed=embed)

#fox
@client.command()
 
async def fox(ctx):
  global foxes123456
  global upvote_fox
  random_sub = random.choice(foxes123456)
  index_for_meme = foxes123456.index(random_sub)
  up_vote_count = upvote_fox[index_for_meme]
  name = random_sub.title
  url = random_sub.url
  color=color_picker()
  embed = discord.Embed(title = name, url = f"https://www.reddit.com{random_sub.permalink})", color = color)
  embed.set_image(url = url)
  parsed_date = datetime.utcfromtimestamp(random_sub.created_utc)
  year = parsed_date.year
  month = parsed_date.month
  day = parsed_date.day
  embed.set_footer(text=f"Author: {random_sub.author} ︱ Date: {month}/{day}/{year} ︱ 👍  {up_vote_count}")
  await ctx.send(embed=embed)


#dog
@client.command()
 
async def dog(ctx):
  global dogs123456
  global upvote_dog
  random_sub = random.choice(dogs123456)
  index_for_meme = dogs123456.index(random_sub)
  up_vote_count = upvote_dog[index_for_meme]
  name = random_sub.title
  url = random_sub.url
  color=color_picker()
  embed = discord.Embed(title = name, url = f"https://www.reddit.com{random_sub.permalink})", color = color)
  embed.set_image(url = url)
  parsed_date = datetime.utcfromtimestamp(random_sub.created_utc)
  year = parsed_date.year
  month = parsed_date.month
  day = parsed_date.day
  embed.set_footer(text=f"Author: {random_sub.author} ︱ Date: {month}/{day}/{year} ︱ 👍  {up_vote_count}")
  await ctx.send(embed=embed)

#cat
@client.command()
 
async def cat(ctx):
  global cats
  global upvote_cat
  random_sub = random.choice(cats)
  index_for_meme = cats.index(random_sub)
  up_vote_count = upvote_cat[index_for_meme]
  name = random_sub.title
  url = random_sub.url
  color=color_picker()
  embed = discord.Embed(title = name, url = f"https://www.reddit.com{random_sub.permalink})", color = color)
  embed.set_image(url = url)
  parsed_date = datetime.utcfromtimestamp(random_sub.created_utc)
  year = parsed_date.year
  month = parsed_date.month
  day = parsed_date.day
  embed.set_footer(text=f"Author: {random_sub.author} ︱ Date: {month}/{day}/{year} ︱ 👍  {up_vote_count}")
  await ctx.send(embed=embed)


#showerthoughts
@client.command(aliases=['showerthoughts'])
 
async def st(ctx):
  global shower_thoughts
  global upvote_st
  random_sub = random.choice(shower_thoughts)
  index_for_meme = shower_thoughts.index(random_sub)
  up_vote_count = upvote_st[index_for_meme]
  name = random_sub.title
  color=color_picker()
  embed = discord.Embed(title = name, url = f"https://www.reddit.com{random_sub.permalink})", color = color)
  parsed_date = datetime.utcfromtimestamp(random_sub.created_utc)
  year = parsed_date.year
  month = parsed_date.month
  day = parsed_date.day
  embed.set_footer(text=f"Author: {random_sub.author} ︱ Date: {month}/{day}/{year} ︱ 👍  {up_vote_count}")
  await ctx.send(embed=embed)


  

#lock channel
@client.command()
 
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel=None):
  try:
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    color = color_picker()
    embed = discord.Embed(
      title = "Request Accepted.",
      description = str(ctx.channel) + " has successfully been locked down.",
      color=color
    )
    await ctx.send(embed=embed)
  
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)

#unlock channel
@client.command()
 
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel=None):
  try:
    channel = channel or ctx.channel
    overwrite = channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
    color = color_picker()
    embed = discord.Embed(
      title = "Request Accepted.",
      description = str(ctx.channel) + " has successfully been unlocked.",
      color=color
    )
    await ctx.send(embed=embed)
  
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin or a mod. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)  

#lockdown
@client.command()
 
@commands.has_permissions(manage_channels=True)
async def lockdown(ctx):
  try:
    text_channel_list = []
    for channel in ctx.guild.text_channels:
            text_channel_list.append(channel.id)

    for id in text_channel_list:
        channel = client.get_channel(id)
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        color = color_picker()
        embed = discord.Embed(
        title = "Server lockdown.",
        description = "The server has temporarily been locked down. Please refer to your announcement channel for more details as to why it was locked. Sorry for any inconvenience this may have caused.",
        color=color
        )
        await channel.send(embed=embed)
    color = color_picker()
    embed = discord.Embed(
        title = "Server lockdown.",
        description = f"The server has successfully been locked down. To unlock, please type **{message_prefixes_custom(ctx.message.guild)}unlockdown**.",
        color=color
    )
    await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin or a mod. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)

#unlockdown
@client.command()
 
@commands.has_permissions(manage_channels=True)
async def unlockdown(ctx):
  try:
    text_channel_list = []
    for channel in ctx.guild.text_channels:
            text_channel_list.append(channel.id)

    for id in text_channel_list:
        channel = client.get_channel(id)
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        color = color_picker()
        embed = discord.Embed(
        title = "Server unlockdown.",
        description = "The server has been unlocked. Please refer to your announcement channel for more details as to why it was locked. Sorry for any inconvenience this may have caused.",
        color=color
        )
        await channel.send(embed=embed)
    color = color_picker()
    embed = discord.Embed(
        title = "Server lockdown.",
        description = f"The server has successfully been unlocked. To lock, please type **{message_prefixes_custom(ctx.message.guild)}lockdown**.",
        color=color
    )
    await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin or a mod. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)

#mute
@client.command(pass_context=True)
 
@commands.has_permissions(manage_roles = True)
async def mute(ctx, member: discord.Member = None, *, reason = "For violating server rules and policies."):
  try:
    if member == None:
      color = color_picker()
      embed = discord.Embed(
            title = "Error!",
            description = f"Be sure to specify someone to mute first!",
            color=color
      )
      await ctx.send(embed=embed)
      return
    guild = ctx.guild
    mute_role = discord.utils.get(guild.roles, name = "MUTE")
    if mute_role == None:
      color = color_picker()
      embed = discord.Embed(
            title = "Error!",
            description = f"Be sure to creat a role called `'MUTE'` first!",
            color=color
      )
      await ctx.send(embed=embed)
      return
    for role in member.roles:
        if role == mute_role:
          color = color_picker()
          embed = discord.Embed(
            title = "Error!",
            description = f"{member} was already muted.",
            color=color
          )
          await ctx.send(embed=embed)
          return
    await member.add_roles(mute_role)
    color = color_picker()
    embed = discord.Embed(
      title = "Success!",
      description = f"{member} has been muted.",
      color=color
    )
    await ctx.send(embed=embed)
    color = color_picker()
    embed2 = discord.Embed(
      title = "Muted!",
      description = f"**Reason: ** {reason}",
      color=color
    )
    await member.send(embed=embed2)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin or a mod. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)

#unmute
@client.command(pass_context=True)
 
@commands.has_permissions(manage_roles = True)
async def unmute(ctx, member: discord.Member = None):
  try:
    if member == None:
      color = color_picker()
      embed = discord.Embed(
            title = "Error!",
            description = f"Be sure to specify someone to unmute first!",
            color=color
      )
      await ctx.send(embed=embed)
      return
    guild = ctx.guild
    mute_role = discord.utils.get(guild.roles, name = "MUTE")
    if mute_role == None:
      color = color_picker()
      embed = discord.Embed(
            title = "Error!",
            description = f"Be sure to create a role called `'MUTE'` first!",
            color=color
      )
      await ctx.send(embed=embed)
      return
    for role in member.roles:
        if role == mute_role:
          await member.remove_roles(mute_role)
          color = color_picker()
          embed = discord.Embed(
            title = "Success!",
            description = f"{member} has successfully been unmuted.",
            color=color
          )
          color = color_picker()
          embed2 = discord.Embed(
            title = "Yay!",
            description = f"You have been unmuted. Be sure not to break any rules again!",
            color=color
          )
          await ctx.send(embed=embed)
          await member.send(embed=embed2)
          return

       
    color = color_picker()
    embed = discord.Embed(
      title = "Error!",
      description = f"{member} was not previously muted.",
      color=color
    )
    await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin or a mod. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)
    
#warn
@client.command()
 
@commands.has_permissions(manage_roles = True)
async def warn(ctx, member: discord.Member = None, *reason):
  color=color_picker()
  try:
    if member == None:
      color = color_picker()
      embed = discord.Embed(
        title = "Request Declined.",
        description = "Make sure you enter a member to warn!",
        color=color
      )
      await ctx.send(embed=embed)
    global x
    x = ""
    for letter in reason:
        x += letter
        x+=" "
    if x == "":
      x += "For violating server rules."
    embed = discord.Embed(title = "Warning!", description = f"**Reason:** {x}", color=color).set_author(name=ctx.message.author, icon_url="https://icons-for-free.com/iconfiles/png/512/danger+warn+warning+icon-1320196066636054085.png")
    embed.timestamp = ctx.message.created_at
    await member.send(embed=embed)
    embed2 = discord.Embed(title = f"{member} has been warned.", color=color)
    await ctx.channel.send(embed=embed2)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin or a mod. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)
  
@client.command(pass_context=True, aliases=['nick'])
 
@commands.has_permissions(manage_roles = True)
async def nickname(ctx, member: discord.Member = None, *, nick = None):
  try:
    if nick == None or member == None:
      color = color_picker()
      embed = discord.Embed(
        title = "Request Declined.",
        description = "Please specify a valid nickname or person.",
        color=color
      )
      await ctx.send(embed=embed)
    else:
      before = member.name
      await member.edit(nick=nick)
      color = color_picker()
      embed = discord.Embed(
        title = "Request Accepted!",
        description = f"Success! <@{member.id}> name was changed from {before} to {nick}!",
        color=color
      )
      await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin or a mod. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)






#role
@client.command()
 
@commands.has_permissions(manage_roles = True)
async def role(ctx, member: discord.Member, *role):
  try:
    color=color_picker()
    server_roles = ctx.guild.roles
    y = ""
    for tru in role:
      if tru == role[-1]:
        y += tru
      else:
        y += tru
        y += " "
    for item in server_roles:
        if y == item.name:
          for ll in member.roles:
            if ll.name == item.name:
              x = ctx.guild.get_role(item.id)
              try:
                await member.remove_roles(x)
              except:
                embed = discord.Embed(
                  title = "Request Declined.",
                  description = "Make sure the role you are trying to remove is lower than my role.",
                  color=color
                )
                await ctx.send(embed=embed)
                return

              embed = discord.Embed(
                title = "Role Removed.",
                description = f"The role {item.name} has been removed from {member}.",
                color=color
              )
              await ctx.send(embed=embed)
              return
    for item in server_roles:
        if y == item.name:
          x = ctx.guild.get_role(item.id)
          try:
            await member.add_roles(x)
          except:
            embed = discord.Embed(
              title = "Request Declined.",
              description = "make sure the role you are trying to remove is lower than my role.",
              color=color
            )
            await ctx.send(embed=embed)
            return
          embed = discord.Embed(
            title = "Role Added.",
            description = f"The role {item.name} has been added to {member}.",
            color=color
          )
          await ctx.send(embed=embed)
          return
    embed = discord.Embed(
      title = "Request Declined.",
      description = "That role does not exist.",
      color=color
    )
    await ctx.send(embed=embed)
  except:
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin or a mod. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)

#voice join
@client.command()
 
async def join(ctx):
  color = color_picker()
  try:
      channel = ctx.message.author.voice.channel
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      if voice and voice.is_connected():
          await voice.move_to(channel)
      else:
          await channel.connect()
      embed = discord.Embed(
        title = "Success!",
        description = "I have joined your voice channel!",
        color=color
      )
      await ctx.send(embed=embed)
  except:
      embed = discord.Embed(
        title = "Error!",
        description = "Join a voice channel first to invite me!",
        color=color
      )
      await ctx.send(embed=embed)
      return

#voice leave
@client.command()
 
async def leave(ctx):
  try:
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        color = color_picker()
        embed = discord.Embed(
          title = "Disconnected.",
          description = "I hope to see you soon again!",
          color=color
        )
        await ctx.send(embed=embed)
    else:
        color = color_picker()
        embed = discord.Embed(
          title = "Error!",
          description = "Join a voice channel first to disconnect me!",
          color=color
        )
        await ctx.send(embed=embed)

  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Error!",
      description = "Join a voice channel first to disconnect me!",
      color=color
    )
    await ctx.send(embed=embed)
    return


# voice play
# @client.command()
# async def play(ctx, url: str):
#   song_there = os.path.isfile("song.mp3")
#   try:
#         if song_there:
#             os.remove("song.mp3")
#   except PermissionError:
#         await ctx.send(f"Wait for the current playing music to end or use the `{message_prefixes_custom(ctx.message.guild)}stop` command")
#         return
#   try:
#     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
#     if voice.is_connected():
#       ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#       }
#       with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#           ydl.download([url])
#       for file in os.listdir("./"):
#           if file.endswith(".mp3"):
#               os.rename(file, "song.mp3")
#       voice.play(discord.FFmpegPCMAudio("song.mp3"))
#       color = color_picker()
#       embed = discord.Embed(
#         title = "Playing:",
#         description = url,
#         color=color
#       )
#       await ctx.send(embed=embed)
#     else:
#         color = color_picker()
#         embed = discord.Embed(
#           title = "Error!",
#           description = "Join a voice channel first to play music!",
#           color=color
#         )
#         await ctx.send(embed=embed)

#   except:
#     color = color_picker()
#     embed = discord.Embed(
#       title = "Error!",
#       description = "Join a voice channel first to play music!",
#       color=color
#     )
#     await ctx.send(embed=embed)
#     return





#voice pause
@client.command()
 
async def pause(ctx):
  try:
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        color = color_picker()
        embed = discord.Embed(
          title = "Paused!",
          description = f"Requested by: {ctx.message.author}",
          color=color
        )
        await ctx.send(embed=embed)
    else:
        color = color_picker()
        embed = discord.Embed(
          title = "Error!",
          description = "Currently no audio is playing.",
          color=color
        )
        await ctx.send(embed=embed)
  except:
    color = color_picker()
    embed = discord.Embed(
          title = "Error!",
          description = "Invite me to a voice channel first!",
          color=color
    )
    await ctx.send(embed=embed)

#voice resume
@client.command()
 
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        color = color_picker()
        embed = discord.Embed(
          title = "Resumed!",
          description = f"Requested by: {ctx.message.author}",
          color=color
        )
        await ctx.send(embed=embed)
    else:
        color = color_picker()
        embed = discord.Embed(
          title = "Error!",
          description = "Currently no audio is playing.",
          color=color
        )
        await ctx.send(embed=embed)

#voice stop
@client.command()
 
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    color = color_picker()
    embed = discord.Embed(
          title = "Stopped!",
          description = f"Requested by: {ctx.message.author}",
          color=color
    )
    await ctx.send(embed=embed)

#wanted img
@client.command()
 
async def wanted(ctx, user: discord.Member = None):
  try:
    if user == None:
      user = ctx.author
    wanted = image.open("Images/wanted.jpeg")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = image.open(data)
    pfp = pfp.resize((90,90))
    wanted.paste(pfp, (50,87))
    wanted.save("Images/profile.jpeg")
    await ctx.send(file = discord.File("Images/profile.jpeg"))
  except:
    color = color_picker()
    embed = discord.Embed(
          title = "Error!",
          description = "Enter a valid member!",
          color=color
    )
    await ctx.send(embed=embed)

#avatar
@client.command(aliases=['pfp'])
 
async def avatar(ctx, user: discord.Member = None):
  try:
    if user == None:
      user = ctx.author
    url = user.avatar_url
    color = color_picker()
    embed = discord.Embed(title = f"Avatar for {user}:", color = color)
    embed.set_image(url=url)
    await ctx.send(embed= embed)
  except:
    color = color_picker()
    embed = discord.Embed(
          title = "Error!",
          description = "Enter a valid member!",
          color=color
    )
    await ctx.send(embed=embed)

#slap
@client.command()
 
async def slap(ctx, user: discord.Member = None, user1: discord.Member = None):
  try:
    if user == None:
      user = client.get_user(818651306641326121)
      user1 = ctx.author
    elif user1 == None:
      user1 = user
      user = ctx.author
    slap = image.open("Images/slap.jpeg")
    asset = user.avatar_url_as(size = 128)
    asset1 = user1.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    data1 = BytesIO(await asset1.read())
    pfp = image.open(data)
    pfp = pfp.resize((70,70))
    pfp1 = image.open(data1)
    pfp1 = pfp1.resize((70,70))
    slap.paste(pfp, (200,89))
    slap.paste(pfp1, (171,257))
    slap.save("Images/profile.jpeg")
    await ctx.send(file = discord.File("Images/profile.jpeg"))
  except:
    color = color_picker()
    embed = discord.Embed(
          title = "Error!",
          description = "Enter a valid member!",
          color=color
    )
    await ctx.send(embed=embed)

#boot
@client.command()
 
async def boot(ctx, user: discord.Member = None, user1: discord.Member = None):
  try:
    if user == None:
      user = client.get_user(818651306641326121)
      user1 = ctx.author
    elif user1 == None:
      user1 = user
      user = ctx.author
    boot = image.open("Images/boot.jpeg")
    asset = user.avatar_url_as(size = 128)
    asset1 = user1.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    data1 = BytesIO(await asset1.read())
    pfp = image.open(data)
    pfp = pfp.resize((100,100))
    pfp1 = image.open(data1)
    pfp1 = pfp1.resize((100,100))
    boot.paste(pfp, (207,13))
    boot.paste(pfp1, (650,217))
    boot.save("Images/profile.jpeg")
    await ctx.send(file = discord.File("Images/profile.jpeg"))
  except:
    color = color_picker()
    embed = discord.Embed(
          title = "Error!",
          description = "Enter a valid member!",
          color=color
    )
    await ctx.send(embed=embed)

#tweet
@client.command()
 
async def tweet(ctx, *, tweet = None):
  if tweet == None:
    color = color_picker()
    embed = discord.Embed(
          title = "Error!",
          description = "What are you tweeting about!",
          color=color
    )
    await ctx.send(embed=embed)
    return
  else:
    img = image.open("Images/tweet.jpg")
    font = ImageFont.truetype("Images/Fonts/Open_Sans/OpenSans-Regular.ttf", 24)

    draw = ImageDraw.Draw(img)
    text = tweet
    draw.text((0, 150), text, (0, 0, 0), font=font)
    img.save("Images/profile.jpeg")
    await ctx.send(file = discord.File("Images/profile.jpeg"))


#invite
@client.command()
 
async def invite(ctx):
  color = color_picker()
  embed = discord.Embed(
      title = "Here's my Invite!",
      description = "Thank you so much for inviting me! It really means a lot, and I promise I won't let you down!",
      url = "https://discord.com/oauth2/authorize?client_id=818651306641326121&permissions=8&scope=bot",
      color=color
  )
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png')
  await ctx.send(embed=embed)

#website
@client.command()
 
async def website(ctx):
  color = color_picker()
  embed = discord.Embed(
      title = "Website!",
      description = f"Check out my website, and a few of my commands there! For more help, try `{message_prefixes_custom(ctx.message.guild)}help`!",
      url = "https://celeste.gq/",
      color=color
  )
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png')
  await ctx.send(embed=embed)

#vote
@client.command(aliases=['upvote'])
async def vote(ctx):
  color = color_picker()
  embed = discord.Embed(
      title = "Vote for me!",
      description = f"Upvote me at this link! It means a lot, and you will earn free rewards!",
      url = "https://discordbotlist.com/bots/celeste/upvote",
      color=color
  )
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png')
  await ctx.send(embed=embed)
  # await ctx.send("https://discord.gg/jK3HZAPrc2")

#support
@client.command(aliases=['supportserver'])
async def support(ctx):
  color = color_picker()
  embed = discord.Embed(
      title = "My Support Server!",
      description = f"Have Questions? Join my support server to get them answered and make suggestions!",
      url="https://discord.gg/jK3HZAPrc2",
      color=color
  )
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png')
  await ctx.send(embed=embed)

#credits
@client.command()
 
async def credits(ctx):
  color = color_picker()
  embed = discord.Embed(
      title = "Credits:",
      description = f"Hi! I am a discord bot made by [Justice](https://discord.bio/p/justice0364)! I can manage servers and have fun! Check out my website (`{message_prefixes_custom(ctx.message.guild)}website`) for more info!",
      color=color
  )
  embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png')
  await ctx.send(embed=embed)


#punch
@client.command()
 
async def punch(ctx, user: discord.Member = None, user1: discord.Member = None):
  # try:
    if user == None:
      user = client.get_user(818651306641326121)
      user1 = ctx.author
    elif user1 == None:
      user1 = user
      user = ctx.author
    punch = image.open("Images/punch.jpeg")
    asset = user.avatar_url_as(size = 256)
    asset1 = user1.avatar_url_as(size = 256)
    data = BytesIO(await asset.read())
    data1 = BytesIO(await asset1.read())
    pfp = image.open(data)
    pfp = pfp.resize((256,256))
    pfp1 = image.open(data1)
    pfp1 = pfp1.resize((256,256))
    punch.paste(pfp, (396, 22))
    punch.paste(pfp1, (870, 121))
    punch.save("Images/profile.jpeg")
    await ctx.send(file = discord.File("Images/profile.jpeg"))
  # except:
  #   color = color_picker()
  #   embed = discord.Embed(
  #         title = "Error!",
  #         description = "Enter a valid member!",
  #         color=color
  #   )
  #   await ctx.send(embed=embed)

#steal emoji
@commands.has_permissions(manage_emojis = True)
@client.command()
 
async def steal(ctx, url: str, *, name=None):
  if name == None:
    ctx.send("Please be sure to enter an emoji name!")
  try:
    async with aiohttp.ClientSession() as ses:
      async with ses.get(url) as r:
        try:
          img_or_gif = BytesIO(await r.read())
          b_value = img_or_gif.getvalue()
          if r.status in range(200, 299):
            emoji = await ctx.guild.create_custom_emoji(image=b_value, name=name)
            if ".gif?v=" in url:
              await ctx.send(f'Successfully created gif: <a:{name}:{emoji.id}>')
            else:
              await ctx.send(f'Successfully created emoji: <:{name}:{emoji.id}>')
            await ses.close()
          else:
            await ctx.send(f'Error when making request | {r.status} response.')
            await ses.close()
        except discord.HTTPException:
          await ctx.send('File size is too big!')
  except:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "Make sure you use the emoji _LINK_, not the actual emoji. If this still doesn't work, it means you are not an admin. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)

#del emoji
@client.command()
 
async def remoji(ctx, emoji: discord.Emoji):
  if ctx.author.guild_permissions.manage_emojis:
    await ctx.send(f'Successfully deleted: {emoji}')
    await emoji.delete()
  else:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)
    
#list all emojis
@client.command()
 
async def lsemoji(ctx):
  if ctx.author.guild_permissions.manage_emojis:
    sender = ""
    for emoji in client.emojis:
      sender = ""
      sender += f"{emoji} Name: `{emoji.name}`︱ ID: `{emoji.id}`\n"
      await ctx.send(sender)
  else:
    color = color_picker()
    embed = discord.Embed(
      title = "Request Declined.",
      description = "You are not an admin. Nice try.",
      color=color
    )
    await ctx.send(embed=embed)

#emoji info
@client.command()
 
async def emoji_info(ctx, emoji: discord.Emoji):
  sender = ""
  sender += f"{emoji} Name: `{emoji.name}` ︱ ID: `{emoji.id}`\n"
  await ctx.send(sender)

global progress
progress = False

#battle
@client.command(aliases=['fight'])
 
async def battle(ctx, f2: discord.Member = None):
  global progress
  if progress != False:
    await ctx.send(f"There is already a game in progress! Please type `{message_prefixes_custom(ctx.message.guild)}end battle` to quit the game.")
    return
  elif ctx.author == f2:
    await ctx.send("You can't play against yourself!")
    return
  elif f2 == None:
    await ctx.send("Please enter an user to play against!")
    return
  elif f2.bot:
    await ctx.send("You can't play against a bot!")
    return
  else:
    progress = True

  gamer1 = ctx.author
  gamer2 = f2

  num = random.randint(1, 2)
  if num == 1:
    turn = gamer1
  elif num == 2:
    turn = gamer2
  await ctx.send(f"{turn.mention} starts the game! Please type `fight`, `heal` or `surrender`.")

  global check_for
  check_for = turn

  health1 = 100
  health2 = 100

  while progress == True:
    try:
      response = await client.wait_for('message', check = lambda message: message.author == check_for, timeout = 30)
      if "heal" in response.content.lower():
        health_potion = random.randint(1, 20)
        if response.author == gamer1 and health1 < 80:
          health1 += health_potion
          await ctx.send(f"You have healed {health_potion} hp! You now have {health1} hp!")
          check_for = gamer2
        elif response.author == gamer2 and health2 < 80:
          health2 += health_potion
          await ctx.send(f"You have healed {health_potion} hp! You now have {health2} hp!")
          check_for = gamer1
        elif health1 > 80 or health2 > 80:
          await ctx.send("You can only heal if you have less than 80 hp! Enter another command.")
          continue
        
      elif "fight" in response.content.lower():
        fight_potion = -1*random.randint(1, 50)
        if response.author == gamer1:
          health2 += fight_potion
          if health2 <= 0:
            health2 = 0
            await ctx.send(f"You fought {gamer2.mention}! They now have {health2} hp!\nCongratulations {gamer1.mention}! You won!")
            progress = False
            return
          else:
            await ctx.send(f"You fought {gamer2.mention}! They now have {health2} hp!")
            check_for = gamer2
        elif response.author == gamer2:
          health1 += fight_potion
          if health1 <= 0:
            health1 = 0
            await ctx.send(f"You fought {gamer1.mention}! They now have {health1} hp!\nCongratulations {gamer2.mention}! You won!")
            progress = False
            return
          else:
            await ctx.send(f"You fought {gamer1.mention}! They now have {health1} hp!")
            check_for = gamer1
      elif "surrender" in response.content.lower():
        if response.author == gamer1:
          await ctx.send(f"Congratulations {gamer2.mention}! You win!")
          progress = False
          return
        elif response.author == gamer2:
          await ctx.send(f"Congratulations {gamer1.mention}! You win!")
          progress = False
          return
      else:
        pass
      await ctx.send(f"It is now {check_for.mention} turn. Please type `fight`, `heal` or `surrender`.")
    except:
      await ctx.send(f"Game Over! {check_for.mention} took too long to respond.")
      progress = False
      return








  
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command(aliases=['ttt'])
 
async def tictactoe(ctx, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if ctx.author == p2:
          await ctx.send("You can't play against yourself!")
          return
    elif p2.bot:
          await ctx.send("You can't play against a bot!")
          return

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = ctx.author
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
        elif num == 2:
            turn = player2
        await ctx.send(f"{turn.mention} starts the game! Type `{message_prefixes_custom(ctx.message.guild)}place [position]` to place a counter, or `{message_prefixes_custom(ctx.message.guild)}end` to end the game.")
    else:
        await ctx.send(f"A game is already in progress! Finish it before starting a new one, or type `{message_prefixes_custom(ctx.message.guild)}end` to end.")

@client.command()
async def end(ctx):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver != True:
      count = 0
      player1 = ""
      player2 = ""
      turn = ""
      gameOver = True
    else:
      await ctx.send("You never started a game!")
      return


    await ctx.send("Game ended. I hope you play again!")



@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                    return
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")
                    return

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
                await ctx.send(f"{turn.mention}, it is your turn! Type `{message_prefixes_custom(ctx.message.guild)}place [position]` to place a counter, or `{message_prefixes_custom(ctx.message.guild)}end` to end the game.")
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game to play!")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")






hmpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


@client.command(aliases=['hangman', 'hang'])
async def hm(ctx):
  subject=""
  randomint = random.randint(1, 2)
  if randomint == 1:
    wordstring = random.choice(countries).lower()
    subject = "Countries"
  if randomint == 2:
    wordstring = random.choice(fruits).lower()
    subject = "Fruits"
  word = []
  for thing in wordstring:
    word.append(thing.lower())
  difficulty = ""
  if len(word) <= 4:
    difficulty = "Easy"
  else:
    difficulty = "Hard"
  color=color_picker()
  chance = 0
  chancewords = []
  dashes = ""
  for letter in word:
    dashes += "**﹏** "

  dashlist = dashes.split(" ")
  guesses = ""
  for thing in chancewords:
          guesses+= f"{thing}, "
          guesses = guesses[:-2]

  embed = discord.Embed(title = f"Let's Play Hangman!", description = f"**Difficulty: **{difficulty} | **Subject:** {subject}\n**Chances Remaining:** {chance*-1+7}\n\n```{hmpics[chance]}```\n\n{dashes}\n\n**Guesses:** {guesses}", color=color)
  msg = await ctx.send(embed=embed)
  def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
  
  while True:
    try:
      guess = await client.wait_for('message', check=check, timeout=30)
      if " " in guess.content or len(guess.content) > 1:
        await ctx.send("Please only guess one letter at a time.")
      elif guess.content.lower() in chancewords:
        await ctx.send("You already guessed that letter! Try again!")
      elif guess.content.lower() in word:
          chancewords.append(guess.content.lower())
          guesses = ""
          for thing in chancewords:
            guesses+= f"{thing}, "
          guesses = guesses[:-2]
          
          indexs = [index for index, element in enumerate(word) if element == guess.content.lower()]
          if indexs != None:
            for index in indexs:
              dashlist[index] = f"**{guess.content.upper()}**"
              dashes = ""
              for thing in dashlist:
                dashes += thing + " "
          
          embed = discord.Embed(title = f"Let's Play Hangman!", description = f"**Difficulty: **{difficulty} | **Subject:** {subject}\n**Chances Remaining:** {chance*-1+7}\n\n```{hmpics[chance]}```\n\n{dashes}\n\n**Guesses:** {guesses}", color=color)
          await msg.edit(embed=embed)
          if '**﹏**' in dashes:
            pass
          else:
            await ctx.send("Congratulations! You won! I hope to play again soon!")
            return
          await ctx.send("That's right! Keep it going!")
          pass
      else:
        chancewords.append(guess.content.lower())
        if chance >= 6:
          await ctx.send("You are out of turns! Game over.")
          return
        await ctx.send("Try again!")
        chance += 1
        guesses = ""
        for thing in chancewords:
          guesses+= f"{thing}, "
        guesses = guesses[:-2]
        embed = discord.Embed(title = f"Let's Play Hangman!", description = f"**Difficulty: **{difficulty} | **Subject:** {subject}\n**Chances Remaining:** {chance*-1+7}\n\n```{hmpics[chance]}```\n\n{dashes}\n\n**Guesses:** {guesses}", color=color)
        await msg.edit(embed=embed)
      
      if '**﹏**' in dashes:
        pass
      else:
        await ctx.send("Congratulations! You won! I hope to play again soon!")
        return
      
      
      

    except:
      await ctx.send("Time is up! Since you didn't not type an answer in time, the game is over! ")
      return
































@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx, channel: discord.TextChannel = None):
  try:
    if channel == None: 
        channel = ctx.channel

    color = color_picker()
    embed = discord.Embed(title = "Are You Sure?", description = f"This cannot be undone, and all messages will be lost. React with the 🔥 to nuke {channel.mention}, and ❌ to stop.", color = color)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🔥")
    await msg.add_reaction("❌")

    emoji = []

    def reaction_check(reaction, user):
              if user.id != 818651306641326121 and user.id == ctx.author.id and str(reaction.emoji) == '🔥':
                emoji.append(False)
                return True
              elif user.id != 818651306641326121 and user.id == ctx.author.id and str(reaction.emoji) != '🔥':
                emoji.append(True)
                return True

    try:
      result = await client.wait_for('reaction_add', check = reaction_check, timeout = 30)
    except:
      embed = discord.Embed(title = "Nuke Cancelled", description = f"You did not react in time. Please run the command again to nuke.", color = color)
      await ctx.send(embed=embed)
      return

    if emoji[-1] == True:
      embed = discord.Embed(title = "Nuke Cancelled", description = f"{ctx.author.mention} has cancelled the nuke on {channel.mention}.", color = color)
      await ctx.send(embed=embed)
      return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        embed = discord.Embed(title = "Nuked!", description = f"{ctx.author.mention} has successfully nuked {new_channel.mention}.", color = color)
        embed1 = discord.Embed(title = "Nuked!", description = f"{ctx.author.mention} has successfully nuked this channel.", color = color)
        await new_channel.send(embed=embed1)
        try:
          await ctx.send(embed=embed)
        except:
          pass

    else:
      try:
        embed1 = discord.Embed(title = "Error!", description = f"The channel {channel} could not be found. Please try again.", color = color)
        await ctx.send(embed=embed1)
      except:
        pass
  except:
    embed1 = discord.Embed(title = "Error!", description = f"You either do not have manage channels permissions, or the channel {channel} could not be found. Please try again.", color = color)
    await ctx.send(embed=embed1)







@client.command()
async def rps(ctx):
    color = color_picker()
    embed = discord.Embed(title = "Let's Play Rock Paper Scissors!", description = f"React to your choice below!\n\n**Rock:** 🪨\n**Paper:** 🗒️\n**Scissor:** ✂️", color = color)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction("🪨")
    await msg.add_reaction("🗒️")
    await msg.add_reaction("✂️")

    emoji = []

    def reaction_check(reaction, user):
              if user.id != 818651306641326121 and user.id == ctx.author.id and str(reaction.emoji) == '🪨':
                emoji.append("rock")
                return True
              elif user.id != 818651306641326121 and user.id == ctx.author.id and str(reaction.emoji) == '🗒️':
                emoji.append("paper")
                return True
              elif user.id != 818651306641326121 and user.id == ctx.author.id and str(reaction.emoji) == '✂️':
                emoji.append("scissor")
                return True

    try:
      result = await client.wait_for('reaction_add', check = reaction_check, timeout = 30)
    except:
      embed = discord.Embed(title = "Game Over!", description = f"You did not react in time. Please run the command again to play.", color = color)
      await ctx.send(embed=embed)
      return

    cpu = random.randint(1, 3)

    if emoji[-1] == "rock":
      if cpu == 1:
        embed = discord.Embed(title = "It's a Tie!", description = f"Both of you chose rock!", color = color)
        embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"🪨" , inline = True)
        
        embed.add_field(name = "** **", value= f"** **" , inline = True)

        embed.add_field(name = f"**Celeste's Choice**", value= f"🪨" , inline = True)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/13/b2/6c/13b26ce19dfde6f475073081c1359d92.jpg")
      elif cpu == 2:
        embed = discord.Embed(title = "Celeste Wins!", description = f"Paper beats Rock!", color = color)
        embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"🪨" , inline = True)
        
        embed.add_field(name = "** **", value= f"** **" , inline = True)

        embed.add_field(name = f"**Celeste's Choice**", value= f"🗒️" , inline = True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png")

      elif cpu == 3:
          embed = discord.Embed(title = f"{ctx.author.name.title()} Wins!", description = f"Rock beats Scissors!", color = color)
          embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"🪨" , inline = True)
          
          embed.add_field(name = "** **", value= f"** **" , inline = True)

          embed.add_field(name = f"**Celeste's Choice**", value= f"✂️" , inline = True)
          embed.set_thumbnail(url=ctx.author.avatar_url)
      await msg.edit(embed=embed)
      return
    

    if emoji[-1] == "paper":
      if cpu == 2:
        embed = discord.Embed(title = "It's a Tie!", description = f"Both of you chose paper!", color = color)
        embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"🗒️" , inline = True)
        
        embed.add_field(name = "** **", value= f"** **" , inline = True)

        embed.add_field(name = f"**Celeste's Choice**", value= f"🗒️" , inline = True)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/13/b2/6c/13b26ce19dfde6f475073081c1359d92.jpg")
      elif cpu == 3:
        embed = discord.Embed(title = "Celeste Wins!", description = f"Scissors beat Paper!", color = color)
        embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"🗒️" , inline = True)
        
        embed.add_field(name = "** **", value= f"** **" , inline = True)

        embed.add_field(name = f"**Celeste's Choice**", value= f"✂️" , inline = True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png")

      elif cpu == 1:
          embed = discord.Embed(title = f"{ctx.author.name.title()} Wins!", description = f"Paper beats Rock!", color = color)
          embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"🗒️" , inline = True)
          
          embed.add_field(name = "** **", value= f"** **" , inline = True)

          embed.add_field(name = f"**Celeste's Choice**", value= f"🪨" , inline = True)
          embed.set_thumbnail(url=ctx.author.avatar_url)
      await msg.edit(embed=embed)
      return
      
    


    if emoji[-1] == "scissor":
      if cpu == 3:
        embed = discord.Embed(title = "It's a Tie!", description = f"Both of you chose scissors!", color = color)
        embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"✂️" , inline = True)
        
        embed.add_field(name = "** **", value= f"** **" , inline = True)

        embed.add_field(name = f"**Celeste's Choice**", value= f"✂️" , inline = True)
        embed.set_thumbnail(url="https://i.pinimg.com/originals/13/b2/6c/13b26ce19dfde6f475073081c1359d92.jpg")
      elif cpu == 2:
        embed = discord.Embed(title = f"{ctx.author.name.title()} Wins!", description = f"Scissors beat Paper!", color = color)
        embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"✂️" , inline = True)
        
        embed.add_field(name = "** **", value= f"** **" , inline = True)

        embed.add_field(name = f"**Celeste's Choice**", value= f"🗒️" , inline = True)
        embed.set_thumbnail(url=ctx.author.avatar_url)

      elif cpu == 1:
          embed = discord.Embed(title = f"Celeste Wins!", description = f"Rock beat Scissors!", color = color)
          embed.add_field(name = f"**{ctx.author.name.title()}'s Choice**", value= f"✂️" , inline = True)
          
          embed.add_field(name = "** **", value= f"** **" , inline = True)

          embed.add_field(name = f"**Celeste's Choice**", value= f"🪨" , inline = True)
          embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png")
      await msg.edit(embed=embed)
      return

    











































@client.command(aliases=['cinvite'])
 
async def create_invite(ctx):
    """Create instant invite"""
    link = await ctx.channel.create_invite(max_age = 0)
    await ctx.send(f"Here is an instant invite to your server: {link}")



@client.command(aliases=['balance'])
 
async def bal(ctx, user: discord.Member = None):
  if user == None:
    user = ctx.author

  await open_account(user)
  users = await get_bank_data()

  wallet_amt = users[str(user.id) + "wallet"]
  bank_amt = users[str(user.id) + "bank"]

  color = color_picker()
  embed = discord.Embed(title = f"{user.name}'s Balance:", description = f"**Wallet:** ◈ {'{:,}'.format(wallet_amt)}\n**Bank:** ◈ {'{:,}'.format(bank_amt)}", color = color)
  embed.set_footer(text=f"💸    ○   {user.name}")

  await ctx.send(embed=embed)

async def open_account(user):
  users = await get_bank_data()

  if (str(user.id) + "wallet") in users or (str(user.id) + "bank") in users:
    return False

  else:
    users[str(user.id) + "wallet"] = 0
    users[str(user.id) + "bank"] = 0

  with open("mainbank.json", "w") as f:
    json.dump(users, f)
  return True


async def get_bank_data():
  with open("mainbank.json", "r") as f:
    users = json.load(f)
  return users



async def update_bank(user, change = 0, mode = "wallet"):
  users = await get_bank_data()
  users[str(user.id) + mode] += change
  
  with open("mainbank.json", "w") as f:
    json.dump(users, f)

  bal = [users[str(user.id) + "wallet"], users[str(user.id) + "bank"]]
  return bal


@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def beg(ctx):
  await open_account(ctx.author)
  users = await get_bank_data()
  user = ctx.author
  earnings = random.randint(300, 4000)
  decide = random.randint(1, 2)
  color = color_picker()
  if decide == 1:
    embed = discord.Embed(title = "Here you go!", description = f'Someone gave you {"{:,}".format(earnings)} coins! Be grateful.', color = color)
  elif decide == 2:
    embed = discord.Embed(title = "No Way!", description = f"Go get a job for money! Stop begging.", color = color)
    await ctx.send(embed=embed)
    return
  await ctx.send(embed=embed)
  users[str(user.id) + "wallet"] += earnings
  with open("mainbank.json", "w") as f:
    json.dump(users, f)

worklist = ["as a cashier in Celeste's Moon Store", "as a janitor in your local high school", "as a ghost in haunting your best friend", "as a teacher that nobody likes"]
@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def work(ctx):
  await open_account(ctx.author)
  users = await get_bank_data()
  user = ctx.author
  earnings = random.randint(3000, 4000)
  color = color_picker()
  embed = discord.Embed(title = "Here you go!", description = f'You worked {random.choice(worklist)} and earned {"{:,}".format(earnings)} coins!', color = color)
  await ctx.send(embed=embed)
  users[str(user.id) + "wallet"] += earnings
  with open("mainbank.json", "w") as f:
    json.dump(users, f)




@client.command(aliases=['with'])
async def withdraw(ctx, amount = None):
  try:
    await open_account(ctx.author)

    color = color_picker()
    if amount == None:
      embed = discord.Embed(
        title = "Error!",
        description = "Please specify an amount.",
        color=color
      )
      await ctx.send(embed=embed)
      return

    bal = await update_bank(ctx.author)
    if amount == "max" or amount == "all":
      if bal[1] == 0:
        embed = discord.Embed(
          title = "Error!",
          description = "Stop! Are you trying to break me?! You have no money to withdraw!",
          color=color
        )
        await ctx.send(embed=embed)
        return
      else:
        amount = bal[1]

    amount = int(amount)

    if amount > bal[1]:
      embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You don't even have that much!",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if amount < 0:
      embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You can't withdraw a negative amount!",
        color=color
      )
      await ctx.send(embed=embed)
      return
    
    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1*amount, "bank")

    embed = discord.Embed(
        title = "Success!",
        description = f"You withdrew {'{:,}'.format(amount)} coins!",
        color=color
    )
    await ctx.send(embed=embed)
  except:
    embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You can't withdraw letters!",
        color=color
    )
    await ctx.send(embed=embed)
      

  
@client.command(aliases=['dep'])
 
async def deposit(ctx, amount = None):
  try:
    await open_account(ctx.author)

    color = color_picker()
    if amount == None:
      embed = discord.Embed(
        title = "Error!",
        description = "Please specify an amount.",
        color=color
      )
      await ctx.send(embed=embed)
      return

    bal = await update_bank(ctx.author)
    if amount == "max" or amount == "all":
      if bal[0] == 0:
        embed = discord.Embed(
          title = "Error!",
          description = "Stop! Are you trying to break me?! You have no money to deposit!",
          color=color
        )
        await ctx.send(embed=embed)
        return
      else:
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
      embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You don't even have that much!",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if amount < 0:
      embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You can't deposit a negative amount!",
        color=color
      )
      await ctx.send(embed=embed)
      return
    
    await update_bank(ctx.author, -1*amount)
    await update_bank(ctx.author, amount, "bank")

    embed = discord.Embed(
        title = "Success!",
        description = f"You deposited {'{:,}'.format(amount)} coins!",
        color=color
    )
    await ctx.send(embed=embed)
  except:
    embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You can't deposit letters!",
        color=color
    )
    await ctx.send(embed=embed)


@client.command(aliases=['give'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def send(ctx, member: discord.Member = None, amount = None):
  try:
    await open_account(ctx.author)
    await open_account(member)

    color = color_picker()
    if amount == None:
      embed = discord.Embed(
        title = "Error!",
        description = "Please specify an amount.",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if member == None:
      embed = discord.Embed(
        title = "Error!",
        description = "Please specify a member to send money to.",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if member == ctx.author:
      embed = discord.Embed(
        title = "Error!",
        description = "You can't send money to yourself!",
        color=color
      )
      await ctx.send(embed=embed)
      return

    bal = await update_bank(ctx.author)
    if amount == "max" or amount == "all":
      if bal[0] == 0:
        embed = discord.Embed(
          title = "Error!",
          description = "Stop! Are you trying to break me?! You have no money to send!",
          color=color
        )
        await ctx.send(embed=embed)
        return
      else:
        amount = bal[0]

    amount = int(amount)

    if amount > bal[0]:
      embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You don't even have that much!",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if amount < 0:
      embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You can't give a negative amount!",
        color=color
      )
      await ctx.send(embed=embed)
      return
    
    await update_bank(ctx.author, -1*amount)
    await update_bank(member, int(amount*0.98))

    embed = discord.Embed(
        title = "Success!",
        description = f"You gave {member.mention} {'{:,}'.format(int(amount*0.98))} coins!\n\n**Tax:** 2%  ○  {int(amount-amount*0.98)} coins",
        color=color
    )
    await ctx.send(embed=embed)
    embed1 = discord.Embed(
        title = "Nice!",
        description = f"{ctx.author.mention} has given you {'{:,}'.format(int(amount*0.98))} coins! Be sure to thank them!",
        color=color
    )
    await member.send(embed=embed1)
    return
  except:
    embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You can't give letters!",
        color=color
    )
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def slots(ctx, amount = None):
  try:
      await open_account(ctx.author)

      color = color_picker()
      if amount == None:
        embed = discord.Embed(
          title = "Error!",
          description = "Please specify an amount.",
          color=color
        )
        await ctx.send(embed=embed)
        return

      bal = await update_bank(ctx.author)
      if amount == "max" or amount == "all":
        if bal[0] == 0:
          embed = discord.Embed(
            title = "Error!",
            description = "Stop! Are you trying to break me?! You have no money to gamble!",
            color=color
          )
          await ctx.send(embed=embed)
          return
        elif bal[0] > 25000:
          amount = 25000
        else:
          amount = bal[0]

      amount = int(amount)

      if amount > 25000:
        embed = discord.Embed(
            title = "Error!",
            description = "Stop! You can't gamble more than 25,000 coins at a time! It's for your own good, trust me.",
            color=color
        )
        await ctx.send(embed=embed)
        return

      if amount > bal[0]:
        embed = discord.Embed(
          title = "Error!",
          description = "Stop! Are you trying to break me?! You don't even have that much!",
          color=color
        )
        await ctx.send(embed=embed)
        return

      if amount < 0:
        embed = discord.Embed(
          title = "Error!",
          description = "Stop! Are you trying to break me?! You can't gamble a negative amount!",
          color=color
        )
        await ctx.send(embed=embed)
        return
      
      final = []
      for i in range(3):
        a = random.choice(["🔥", "💖", "🚀"])
        final.append(a)

      final_words = ""
      for thing in final:
        final_words += f"{thing} ︱ "
      
      final_words = final_words[:-3]

      if final[0] == final[1] and final[0] == final[2]:
        await update_bank(ctx.author, 2*amount)
        embed = discord.Embed(
          title = "You Won!",
          description = f"You won {'{:,}'.format(2*amount)} coins!\n\n{final_words}",
          color=color
        )
        await ctx.send(embed=embed)
        return
      else:
        await update_bank(ctx.author, -1*amount)
        embed = discord.Embed(
          title = "You Lost!",
          description = f"You lost {'{:,}'.format(amount)} coins.\n\n{final_words}",
          color=color
        )
        await ctx.send(embed=embed)
        return
      
  except:
    embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You can't gamble letters!",
        color=color
    )
    await ctx.send(embed=embed)



@client.command(aliases=['gamble'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def bet(ctx, amount = None):
  try:
      await open_account(ctx.author)

      color = color_picker()
      if amount == None:
        embed = discord.Embed(
          title = "Error!",
          description = "Please specify an amount.",
          color=color
        )
        await ctx.send(embed=embed)
        return

      bal = await update_bank(ctx.author)
      if amount == "max" or amount == "all":
        if bal[0] == 0:
          embed = discord.Embed(
            title = "Error!",
            description = "Stop! Are you trying to break me?! You have no money to gamble!",
            color=color
          )
          await ctx.send(embed=embed)
          return
        elif bal[0] > 25000:
          amount = 25000
        else:
          amount = bal[0]

      amount = int(amount)

      if amount > 25000:
        embed = discord.Embed(
            title = "Error!",
            description = "Stop! You can't gamble more than 25,000 coins at a time! It's for your own good, trust me.",
            color=color
        )
        await ctx.send(embed=embed)
        return

      if amount > bal[0]:
        embed = discord.Embed(
          title = "Error!",
          description = "Stop! Are you trying to break me?! You don't even have that much!",
          color=color
        )
        await ctx.send(embed=embed)
        return

      if amount < 0:
        embed = discord.Embed(
          title = "Error!",
          description = "Stop! Are you trying to break me?! You can't gamble a negative amount!",
          color=color
        )
        await ctx.send(embed=embed)
        return
      
      bet = random.randint(1, 3)

      if bet == 3:
        await update_bank(ctx.author, 2*amount)
        roll_user = random.randint(2, 6)
        roll_bot = random.randint(1, roll_user-1)
        embed = discord.Embed(
          title = "You Won!",
          description = f"You won {'{:,}'.format(2*amount)} coins!\n\n**Celeste's Roll:** `{roll_bot}`\n**{ctx.author.name}'s Roll:** `{roll_user}`",
          color=color
        )
        embed.set_thumbnail(url="https://cdn11.bigcommerce.com/s-5ig7x53cx8/images/stencil/1280x1280/products/4313/3855/C2-1196-Roll-The-Dice__24823.1539613197.png?c=2")
        await ctx.send(embed=embed)
        return
      elif bet == 2:
        roll_bot = random.randint(2, 6)
        roll_user = random.randint(1, roll_bot-1)
        await update_bank(ctx.author, -1*amount)
        embed = discord.Embed(
          title = "You Lost!",
          description = f"You lost {'{:,}'.format(amount)} coins.\n\n**Celeste's Roll:** `{roll_bot}`\n**{ctx.author.name}'s Roll:** `{roll_user}`",
          color=color
        )
        embed.set_thumbnail(url="https://cdn11.bigcommerce.com/s-5ig7x53cx8/images/stencil/1280x1280/products/4313/3855/C2-1196-Roll-The-Dice__24823.1539613197.png?c=2")
        await ctx.send(embed=embed)
        return
      elif bet == 1:
        all_roll = random.randint(1, 6)
        embed = discord.Embed(
          title = "It's a Tie!",
          description = f"You bet {'{:,}'.format(amount)} coins and lost nothing.\n\n**Celeste's Roll:** `{all_roll}`\n**{ctx.author.name}'s Roll:** `{all_roll}`",
          color=color
        )
        embed.set_thumbnail(url="https://cdn11.bigcommerce.com/s-5ig7x53cx8/images/stencil/1280x1280/products/4313/3855/C2-1196-Roll-The-Dice__24823.1539613197.png?c=2")
        await ctx.send(embed=embed)
        return
      
  except:
    embed = discord.Embed(
        title = "Error!",
        description = "Stop! Are you trying to break me?! You can't gamble letters!",
        color=color
    )
    await ctx.send(embed=embed)


@client.command()
@commands.cooldown(1, 10800, commands.BucketType.user)
async def rob(ctx, member: discord.Member = None):
  try:
    await open_account(ctx.author)
    await open_account(member)

    color = color_picker()
    if member == None:
      embed = discord.Embed(
        title = "Error!",
        description = "Please specify a member to rob money.",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if member == ctx.author:
      embed = discord.Embed(
        title = "Error!",
        description = "You can't rob money from yourself!",
        color=color
      )
      await ctx.send(embed=embed)
      return

    bal = await update_bank(member)
    author_bal = await update_bank(ctx.author)
    if bal[0] < 500:
        embed = discord.Embed(
          title = "Stop!",
          description = f"It's not worth it! {member.mention} has less than 500 coins.",
          color=color
        )
        await ctx.send(embed=embed)
        return
    if author_bal[0] < 500:
        embed = discord.Embed(
          title = "Stop!",
          description = f"You don't have the required 500 coins to rob someone.",
          color=color
        )
        await ctx.send(embed=embed)
        return
    

    basic = random.randint(0, 1)

    if basic == 1:
      earnings = random.randint(500, bal[0])
      await update_bank(ctx.author, earnings)
      await update_bank(member, -1*earnings)
      embed = discord.Embed(
        title = "Success!",
        description = f"You robbed {member.mention} for {'{:,}'.format(earnings)} coins!",
        color=color
      )
      await ctx.send(embed=embed)
      embed1 = discord.Embed(
        title = "Look Out!",
        description = f"{ctx.author.mention} robbed you for {'{:,}'.format(earnings)} coins!",
        color=color
      )
      await member.send(embed=embed1)
      return
    elif basic == 0:
      earnings = 500
      await update_bank(ctx.author, -1*earnings)
      embed = discord.Embed(
        title = "Failed!",
        description = f"The police caught you while you robbed {member.mention}! You ended up paying the police 500 coins for bail.",
        color=color
      )
      await ctx.send(embed=embed)
      embed1 = discord.Embed(
        title = "Phew!",
        description = f"{ctx.author.mention} tried to rob you for {'{:,}'.format(earnings)} coins, but failed!",
        color=color
      )
      await member.send(embed=embed1)
      return
  except:
    embed = discord.Embed(
        title = "Error!",
        description = "Something went wrong. Try again! Sorry about the inconvenience. ",
        color=color
    )
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1, 10800, commands.BucketType.user)
async def heist(ctx, member: discord.Member = None):
  try:
    await open_account(ctx.author)
    await open_account(member)

    color = color_picker()
    if member == None:
      embed = discord.Embed(
        title = "Error!",
        description = "Please specify a member to rob money.",
        color=color
      )
      await ctx.send(embed=embed)
      return

    if member == ctx.author:
      embed = discord.Embed(
        title = "Error!",
        description = "You can't rob money from yourself!",
        color=color
      )
      await ctx.send(embed=embed)
      return

    bal = await update_bank(member)
    author_bal = await update_bank(ctx.author)
    if bal[1] < 500:
        embed = discord.Embed(
          title = "Stop!",
          description = f"It's not worth it! {member.mention} has less than 500 coins.",
          color=color
        )
        await ctx.send(embed=embed)
        return
    if author_bal[0] < 500:
        embed = discord.Embed(
          title = "Stop!",
          description = f"You don't have the required 500 coins to rob someone.",
          color=color
        )
        await ctx.send(embed=embed)
        return
    

    basic = random.randint(0, 3)

    if basic == 1:
      earnings = random.randint(500, bal[0])
      await update_bank(ctx.author, earnings)
      await update_bank(member, -1*earnings, "bank")
      embed = discord.Embed(
        title = "Success!",
        description = f"You heisted {member.mention} for {'{:,}'.format(earnings)} coins!",
        color=color
      )
      await ctx.send(embed=embed)
      embed1 = discord.Embed(
        title = "Look Out!",
        description = f"{ctx.author.mention} heisted you for {'{:,}'.format(earnings)} coins!",
        color=color
      )
      await member.send(embed=embed1)
      return
    else:
      earnings = 500
      await update_bank(ctx.author, -1*earnings)
      embed = discord.Embed(
        title = "Failed!",
        description = f"The police caught you while you heisted {member.mention}! You ended up paying the police 500 coins for bail.",
        color=color
      )
      await ctx.send(embed=embed)
      embed1 = discord.Embed(
        title = "Phew!",
        description = f"{ctx.author.mention} tried heist you for {'{:,}'.format(earnings)} coins, but failed!",
        color=color
      )
      await member.send(embed=embed1)
      return
      return
  except:
    embed = discord.Embed(
        title = "Error!",
        description = "Something went wrong. Try again! Sorry about the inconvenience. ",
        color=color
    )
    await ctx.send(embed=embed)


@client.command(aliases=["item"])
 
async def shop(ctx):
  color = color_picker()
  embed = discord.Embed(title="Celeste's Moon Shop:", description = f"Welcome to Celeste's Moon Shop! To buy an item, just run `{message_prefixes_custom(ctx.message.guild)}buy [item_name]`. Thank you for shopping here {ctx.author.mention}.\n\n", color=color)
  embed.add_field(name = "** **", value = "** **", inline = False)

  for item in mainshop:
    name = item["name"]
    price = item["price"]
    desc = item["description"]

    embed.add_field(name = name, value = f"{'{:,}'.format(price)} coins\n\n   ○   {desc}", inline = False)
    embed.add_field(name = "** **", value = "** **", inline = False)

  await ctx.send(embed=embed)


mainshop = [{"name":"<:moonstone:841034690369945620> Moonstone","price":10000,"description":"A moonstone helps improve your chances in slots and gambling! However, you still might lose, so be careful!"},
            {"name":"<:phone:841035401857859585> Phone","price":100000,"description":"Need money? Using the phone, you can call people for instant money!"},
            {"name":"<:wolfceleste:841036632055480341> Wolf","price":1000000,"description":"The most expensive item, this is used to show your power to others! The Wolf will also help protect you from robberies, making them less frequent. However, there is only so much he can do, and robberies will still occur."}]





@client.command()
 
async def buy(ctx,item = None,amount = 1):
    await open_account(ctx.author)
    color = color_picker()
    if item == None:
      embed = discord.Embed(
            title = "Error!",
            description = f"Be sure to specify an item to buy first!",
            color=color
      )
      await ctx.send(embed=embed)
      return

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            embed = discord.Embed(
              title = "Error!",
              description = f"Check your spelling! That item isn't there.",
              color=color
            )
            await ctx.send(embed=embed)
            return
        if res[1]==2:
            embed = discord.Embed(
              title = "Error!",
              description = f"You don't have enough money in your wallet to buy {amount} {item.title()}.",
              color=color
            )
            await ctx.send(embed=embed)
            return

    buyem = discord.Embed(
              title = "Purchase Successful!",
              description = f"Congratulations! You just bought {amount} {item}!",
              color=color
    )
    buyem.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/wo_ub8eLde5stIX2Jb5ICiWFgR7CcruiOxN5Z1gd8PScLtBTPL3W2ILgmPQAaSr4q6mYh_yd-kWQ2rliJUMbNnmR")

    await ctx.send(embed=buyem)


@client.command(aliases=["inventory", "inv"])
 
async def bag(ctx):
    color = color_picker()
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id) + "bag"]
    except:
        bag = []

    desc = ""
    em = discord.Embed(title = f"{ctx.author.name}'s Inventory:", description = desc, color=color)
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        for abc in mainshop:
          for kid in abc.keys():
            if kid == "name":
              thing = abc.get(kid)

              thing1 = thing.split(' ')[1]
              if name.lower() == thing1.lower():
                name = thing

        desc += f"{name} │ {amount}\n"
    em = discord.Embed(title = f"{ctx.author.name}'s Inventory:", description = desc, color=color)

    await ctx.send(embed = em)    

async def buy_this(user,item_name,amount):
    item_name = item_name.title()
    name_ = None
    for item in mainshop:
        name = item["name"].title().split(' ')[1]
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id) + "bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id) + "bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id) + "bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id) + "bag"] = [obj]

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]


def color_chooser(color):
  if color.lower == "none":
    return 0x000000
  if color.lower() == "random":
    return color_picker()
  if color.lower() == "light grey" or color.lower == "light gray":
    return discord.Color.light_grey()
  if color.lower() == "dark grey" or color.lower == "dark gray":
    return discord.Color.darker_grey()
  if color.lower() == "blurple":
    return discord.Color.blurple()
  if color.lower() == "greyple" or color.lower == "grayple":
    return discord.Color.greyple()
  if color.lower() == "dark theme":
    return discord.Color.dark_theme()
  if color.lower() == "teal":
    return discord.Color.teal()
  if color.lower() == "dark teal":
    return discord.Color.dark_teal()
  if color.lower() == "green":
    return discord.Color.green()
  if color.lower() == "dark green":
    return discord.Color.dark_green()
  if color.lower() == "blue":
    return discord.Color.blue()
  if color.lower() == "dark blue":
    return discord.Color.dark_blue()
  if color.lower() == "purple":
    return discord.Color.purple()
  if color.lower() == "dark purple":
    return discord.Color.dark_purple()
  if color.lower() == "magenta":
    return discord.Color.magenta()
  if color.lower() == "dark magenta":
    return discord.Color.dark_magenta()
  if color.lower() == "gold":
    return discord.Color.gold()
  if color.lower() == "dark gold":
    return discord.Color.dark_gold()
  if color.lower() == "orange":
    return discord.Color.orange()
  if color.lower() == "dark orange":
    return discord.Color.dark_orange()
  if color.lower() == "red":
    return discord.Color.red()
  if color.lower() == "dark red":
    return discord.Color.dark_red()

  return 0x000000


def none(word):
  if word.lower() == "none":
    return None
  return word





@client.command(aliases=["createembed", "makeembed", "membed"])
 
async def cembed(ctx):
  await ctx.message.delete()
  try:
    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    color = color_picker()

    embed = discord.Embed(title="Title!", description="Please type a title into the chat. Type `none` if you do not want one.", color=color)
    msg = await ctx.send(embed=embed)
    title1 = await client.wait_for("message", check = check, timeout = 30)
    await msg.delete()
    title = none(title1.content)
    await title1.delete()
  
    embed = discord.Embed(title="Description!", description="Please type a description into the chat. Type `none` if you do not want one.", color=color)
    msg = await ctx.send(embed=embed)
    desc1 = await client.wait_for("message", check = check, timeout = 30)
    await msg.delete()
    desc = none(desc1.content)
    await desc1.delete()

    embed = discord.Embed(title="Color!", description="Please type a color into the chat.\n\n**Options:** Teal, Dark Teal, Green, Dark Green, Blue, Dark Blue, Purple, Dark Purple, Magenta, Dark Magenta, Gold, Dark Gold, Orange, Dark Orange, Red, Dark Red, Light Grey, Dark Grey, Blurple, Greyple, Dark Theme, None, Random", color=color)
    msg = await ctx.send(embed=embed)
    color1 = await client.wait_for("message", check = check, timeout = 30)


    color = color_chooser(color1.content)
    await msg.delete()
    await color1.delete()


    embed = discord.Embed(title="Footer!", description="Please type a footer into the chat. Type `none` if you do not want one.", color=color)
    msg = await ctx.send(embed=embed)
    footer1 = await client.wait_for("message", check = check, timeout = 30)
    footer = none(footer1.content)

    await msg.delete()
    await footer1.delete()

    embed = discord.Embed(title="Thumbnail!", description="Please type thumbnail url into the chat. Type `none` if you do not want one.", color=color)
    msg = await ctx.send(embed=embed)
    thumbnail1 = await client.wait_for("message", check = check, timeout = 30)
    thumbnail = none(thumbnail1.content)

    await msg.delete()
    await thumbnail1.delete()

    embed = discord.Embed(title=title, description=desc, color=color)
    if footer != None:
      embed.set_footer(text=footer)
    if thumbnail != None:
      embed.set_thumbnail(url = thumbnail)
    await ctx.send(embed=embed)
  except:
    embed = discord.Embed(title="Time's Up!", description="An answer was not detected. Run the command to try again.", color=color_picker())
    await ctx.send(embed=embed)
    return





@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
        color = color_picker()
        if int(error.retry_after) < 60:
          embed = discord.Embed(title = "Cooldown!", description = 'The {} command is still on cooldown for {} seconds. Try again later.'.format(ctx.command.name, round(int(error.retry_after) + 1)), color = color, timestamp = datetime.utcnow())
        elif int(error.retry_after) > 60 and int(error.retry_after) < 3600:
          embed = discord.Embed(title = "Cooldown!", description = 'The {} command is still on cooldown for {} minutes. Try again later.'.format(ctx.command.name, round(int(error.retry_after)/60)), color = color, timestamp = datetime.utcnow())
        else:
          embed = discord.Embed(title = "Cooldown!", description = 'The {} command is still on cooldown for {} hours. Try again later.'.format(ctx.command.name, round(int(error.retry_after)/60/60)), color = color, timestamp = datetime.utcnow())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/819108951072178218/841534947860152320/coffee-clipart-transparent-11.png")
        return await ctx.send(embed=embed)
    else:
      raise error



@client.command(aliases=['gaw', 'gstart', 'gcreate'], manage_channels=True)
 
async def giveaway(ctx, timer = None, *, prize = None):
  await ctx.message.delete()
  try:
    color = color_picker()
    if timer == None:
      embed = discord.Embed(title="Error!", description="Please enter a time for the giveaway.", color=color)
      await ctx.send(embed=embed)
      return
    elif prize == None:
      embed = discord.Embed(title="Error!", description="Please enter a prize for the giveaway.", color=color)
      await ctx.send(embed=embed)
      return
    
    
    embed = discord.Embed(title=f"🎉 Giveaway: {prize} 🎉", description=f"React with 🎉 to enter. \n\n**Hosted By:** {ctx.author.mention}\n**Prize:** {prize}", color=color)
    str_time = None
    gawtime = None
    time_words = None
    if "w" in timer:
      str_time = timer.split("w",1)[0]
      gawtime = int(str_time) * 604800
      time_words = f"{str_time} weeks"
    elif "d" in timer:
      str_time = timer.split("d",1)[0]
      gawtime = int(str_time) * 86400
      time_words = f"{str_time} days"
    elif "h" in timer:
      str_time = timer.split("h",1)[0]
      gawtime = int(str_time) * 3600
      time_words = f"{str_time} hours"
    elif "m" in timer:
      str_time = timer.split("m",1)[0]
      gawtime = int(str_time) * 60
      time_words = f"{str_time} minutes"
    elif "s" in timer:
      str_time = timer.split("s",1)[0]
      gawtime = int(str_time)
      time_words = f"{str_time} seconds"


    embed.set_footer(text=f"Ends In: {time_words}")
    gaw_msg = await ctx.send(embed = embed)

    await gaw_msg.add_reaction("🎉")
    global reminder_count
    wait_time = reminder_count + gawtime

    with open('giveaway.json', 'r') as f:
      gawjson = json.load(f)

    gawjson[str(wait_time)] = [str(gaw_msg.id), str(ctx.channel.id), str(ctx.author.id), prize, str(ctx.guild.id)]

    with open("giveaway.json", "w") as f:
      json.dump(gawjson, f)
  except:
    embed = discord.Embed(title="Error!", description=f"Please verify that you have the manage channels role. If you do, please make sure you use the following convention:\n\n`{message_prefixes_custom(ctx.message.guild)}gstart [time] [prize]`\n\n> For example: `{message_prefixes_custom(ctx.message.guild)}gstart 1m 1 Mil Celeste Coins` or `{message_prefixes_custom(ctx.message.guild)}gstart 1h 2 Wolf`", color=color)
    await ctx.send(embed=embed)
    return



@client.command(aliases=['rr', 're_roll', 'rroll'], manage_channels=True)
async def reroll(ctx, id_: int):
  await ctx.message.delete()
  new_gaw_msg = await ctx.fetch_message(id_)

  users = await new_gaw_msg.reactions[0].users().flatten()
  users.pop(users.index(client.user))

  try:

    winner = random.choice(users)


    await ctx.send(f"🎉 🎉 🎉  {winner.mention} won the reroll by {ctx.author.mention} 🎉 🎉 🎉")

  except:
    await ctx.send(f"🎉 🎉 🎉  Nobody won the reroll by {ctx.author.mention} 🎉 🎉 🎉")

@client.command(aliases=['end_gaw', 'gend'], manage_channels=True)
async def endgaw(ctx, id_: int):
  await ctx.message.delete()
  new_gaw_msg = await ctx.fetch_message(id_)

  users = await new_gaw_msg.reactions[0].users().flatten()
  users.pop(users.index(client.user))

  

  await new_gaw_msg.delete()

  try:
    winner = random.choice(users)
    await ctx.send(f"🎉 🎉 🎉  Giveaway ended! {winner.mention} won the prize, hosted by {ctx.author.mention} 🎉 🎉 🎉")
  except:
    await ctx.send(f"🎉 🎉 🎉  Giveaway ended! Nobody won the prize, hosted by {ctx.author.mention} 🎉 🎉 🎉")



#serverinfo
@client.command(aliases=['srv', 'serverinfo'])
 
async def srvinfo(ctx):
  name = str(ctx.guild.name)

  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
  
  total_text_channels = len(ctx.guild.text_channels)
  total_voice_channels = len(ctx.guild.voice_channels)
  total_channels = total_text_channels  + total_voice_channels

  roles = len(ctx.guild.roles)
  emojis = len(ctx.guild.emojis)

  color = color_picker()

  embed = discord.Embed(
      title=name + ":",
      color=color
  )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="\n📟 Server ID:", value=id, inline=True)
  embed.add_field(name = '** **', value= "** **" , inline = True)
  embed.add_field(name="\n🌎 Region:", value=region, inline=True)

  # embed.add_field(name = '** **', value= "** **" , inline = False)

  embed.add_field(name="💁 Member Count:", value=f"{memberCount} members", inline=True)
  embed.add_field(name = '** **', value= "** **" , inline = True)
  embed.add_field(name="📚 Total Channels:", value=f"{total_channels} channels", inline=True)

  # embed.add_field(name = '** **', value= "** **" , inline = False)
  
  embed.add_field(name="📱 Text Channels:", value=f"{total_text_channels} channels", inline=True)
  embed.add_field(name = '** **', value= "** **" , inline = True)
  embed.add_field(name="🎙️ Voice Channels:", value=f"{total_voice_channels} channels", inline=True)

  # embed.add_field(name = '** **', value= "** **" , inline = False)
  
  embed.add_field(name="📒 Roles:", value=f"{roles} roles", inline=True)
  embed.add_field(name = '** **', value= "** **" , inline = True)
  embed.add_field(name="😊 Emojis:", value=f"{emojis} emojis", inline=True)

  await ctx.send(embed=embed)

#help
@client.command(pass_context = True)
 
async def help(ctx, cmd = None):
  if cmd == None:
    color = color_picker()
    embed = discord.Embed(
      title = "Celeste's Command List:\n ** **", description = "Here's a list of commands I can run!\nType the command listed under each category for more information.\n\n ** **", color=color
    )
    embed.add_field(name = '⚙️ Moderation Commands:', value= f"> `{message_prefixes_custom(ctx.message.guild)}help mod`", inline = True)
    embed.add_field(name = '** **', value= "** **" , inline = True)
    embed.add_field(name = '🎉 Giveaway Commands:', value= f"> `{message_prefixes_custom(ctx.message.guild)}help giveaway`", inline = True)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '🌴 Fun Commands:', value= f"> `{message_prefixes_custom(ctx.message.guild)}help fun`", inline = True)
    embed.add_field(name = '** **', value= "** **" , inline = True)
    embed.add_field(name = '🎮 Game Commands:', value= f"> `{message_prefixes_custom(ctx.message.guild)}help game`", inline = True)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '📷 Image Commands:', value= f"> `{message_prefixes_custom(ctx.message.guild)}help image`", inline = True)
    embed.add_field(name = '** **', value= "** **" , inline = True)
    embed.add_field(name = '💵 Currency Commands:', value= f"> `{message_prefixes_custom(ctx.message.guild)}help currency`", inline = True)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = "💬 Chatbot Commands: ", value = f"> `{message_prefixes_custom(ctx.message.guild)}help chatbot`", inline = True)
    embed.add_field(name = '** **', value= "** **" , inline = True)
    embed.add_field(name = "💳 Credit Commands: ", value = f"> `{message_prefixes_custom(ctx.message.guild)}help credits`", inline = True)
    embed.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    await ctx.send(embed=embed)
  elif cmd == 'currency':
    color = color_picker()
    embed = discord.Embed(
      title = "Currency Command List:\n ** **", description = "Here's a list of currency commands I can run!\n\n ** **", color=color
    )
    embed2 = discord.Embed(
      title = "Currency Command List:\n ** **", description = "Here's a list of currency commands I can run!\n\n ** **", color=color
    )

    embed.add_field(name = '💰 Balance:', value= f"> Enter a user's balance, or check your own!\n> `{message_prefixes_custom(ctx.message.guild)}bal` or `{message_prefixes_custom(ctx.message.guild)}bal [@user]`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '💳 Withdraw:', value= f"> Withdraw money from your bank!\n> `{message_prefixes_custom(ctx.message.guild)}with [amount]`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '🏦 Deposit:', value= f"> Deposit money to your bank!\n> `{message_prefixes_custom(ctx.message.guild)}dep [amount]`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '🤲 Beg:', value= f"> Beg for money!\n> `{message_prefixes_custom(ctx.message.guild)}beg`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '🎰 Slots:', value= f"> Put your money into a slots machine to possibly get more!\n> `{message_prefixes_custom(ctx.message.guild)}slots [amount]`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '🛒 Buy:', value= f"> Buy items from the shop!\n> `{message_prefixes_custom(ctx.message.guild)}buy [item]`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)

    embed2.add_field(name = '🥽 Rob:', value= f"> Rob a user for money!\n> `{message_prefixes_custom(ctx.message.guild)}rob [@user]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '📡 Send:', value= f"> Send a user money!\n> `{message_prefixes_custom(ctx.message.guild)}send [@user]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🤑 Bet:', value= f"> Bet for more money!\n> `{message_prefixes_custom(ctx.message.guild)}bet [amount]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '💴 Heist:', value= f"> heist a user's bank!\n> `{message_prefixes_custom(ctx.message.guild)}heist [@user]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '💼 Work:', value= f"> Work for money!\n> `{message_prefixes_custom(ctx.message.guild)}work`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🛍️ Shop:', value= f"> View items to buy!\n> `{message_prefixes_custom(ctx.message.guild)}shop`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed2.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed.set_footer(text="Page 1/2")
    embed2.set_footer(text="Page 2/2")
    embeds = [embed, embed2]

    msg = await ctx.send(embed = embed)
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    for button in buttons:
          await msg.add_reaction(button)

    current=0  
    while True:
          try:
              reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

          except asyncio.TimeoutError:
              return

          else:
              previous_page = current
              if reaction.emoji == u"\u23EA":
                  current = 0
                  
              elif reaction.emoji == u"\u2B05":
                  if current > 0:
                      current -= 1
                      
              elif reaction.emoji == u"\u27A1":
                  if current < len(embeds)-1:
                      current += 1

              elif reaction.emoji == u"\u23E9":
                  current = len(embeds)-1

              for button in buttons:
                  await msg.remove_reaction(button, ctx.author)

              if current != previous_page:
                  await msg.edit(embed=embeds[current])


  if cmd == "chatbot":
    color = color_picker()
    embed = discord.Embed(
      title = "Chatbot Command List:\n ** **", description = "Celeste can be a chatbot as well!\nTo set up the chatbot, simply make a channel with `celeste` in the channel name! That channel will automaticaly become the chatbot channel.\n\n ** **", color=color
    )

    embed.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    await ctx.send(embed=embed)


  elif cmd == 'mod':
    color = color_picker()
    embed1 = discord.Embed(
      title = "Moderation Command List:\n ** **", description = "Here's a list of moderation commands I can run!\n\n ** **", color=color
    )
    embed2 = discord.Embed(
      title = "Moderation Command List:\n ** **", description = "Here's a list of moderation commands I can run!\n\n ** **", color=color
    )
    embed3 = discord.Embed(
      title = "Moderation Command List:\n ** **", description = "Here's a list of moderation commands I can run!\n\n ** **", color=color
    )
    embed4 = discord.Embed(
      title = "Moderation Command List:\n ** **", description = "Here's a list of moderation commands I can run!\n\n ** **", color=color
    )
    embed5 = discord.Embed(
      title = "Moderation Command List:\n ** **", description = "Here's a list of moderation commands I can run!\n\n ** **", color=color
    )
    embed6 = discord.Embed(
      title = "Moderation Command List:\n ** **", description = "Here's a list of moderation commands I can run!\n\n ** **", color=color
    )
    embed7 = discord.Embed(
      title = "Moderation Command List:\n ** **", description = "Here's a list of moderation commands I can run!\n\n ** **", color=color
    )
    embed8 = discord.Embed(
      title = "Moderation Command List:\n ** **", description = "Here's a list of moderation commands I can run!\n\n ** **", color=color
    )

    embed1.set_footer(text="Page 1/8")
    embed2.set_footer(text="Page 2/8")
    embed3.set_footer(text="Page 3/8")
    embed4.set_footer(text="Page 4/8")
    embed5.set_footer(text="Page 5/8")
    embed6.set_footer(text="Page 6/8")
    embed7.set_footer(text="Page 7/8")
    embed8.set_footer(text="Page 8/8")


    embed1.add_field(name = '🔒 Lock:', value= f"> Lock any channel with this command! Only moderators and admin will be able to do this.\n> `{message_prefixes_custom(ctx.message.guild)}lock`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '🔓 Unlock:', value= f"> Unlock any peviously locked channel! Only moderators and admin will be able to do this.\n> `{message_prefixes_custom(ctx.message.guild)}unlock`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '🔐 Lockdown:', value= f"> Lockdown the entire server with this command!\n> `{message_prefixes_custom(ctx.message.guild)}lockdown`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '🔑 Unlockdown:', value= f"> This will unlock the entire server!\n> `{message_prefixes_custom(ctx.message.guild)}unlockdown`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '📘 Edit Channel Name:', value= f"> Seamlessly edit a channel's name in seconds!\n> `{message_prefixes_custom(ctx.message.guild)}cedit [old_channel_name] [new_channel_name]`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    
    
    embed2.add_field(name = '⚠️ Warn:', value= f"> Warn a user with this command! This will send a message to their dms.\n> `{message_prefixes_custom(ctx.message.guild)}warn [@user]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🔇 Mute:', value= f"> Mute a user!\n> `{message_prefixes_custom(ctx.message.guild)}mute [@user] [reason - optional]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🔈 Unmute:', value= f"> Unmute a user!\n> `{message_prefixes_custom(ctx.message.guild)}unmute [@user]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🚫 Ban:', value= f"> Ban a user with this command!\n> `{message_prefixes_custom(ctx.message.guild)}ban [@user]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '⛔ Temp Ban:', value= f"> Temporarily ban a user with this command!\n> `{message_prefixes_custom(ctx.message.guild)}tban [@user] [0d 0h 0m 0s] [reason]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)


    embed3.add_field(name = '❌ Kick:', value= f"> Kick a user with this command!\n> `{message_prefixes_custom(ctx.message.guild)}kick [@user]`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.add_field(name = '✅ Unban:', value= f"> Unban a user with this command!\n> `{message_prefixes_custom(ctx.message.guild)}unban [@user]`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.add_field(name = '🔖 Nickname:', value= f"> Change a user's nickname!\n> `{message_prefixes_custom(ctx.message.guild)}nickname [new nickname]`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.add_field(name = '🖼️ Avatar:', value= f"> Be able to see a user's avatar up close and bigger!\n> `{message_prefixes_custom(ctx.message.guild)}avatar` or `{message_prefixes_custom(ctx.message.guild)}avatar @user`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.add_field(name = '💈 Poll:', value= f"> Poll users in your server!\n> `{message_prefixes_custom(ctx.message.guild)}poll [question]`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)

    embed4.add_field(name = '🔄 Prefix:', value= f"> Change my prefix! Only admins will be able to do this.\n> `{message_prefixes_custom(ctx.message.guild)}prefix [new prefix]`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)
    embed4.add_field(name = '🚫 Snipe:', value= f"> Snipe the last deleted message in a channel!\n> `{message_prefixes_custom(ctx.message.guild)}snipe`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)
    embed4.add_field(name = '📓 Edit Snipe:', value= f"> Snipe the last edited message in a channel!\n> `{message_prefixes_custom(ctx.message.guild)}esnipe`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)
    embed4.add_field(name = '📝 Suggest:', value= f"> Have a suggestion? Run this command!\n> `{message_prefixes_custom(ctx.message.guild)}suggest [suggestion]`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)
    embed4.add_field(name = '🏎️ Ping:', value= f"> Test my speed and response time!\n> `{message_prefixes_custom(ctx.message.guild)}ping`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)


    embed5.add_field(name = '🎒 Role:', value= f"> Assign or remove rules from a user!\n> `{message_prefixes_custom(ctx.message.guild)}role [@user] [role name]`", inline = False)
    embed5.add_field(name = '** **', value= "** **" , inline = False)
    embed5.add_field(name = '❎ Purge:', value= f"> Delete messages with this command!\n> `{message_prefixes_custom(ctx.message.guild)}purge [amount of messages]`", inline = False)
    embed5.add_field(name = '** **', value= "** **" , inline = False)
    embed5.add_field(name = '💡 Remind:', value= f"> Set a reminder, and I'll remind you when you want! Not all times are necessary!\n> Please set reminders using the following convention:\n> \n> `d` - Days │ `h` - Hours │ `m` - Minutes │ `s` - Seconds\n> \n> For example: `4d 6h 7m 3s` or `0d 2h 0m 3s`\n> \n> `{message_prefixes_custom(ctx.message.guild)}2d4h5m10s` or `{message_prefixes_custom(ctx.message.guild)}0d0h5m10s`", inline = False)
    embed5.add_field(name = '** **', value= "** **" , inline = False)
    embed5.add_field(name = '🤖 Autoresponses:', value= f"> I'll send autoresponses for the messages you mark!\n> `{message_prefixes_custom(ctx.message.guild)}ar trigger & response`", inline = False)
    embed5.add_field(name = '** **', value= "** **" , inline = False)
    embed5.add_field(name = '📚 Server Info:', value= f"> Here is some info on your server!\n> `{message_prefixes_custom(ctx.message.guild)}srvinfo`", inline = False)
    embed5.add_field(name = '** **', value= "** **" , inline = False)


    embed6.add_field(name = '📒 Check Autoresponses:', value= f"> Check the autoresponses you already have with this command!\n> `{message_prefixes_custom(ctx.message.guild)}archeck`", inline = False)
    embed6.add_field(name = '** **', value= "** **" , inline = False)
    embed6.add_field(name = '📖 Info:', value= f"> Check a member's info!\n> `{message_prefixes_custom(ctx.message.guild)}info [@user]`", inline = False)
    embed6.add_field(name = '** **', value= "** **" , inline = False)
    embed6.add_field(name = '⌨️ AFK:', value= f"> Go AFK for a while! It's always good to get a break. I'll take care of your pings, don't worry!\n> `{message_prefixes_custom(ctx.message.guild)}afk [reason]`", inline = False)
    embed6.add_field(name = '** **', value= "** **" , inline = False)
    embed6.add_field(name = '💻 UNAFK:', value= f"> Come back after being AFK! This command will only work if you used the AFK command to go AFK.\n> `{message_prefixes_custom(ctx.message.guild)}unafk`", inline = False)
    embed6.add_field(name = '** **', value= "** **" , inline = False)
    embed6.add_field(name = '📔 Create Role:', value= f"> Seamlessly create a role in seconds!\n> `{message_prefixes_custom(ctx.message.guild)}crole [role name]`", inline = False)
    embed6.add_field(name = '** **', value= "** **" , inline = False)


    embed7.add_field(name = '😊 Steal:', value= f"> Add new emojis to your server!\n> `{message_prefixes_custom(ctx.message.guild)}steal [emoji url]`", inline = False)
    embed7.add_field(name = '** **', value= "** **" , inline = False)
    embed7.add_field(name = '📎 Remove Emoji:', value= f"> Remove emojis in your server!\n> `{message_prefixes_custom(ctx.message.guild)}remoji [emoji]`", inline = False)
    embed7.add_field(name = '** **', value= "** **" , inline = False)
    embed7.add_field(name = '🔖 List Emojis:', value= f"> List every emoji in your server, with its name and id!\n> `{message_prefixes_custom(ctx.message.guild)}lsemoji`", inline = False)
    embed7.add_field(name = '** **', value= "** **" , inline = False)
    embed7.add_field(name = '📙 Emoji Info:', value= f"> Gives you information on a specific emoji!\n> `{message_prefixes_custom(ctx.message.guild)}emoji_info [emoji]`", inline = False)
    embed7.add_field(name = '** **', value= "** **" , inline = False)
    embed7.add_field(name = '✉️ Create Invite:', value= f"> Create an invite for your server!\n> `{message_prefixes_custom(ctx.message.guild)}cinvite`", inline = False)
    embed7.add_field(name = '** **', value= "** **" , inline = False)
    
    embed8.add_field(name = '🎟️ Ticket System:', value= f"> Create tickets in your server!\n> `{message_prefixes_custom(ctx.message.guild)}config_ticket [message_id] [category_id]`", inline = False)
    embed8.add_field(name = '** **', value= "** **" , inline = False)
    embed8.add_field(name = '✍️ Create Embed:', value= f"> Create custom embeds for your server!\n> `{message_prefixes_custom(ctx.message.guild)}cembed`", inline = False)
    embed8.add_field(name = '** **', value= "** **" , inline = False)
    embed8.add_field(name = '💥 Nuke:', value= f"> Nuke channels in your server!\n> `{message_prefixes_custom(ctx.message.guild)}nuke` or `{message_prefixes_custom(ctx.message.guild)}nuke [channel]`", inline = False)
    embed8.add_field(name = '** **', value= "** **" , inline = False)

    embed2.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )

    embed1.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed3.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed4.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed5.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed6.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed7.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed8.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    

    embeds = [embed1, embed2, embed3, embed4, embed5, embed6, embed7, embed8]

    msg = await ctx.send(embed = embed1)
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    for button in buttons:
          await msg.add_reaction(button)

    current=0  
    while True:
          try:
              reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

          except asyncio.TimeoutError:
              return

          else:
              previous_page = current
              if reaction.emoji == u"\u23EA":
                  current = 0
                  
              elif reaction.emoji == u"\u2B05":
                  if current > 0:
                      current -= 1
                      
              elif reaction.emoji == u"\u27A1":
                  if current < len(embeds)-1:
                      current += 1

              elif reaction.emoji == u"\u23E9":
                  current = len(embeds)-1

              for button in buttons:
                  await msg.remove_reaction(button, ctx.author)

              if current != previous_page:
                  await msg.edit(embed=embeds[current])
  elif cmd == 'image':
    color = color_picker()
    embed = discord.Embed(
      title = "Image Command List:\n ** **", description = "Here's a list of image commands I can run!\n\n ** **", color=color
    )
    embed2 = discord.Embed(
      title = "Image Command List:\n ** **", description = "Here's a list of image commands I can run!\n\n ** **", color=color
    )

    embed.add_field(name = '👮 Wanted:', value= f"> Enter a user and I'll make a wanted poster for them!\n> `{message_prefixes_custom(ctx.message.guild)}wanted` or `{message_prefixes_custom(ctx.message.guild)}wanted @user`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '💢 Slap:', value= f"> Enter a user to slap!\n> `{message_prefixes_custom(ctx.message.guild)}slap` or `{message_prefixes_custom(ctx.message.guild)}slap @user` or `{message_prefixes_custom(ctx.message.guild)}slap @user @user`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '👊 Punch:', value= f"> Enter a user to punch!\n> `{message_prefixes_custom(ctx.message.guild)}punch` or `{message_prefixes_custom(ctx.message.guild)}punch @user` or `{message_prefixes_custom(ctx.message.guild)}punch @user @user`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '🦵 Boot:', value= f"> Enter a user to boot!\n> `{message_prefixes_custom(ctx.message.guild)}boot` or `{message_prefixes_custom(ctx.message.guild)}boot @user` or `{message_prefixes_custom(ctx.message.guild)}boot @user @user`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '😂 Meme:', value= f"> Here's a fun meme for you!\n> `{message_prefixes_custom(ctx.message.guild)}meme`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🐕 Dogs:', value= f"> See cute images of dogs!\n> `{message_prefixes_custom(ctx.message.guild)}dog`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🐈 Cats:', value= f"> See cute images of cats!\n> `{message_prefixes_custom(ctx.message.guild)}cat`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🦊 Foxes:', value= f"> See cute images of foxs!\n> `{message_prefixes_custom(ctx.message.guild)}fox`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🖼️ Gif:', value= f"> Search for any gif you want!\n> `{message_prefixes_custom(ctx.message.guild)}gif [topic]`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '📰 Comic:', value= f"> Ask me to show you a fun comic!\n> `{message_prefixes_custom(ctx.message.guild)}comic`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed2.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed.set_footer(text="Page 1/2")
    embed2.set_footer(text="Page 2/2")
    embeds = [embed, embed2]

    msg = await ctx.send(embed = embed)
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    for button in buttons:
          await msg.add_reaction(button)

    current=0  
    while True:
          try:
              reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

          except asyncio.TimeoutError:
              return

          else:
              previous_page = current
              if reaction.emoji == u"\u23EA":
                  current = 0
                  
              elif reaction.emoji == u"\u2B05":
                  if current > 0:
                      current -= 1
                      
              elif reaction.emoji == u"\u27A1":
                  if current < len(embeds)-1:
                      current += 1

              elif reaction.emoji == u"\u23E9":
                  current = len(embeds)-1

              for button in buttons:
                  await msg.remove_reaction(button, ctx.author)

              if current != previous_page:
                  await msg.edit(embed=embeds[current])



  elif cmd == 'game':
    color = color_picker()
    embed3 = discord.Embed(
      title = "Game Command List:\n ** **", description = "Here's a list of game commands I can run!\n \n ** **", color=color
    )
    value = (
      f"""> Play tic tac toe with a friend!
      > 
      > *Start:* `{message_prefixes_custom(ctx.message.guild)}ttt [@user]`
      > *Place:* `{message_prefixes_custom(ctx.message.guild)}place [number 1-9]`
      > *End:* `{message_prefixes_custom(ctx.message.guild)}end`"""
    )
    embed3.add_field(name = ':o2: Tic Tac Toe:', value=value, inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.add_field(name = '⚔️ Battle:', value=f"> Battle with your friends!\n> `{message_prefixes_custom(ctx.message.guild)}battle [@user]`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.add_field(name = '💭 Guess:', value=f"> I can guess any character you think of!\n> `{message_prefixes_custom(ctx.message.guild)}guess`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.add_field(name = '🕴 Hangman:', value=f"> Play Hangman with me!\n> `{message_prefixes_custom(ctx.message.guild)}hm`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.add_field(name = '🪨 Rock Paper Scissors:', value=f"> Play RPS with me!\n> `{message_prefixes_custom(ctx.message.guild)}rps`", inline = False)
    embed3.add_field(name = '** **', value= "** **" , inline = False)
    embed3.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    embed3.set_footer(text="Page 1/1")
    await ctx.send(embed=embed3)
  
  elif cmd == 'credits':
    color = color_picker()
    embed = discord.Embed(
      title = "Credit Command List:\n ** **", description = "Here's a list of credit commands I can run!\n\n ** **", color=color
    )
    embed.add_field(name = '📚 Credits:', value= f"> Meet my creators!\n> `{message_prefixes_custom(ctx.message.guild)}credits`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '💻 Website:', value= f"> View my website and my invite link!\n> `{message_prefixes_custom(ctx.message.guild)}website`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '💌 Invite:', value= f"> Invite me to any server of yours!\n> `{message_prefixes_custom(ctx.message.guild)}invite`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '⏲️ Server Count:', value= f"> Check how many servers Celeste is in!\n> `{message_prefixes_custom(ctx.message.guild)}servers`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '🗳️ Vote:', value= f"> Upvote Celeste! It means a lot!\n> `{message_prefixes_custom(ctx.message.guild)}vote`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.add_field(name = '⚖️ Support Server:', value= f"> Join the official support server of Celeste!\n> `{message_prefixes_custom(ctx.message.guild)}support`", inline = False)
    embed.add_field(name = '** **', value= "** **" , inline = False)
    embed.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    await ctx.send(embed=embed)
    embed.set_footer(text="Page 1/1")
  
  elif cmd == 'fun':
    color = color_picker()
    embed1 = discord.Embed(
      title = "Fun Command List:\n ** **", description = "Here's a list of fun commands I can run!\n\n ** **", color=color
    )
    embed2 = discord.Embed(
      title = "Fun Command List:\n ** **", description = "Here's a list of fun commands I can run!\n\n ** **", color=color
    )

    embed3 = discord.Embed(
      title = "Fun Command List:\n ** **", description = "Here's a list of fun commands I can run!\n\n ** **", color=color
    )

    embed4 = discord.Embed(
      title = "Fun Command List:\n ** **", description = "Here's a list of fun commands I can run!\n\n ** **", color=color
    )

    embed1.add_field(name = '🎱 8ball:', value= f"> Ask the 8 ball a question, and it will answer!\n> `{message_prefixes_custom(ctx.message.guild)}8ball [question]`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '🖌️ Ascii:', value= f"> Convert text to ASCII art!\n> `{message_prefixes_custom(ctx.message.guild)}ascii [text]`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '😛 Mock:', value= f"> Need to mock someone? Just type your message, and I'll do it for you!\n> `{message_prefixes_custom(ctx.message.guild)}mock [message]`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '🗣️ Say:', value= f"> I'll speak whatever you want!\n> `{message_prefixes_custom(ctx.message.guild)}say [message]`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)


    embed2.add_field(name = '🤣 Dad Jokes:', value= f"> Ask me for a dad joke!\n> `{message_prefixes_custom(ctx.message.guild)}dadjoke`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '📜 Inspire:', value= f"> Feeling down? I'll give you an inspiring quote!\n> `{message_prefixes_custom(ctx.message.guild)}inspire`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '🎲 Dice Roll:', value= f"> I'll roll a number for you!\n> `{message_prefixes_custom(ctx.message.guild)}roll [range and exclusives]` - Ex: `{message_prefixes_custom(ctx.message.guild)}roll 1-2-4-10`, where 1-10 would be the range, and 2 and 4 would be the exclusives.", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)
    embed2.add_field(name = '👾 Hack:', value= f"> Hack the accounts of other users!\n> `{message_prefixes_custom(ctx.message.guild)}hack @user`", inline = False)
    embed2.add_field(name = '** **', value= "** **" , inline = False)

    

    embed4.add_field(name = '🚿 Shower Thoughts:', value= f"> Shower Thoughts to make you think!\n> `{message_prefixes_custom(ctx.message.guild)}st`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)
    embed4.add_field(name = '🤗 Hugs:', value= f"> Hug a friend!\n> `{message_prefixes_custom(ctx.message.guild)}hug [@user]`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)
    embed4.add_field(name = '💋 Kiss:', value= f"> Kiss a friend!\n> `{message_prefixes_custom(ctx.message.guild)}kiss [@user]`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)
    embed4.add_field(name = '🫂 Cuddle:', value= f"> Cuddle with a friend!\n> `{message_prefixes_custom(ctx.message.guild)}cuddle [@user]`", inline = False)
    embed4.add_field(name = '** **', value= "** **" , inline = False)


    embed1.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )


    embed2.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )

    embed3.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )

    embed4.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    
    embed1.set_footer(text="Page 1/3")
    embed2.set_footer(text="Page 2/3")
    embed3.set_footer(text="Page 3/4")
    embed4.set_footer(text="Page 3/3")

    embeds = [embed1, embed2, embed4]

    msg = await ctx.send(embed = embed1)
    buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] # skip to start, left, right, skip to end
    for button in buttons:
          await msg.add_reaction(button)

    current=0  
    while True:
          try:
              reaction, user = await client.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

          except asyncio.TimeoutError:
              return

          else:
              previous_page = current
              if reaction.emoji == u"\u23EA":
                  current = 0
                  
              elif reaction.emoji == u"\u2B05":
                  if current > 0:
                      current -= 1
                      
              elif reaction.emoji == u"\u27A1":
                  if current < len(embeds)-1:
                      current += 1

              elif reaction.emoji == u"\u23E9":
                  current = len(embeds)-1

              for button in buttons:
                  await msg.remove_reaction(button, ctx.author)

              if current != previous_page:
                  await msg.edit(embed=embeds[current])
  elif cmd == 'giveaway':
    color = color_picker()
    embed1 = discord.Embed(
      title = "Giveaway Command List:\n ** **", description = "Here's a list of giveaway commands I can run!\n\n ** **", color=color
    )


    embed1.add_field(name = '🎉 Giveaways:', value= f"> Host giveaways in your server!\n> `{message_prefixes_custom(ctx.message.guild)}gstart [time] [prize]`\n> ** **\n> Ex: `{message_prefixes_custom(ctx.message.guild)}gstart 1m 1 Mil Celeste Coins` or `{message_prefixes_custom(ctx.message.guild)}gstart 1h 1 Wolf`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '🥳 Reroll:', value= f"> Reroll your giveaway for a new winner!\n> `{message_prefixes_custom(ctx.message.guild)}rr [message_id]`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)
    embed1.add_field(name = '🎊 End Giveaway:', value= f"> End an on going giveaway sooner!\n> `{message_prefixes_custom(ctx.message.guild)}gend [message_id]`", inline = False)
    embed1.add_field(name = '** **', value= "** **" , inline = False)

    embed1.set_thumbnail(
      url="https://cdn.discordapp.com/attachments/766158371820666940/829486346066329650/celeste.png"
    )
    
    embed1.set_footer(text="Page 1/1")

    await ctx.send(embed=embed1)


reminders_function.start()
client.loop.create_task(reminders_function())
client.loop.create_task(ch_pr())

keep_alive.keep_alive()
client.run('ODE4NjUxMzA2NjQxMzI2MTIx.YEbKcQ.IFAmRKY2fzVYH85_PkmO0UOPPA0')
