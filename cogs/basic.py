import discord
from discord.ext import commands
import random
import sys
import os

class Basic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Bot ping is: {round(self.bot.latency,3)*1000} ms')
    
    @commands.command()
    async def signora(self,ctx):
        await ctx.send('Signora will come home',file = discord.File('./data/images/signora.png'))
    @commands.command()
    async def kickme(self,ctx):
        await ctx.send(f'Signora kicked {ctx.message.author.mention}',file=discord.File('./data/gif/kick.gif'))
def setup(bot):
    bot.add_cog(Basic(bot))