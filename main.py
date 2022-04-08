import discord, os, logging, datetime, sys, random, socket, re
from keep_alive import keep_alive
from pythonping import ping
from PIL import Image
import json
import requests
from discord.ext import commands
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pprint import PrettyPrinter

pp = PrettyPrinter()

intents = discord.Intents.default()
intents.members = True
#import spotipy
#from spotipy.oauth2 import SpotifyOAuth
#bot = discord.bot()
bot = commands.Bot(command_prefix='.', intents=intents)
#slash = SlashCommand(bot, sync_commands = True)
guild_ids = [600195673886818314, 650217909687156741]

apiKey = '917a0892'

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log',
                              encoding='utf-8',
                              mode='w')
handler.setFormatter(
    logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
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
    user = bot.get_user(user_id)
    print(user)
    return (user)


@bot.event
async def on_message(message):
    try:
        #Message to see if bot is up
        if message.content.startswith('.Ping'):
            await message.channel.send('Pong!')

    #Help info
        if message.content.startswith("halp"):
            await message.channel.send(
                "Current commands: \n .Info\n2.Purge\n3. .add\n4. .playList\n 5. SuggestedList"
            )

        await bot.process_commands(message)

    except UnboundLocalError as error:
        # Output expected UnboundLocalErrors.
        logger.error(error)



#Info command
@bot.command()
async def info(ctx):
    await ctx.channel.send(
        "Hi there, im Snakey. Im written in python. Im here to mainly keep track of songs we have played. For beginners, each command is case sensitive, and most require a .before them. IDk, im working on fixing that. Most of the commands you can figure out. Im getting kinda high :)"
    )


#Rock paper scissors command
@bot.command()
async def rps(ctx, *, args):
    output1 = random.choice(RPS)
    player1 = ctx.author.name
    randInt = random.randint(1, 10)
    args = args.strip().lower()

    if args != "paper" and args != "rock" and args != "scissors" and args != "lizard" and args != "spock":
        img = 'imgs/kirby.jpg'
        await ctx.send(file=discord.File(img))
        await ctx.channel.send(
            "Hey, dont do that. You cant just add " + args +
            " into the game. Kirby's not mad, he's just disappointed.")
    elif args == output1:
        await ctx.channel.send("You both tied :)")
    elif args == "paper" and output1 == "rock":
        await ctx.channel.send("Snakey chose " + output1 + ", " + player1 +
                               " won that round")
    elif args == "paper" and output1 == "spock":
        await ctx.channel.send("paper disproves " + output1 + ", " + player1 +
                               " won that round")
    elif args == "rock" and output1 == "scissors":
        await ctx.channel.send("Snakey chose " + output1 + ", " + player1 +
                               " won that round")
    elif args == "rock" and output1 == "lizard":
        await ctx.channel.send("Rock crushes " + output1 + ", " + player1 +
                               " won that round")
    elif args == "scissors" and output1 == "paper":
        await ctx.channel.send("Snakey chose " + output1 + ", " + player1 +
                               " won that round")
    elif args == "scissors" and output1 == "lizard":
        await ctx.channel.send("the scissors decaptitates the " + output1 +
                               ", must have been a small lizard. " + player1 +
                               " won that round")
    elif args == "spock" and output1 == "rock":
        await ctx.channel.send("Spock vaporized " + output1 + ", " + player1 +
                               " won that round")
    elif args == "spock" and output1 == "scissors":
        await ctx.channel.send("Spock smashes " + output1 + ", " + player1 +
                               " won that round")
    elif args == "lizard" and output1 == "paper":
        await ctx.channel.send("Your lizard just ate snakey's " + output1 +
                               ", " + player1 + " won that round")
    elif args == "lizard" and output1 == "spock":
        await ctx.channel.send("Big lizard poisons " + output1 + ", " +
                               player1 + " won that round")
    elif (randInt == 5):
        await ctx.channel.send(
            "Snakey brought a gun to a hand fight. Good luck beating that.")
    else:
        await ctx.channel.send("Snakey beat your " + args + " with his " +
                               output1)

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
    embed = discord.Embed(
        title="RPSLS Rules",
        description=
        "Here are the rules: \n\nScissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.",
        color=0xFF5733)

    file = discord.File("imgs/RPSLS.png")
    embed.set_thumbnail(url="attachment://RPSLS.png")
    #e = discord.Embed()
    embed.set_author(
        name="Ya Boi Snakey",
        url=
        "https://discord.com/developers/applications/819659006268276796/information",
        icon_url=
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png"
    )
    await self.send(file=file, embed=embed)


#Clears the chat 25 messages.
@bot.command()
async def clear(ctx, amount=25):
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title="Sweep sweep sucka",
        description="Just swept away 25 messages, no problem at all",
        color=0x33FFFF)
    embed.set_author(
        name="Ya Boi Snakey",
        url=
        "https://discord.com/developers/applications/819659006268276796/information",
        icon_url=
        "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png"
    )
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
    timeout_seconds = 1
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout_seconds)
    result = sock.connect_ex((host, int(port)))
    if result == 0:
        print("Host: {}, Port: {} - True".format(host, port))
        await ctx.channel.send("Server is up and ready to go baby")
    else:
        print("Host: {}, Port: {} - False".format(host, port))
        await ctx.channel.send(
            "Server is temporarily down. Please contact your server administrator and tell him to get on it"
        )
    sock.close()



#------------------------------Artist Info----------------------------------------#
#, "https://www.lyrics.com/sub-artist/"

@bot.command()
async def artist(ctx, *, artist_query):

    #int_Value = int(numQuery)
    artistQ = artist_query
    print("Full url: https://www.lyrics.com/" + artist_query)
    page = requests.get("https://www.lyrics.com/artist/" + artistQ)
    #print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')


    #pattern for determining if there is an artist by the users requested FileNotFoundError
    pattern = "We couldn't find any artists matching your query."

    #avail_artist = soup.findAll("h4", string = pattern)
    avail =  soup.find(string=re.compile(pattern))
    #print(avail)

    
    profile_pic = soup.findAll("img", class_="artist-thumb")
    pic_Str = str(profile_pic)
    print(pic_Str)
    p = str(re.findall(r"(https.{1,})title", pic_Str))
    Artist_pic = re.sub(r'[\"([{})\]]', "", p)
    Artist_pic1 =  Artist_pic.strip('\'')
    

    #-------------------------------Get info about artist---------------------------------------#
    head = soup.findAll("p",  class_="artist-bio")
    Artist_bio = str(head)
    b = str(re.findall(r">(.{1,})<",  Artist_bio, flags= re.S)) # re.S flag for newline spaces i believe.
    Bio = re.sub(r"[\'([{})'\]]", " ", b)

    artist_Album = soup.findAll("h3",limit=6,  class_="artist-album-label")
    album_list= str(artist_Album)
    ab = str(re.findall(r"([\’\'!.,\(\)A-Z a-z0-9\w\-\:\+\%\[\]\+\/\;\&]{2,}</a)", album_list))
    
    #replace the </a with a blank space. 
    ab1 = str(re.sub(r"</a", "", ab))
  
    embed = discord.Embed(title=artistQ, description=Bio, color=0x00ffbf)
    embed.add_field(name="Top Albums", value=ab1, inline=True)
    imageURL = str(Artist_pic1)
    embed.set_image(url=imageURL)

    await ctx.channel.send(embed=embed)


    #Testing out what values i get in  text value so i kno wwhat to look for 
    #with open("Example.txt", "w") as f:
        #f.write(Bio + "\n")
       # f.write(Artist_pic1)


    #--------------------------------get artist int value for query--------------------------------#
  #<h3><a href="artist/Eminem/347307">Famous lyrics by&nbsp;&raquo;</a></h3></hgroup>
    artistVal = soup.findAll("h1", class_="artist")
    artistNum = str(artistVal)
    n = str(re.findall(r'(/[0-9]*)\"', artistNum))
    
    Anum1 = str(re.sub(r"[^0-9]*", "", n))
    #print("Anum: " + Anum1)
    #ANum = str(re.findall(r'([0-9]{6})', Anum1))

#---------------------------get artist albums-------------------------------#
@bot.command()
async def album(ctx, *, artist_query):

    artistQ = artist_query
    page = requests.get("https://www.lyrics.com/artist/" + artistQ)
    #print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')


    artist_Album = soup.findAll("h3",limit=30,  class_="artist-album-label")
    album_list= str(artist_Album)
    ab = str(re.findall(r"([\’\'!.,\(\)A-Z a-z0-9\w\-\:\+\%\[\]\+\/\;\&]{2,}</a)", album_list))
    
    #replace the </a with a blank space. 
    ab1 = str(re.sub(r"</a", "", ab))
    with open("Album.txt", "w") as f:
      f.write(ab1)

    #Write full html for certain album for regex testing purposes
      #f.write(album_list) 
    f.close()

  
    embed = discord.Embed(title=(artist_query + "Top 3 albums"), description=ab1, color=0x00ffbf)


    await ctx.channel.send(embed=embed)
    #Send embedded message in chat



#----------------------get lyrics for requested song---------------------------#
@bot.command()
async def lyrics(ctx, *, song):

    #int_Value = int(numQuery)
  songQ = song
  page = requests.get("https://www.azlyrics.com/lyrics/kodakblack" + songQ + ".html")
    #print(page.status_code)
  soup = BeautifulSoup(page.content, 'html.parser')

  with open("output.html", "w", encoding = 'utf-8') as file:
    # prettify the soup object and convert it into a string  
    file.write(str(soup.prettify()))


  
  
#f.close()

@bot.command()
async def test_arg(ctx, *args):
  page = requests.get("https://www.azlyrics.com/lyrics/" + args[0] + "/" + args[1] + ".html")
    #print(page.status_code)
  soup = BeautifulSoup(page.content, 'html.parser')
  print(soup)
 
  info = str(page)
  with open("Album.txt", "w") as f:
    f.write(info)
    

    
bot.load_extension("cogs.ping")
bot.load_extension("cogs.Purge")
bot.load_extension("cogs.gey")
bot.load_extension("cogs.phrases")
bot.load_extension("cogs.rpsInfo")

keep_alive()
bot.run(os.getenv('TOKEN'))


#https://stackoverflow.com/questions/41334058/soup-findall-return-null-for-div-class-attribute-beautifulsoup



#page = requests.get("https://www.lyrics.com/sub-artist/" +artistQ)
      #soup = BeautifulSoup(page.content, 'lxml')
      #print(page)
      #head = soup.findAll("p",  class_="artist-bio")
      #b = str(re.findall(r">(.{1,})<", Artist_bio))
      #Bio = re.sub(r"[\'([{})'\]]", " ", b)


# page = requests.get("https://www.lyrics.com/sub-artist/" +artistQ)
     # print(page)