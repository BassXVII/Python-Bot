import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '.', intents = intents)

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




@bot.command()
async def pings(self):
    await self.channel.send("Ching Chong, im up")

def setup(bot):
  bot.add_cog(ping(bot))