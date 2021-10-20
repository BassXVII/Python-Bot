import discord
import logging
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '.', intents = intents)

#handle logging errors
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@bot.command()
async def delete(self, amount=25):
  await self.channel.purge(limit=amount)
  await self.channel.send("Snakey deleted 25 previous messages!")



def setup(bot):
  bot.add_cog(MyCog(bot))