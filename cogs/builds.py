import discord
from discord.ext import commands
import random
import sys
import os
from random import randint
import json

class Build(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(brief='Gives the build for the character,Please write only one character at a single time ')
    async def build(self,ctx,*args):
        b = open('./data/builds.json')
        data = json.load(b)
        yt_link=""
        sr_link=""
        for name in args:
            char_name=""
            char_name=char_name+name

        for i in data:
            if i['name'] == char_name.lower():
                yt_link=yt_link+i["yt_vid"]
                sr_link=sr_link+i["sr_link"]
    

        embed=discord.Embed(title=f"Heres your build for {char_name.upper()}",description=f"You find a video explaining the best build [here]({yt_link}) for more information about the character,You can join the subreddit [here]({sr_link})",colour=discord.Colour.blue())
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text="Build requested by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Build(bot))

