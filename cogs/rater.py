from utils import rater as ra
import translations as tr
import discord
from discord.ext import commands
import random
import sys
import os
import random
from random import randint
import validators
import asyncio

class Rater(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    #ctx.send
    
    @commands.command()
    async def rate(self, ctx):
        url = None
        if ctx.message.attachments:
            url = ctx.message.attachments[0].url
        msg = ctx.message.content.split()[1:]
        options = []
        for word in msg:
            if not url and validators.url(word):
                url = word
                if '.' not in url.split('?')[0].split('/')[-1]:
                    if '?' in url:
                        url = '.png?'.join(url.split('?'))
                    else:
                        url += '.png'
            elif '=' in word:
                options.append(word)
            else:
                print(f'Error: Could not parse "{ctx.message.content}"')
                await send(ctx, msg=lang.err_parse)
                return
        
        if not url:
            await send(ctx, msg=lang.err_not_found)
            return
        
        lang = tr.en()
        print(ra.ocr(url,2,lang))
        suc, text = ra.ocr(url, 2, lang)
        print(text)
        if suc:
            level, results = ra.parse(text, lang)
            if level == None:
                level = 20
            score, main_score, main_weight, sub_score, sub_weight = ra.rate(level, results, {}, lang)
        
        if not results:
            await send(ctx, msg=lang.err_unknown)
            return

        if score <= 50:
            color = discord.Color.blue()
        elif score > 50 and score <= 75:
            color = discord.Color.purple()
        else:
            color = discord.Color.orange()

        msg = f'\n\n**{results[0][0]}: {results[0][1]}**'
        for result in results[1:]:
            msg += f'\n{result[0]}: {result[1]}'
        msg += f'\n\n**{lang.score}: {int(score * (main_weight + sub_weight))} ({score:.2f}%)**'
        msg += f'\n{lang.main_score}: {int(main_score * main_weight)} ({main_score:.2f}%)'
        msg += f'\n{lang.sub_score}: {int(sub_score * sub_weight)} ({sub_score:.2f}%)'
        msg += f'\n\n{lang.join}'

        embed = discord.Embed(color=color)
        embed.set_author(name=ctx.message.author.display_name, icon_url=ctx.message.author.avatar_url)
        embed.add_field(name=f'{lang.art_level}: {level}', value=msg)

        await send(ctx, embed=embed)

    
def setup(bot):
    bot.add_cog(Rater(bot))

