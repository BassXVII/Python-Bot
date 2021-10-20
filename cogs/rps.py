import discord

from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '.', intents = intents)


RPS = ["Rock", "Paper", "Scissors"]
Player_input = ["Rock", "rock", "Paper", "paper", "Scissors", "scissors"]

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@bot.command()
async def ping(self, member):
    await self.send(f"Pinging, {self.author.mention}")

def setup(bot):
  bot.add_cog(MyCog(bot))