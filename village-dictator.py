import discord
import os
import random
from discord.ext import commands
import time
from keep_alive import keep_alive
from music_cog import music_cog
from help_cog import help_cog
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents)

client.remove_command("help")

client.add_cog(music_cog(client))
client.add_cog(help_cog(client))


first_twelve = []
fat_kids = []
captains_list = []
coin = ['Heads', 'Tails']


@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}.')

    

@client.command()
async def roll(ctx, a: int):
    captains = client.get_channel(747231732671053834)
    building = client.get_channel(913316240972455936)
    if len(building.members) < 2:
        await ctx.send("Not enough for pugs")
        return
    else:
        for i in range(a):
            captain = random.choice(building.members)
            if captain.name in captains_list:
              await ctx.send(f'{captain.name} has already been captain.')
            else: 
              await ctx.send(f'<@{captain.id}>')
              await captain.move_to(captains)
              captains_list.append(captain.name)


@client.command()
async def fat(ctx):
    fat_kids.clear()
    building = client.get_channel(913316240972455936)
    fat = client.get_channel(775990913817640960)
    fat_text = client.get_channel(771978568196292608)
    for member in building.members:
        fat_kids.append(member.name)
        await member.move_to(fat)
    output = ""
    if len(fat_kids) > 0:
        for member in fat.members:
            output += f'{member.name}, '
        await fat_text.send(f"{output}= fat")
    else:
        await ctx.send("There are no obese children")

@client.command()
async def showfat(ctx):
    fat_text = client.get_channel(771978568196292608)
    await fat_text.send(fat_kids)

@client.command()
async def showcap(ctx):
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
    if len(captains_list) >= 0:
        await ctx.send("Captains have been cleared!")

@client.command()
async def coinflip(ctx):
    captains = client.get_channel(771978568196292608)
    winner = random.choice(coin)
    await captains.send(f"{winner} is the winner and gets to pick first!")

@client.command()
async def end(ctx):
    blue = client.get_channel(746593787131985951)
    red = client.get_channel(929960822229327892)
    building = client.get_channel(913316240972455936)
    for member in blue.members:
        await member.move_to(building)
        time.sleep(.4)
    for member in red.members:
        time.sleep(.4)
        await member.move_to(building)

keep_alive()
client.run(os.environ['DISCORD_TOKEN'])