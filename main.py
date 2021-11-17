import discord, os, logging, datetime, sys, random, socket, re
from keep_alive import keep_alive
from pythonping import ping
from PIL import Image
import json
from discord.ext import commands
import pandas as pd
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import ast

from urllib.request import Request, urlopen
#from discord_slash import SlashCommand, SlashContext
#from discord_slash.utils.manage_commands import create_choice, create_option
import requests
from pprint import PrettyPrinter
pp = PrettyPrinter()

#genius_client_id = 'CLQVbNC3QwV_yLUqufIS_nJPqyrOpylB69nn6eLQZSIva_AJeE0TIyFQqLvU92sN'
#genius_secret_id = 'bqIijTDld-eoSr6E5igdhqV4wEBDX5FmzyJQBo3bb-324lBIEDteFaOhaEKH7cd19QucnCY2f3rirTau8D8hAA'
client_access_token = 'x-Ip1tsZKQcKQQHhsLUAARDtltGp62ujVLz9s_Dqd-Fu4EBhRwMZuclD2UDZkdZ1'


intents = discord.Intents.default()
intents.members = True
#import spotipy
#from spotipy.oauth2 import SpotifyOAuth
#bot = discord.bot()
bot = commands.Bot(command_prefix = '.', intents = intents)
#slash = SlashCommand(bot, sync_commands = True)
guild_ids = [600195673886818314, 650217909687156741]



apiKey = '917a0892'


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


RPS = ["rock", "paper", "scissors", "lizard", "spock"]
sanitized_input = ["rock", "paper", "scissors", "lizard", "spock"]


IP = "0.0.0.0"

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

 #Add a song suggestion. | need to add by guild or find a better way to store
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

#@slash.slash(
 # name = "Info",
 # description = "Who am i? Who U?",
  
#)
#async def _poo(ctx:SlashContext):
#  await ctx.send("Hi there, im Snakey. Im written in python. Im here to mainly keep track of songs we have played. For beginners, each command is case sensitive, an dmost require a .before them. IDk, im working on fixing that. Most of the commands you can figure out. Im getting kinda high :)")


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
    


  
#Prints details to the Rock paper lizard spock game and outputs in embedded format.
@bot.command()
async def rpsInfo(self):
  embed=discord.Embed(title="RPSLS Rules", description="Here are the rules: \n\nScissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.", color=0xFF5733)

  file = discord.File("imgs/RPSLS.png")
  embed.set_thumbnail(url="attachment://RPSLS.png")
  #e = discord.Embed()
  embed.set_author(name = "Ya Boi Snakey", url = "https://discord.com/developers/applications/819659006268276796/information", icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png")
  await self.send(file = file, embed=embed)
 

#Clears the chat 25 messages. 
@bot.command()
async def clear(ctx, amount=25):
  await ctx.channel.purge(limit=amount)
  embed=discord.Embed(title="Sweep sweep sucka", description="Just swept away 25 messages, no problem at all", color=0x33FFFF)
  embed.set_author(name = "Ya Boi Snakey", url = "https://discord.com/developers/applications/819659006268276796/information", icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png")
  await ctx.channel.send(embed=embed)  



#Sets a IP to be able to be pinged later with the .pingmc command. Basically stores a minecraft IP with this stored value so that it can be pinged. 
@bot.command()
async def setIP(ctx, ip):
  global IP 
  IP = ip
  await ctx.channel.send("Snakey set the MC server IP to " + ip)  

#MC command to see if server is up or not. USed alongside with setIP.
@bot.command()
async def pingmc(ctx, port):
  
  host = IP
  timeout_seconds=1
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.settimeout(timeout_seconds)
  result = sock.connect_ex((host,int(port)))
  if result == 0:
    print("Host: {}, Port: {} - True".format(host, port))
    await ctx.channel.send("Server is up and ready to go baby")
  else:
    print("Host: {}, Port: {} - False".format(host, port))
    await ctx.channel.send("Server is temporarily down. Please contact your server administrator and tell him to get on it")
  sock.close()

#see what members the bot picks up in the current server. Gets all user id's.
@bot.command()
async def mem(ctx):
  f= open("membersList.txt","w+")
  for guild in bot.guilds:
    for member in guild.members:
        f.write(member.name + "\n")
    f.close()

#see is a member is part of guild. Can also use .mem command
@bot.command()
async def isMem(ctx, memb):
  with open('membersList.txt') as f:
    if memb in f.read():
        print("true")
    else:
      print("False")
  
  f.close()


#------------------------------------------------#
#Moive query command to get some info from movies.
@bot.command()
async def movieQ(ctx, * , movieSearch):
  data_URL = 'http://www.omdbapi.com/?apikey='+apiKey
  
  year = ''

  movie = movieSearch 
  params = {
      't': movie,
      'type':'movie',
      'y':year,
      'plot':'full',
      'tomatoes':'true'
      
}
  response = requests.get(data_URL,params=params).json()
 
  #Opens a file to read the response from in json format. 
  with open ("Movie.json", "w") as f:
    json.dump (response, f)

  #read file contents and store in a dict.
  f = open('Movie.json', 'r')
  db = json.load(f)

  if db['Response'] == 'False':
    await ctx.channel.send("Movie not found, please re-enter the movie title.")
  else:

    moviePlot = db["Plot"]
 
    value_string = "\n".join(f"{rating['Source']}: {rating['Value']}" for rating in db['Ratings'])  

    embed=discord.Embed(title=movieSearch, description= moviePlot, color=0xFF5733)
    imageURL = db["Poster"]
    embed.set_image(url=imageURL)  
  #e = discord.Embed()
    embed.set_author(name = "Ya Boi Snakey", url = "https://discord.com/developers/applications/819659006268276796/information", icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png")

    embed.add_field(name='Ratings', value= value_string, inline=True)
    embed.add_field(name = "Misc details" , value = "Year released: " + db['Year'] + "\nRating: " + db['Rated'], inline= True)
    await ctx.channel.send(embed=embed)
   
  
  #(movieSearch + " Scores: \n"+ "Rotten Tomatoes  score: " + RottenTom_Rating + "\nIMDB score: " + IMDB_Rating + "\nMetaCritic score: " + MetaCritic_Rating


  #------------------------------LYRICS----------------------------------------#
@bot.command()
async def Lyrics(ctx, * , songname):
  
  search_term = songname

  genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"

  response = requests.get(genius_search_url)
  json_data = response.json()


  
  with open ("Artist_Query.json", "w") as f:
    json.dump ( json_data, f)
  
  
  f = open('Artist_Query.json', 'r')  
  db = json.load(f)
  json_data['response']['hits'][0]
  
  for song in json_data['response']['hits']:
    print(song['result']['full_title'], song['result']['stats'])
  
      
    #KOgmt4ELM3VC7D598oXLBwFVcdNxyP7aihveOI41Cin7wn-Ge_qbeywI0ROSsMRa
  

@bot.command()
async def artist(ctx, artist_query, numQuery):

  int_Value = int(numQuery)
  artistQ = artist_query
  page = requests.get("https://www.lyrics.com/artist/" + artistQ)
  soup = BeautifulSoup(page.content, 'lxml')
  title1 = soup.title.text # gets you the text of the <title>(...)</title>
  head = soup.findAll("p",  class_="artist-bio")
  pp.pprint(head)
  profile_pic = soup.findAll("div" ,id="featured-artist-avatar")
  pp1 = str(profile_pic)
  headstr = str(head)
  pp.pprint(profile_pic)
 
  num_albums = []
  #Find all albums from artist
  albums = soup.findAll('h3', class_ = 'artist-album-label')

  for i in albums[:int_Value]:
    num_albums[i] = str(albums)
  #x = re.findall(r'(?=src)src=\"(?P<src>[^\[.*?\]+)' , pp1)

  
  #artist_pic = str(x)
  with open ("Example.txt", "w") as f:
    #f.write(headstr)
    #f.write(pp1)
    f.write(num_albums)
    

    

    
    embed=discord.Embed(title=artistQ, description=headstr, color=0xFF5733)
    #embed.set_image(url=pp1) 
    
    
    await ctx.channel.send(embed=embed)
  f.close()



bot.load_extension("cogs.ping")
bot.load_extension("cogs.Purge")

bot.load_extension("cogs.gey")
bot.load_extension("cogs.phrases")
bot.load_extension("cogs.rpsInfo")



keep_alive()
bot.run(os.getenv('TOKEN'))




