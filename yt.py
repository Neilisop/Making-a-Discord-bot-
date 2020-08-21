import discord
from discord.ext import commands 

client = commands.Bot(command_prefix="-")

@client.event
async def on_ready():
    print("Bot is online")
     
@client.command()
async def test(ctx):
    await ctx.send(f"Hi I am a bot {ctx.author} ") 

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
   

client.run("NzM5MDI2NjgzMzYwNzA2NjIx.XyUeOw.soY9jyCmhmoHKV6KMZSYLe-O3HU")