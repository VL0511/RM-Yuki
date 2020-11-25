__author__ = "Zury"

import discord
import asyncio
from datetime import datetime
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        embed=discord.Embed(icon_url="https://artfiles.alphacoders.com/136/thumb-136777.jpg", title=":space_invader: Ajuda Yuki", description=f"Olá {ctx.author.mention} sou o mini-Yuki, tenho apenas 16 anos, sou apenas mais um bot do discord. Tenho funções para anti-sapm, interação e limpar chats.", color=0x00ff11)
        embed.add_field(name="📋 Veja nossa lista de comandos", value="Consulte nossas lista de comandos utilizando o comando 'cmd'.", inline=False)
        embed.add_field(name="💻Deseja ver informações sobre desenvolvedor?", value="Utilize o comando 'dev'.", inline=False)
        embed.add_field(name=":robot:Ver informações sobre o bot", value="Utilize o comando 'info'.", inline=False)
        embed.set_footer(text="Lista de comandos para interação do servidor caso tenha alguma duvida, chame um administrador para tirar suas dúvidas.")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if (f'<@{str(self.client.user.id)}>' == message.content) or (f'<@!{str(self.client.user.id)}>' == message.content):
                ctx = await self.client.get_context(message)
                await self.client.get_command('help')(ctx)

    @commands.command()
    async def cmd(self, ctx):
        embed = discord.Embed( title=":space_invader: Ajuda Yuki", colour=discord.Colour(0x00ff11), description=f"📋{ctx.author.mention}\nLista de comandos", timestamp=datetime.utcnow())
        embed.add_field(name="📄info", value="Ver informações sobre o bot", inline=False)
        embed.add_field(name="🚀dev", value="Ver informações de desenvolvedor", inline=False)
        embed.add_field(name="😂zuar", value="Zuar alguém", inline=False)
        embed.add_field(name="😂mock", value="Zuar alguém", inline=False)
        embed.add_field(name="📳zap", value="chamar alguem pro zap", inline=False)
        embed.add_field(name="📷fotos", value="Roubar a foto de algum mebro", inline=False)
        embed.add_field(name="💬palavra", value="printar uma palavra", inline=False)
        embed.add_field(name="📶lat", value="Ver o ping do bot", inline=False)
        embed.add_field(name="🎾ping", value="pong", inline=False)
        embed.add_field(name="🐒mock_betoneira", value="Zuar racistas", inline=False)
        embed.set_footer(text="Lista de comandos para interagir com membros.")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))