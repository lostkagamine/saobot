import discord
from discord.ext import commands

def _owner(ctx):
    return ctx.author.id in ctx.bot.cfg['owners']

def owner():
    return commands.check(_owner)
