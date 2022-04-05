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


async def rpsInfo(self):

  embed=discord.Embed(title="RPSLS Rules", description="Here are the rules: \n\nScissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.", color=0xFF5733)

  file = discord.File("imgs/RPSLS.png")
  embed.set_thumbnail(url="attachment://RPSLS.png")
  #e = discord.Embed()
  embed.set_author(name = "Ya Boi Snakey", url = "https://discord.com/developers/applications/819659006268276796/information", icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/2048px-Python-logo-notext.svg.png")
  await self.send(file = file, embed=embed)

#await ctx.send('Working!', file=discord.File('upvote.png'))


def setup(bot):
  bot.add_cog(rpsinfo(bot))