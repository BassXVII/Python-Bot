from keep_alive import keep_alive
import discord
import os
import logging
from discord.ext import commands
#from discord.ext.commands import Bot
import random


#bot = discord.bot()
bot = commands.Bot(command_prefix = '.')


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)



testWords = [ "Fuck", "shit", "Damn", "Ass", "cunt", "bitch"]
responses = [ "Thats not nice. Im dissapointed in you.", "Get that dirty language outta here", "Do you kiss your momma with that mouth?"]


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

 
@bot.event
async def on_message(message):

    
    if message.content.startswith("Purge"):
        if str(message.channel) == "bot" and message.content != "":
          await message.channel.purge(limit=30)
          await message.channel.send("Snakey cleared away 30 messages")


    #if message.author == bot.author:
      #await message.channel.send(message.author.id)
      #print(message.author.id)
      #return
    
    #Message to see if bot is up
    if message.content.startswith('.Ping'):
        await message.channel.send('Pong!')
      

    
    if(message.author.id == 234395307759108106): 
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

       print("Extracted Data " + res)
       with open("SongsFile.txt", "a+") as f:
        f.write(res + "\n")

     

    


    #Message based on a random word
    if any(word in message.content for word in testWords):
        await message.channel.purge(limit=1)
        await message.channel.send(random.choice(responses))


    #Help info

    if message.content.startswith("!halp"):
        await message.channel.send("Current commands: \n1.Gey\n2.Purge\n3. .add\n4. .playList")

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
async def add(ctx, args):
    
    await ctx.channel.send("Snakey added " + args + " to the playlist!")

    with open("SongsFile.txt", "a+") as f:
      f.seek(0)
      data = f.read(100)
      if len(data) > 0 :
        f.write(str(args))
        f.write("\n")

    print("message recieved")
    

@bot.command()
async def playList(ctx):
  file = open("SongsFile.txt")
  content = file.read()
 # await ctx.send(content)

  embed: discord.Embed = discord.Embed(
        title="Public Play List", description= content,
        color=0xF1C40F)
 
  await ctx.channel.send(embed=embed)
  




keep_alive()
bot.run(os.getenv('TOKEN'))
