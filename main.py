import discord, os, logging, datetime, sys, random
from keep_alive import keep_alive
from pythonping import ping
from PIL import Image
from discord.ext import commands
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


RPS = ["rock", "paper", "scissors", "lizard", "spock"]
sanitized_input = ["rock", "paper", "scissors", "lizard", "spock"]




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
  args = args.strip().lower()
  
  
    
  if args != "paper" and args != "rock" and args != "scissors" and args != "lizard" and args != "spock":
    img = 'imgs/kirby.jpg'
    await ctx.send(file=discord.File(img))
    await ctx.channel.send("Hey, dont do that. You cant just add " + args + " into the game. Kirby's not mad, he's just disappointed.")
  elif args == output1:
    await ctx.channel.send("You both tied :)")
  elif args == "paper" and output1 == "rock":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args == "paper" and output1 == "spock":
    await ctx.channel.send("paper disproves " + output1 + ", " + player1 + " won that round")
  elif args == "rock" and output1 == "scissors":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args == "rock"  and output1 == "lizard":
    await ctx.channel.send("Rock crushes " + output1 + ", " + player1 + " won that round")
  elif args == "scissors"  and output1 == "paper":
    await ctx.channel.send("Snakey chose " + output1 + ", " + player1 + " won that round")
  elif args == "scissors"  and output1 == "lizard":
    await ctx.channel.send("the scissors decaptitates the " + output1 + ", must have been a small lizard. " + player1 + " won that round")
  elif args == "spock"  and output1 == "rock":
    await ctx.channel.send("Spock vaporized " + output1 + ", " + player1 + " won that round")
  elif args == "spock"  and output1 == "scissors":
    await ctx.channel.send("Spock smashes " + output1 + ", " + player1 + " won that round")
  elif args == "lizard"  and output1 == "paper":
    await ctx.channel.send("Your lizard just ate snakey's " + output1 + ", " + player1 + " won that round")
  elif args == "lizard"  and output1 == "spock":
    await ctx.channel.send("Big lizard poisons " + output1 + ", " + player1 + " won that round")
  elif (randInt == 5):
    await ctx.channel.send("Snakey brought a gun to a hand fight. Good luck beating that.")
  else:
    await ctx.channel.send("Snakey beat your "+ args + " with his " + output1)


  #temp = open('temp', 'wb')
  #with open('membersList.txt', 'r') as f:
    #for line in f:
     # if line.startswith(player1):
        #line = line.strip() + '  + 1\n'
     # temp.write(line.encode('utf-8'))
  #temp.close()
 # shutils.move('temp', 'membersList.txt')
    
@bot.command()
async def pingmc(ctx, host):
  #ping(host)
  await ctx.channel.send("Im working on that for right now. Please wait for this feature " + host)
  await pingmc(['finally the dumbass succeded.LOL']) 

@bot.command()
async def rpsInfo(self):

  embed=discord.Embed(title="RPSLS Rules", description="Here are the rules: \n\nScissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.", color=0xFF5733)

  file = discord.File("imgs/RPSLS.png")
  file2 = discord.File("imgs/logo.png")
  embed.set_thumbnail(url="attachment://RPSLS.png")
  #e = discord.Embed()
  embed.set_author(name = "Ya Boi Snakey", icon_url = "attachment://logo.png")
  
  await self.send(file = file, embed=embed)
  #img = 'imgs/RPSLS.png'
  #await self.send('Here ya go', file=discord.File(img))
  #name="RealDrewData", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg"
  #await self.send(embed=embed)


@bot.command()
async def clear(ctx, amount=25):
  await ctx.channel.purge(limit=amount)
  await ctx.channel.send("Snakey deleted 25 previous messages!")  



@bot.command()
async def mem(ctx):
  f= open("membersList.txt","w+")
  for guild in bot.guilds:
    for member in guild.members:
        f.write(member.name + "\n")
  
  f.close()



   

bot.load_extension("cogs.ping")
bot.load_extension("cogs.Purge")
bot.load_extension("cogs.gey")
bot.load_extension("cogs.phrases")
bot.load_extension("cogs.rpsInfo")



keep_alive()
bot.run(os.getenv('TOKEN'))
