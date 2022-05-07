import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
```
Pug Commands:
!roll - roll captains and move them to the captains channel
!coinflip - chose a captain to first pick
!fatkids - move players to fat kids
!captains - view previous captains
!clearcaptains - clear captains for pugs
!end - end the pug and bring everyone to building game.

Music Commands:
!help - displays all the available commands
!p - <keywords> - finds the song on youtube and plays it in your current channel.
!q - displays the current music queue
!skip - skips the current song being played
!clear - stops the music and clears the queue
!leave - Disconnected the bot from the voice channel
!pause - pauses the current song being played or resumes if already paused
!resume - resumes playing the current song
```
"""

        self.text_channel_text = []
    
    
    @commands.command(name="help", help="Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)