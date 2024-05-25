import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)




@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('imagrs'))
    with open(f'imagrs/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def ecology(ctx):
    img_name = random.choice(os.listdir('ecology'))
    with open(f'ecology/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)





bot.run("")




