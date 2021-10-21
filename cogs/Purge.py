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


class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

@bot.command()
async def delete(ctx, amount=25):
  await ctx.channel.purge(limit=amount)
  await ctx.channel.send("Snakey deleted 25 previous messages!")



def setup(bot):
  bot.add_cog(Purge(bot))