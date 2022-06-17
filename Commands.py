#importing
from tkinter.ttk import Style
import discord
import random
from discord.ui import Button
from discord.ext import commands
intents = discord.Intents.all()

bot = commands.Bot(command_prefix = "-", help_command = None)
bot1 = discord.Client(intents = intents)

#Commands


@bot.command()
async def coinflip(ctx):
    num = random.randint(1,2)
    if num == 1:
        await ctx.send("Heads")
    else:
        await ctx.send("Tails")

#RPS
@bot.command()
async def rps(ctx, hand):
    hands = ["rock", "paper", "scissors"]
    botHand = random.choice(hands)
    await ctx.send(botHand)
    if hand == botHand:
        await ctx.send("Its a Draw! Shall we play again?")
    elif hand == "rock":
        if botHand == "paper":
            await ctx.send("HAH I WON https://tenor.com/view/dancing-cat-dancing-kitten-60fps-boogie-cat-gif-24303276")
        else:
            await ctx.send("DUDE MY INTERNET WAS LAGGING I SHOULD HAVE WON THA- i mean yay you won haha")

    elif hand == "paper":
        if botHand == "rock":
            await ctx.send("I FRICKING HATE YOU SO MUC- you won https://tenor.com/view/i-hate-you-anakin-star-wars-gif-10358450")
        else:
            await ctx.send("WHEEE I WONNN https://tenor.com/view/dance-dog-dancing-pet-boy-123asd-gif-18609627")

    elif hand == "scissors":
        if botHand == "paper":
            await ctx.send("yay you won '*how much longer do i have to do this again?*'")
        else:
            await ctx.send("SUCK IT LOSER I WON")

#Help Embed
@bot.command(aliases = ["about", "what"])
async def help(ctx):
    helpEmbed = discord.Embed(title = "Commands", description = "These are the commands I know so far :D", color = discord.Color.dark_orange())
    helpEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    helpEmbed.add_field(name = "Rock Paper Scissors [-rps]", value = "This command allows you to play rock paper scissors against the bot! How to use the command: `-rps value` exchange the value with **rock paper or scissors**!", inline = False)
    helpEmbed.add_field(name = "Coinflip [-coinflip]", value = "This command lets you flip a coin", inline = False)
    helpEmbed.add_field(name = "Custom commands [-custom]", value = "This command show the list of custom commands for friends!")
    helpEmbed.add_field(name = "IP Help [-serverIp]", value = "This tells you what servers we have and their ips!", inline = False)
    await ctx.send(embed = helpEmbed)

#Cutsom Embed
@bot.command(aliases = ["friend"])
async def custom(ctx):
    customEmbed = discord.Embed(title = "Commands", description = "These are the commands I know so far :D", color = discord.Color.blurple())
    customEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg") 
    customEmbed.add_field(name = "City's Custom Command [-city]", value = "This is a custom command for <@701981194971119690>! Only <@701981194971119690 can use it!", inline = False)
    customEmbed.add_field(name = "Marchly's Custom Command [-march]", value = "This is a custom command for <@706876255064293416>! Only <@706876255064293416> can use it!", inline = False)
    customEmbed.add_field(name = "Ghost's Custom Command [-ghost]", value = "This is a custom command for <@606870679543087154>! Only <@606870679543087154> can use it!", inline = False)
    customEmbed.add_field(name = "Shiv's Custom Command [-shiv]", value = "This is a custom command for <@518744853832794112>! Only <@518744853832794112> can use it!", inline = False)
    customEmbed.add_field(name = "Stellar's Custom Command [-stellar]", value = "This is a custom command for <@820304171764416582>! Only <@820304171764416582> can use it!", inline = False)
    customEmbed.add_field(name = "F O O T [-foot]", value = "F O O T")
    customEmbed.add_field(name = "El Pepe's custom command [-elpepe]", value = "This is a custom command for <@7852834698300620820>! Only <@7852834698300620820> can use it")
    await ctx.send(embed = customEmbed)

#Edit command

@bot.group()
async def edit(ctx):
    pass

@edit.command()
async def servername(ctx,*, input):
    await ctx.guild.edit(name = input)
    await ctx.send("Success! The Guild name is now " + "**" + input + "**")

@edit.command()
async def createText(ctx,*, input):
    await ctx.guild.create_text_channel(name = input)
    await ctx.send("Success! A new Text channel called " + "**" + input + "** has been created!")

@edit.command()
async def createVoice(ctx,*, input):
    await ctx.guild.create_voice_channel(name = input)
    await ctx.send("Success! A new Voice channel called " + "**" + input + "** has been created!")

@edit.command()
async def createRole(ctx,*, input):
    await ctx.guild.create_role(name = input)
    await ctx.send("Success! A new Role called " + "**" + input + "** has been created!")

#Ip embed

@bot.command(aliases = ["ip", "server", "serverip"])
async def serverIp(ctx):
    ipEmbed = discord.Embed(title = "Server IPs", description = "We currently have 2 servers!", color = discord.Color.green())
    ipEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    ipEmbed.add_field(name = "1.18.2 Modded SMP", value = "**IP: StarCraftReal.aternos.me:27226**. This is an smp with a lot of mods, including Origins, Gravestones, Waystones and more! Check <#971649825630203945> for the modlist! **Cracked is enabled on this server!**", inline = False)
    ipEmbed.add_field(name = "1.19 Vanilla SMP", value = "**IP: OMGLETSGOOOOO.aternos.me**, This is a vanilla 1.19 server! **Cracked is not enabled on this server**", inline = False)
    ipEmbed.set_footer(text = "Ask us if you want any more smps!")
    await ctx.send(embed = ipEmbed)
#custom commands

@bot.command()
async def foot(ctx):
    await ctx.send("https://i.kym-cdn.com/photos/images/original/001/526/968/043.jpg")

@bot.command()
async def shiv(ctx):
    await ctx.send("https://tenor.com/view/kidnapping-roblox-roblox-kidnapping-lol-uwu-gif-24871536")

@bot.command()
async def stellar(ctx):
    await ctx.send("https://tenor.com/view/among-us-gif-24283650")
    await ctx.send("https://tenor.com/view/sushichaeng-among-us-among-us-meme-shocked-confused-gif-22454610")

@bot.command()
async def elpepe(ctx):
    await ctx.send("https://tenor.com/view/stare-staring-cat-gif-20275090")

@bot.command()
async def march(ctx):
    await ctx.send("> 'no' - Marchly , 2022")

@bot.command()
async def ghost(ctx):
    await ctx.send("GHOST IS A LITTLE SUSSY BAKA AMOGUS UWU https://tenor.com/view/oops-haha-epic-fail-escalator-sliding-gif-15280329")

@bot.command()
async def city(ctx):
    await ctx.send("city is sus AMOGUS https://c.tenor.com/o9bbZuiIt0AAAAAd/amogus.gif")
    print("yes")

#Events

@bot1.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "hello":
            await msg.channel.send("Hello " + username)

@bot.event
async def on_ready():
    activity  = discord.Game(name="!help")
    await bot.change_presence(activity=discord.Game(name="amogus | listening to -help"))
    print("Bot is ready!")

@bot1.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name 
    dmchannel = await member.create_dm()
    await dmchannel.send(f"Welcome to {guildname}! Have Fun!")

@bot1.event 
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    member = payload.member
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    if emoji == "poggers" and message_id == 985404494642831360:
        role = discord.utils.get(guild.roles, name = "Minecraft")
        await member.add_roles(role)
      
    if emoji == "amogus" and message_id == 985404494642831360:
        role = discord.utils.get(guild.roles, name = "Valorant")
        await member.add_roles(role)
@bot1.event
async def on_raw_reaction_remove(payload):
    user_id = payload.user_id
    emoji = payload.emoji.name
    message_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    member = guild.get_member(user_id)
    if emoji == "poggers" and message_id == 985404494642831360:
        role = discord.utils.get(guild.roles, name = "Minecraft")
        await member.remove_roles(role)
      
    if emoji == "amogus" and message_id == 985404494642831360:
        role = discord.utils.get(guild.roles, name = "Valorant")
        await member.remove_roles(role)
        
from config import TOKEN       
bot.run(TOKEN)