from datetime import datetime

import discord
from discord.ext import commands


class Yuki(commands.Cog):
    def __init__(self, client):
        self.client = client

    """
    COMANDOS PARA ZUAR O YUKI

    TOPICOS:
    PUXAR FOTOS DO YUKI.
    NUKE DE AUTO LIMPEZA EM CHAT.
    """

    @commands.command()
    async def info(self, ctx):
        file = discord.File("./img/sobre_yuki.jpeg", filename="sobre_yuki.jpeg")
        embed = discord.Embed(title="Sobre mim", colour=discord.Colour(0x00ff11),
                              description=f"{ctx.author.mention} sou apenas um bot para interação no discord"
                                          f", fui desenvolvivo em python. Contenho funções para interação e "
                                          f"limpar o chat!\nQue tal olhar meu código fonte no github?\n"
                                          f"url:https://github.com/VL0511/Yuki_bot\n artista da imagem: @ZenX#7728",
                              timestamp=datetime.utcnow())
        embed.set_image(url="attachment://sobre_yuki.jpeg")
        await ctx.send(file=file, embed=embed)

    @commands.command()
    async def yukizinho(self, ctx):
        await ctx.send(file=discord.File('./img/Yuki_Pensativo.jpeg'))

    @commands.command()
    async def yuki_raid(self, ctx):
        await ctx.send(file=discord.File('./img/yuki_vendo_o_raid.jpeg'))

    @commands.command()
    async def yuki_diva(self, ctx):
        await ctx.send(file=discord.File('./img/yuki_diva.jpeg'))

    @commands.command()
    async def yuki_gamer(self, ctx):
        await ctx.send(file=discord.File('./img/yuki_gamer.jpeg'))

    @commands.command()
    async def yuki_lindo(self, ctx):
        await ctx.send(file=discord.File('./img/yuki_lindo.jpeg'))

    @commands.command()
    async def yuki_maligno(self, ctx):
        await ctx.send(file=discord.File('./img/yuki_maligno.jpeg'))

    @commands.command()
    async def yuki_pensativo(self, ctx):
        await ctx.send(file=discord.File('./img/Yuki_Pensativo.jpeg'))

    @commands.command()
    async def yuki_profile(self, ctx):
        await ctx.send(file=discord.File('./img/yuki_profile.jpeg'))

    @commands.command()
    async def yuki_tia(self, ctx):
        await ctx.send(file=discord.File('./img/yuki_tia_zenx.jpeg'))


def setup(client):
    client.add_cog(Yuki(client))
