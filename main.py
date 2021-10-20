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


RPS = ["Rock", "Paper", "Scissors"]
Player_input = ["Rock", "rock", "Paper", "paper", "Scissors", "scissors"]


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
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
  output1 = random.choice(RPS);
  player1 = ctx.author.name
  randInt = random.randint(1,10)

  
  if (randInt == 5):
    await ctx.channel.send("Snakey chose very pointy scissors and cut ya nuts off. That must suck.")
  elif args.lower() == output1.lower():
    await ctx.channel.send("You both tied :)")
  elif args == "Paper" or args == "paper" and output1 == "Rock":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args == "Rock" or args == "rock" and output1 == "Scissors":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args == "Scissors" or args == "scissors"  and output1 == "Paper":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args != Player_input:
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
