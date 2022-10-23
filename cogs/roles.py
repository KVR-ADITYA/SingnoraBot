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

    @commands.command(brief="Change role using `$changerole <role_name>`")
    async def changerole(self, ctx, *args):
        member = ctx.message.author
        # if len(args) == 1:
        role_name = ''
        for i in range(len(args)):
            role_name += args[i]+' '
        role_name = role_name[:-1]
        if role_name == 'Mod' and "plum" not in member.name.lower():
            await ctx.send('Ask admin')
        else:
            role = None
            roles = ctx.guild.roles
            for rol in roles:
                if rol.name == role_name:
                    role = rol
            if role == None:
                print('changerole:', end=' ')
                print(role)
                await ctx.send('Enter a valid role name')
            else:
                print(role)
                await member.add_roles(role,reason='User prompt')
                await ctx.send('Changed role to: '+role.name)
        # else:
        #     await ctx.send('Enter one role')
    
    
    @commands.command(brief="Remomve role using `$rmrole <role_name>`")
    async def rmrole(self, ctx, *args):
        member = ctx.message.author
        # if len(args) == 1:
        role_name = ''
        for i in range(len(args)):
            role_name += args[i]+' '
        role_name = role_name[:-1]
        role = None
        roles = ctx.guild.roles
        for rol in roles:
            if rol.name == role_name:
                role = rol
        if role == None:
            print('rmrole', end=' ')
            print(role)
            print(role_name)
            await ctx.send('Enter a valid role name')
        else:
            await member.remove_roles(role,reason='User prompt')
            await ctx.send('Removed role: '+role.name)
        # else:
        #     await ctx.send('Enter one role')

    
def setup(bot):
    bot.add_cog(Roles(bot))

