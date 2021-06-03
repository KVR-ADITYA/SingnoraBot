import discord
from discord.ext import commands
import random
import sys
import os
import random
from random import randint
class Gamba(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    #ctx.send
    @commands.command()
    async def fifty(self, ctx):
        x=randint(0,1)
        if x==1:
            await ctx.send(f"Yes,{ctx.message.author.mention} will win the fifty/fifty for the featured character!! <:hopium:849339347534741584>")
        else:
            await ctx.send(f'Im sorry,{ctx.message.author.mention} will lose the fifty/fifty for the featured character <:pepe_copium:847462168319885332>')
    
def setup(bot):
    bot.add_cog(Gamba(bot))

