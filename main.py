__author__ = "Zury"

import os
import discord
import asyncio
from json import load
from asyncio import sleep
from random import choice
from discord.ext import commands
from discord.ext.commands import AutoShardedBot, when_mentioned_or

client = discord.Client()
client = AutoShardedBot(command_prefix="y!", case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    __version__ = "2.0.0"
    __url__ = "https://github.com/VL0511/Yuki_bot"
    print("=====================================================")
    print(f"{client.user.name} Online.")
    print(f"Versão {__version__}")
    print(f"Autor: {__author__}")
    print(f"Total de servidores com o bot: {len(client.guilds)}")
    print("Nova atualização do bot RM Yuki!")
    print(f"Github: {__url__}")
    print("=====================================================")
    game = discord.Game("Desenvolvedor: Zury")
    await client.change_presence(status=discord.Status.idle, activity=game)
    await client.change_presence(activity=discord.Game(name=f"Estou em {len(client.guilds)} servidores | meu prefixo é y!help "))
    await client.change_presence(activity=discord.Streaming(name="Estou ao vivo na twitch!", url="https://twitch.tv/123"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Lofi"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Netflix"))

async def ch_pr():
    await client.wait_until_ready()
    statuses = ["Valorant", "Digite y!help", "Use o comando y!info para saber mais sobre mim!", "Desenvolvedor: Zury"]
    while not client.is_closed():
        status = choice(statuses)
        await client.change_presence(activity=discord.Game(name=status))
        await sleep(10)
client.loop.create_task(ch_pr())

@client.event 
async def on_command_error(ctx, error):
    await ctx.send(error)

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"cogs.{name}")

for file in os.listdir("games"):
    if file.endswith(".py"):
        name = file[:-3]
        client.load_extension(f"games.{name}")


path = "config.json"
with open(path) as file:
    json = load(file)

client.run(json['token'])
