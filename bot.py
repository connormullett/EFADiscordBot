#!/usr/bin/env python3.6

import discord
import asyncio

import sys, os
import requests

from datetime import datetime
from discord.ext import commands
from clint.textui import puts, colored


desc = '''Discord Bot For Eleven Fifty Academy'''
bot = commands.Bot(command_prefix='~', description=desc)


@bot.event
@asyncio.coroutine
def on_ready():
    sys.stdout.write('logged in as\n')
    sys.stdout.write(f'{bot.user.name}\n')
    sys.stdout.write(f'{bot.user.id}\n')


@bot.command(help='Run a test on the server')
@asyncio.coroutine
def test():
    yield from bot.say('Test SUXful!')


@bot.command(help='Repeats message sent with command, used for testing messages to bot')
@asyncio.coroutine
def echo(*args):
    print(args)
    if not args:
        yield from bot.say('ERROR: No message supplied')
    for message in args:
        message = yield from bot.say(f'echoing: {message}')
        if message:
            yield from bot.say('Test Successful')


@bot.command(name='joke', help='print a dad joke')
@asyncio.coroutine
def dad_joke():
    puts('[%s] - Dad Joke requested \n' % (datetime.now()))
    headers = {'Accept': 'application/json'}
    url = 'https://icanhazdadjoke.com/'
    response = requests.get(url, headers=headers).json()
    if response['status'] == 200:
        puts(colored.green('[%s] - Dad joke sent to server' % (datetime.now())))
        yield from bot.say(response['joke'])
    else:
        puts(colored.red('[%s] - ERROR RETRIEVING DAD JOKE '
                         'STATUS CODE %') % (datetime.now(), response.status_code))
        yield from bot.say('I couldn\'t come up with a joke because ' \
                'I\'m a bad bot :(')


@bot.command(name='dog', help='send a random dog image')
@asyncio.coroutine
def dog():
    puts('[%s] - Dog photo requested' % (datetime.now()))
    response = requests.get('https://random.dog/woof.json').json()
    dog_file = response.get('url', None)
    if not dog_file:
        yield from bot.say('I couldn\'t find a dog image cause im a bad bot :(')
        puts(colored.red('[%s] - Failed to retrieve dog image'))
    else:
        yield from bot.say(dog_file)
        puts(colored.green('[%s] - File sent Succesffully'))


bot.run(os.getenv('DISCORD'))

