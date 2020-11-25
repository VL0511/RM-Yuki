import random

from discord.ext import commands


class Betoneira(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mock_betoneira(self, ctx):
        phrase = ['Ainnn eu muto as pessoas e só sei xingar dizendo que é argumento😂',
                  'Ala o racistaKKKKKKKKKK😂',
                  'Eu sou uma vadia da buceta preta(͠≖ ͜ʖ͠≖)👌',
                  'No fim temos o cu preto😔',
                  'Cu de betoneira!\nNão chama ela assim cara ela é minha amiga!🐂',
                  'Ala o gadinho dela sksk']
        element = random.choice(phrase)
        await ctx.send(f"{ctx.author.mention}\n{element}")


def setup(client):
    client.add_cog(Betoneira(client))
