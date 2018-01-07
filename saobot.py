## saobot - A bot for serving Sword Art Online content ##
# Written in discord.py rewrite + commands.ext by ry00001#3487

import discord
import json
from discord.ext import commands
import time
import glob
import os
import random
import math
import logs
from utils import perms

class Saobot(commands.Bot):
    def __init__(self, **kwargs):
        self.cfg = json.load(open('./config.json')) # configuration file
        self.prefix = self.cfg['prefix']
        super().__init__(command_prefix=commands.when_mentioned_or(*self.prefix), **kwargs) # may as well. - oh wait this is needed for it to actually work lol

    async def on_ready(self):
        self.do_cogs()
        print('saobot started, by ry00001#3487\n'
              f'logged in as {self.user} ({self.user.id})')

    def do_cogs(self):
        for i in glob.iglob('extensions/*.py'):
            logs.log(f'Loading extension {os.path.basename(i)}', logs.LogType.INFO)
            self.load_extension(f'extensions.{os.path.basename(i)[:-3]}')

bot = Saobot()

@bot.command() # setup basic stuff
async def ping(ctx):
    pingstrings = open('content/pings.txt').read().split('\n')
    before = time.monotonic()
    m = await ctx.send(random.choice(pingstrings))
    after = time.monotonic()
    ping = ((before - after) * 1000) * -1
    await m.edit(content=f'Pong! {math.floor(ping)}ms.')

@bot.command(aliases=['die', 'restart', 'disconnect'])
@perms.owner()
async def reboot(ctx):
    await ctx.send('Now restarting...')
    exit(0)

@bot.command(aliases=['rle'])
@perms.owner()
async def reload(ctx, ext:str):
    m = await ctx.send(f'Reloading {ext}...')
    try:
        ctx.bot.unload_extension(f'extensions.{ext}')
        ctx.bot.load_extension(f'extensions.{ext}')
    except Exception as err:
        return await m.edit(content=f'An error occurred.\n```\n{err}```')
    
    await m.edit(content='Reloaded.')

bot.run(bot.cfg['token'])
