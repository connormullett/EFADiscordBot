#!/usr/bin/env python3.6

import discord
import asyncio

import sys
import requests

from datetime import datetime
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


@bot.command()
@asyncio.coroutine
def echo(message):
    message = yield from bot.say(f'echoing: {message}')
    if message:
        yield from bot.say('Test Successful')


@bot.command(name='joke')
@asyncio.coroutine
def dad_joke():
    headers = {'Accept': 'application/json'}
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers=headers).json()
    if response['status'] == 200:
        yield from bot.say(response['joke'])
    else:
        print(f"JOKE COMMAND FAILED AT {datetime.now()} "\
                "STATUS CODE {response['status']}")
        yield from bot.say('I couldn\'t come up with a joke because ' \
                'I\'m a bad bot :(')


bot.run('NTUwODgxMjU1MjYxMjA4NTg2.D1to-Q.cuVv2UdHZfqGmc5D35GBUROUtDI')

