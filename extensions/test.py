# test saobot cog

import discord
from discord.ext import commands

class Test:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def echo(self, ctx, *, args):
        await ctx.send(args)

def setup(bot):
    bot.add_cog(Test(bot))
