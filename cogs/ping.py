import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '.', intents = intents)

class ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot




@commands.command(name="pings")
async def pings(self, ctx: commands.Context):
    await ctx.channel.send("Ching Chong, im up")

def setup(bot):
  bot.add_cog(ping(bot))