__author__ = "Zury"

import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init___(self, client):
        self.client = client

    @commands.command()
    @commands.has_role(777699227831631892)
    async def nuked(self, ctx):
        canal = await ctx.guild.create_text_channel('CHAT')
        await ctx.send(f"{ctx.author.mention} criou o canal {canal}")

    @commands.command()
    @commands.has_role(777699227831631892)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason="Quebrou as diretrizes do servidor."):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Banned {user.name}!",
                            description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

    @commands.command()
    @commands.has_role(777699227831631892)
    async def limpar(self, ctx, amount=500):
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Chat limpo por: {ctx.author.mention}")

    @commands.command()
    @commands.has_role(777699227831631892)
    @commands.has_permissions(manage_messages=True, kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, razao=None):
        await user.kick(reason=razao)

    @commands.command()
    @commands.has_role(777699227831631892)
    @commands.has_permissions(manage_messages=True, ban_members=True)
    async def unban(self, ctx, *, Member):
        lista_banidos = await ctx.guild.bans()
        membro_name, membro_descrimantor = Member.split("#")

        for banido in lista_banidos:
            user = banido.user
            if (user.name, user.discriminator) == (membro_name, membro_descrimantor):
                await ctx.guild.unban(user)


def setup(client):
    client.add_cog(Admin(client))
