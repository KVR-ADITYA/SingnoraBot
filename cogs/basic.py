import discord
from discord.ext import commands
import random
import sys
import os
from random import randint
import json
class Basic(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(brief="ping of the bot. If this doesn't work nothing will")
    async def ping(self, ctx):
        await ctx.send(f'Bot ping is: {round(self.bot.latency,3)*1000} ms')
    
    @commands.command(brief="signora")
    async def signora(self,ctx):
        await ctx.send('Signora will come home',file = discord.File('./data/images/signora.png'))
    
    @commands.command(brief="yes yes yes")
    async def kickme(self,ctx):   
        await ctx.send(f'Signora kicked {ctx.message.author.mention}',file=discord.File('./data/gif/kick.gif'))

    @commands.command(brief="yes yes yes for others")
    async def kick(self,ctx,user : discord.User):
        id=user.id
        await ctx.send('Signora kicked' + ' ' + user.mention ,file=discord.File('./data/gif/kick.gif'))

    @commands.command(brief="send others to horny jail ")
    async def bonk(self,ctx,user : discord.User):
        id=user.id
        await ctx.send('Signora bonk ' + ' ' + user.mention ,file=discord.File('./data/gif/zhongli-bonk.gif'))

    @commands.command(brief="mihoyo is trapping and you know it, and still fall for it")
    async def boobasword(self,ctx):   
        await ctx.send(f'{ctx.message.author.mention} get booba sword',file=discord.File('./data/gif/booba.gif'))
    
    @commands.command(brief="seriously something is wrong with you, get some help")
    async def roastme(self,ctx):
        f = open('./data/roasts.json')
        data = json.load(f)
        i=randint(0,len(data)-1)
        await ctx.send(data[i]['submission'])

    @commands.command(brief="barsibato drinking")
    async def drink(self, ctx):
        await ctx.send(f'{ctx.message.author.mention} drink with Venti',file=discord.File('./data/gif/ventiDrink.gif'))

    @commands.command(brief="raiden bullying dasyud")
    async def bully(self, ctx):
        dasyud_id = '435750497316765697'
        await ctx.send(f'<@{dasyud_id}> get bullied',file=discord.File('./data/gif/raidenRide.gif'))

def setup(bot):
    bot.add_cog(Basic(bot))
