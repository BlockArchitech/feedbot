
import os
import discord
import time
import feedparser
from discord.ext import commands

client=commands.Bot(command_prefix="feed.")

newsFeed = feedparser.parse("https://blogs.nasa.gov/stationreport/feed/")
newsFeed2 = feedparser.parse("http://feeds.foxnews.com/foxnews/latest")
entry = newsFeed.entries[1]
entry2 = newsFeed2.entries[1]

#Ready Bot
@client.event
async def on_ready():
  print(f"[SYSTEM] FeedBot - Built on blockybot.")
  time.wait(4)
  print(f"[SYSTEM] FeedBot is ready!")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="feed.assist"))


@client.command()
async def read(ctx, *, feed):
    if feed == 'nasa':
        embedVar = discord.Embed(title=f"FeedBot - NASA ISS blog", description=f"article publish date/time: {entry.published}", color=0x7289DA)
        embedVar.add_field(name=f"{entry.title}", value=f"{entry.summary}", inline=False)
        await ctx.send(embed=embedVar)

    else:
        if feed == 'foxnews':
            embedVar = discord.Embed(title=f"FeedBot - Fox News Output", description=f"article publish date/time: {entry2.published}", color=0x7289DA)
            embedVar.add_field(name=f"{entry2.title}", value=f"{entry2.summary}", inline=False)
            await ctx.send(embed=embedVar)
        else:
            entryURLfeed = feedparser.parse(feed)
            entryURL = entryURLfeed.entries[1]
            embedVar = discord.Embed(title=f"FeedBot - RSS URL Output", description=f"article publish date/time: {entryURL.published}", color=0x7289DA)
            embedVar.add_field(name=f"{entryURL.title}", value=f"{entryURL.summary}", inline=False)
            await ctx.send(embed=embedVar)

@read.error
async def read_error(ctx, error):
    embedVar = discord.Embed(title=f"Read Error", description=f"Could not parse the feed! Is the URL or spelling correct? Want a feed that isn't natively supported? Request it! https://forms.gle/GPtZz8UVeHACzHgQ8", color=0xf55742)
    await ctx.send(embed=embedVar)







@client.command()
async def assist(ctx):
    embed = discord.Embed(title="Help", description=f"I have one command. Here is how to use it.", color=0x99AAB5)
    embed.add_field(name=f"`feed.read <feed>`", value=f"You can put an active and supported feed here. You can enter a feed URL or use one of the feeds we give. They are `nasa` and `foxnews`", inline=False)
    await ctx.send(embed=embed)

client.run('token')
