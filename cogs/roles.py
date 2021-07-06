import discord
from discord.ext import commands
import random
import sys
import os
import random
from random import randint

class Roles(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    #ctx.send

    @commands.command()
    async def changerole(self, ctx, *args):
        member = ctx.message.author
        if len(args) == 1:
            role_name = args[0]
            if role_name == 'Mod':
                await ctx.send('Ask admin')
            else:
                role = None
                roles = ctx.guild.roles
                for rol in roles:
                    if rol.name == role_name:
                        role = rol
                if role == None:
                    print(role)
                    await ctx.send('Enter a valid role name')
                else:
                    print(role)
                    await member.add_roles(role,reason='User prompt')
        else:
            await ctx.send('Enter one role')
    
    
    @commands.command()
    async def rmrole(self, ctx, *args):
        member = ctx.message.author
        if len(args) == 1:
            role_name = args[0]
            role = None
            roles = ctx.guild.roles
            for rol in roles:
                if rol.name == role_name:
                    role = rol
            if role == None:
                await ctx.send('Enter a valid role name')
            else:
                await member.remove_roles(role,reason='User prompt')
        else:
            await ctx.send('Enter one role')

    
def setup(bot):
    bot.add_cog(Roles(bot))

