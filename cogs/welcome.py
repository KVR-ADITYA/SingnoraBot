import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True

class Welcome(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(member)
        guild= self.bot.get_guild(769070407587463168)
        await member.send(f"Hey thanks for joining **{guild.name}**, Make sure to introduce yourself, Thats it , You can now delete the message")
        channel= discord.utils.get(member.guild.channels,id=848125899119656990)
        if guild:
            print("guild ok")
        else:
            print("guild not found")

        if channel is not None:
            await channel.send(f"Welcome to **{guild.name}** {member.mention}!:Head over to <#769070407587463171> to say hi ")
        else:
            print("id channel wrong")
        

    # @Cog.listener()
    # async def on_member_leave(self,member):
    #     pass

def setup(bot):
    bot.add_cog(Welcome(bot))        

