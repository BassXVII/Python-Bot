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
  def __init__(self, bot: commands.Bot):
    self.bot = bot


@commands.command(name="ping")
async def ping(self, ctx: commands.Context):
  await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")





def setup(bot):
  bot.add_cog(Purge(bot))