import discord
from discord.ext import commands
import random
import sys
import os
from random import randint
import json

class Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def binfo(self,ctx,char_name):

        await ctx.send(f'{ctx.message.author.mention} here is the build you requested ',file=discord.File(f'./data/infographic_images/{char_name.lower()}.jpg'))
    
    @commands.command()
    async def rinfo(self,ctx,char_name):           
        await ctx.send(f'{ctx.message.author.mention} here is the resources you requested ',file=discord.File(f'./data/resource_infographic_images/{char_name.lower()}.jpg'))

def setup(bot):
    bot.add_cog(Info(bot))

#xiangling