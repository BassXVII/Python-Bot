import discord
import os
from PIL import Image
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '.', intents = intents)

class rpsinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.command()
async def rpsInfo(self):
  img = 'imgs/RPSLS.png'
  await self.send('Here ya go', file=discord.File(img))

#await ctx.send('Working!', file=discord.File('upvote.png'))


def setup(bot):
  bot.add_cog(rpsinfo(bot))