import discord
import os
from keep_alive import keep_alive
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
from random import randint
from itertools import cycle

client = discord.Client()
Client_ = commands.Bot(command_prefix = "!")

status = ["Catgirl Simulator", "Evangelion: The Game", "Hyperdimension Neptunia V", "Cheek Clapping Simulator", "Catgirl Simulator 2.0"]

chat_filter = ["FUCK", "SHIT", "NIGGER", "CUNT"]
bypass_list = ["# Add your long-form user ID here"]

again = "https://www.youtube.com/watch?v=2uq34TeWEdQ" # You can make these links whatever works for you
snk = "https://www.youtube.com/watch?v=mbaz5gwtQOA"
rain = "https://www.youtube.com/watch?v=cRA5gsdCf4c"
rr = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
tank = "https://www.youtube.com/watch?v=n2rVnRwW0h8"
mha = "https://www.youtube.com/watch?v=0AuPpGuewzw"
space = "https://www.youtube.com/watch?v=00nvJv6gno4"

async def change_status():
  await client.wait_until_ready()
  x = cycle(status)

  while not client.is_closed:
    current_status = next(x)
    await client.change_presence(game=discord.Game(name=current_status))
    await asyncio.sleep(3600)

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

@client.event
async def on_message(message):
  contents = message.content.split(" ")
  if message.content.upper().startswith("!PING"):
    time.sleep(1)
    userID = message.author.id
    await client.send_message(message.channel, "<@%s>, I've got you!" % (userID))
  if message.content.upper().startswith("!EXPLOSION"):
    time.sleep(1)
    await client.send_message(message.channel, "💥")
  if message.content.upper().startswith("!SAY"):
    args = message.content.split(" ")
    time.sleep(1)
    await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
  if message.content.upper().startswith("!HELP"):
    author = message.author.id

    embed = discord.Embed(
      colour = discord.Colour.orange()
    )

    embed.set_author(name="Help")
    embed.add_field(name="Commands:", value="!ping, !music, !version, !headpats, !dev", inline=False)

    await client.send_message(message.channel, embed=embed)
  if message.content.upper().startswith("!MUSIC"):
    for x in range(1):
      val = randint(1,7)
      if val == 1:
        time.sleep(1)
        await client.send_message(message.channel, again)
      if val == 2:
        time.sleep(1)
        await client.send_message(message.channel, snk)
      if val == 3:
        time.sleep(1)
        await client.send_message(message.channel, rr)
      if val == 4:
        time.sleep(1)
        await client.send_message(message.channel, tank)
      if val == 5:
        time.sleep(1)
        await client.send_message(message.channel, mha)
      if val == 6:
        time.sleep(1)
        await client.send_message(message.channel, rain)
      if val == 7:
        time.sleep(1)
        await client.send_message(message.channel, space)
  if message.content.upper().startswith("!KAWAII"):
    time.sleep(1)
    await client.send_message(message.channel, "(◕‿◕✿)")
  if message.content.upper().startswith("!WHO"):
    time.sleep(1)
    await client.send_message(message.channel, "Sore wa watashidesu, NekoBot")
  if message.content.upper().startswith("!GREETING"):
    if not message.author.id in bypass_list:
      time.sleep(1)
      await client.send_message(message.channel, "You don't have access to this command!")
    else:
      time.sleep(1)
      await client.send_message(message.channel, "Welcome to the Lolice HQ! I'm your local loli-bot Akane. If you have any questions just type !help")
  if message.content.upper().startswith("!MYID"):
    if not message.author.id in bypass_list:
      time.sleep(1)
      await client.send_message(message.channel, "You don't have access to this command!")
    else:
      time.sleep(1)
      await client.send_message(message.channel, "Your id is %s" % message.author.id)
      await client.delete_message(message)
      return
  if message.content.upper().startswith("!VERSION"):
    time.sleep(1)
    await client.send_message(message.channel, "NekoBot is currently running v1.3.0")
  for word in contents:
    if word.upper() in chat_filter:
      if not message.author.id in bypass_list:
        try:
          await client.delete_message(message)
          await client.send_message(message.channel, "**HEY!** You're not allowed to use that word here!")
        except discord.errors.NotFound:
          return
  if message.content.upper().startswith("!HEADPATS"):
    time.sleep(1)
    userID = message.author.id
    val = randint(1,3)
    if val == 1:
      await client.send_message(message.channel, "<@%s>, have some headpats!" % (userID))
      with open('tenor.gif', 'rb') as picture:
        await client.send_file(message.channel, picture)
    if val == 2:
      await client.send_message(message.channel, "<@%s>, have some headpats!" % (userID))
      with open('patpat.gif', 'rb') as picture:
        await client.send_file(message.channel, picture)
    if val == 3:
      await client.send_message(message.channel, "<@%s>, have some headpats!" % (userID))
      with open('military.gif', 'rb') as picture:
        await client.send_file(message.channel, picture)
  if message.content.upper().startswith("!DEBUG"):
    time.sleep(1)
    userID = message.author.id
    if not message.author.id in bypass_list:
      time.sleep(1)
      await client.send_message(message.channel, "You don't have access to this command!")
    else:
      time.sleep(1)
      await client.send_message(message.channel, "Ä̶́̊͜m̶̧̈́̀ ̷̘̋Í̶̘ ̵͇͓͊͑b̷̡̌u̴͓̹̓̂g̵̛̱g̶̙̽ȉ̶̪̠͂n̷̟̍ģ̶̘̂ ̴̡̥̿̀o̵͈̩̿ŭ̷͇t̶̨͛?̴̞̂͝")
      return
  if message.content.upper().startswith("!DEV"):
    time.sleep(1)
    await client.send_message(message.channel, "# This is where my Twitter was")

client.loop.create_task(change_status())
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
