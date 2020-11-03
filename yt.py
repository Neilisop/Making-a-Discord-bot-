import discord
from discord.ext import commands 

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print("Bot is online")
  #
#
#
#
#
#  YOU CAN CUSOTMISE THIS BOT
#
#
#
#

#this will not ping the user and just say the name
@client.command()
async def test(ctx):
    await ctx.send(f"Hi I am a bot {ctx.author} ") 
#this will ping the user
@client.command()
async def test2(ctx):
    await ctx.send(f"Hi I am a bot {ctx.author.mention} ") 

@client.command()
async def embed(ctx):
    embed = discord.Embed(title="tittle", description="Hello This is a embed")
    embed.add_field(name="This is a Field", value="this is value", inline=False)
    embed.add_field(name="This is a Field", value="this is value", inline=False)
    embed.add_field(name="This is a Field", value="this is value", inline=False)
    embed.add_field(name="This is a Field", value="this is value", inline=False)
    embed.add_field(name="This is a Field", value="this is value", inline=False)
    embed.add_field(name="This is a Field", value="this is value", inline=False)
    embed.add_field(name="This is a Field", value="this is value", inline=False)
    embed.add_field(name="This is a Field", value="this is value", inline=False)
    embed.set_footer(text="this is a footer")
    await ctx.send(embed=embed)
   
# replace "your bot token" with the token
client.run("your bot token")
