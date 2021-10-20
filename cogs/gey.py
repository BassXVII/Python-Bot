import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '.', intents = intents)

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

async def get_userID(user_id): 
   # renamed id to user_id to make it more readable
 global user 
 user= bot.get_user(user_id)
 print(user)
 return (user)

@bot.event
async def on_message(message):
  randInt = random.randint(1,100)
  if message.content.startswith("gey"):
        await message.channel.send(f"{message.author.mention} is {randInt} percent gay")

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

def setup(bot):
  bot.add_cog(MyCog(bot))