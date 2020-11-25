__author__ = "Zury"

import random

import discord
from discord.ext import commands


class Comando(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mock(self, ctx):
        list_mock = ['Ala o cearense KSKSKSK',
                     'VAI CURITIÃN KSKSKSK',
                     'NÃO FALA MAL DO MEU FRAMENGU :(',
                     'Sou filho de pedreiro e te enchi a martelada',
                     'Eu sou filho do mato, eu venho da roça, o meu pai foi vaqueiro, a minha rola é grossa',
                     'O mais brabo é o Zury',
                     'AVENGERS!\nEu tenho micro pênis',
                     'Sua mãe é uma vaca',
                     'AIINN NOBRU APELÃO',
                     'Eu tenho um pênis mediano',
                     'Eu sou jojofag',
                     'Eaw Maicon Jackson',
                     'EU QUERO DAR O CU!',
                     'Caiu na vila o peixe fuzila']
        random.shuffle(list_mock)
        element = random.choice(list_mock)
        await ctx.send(f"Zoado por{ctx.author.mention}\n{element}")

    @commands.command()
    async def dev(self, ctx):
        embed = discord.Embed(title="RM Yuki", url="https://images4.alphacoders.com/909/thumb-1920-909912.png",
                              description=f"Olá {ctx.author.name} sou o Zury, sou desenvolvedor de bots para discord"
                                          f". Tenho um servidor onde comercializo bots, caso tenha interesse, "
                                          f"entre em contato.",
                              color=0x11ff00)
        embed.set_author(name="Zury ", url="https://giffiles.alphacoders.com/209/209699.gif",
                         icon_url="https://giffiles.alphacoders.com/297/2970.gif")
        embed.set_thumbnail(
            url="https://s2.glbimg.com/meFVMhlLxjc6Oalv6uymgt7309c=/1200x/smart/filters:cover():strip_icc()/"
                "i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2020/h/w/Abq4oBS"
                "ySsO0xmGnkDlg/discord.jpg")
        embed.add_field(name="Meu github:", value="https://github.com/VL0511", inline=True)
        embed.add_field(name="Loja do desenvolvedor: ", value="https://discord.io/Store-Zury", inline=True)
        embed.add_field(name="Discord do criador: ", value="Sou o Zury#6984", inline=True)
        embed.set_footer(text="Entre em contato comigo caso ache algum erro.",
                         icon_url="https://giffiles.alphacoders.com/209/209699.gif")
        await ctx.send(embed=embed)

    @commands.command()
    async def zuar(self, ctx, *, usuario: discord.Member = None):
        if usuario is None:
            await ctx.send("y!zuar + @usuario")
            return
        zua = f"Nome : {usuario.name}\n"

        await ctx.send(zua)

    @commands.command()
    async def zap(self, ctx, *, usuario: discord.Member = None):
        if usuario is None:
            await ctx.send("$zap + @usuario")
            return
        pm = f"Chama no zap bb @{usuario.name}"

        await ctx.send(pm)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(description="Pong", color=0x11ff00)
        embed.set_author(name="Ping!")

        await ctx.send(embed=embed)

    @commands.command()
    async def lat(self, ctx):
        embed = discord.Embed(description=f"O ping do ping é: {self.client.latency} ms", color=0x11ff00)
        embed.set_author(name="Pingo do bot")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def anuncio(self, ctx):
        await ctx.send("NOVA ATUALIZAÇÃO RM YUKI!! @everyone")
        embed = discord.Embed(title=":space_invader:Nova Atualização RM Yuki!", colour=discord.Colour(0x00ff11),
                              description="Nova atualização RM Yuki!\nConfira agora o que veio de novo e fique por dentro!")
        embed.add_field(name="Info", value="Ver informações sobre desenvolvedor e artista das imagens.", inline=False)
        embed.add_field(name="Retirada de fotos da betoneira",
                        value="Foi retirada fotos da betoneira para não expor sua imagem.", inline=False)
        embed.add_field(name="mock",
                        value="Comando mock tem como função gerar um texto ou palavra aleatória para zuar um membro",
                        inline=False)
        embed.add_field(name="Status", value="Novos status rodando no perfil do bot.", inline=False)
        embed.add_field(name="Game", value="Adiciono o jogo cara ou coroa.", inline=False)
        channel = self.client.get_channel(781006776866832385)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def palavra(self, ctx, *, palavra=None):
        if palavra is None:
            await ctx.send("$palavra + palavra")
            return
        embed = discord.Embed(description=f"Você disse: {palavra}")
        embed.set_author(name="Sua palavra")
        await ctx.send(embed=embed)

    @commands.command()
    async def fotos(self, ctx, *, usuario: discord.Member = None):
        if usuario is None:
            await ctx.send("$fotos + @usuario")
            return
        string = f"Nome : {usuario.name}\nId : {usuario.id}\nAvatar : {usuario.avatar_url}"

        await ctx.send(string)


def setup(client):
    client.add_cog(Comando(client))
