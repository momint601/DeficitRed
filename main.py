import os
import discord
from discord.ext import commands


intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.slash_command(name="pranjal")
async def on_reddy(ctx):
    await ctx.respond("gay")


bot.run(os.environ["DISCORD_TOKEN"])
