from keep_alive import keep_alive
import discord
import os
import logging
import time
from discord.ext import commands
#from discord.ext.commands import Bot
import random
intents = discord.Intents.default()
intents.members = True



#bot = discord.bot()
bot = commands.Bot(command_prefix = '.', intents = intents)



logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



testWords = [ "Fuck", "shit", "Damn", "Ass", "cunt", "bitch"]
responses = [ "Thats not nice. Im dissapointed in you.", "Get that dirty language outta here", "Do you kiss your momma with that mouth?"]


Lonely = ["Where are the boys","where are the boys", "Whos on", "whos on", "where is everybody", "Where is everybody", "where tha boys at", "Where tha hoes at", "where my hoes at", "where tha hoes at", "where the hoes at", "anyone on"]

HereIAm = ["Well, it looks like no one is on at the moment, but im here. ", "Looks liek it's just you bud, but im here! Not that i can do much", "No one likes you.", "Well, I'd keep you company, but it seems as if im programmed with only a limited number of responses to a limited number of questions. So that's not much help,is it.", "IDK, you have a lot of fake friends, huh. "]


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
    if message.content.startswith("Purge"):
        if str(message.channel) == "bot" and message.content != "":
          await message.channel.purge(limit=30)
          await message.channel.send("Snakey cleared away 30 messages")

    #Message to see if bot is up
    if message.content.startswith('.Ping'):
        await message.channel.send('Pong!')
      

    
    if(message.author.id == 234395307759108106): 
      embeds = message.embeds # return list of embeds
      for embed in embeds:
       #print(embed.to_dict()) # it's content of embed in dict
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
       
       print("Extracted Data " + res + " requested By " + str(user))
       with open("SongsFile.txt", "a+") as f:
        f.write(res + " Requested by: " + str(user) + "\n")


    #Message based on a random word
    if any(word in message.content for word in testWords):
        await message.channel.purge(limit=1)
        await message.channel.send(random.choice(responses))

    if any(word in message.content for word in Lonely):
        await message.channel.send(random.choice(HereIAm))


    #Help info
    if message.content.startswith("!halp"):
        await message.channel.send("Current commands: \n1.Gey\n2.Purge\n3. .add\n4. .playList\n 5. SuggestedList")

    #Tell user how gay they are.
    randInt = random.randint(1,100)
    if message.content.startswith("gey"):
        await message.channel.send(f"{message.author} is {randInt} percent gay")

        if randInt in range(1,20):
            await message.channel.send("Wow, thats kinda straight.")
        elif randInt in range(21,30):
            await message.channel.send("Damn, shawty, your getting there.")
        elif randInt in range(31,55):
            await message.channel.send("Hows that closet lookin?")
        elif randInt in range(56,65):
            await message.channel.send("Always wondering why you liked sausage so much.")
        elif randInt in range(65-75):
            await message.channel.send("Your as staight as a circle")
        elif randInt in range(75-85):
            await message.channel.send("You a pee pee muncher")
        else:
            await  message.channel.send("Your gayer than james charles. Quit it.")
    await bot.process_commands(message)


 
@bot.command()
async def add(ctx, * , args):
    msg_author = ctx.message.author
    await ctx.channel.send("Snakey added " + args + " to the suggested songs list :)")

    with open("Suggested.txt", "a+") as f:
      f.seek(0)
      data = f.read(100)
      if len(data) > 0 :
        f.write(str(args) + "- Suggested by: " + str(msg_author))
        f.write("\n")
    

@bot.command()
async def ping(ctx, member):
    await ctx.send(f"Pinging, {ctx.author.mention}")


#commands to get embedded lists of song lists
@bot.command()
async def playList(ctx):
  file = open("SongsFile.txt")
  content = file.read()
  embed: discord.Embed = discord.Embed(
        title="Public Play List", description = content,
        color=0xF1C40F)
  await ctx.channel.send(embed=embed)


@bot.command()
async def SuggestedList(ctx):
  file = open("Suggested.txt")
  content = file.read()
  embed: discord.Embed = discord.Embed(
        title="Suggested songs to play", description = content,
        color=0xF1C40F)
  await ctx.channel.send(embed=embed)
  




keep_alive()
bot.run(os.getenv('TOKEN'))
