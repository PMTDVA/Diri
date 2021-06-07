import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='Diri ')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('DVA Server'))
    print('Bot is ready.')

@client.command()
async def Hi(ctx):
    await ctx.send('Hi!')

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def mute(ctx, member : discord.Member, *, reason=None):
    await member.mute(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')


    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

@client.command()
async def clear10(ctx, amount=10):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clear100(ctx, amount=100):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clearall(ctx, amount=1000):
    await ctx.channel.purge(limit=amount)
    
@client.command(aliases=['8ball', 'test'])
async def tell(ctx, *, question):
    responses = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

client.run('your token here')
