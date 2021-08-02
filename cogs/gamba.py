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
    @commands.command(brief="predicts your next 50-50 outcome. For gambling addicts")
    async def fifty(self, ctx):
        x=randint(0,1)
        copium_emoji = discord.utils.get(ctx.guild.emojis, name="pepe_copium")
        hopium_emoji=  discord.utils.get(ctx.guild.emojis, name="hopium")
        if x==1:
            await ctx.send(f"Yes,{ctx.message.author.mention} will win the fifty/fifty for the featured character!! {hopium_emoji}")
        else:
            await ctx.send(f'Im sorry,{ctx.message.author.mention} will lose the fifty/fifty for the featured character {copium_emoji}')
    
def setup(bot):
    bot.add_cog(Gamba(bot))

