__author__ = "Zury"

import os
import random 
import discord
import asyncio
from discord.ext import commands

class CaraCoroa(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cara_coroa(self, ctx):
        moeda = random.randint(1,2)
        if moeda == 1:
            #👑
            await ctx.send(f"{ctx.author.mention} tirou 👑")
        if moeda == 2:
            #👵
            await ctx.send(f"{ctx.author.mention} tirou 👵")


def setup(client):
    client.add_cog(CaraCoroa(client))