#!/usr/bin/env python3.6

import discord
import asyncio
import sys

from discord.ext import commands


desc = '''Discord Bot For Eleven Fifty Academy'''

bot = commands.Bot(command_prefix='~', description=desc)


@bot.event
@asyncio.coroutine
def on_ready():
    sys.stdout.write('logged in as\n')
    sys.stdout.write(f'{bot.user.name}\n')
    sys.stdout.write(f'{bot.user.id}\n')


@bot.command()
@asyncio.coroutine
def test():
    yield from bot.say('Test SUXful!')

bot.run('NTUwODgxMjU1MjYxMjA4NTg2.D1o3uQ.nVoWclXLH_czso1We9lJ3owA-As')

