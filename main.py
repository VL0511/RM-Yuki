__author__ = 'Zury'

import os
from json import load
from random import choice

import discord
from discord.ext import tasks
from discord.ext.commands import Bot

client = Bot(command_prefix='y!', case_insensitive=True)
client.remove_command('help')


@client.event
async def on_ready():
    __version__ = '2.0.0'
    __url__ = 'https://github.com/VL0511/Yuki_bot'
    print('=====================================================')
    print(f'{client.user.name} Online.')
    print(f'Versão {__version__}')
    print(f'Autor: {__author__}')
    print(f'Total de servidores com o bot: {len(client.guilds)}')
    print('Nova atualização do bot RM Yuki!')
    print(f'Github: {__url__}')
    print('=====================================================')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Netflix'))


@tasks.loop(minutes=1)
async def ch_pr():
    statuses = ['Valorant', 'Digite y!help', 'Use o comando y!info para saber mais sobre mim!', 'Desenvolvedor: Zury']
    status = choice(statuses)
    await client.change_presence(activity=discord.Game(name=status))


@client.event
async def on_command_error(ctx, error):
    await ctx.send(error)


for file in os.listdir('cogs'):
    if file.endswith('.py'):
        name = file[:-3]
        client.load_extension(f'cogs.{name}')

for file in os.listdir('games'):
    if file.endswith('.py'):
        name = file[:-3]
        client.load_extension(f'games.{name}')

path = 'config.json'
with open(path) as file:
    json = load(file)

client.run(json['token'])
