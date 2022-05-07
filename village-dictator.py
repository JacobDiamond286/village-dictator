import os
import discord
import random
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
first_twelve = []
fat_kids = []
captains_list = []

client = commands.Bot(command_prefix = "!", intents=intents)


@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')
    

@client.command()
async def roll(ctx):
    captains = client.get_channel(747231732671053834)
    building = client.get_channel(913316240972455936)
    fat = client.get_channel(775990913817640960)
    if len(building.members) < 12:
        await ctx.send("Not enough for pugs")
        return
    else:
        for i in range(2):
            captain = random.choice(building.members)
            await ctx.send(f'<@{captain.id}>')
            await captain.move_to(captains)
            captains_list.append(captain.name)
    if len(fat_kids) == 0:
        return
    else:
        output = ''
        for member in fat.members:
            output += f'{member.name}, '
        await ctx.send(f"{output}= fat")


@client.command()
async def fatkids(ctx):
    fat_kids.clear()
    building = client.get_channel(913316240972455936)
    fat = client.get_channel(775990913817640960)
    for member in building.members:
        fat_kids.append(member)
        await member.move_to(fat)
    output = ""
    if len(fat_kids) > 0:
        for member in fat.members:
            output += f'{member.name}, '
        await ctx.send(f"{output}= fat")
    else:
        await ctx.send("There are no obese children")

@client.command()
async def captains(ctx):
    output = ''
    if len(captains_list) > 0:
        for member in captains_list:
            output += f'{member}, '
        await ctx.send(f"{output}= safe from captains!")
    else:
        await ctx.send("There haven't been any captains.")

@client.command()
async def clearcaptains(ctx):
    captains_list.clear()
    if len(captains_list) > 0:
        await ctx.send("Captains have been cleared!")
    else:
        await ctx.send("No captains to clear")

@client.command()
async def coinflip(ctx):
    captains = client.get_channel(972191189853933583)
    winner = random.choice(captains.members)
    await ctx.send(f"{winner} is the winner and gets to pick first!")

@client.command()
async def end(ctx):
    blue = client.get_channel(746593787131985951)
    red = client.get_channel(929960822229327892)
    building = client.get_channel(913316240972455936)
    for member in blue.members:
        await member.move_to(building)
    for member in red.members:
        await member.move_to(building)


client.run(os.environ['DISCORD_TOKEN'])