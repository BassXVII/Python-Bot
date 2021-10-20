from keep_alive import keep_alive
import discord
import os
import logging
import datetime
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.members = True
#import spotipy
#from spotipy.oauth2 import SpotifyOAuth
#bot = discord.bot()
bot = commands.Bot(command_prefix = '.', intents = intents)



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


RPS = ["rock", "paper", "scissors"]
Player_input = ["rock", "paper", "scissors"]


testWords = [ "Fuk", "cunt"]
responses = [ "Thats not nice. Im dissapointed in you.", "Get that dirty language outta here", "Do you kiss your momma with that mouth?"]


Lonely = ["Where are the boys","where are the boys", "Whos on", "whos on", "where is everybody", "Where is everybody", "where tha boys at", "Where tha hoes at", "where my hoes at", "where tha hoes at", "where the hoes at", "anyone on"]

HereIAm = ["Well, it looks like no one is on at the moment, but im here. ", "Looks like it's just you bud, but im here! Not that i can do much", "No one likes you.", "Well, I'd keep you company, but it seems as if im programmed with only a limited number of responses to a limited number of questions. So that's not much help,is it.", "IDK, you have a lot of fake friends, huh. "]
@bot.event
async def on_ready():
    print('We have logged in as {0.user}, Yippy ki Yay'.format(bot))
# pass_context is not necesary since more than few versions back


async def get_userID(user_id): 
   # renamed id to user_id to make it more readable
 global user 
 user= bot.get_user(user_id)
 print(user)
 return (user)
  
 
@bot.event
async def on_message(message):
  try:
     #Message to see if bot is up
    if message.content.startswith('.Ping'):
        await message.channel.send('Pong!')

      
    if any(word in message.content for word in testWords):
      await message.channel.purge(limit=1)
      await message.channel.send(random.choice(responses))

    if any(word in message.content for word in Lonely):
      await message.channel.send(random.choice(HereIAm))
    
    if(message.author.id == 369208607126061057): 
      embeds = message.embeds # return list of embeds
      for embed in embeds:
       print(embed.to_dict()) # it's content of embed in dict
       Des = embed.description 
       #Getting substring from description
       Bracket1 = "["
       Bracket2 = "]"

       indx1 = Des.index(Bracket1)
       indx2 = Des.index(Bracket2)

       res = ' '
       for idx in range(indx1 + len(Bracket1), indx2):
        res = res + Des[idx]

        #Getting substring from User
        Usr = embed.description
        carrot1 = "<@"
        carrot2 = ">"
        indx3 = Usr.index(carrot1)
        indx4 = Usr.index(carrot2)
        usr = ' '
        

        #gets the user name from the description field
        for idx in range(indx3 + len(carrot1), indx4):
          usr = usr + Usr[idx]
        
       user_id = int(usr)   
       await get_userID(user_id)
       
      #get current time
      e = datetime.datetime.now()
      date_now = ("%s/%s/%s" % (e.day, e.month, e.year))
      print("Extracted Data " + res + " requested By " + str(user))
      with open("SongsFile.txt", "a+") as f:
        f.write(str(date_now) + ": "+ res + " Requested by: " + str(user) + "\n")

   #Help info
    if message.content.startswith("halp"):
        await message.channel.send("Current commands: \n .Info\n1.Gey\n2.Purge\n3. .add\n4. .playList\n 5. SuggestedList")

 
    await bot.process_commands(message)


  except UnboundLocalError as error:
        # Output expected UnboundLocalErrors.
        logger.error(error)

 
@bot.command()
async def add(ctx, * , args):
    msg_author = ctx.message.author
    e = datetime.datetime.now()
    date_now = ("%s/%s/%s" % (e.day, e.month, e.year))

    await ctx.channel.send("Snakey added " + args + " to the suggested songs list :)")

    


    with open("Suggested.txt", "a+") as f:
      f.seek(0)
      data = f.read(100)
      if len(data) > 0 :
        f.write(str(date_now) + ", " + str(args) + ", added by: " + str(msg_author))
        f.write("\n")
        f.write("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
        f.write("\n")
    
#commands to get embedded lists of song lists
@bot.command()
async def playList(ctx):
  file = open("SongsFile.txt")
  content = file.read()
  embed: discord.Embed = discord.Embed(
        title="Public Play List", description = content,
        color=0xF1C40F)
  await ctx.channel.send(embed=embed)

#Embedded list of suggested songs
@bot.command()
async def SuggestedList(ctx):
  file = open("Suggested.txt")
  content = file.read()
  embed: discord.Embed = discord.Embed(
        title="Suggested songs to play", description = content,
        color=0xF1C40F)
  await ctx.channel.send(embed=embed)
   
#Info command
@bot.command()
async def info(ctx):
   await ctx.channel.send("Hi there, im Snakey. Im written in python. Im here to mainly keep track of songs we have played. For beginners, each command is case sensitive, an dmost require a .before them. IDk, im working on fixing that. Most of the commands you can figure out. Im getting kinda high :)")

#Rock paper scissors command
@bot.command()
async def rps(ctx, * , args):
  output1 = random.choice(RPS)
  player1 = ctx.author.name
  randInt = random.randint(1,10)
  args = args.strip()

  
  if (randInt == 5):
    await ctx.channel.send("Snakey chose very pointy scissors and cut ya nuts off. That must suck.")
  elif args == output1:
    await ctx.channel.send("You both tied :)")
  elif args == "paper" and output1 == "Rock":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args == "rock" and output1 == "scissors":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args == "scissors"  and output1 == "paper":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args != "rock" or args != "paper" or args != "scissors":
    await ctx.channel.send("Hey, dont do that. You cant just add " + args + " into the game. Shame.")
  else:
    await ctx.channel.send("Snakey beat your "+ args + " with his " + output1)


  

bot.load_extension("cogs.rps")
bot.load_extension("cogs.Purge")
bot.load_extension("cogs.gey")
bot.load_extension("cogs.phrases")
#@bot.command()
#async def Purge(ctx, * , args):
#      await ctx.channel.purge(limit=args)
#     await ctx.channel.send("Snakey cleared away 30 messages")

#command not working in cogs folder
@bot.command()
async def clear(ctx, amount=25):
  await ctx.channel.purge(limit=amount)
  await ctx.channel.send("Snakey deleted 25 previous messages!")


keep_alive()
bot.run(os.getenv('TOKEN'))
