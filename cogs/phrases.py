import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '.', intents = intents)

testWords = [ "Fuk", "cunt"]
responses = [ "Thats not nice. Im dissapointed in you.", "Get that dirty language outta here", "Do you kiss your momma with that mouth?"]


Lonely = ["Where are the boys","where are the boys", "Whos on", "whos on", "where is everybody", "Where is everybody", "where tha boys at", "Where tha hoes at", "where my hoes at", "where tha hoes at", "where the hoes at", "anyone on"]

HereIAm = ["Well, it looks like no one is on at the moment, but im here. ", "Looks like it's just you bud, but im here! Not that i can do much", "No one likes you.", "Well, I'd keep you company, but it seems as if im programmed with only a limited number of responses to a limited number of questions. So that's not much help,is it.", "IDK, you have a lot of fake friends, huh. "]

class phrases(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.event
async def on_message(message):
  if any(word in message.content for word in testWords):
    await message.channel.purge(limit=1)
    await message.channel.send(random.choice(responses))

  if any(word in message.content for word in Lonely):
    await message.channel.send(random.choice(HereIAm))

def setup(bot):
  bot.add_cog(phrases(bot))