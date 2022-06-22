# importing
from code import interact
from profile import run
from ssl import Options
from tkinter.ttk import Style
import discord
import random
from discord.ui import Button, View
from discord.ext import commands
from discord.commands import Option

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="-", help_command=None, intents=discord.Intents.all())

# Commands


@bot.command()
async def coinflip(ctx):
    num = random.randint(1, 2)
    if num == 1:
        await ctx.send("Heads")
    else:
        await ctx.send("Tails")


@bot.slash_command(description="Flip a coin")
async def coinflip(ctx):
    num = random.randint(1, 2)
    if num == 1:
        await ctx.respond("Heads")
    else:
        await ctx.respond("Tails")


# RPS
@bot.command()
async def rps(ctx, hand):
    hands = ["rock", "paper", "scissors"]
    botHand = random.choice(hands)
    await ctx.send(botHand)
    if hand == botHand:
        await ctx.send("Its a Draw! Shall we play again?")
    elif hand == "rock":
        if botHand == "paper":
            await ctx.send(
                "HAH I WON https://tenor.com/view/dancing-cat-dancing-kitten-60fps-boogie-cat-gif-24303276"
            )
        else:
            await ctx.send(
                "DUDE MY INTERNET WAS LAGGING I SHOULD HAVE WON THA- i mean yay you won haha"
            )

    elif hand == "paper":
        if botHand == "rock":
            await ctx.send(
                "I FRICKING HATE YOU SO MUC- you won https://tenor.com/view/i-hate-you-anakin-star-wars-gif-10358450"
            )
        else:
            await ctx.send(
                "WHEEE I WONNN https://tenor.com/view/dance-dog-dancing-pet-boy-123asd-gif-18609627"
            )

    elif hand == "scissors":
        if botHand == "paper":
            await ctx.send(
                "yay you won '*how much longer do i have to do this again?*'"
            )
        else:
            await ctx.send("SUCK IT LOSER I WON")

# Help Embed
@bot.command(aliases=["about", "what"])
async def help(ctx):
    helpEmbed = discord.Embed(
        title="Commands",
        description="These are the commands I know so far :D",
        color=discord.Color.dark_orange(),
    )
    helpEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    helpEmbed.add_field(
        name="Rock Paper Scissors [-rps]",
        value="This command allows you to play rock paper scissors against the bot! How to use the command: `-rps value` exchange the value with **rock paper or scissors**!",
        inline=False,
    )
    helpEmbed.add_field(
        name="Coinflip [-coinflip]",
        value="This command lets you flip a coin",
        inline=False,
    )
    helpEmbed.add_field(
        name="Custom commands [-custom]",
        value="This command show the list of custom commands for friends!",
    )
    helpEmbed.add_field(
        name="IP Help [-serverIp]",
        value="This tells you what servers we have and their ips!",
        inline=False,
    )
    await ctx.send(embed=helpEmbed)


@bot.slash_command(
    aliases=["about", "what"], description="These are the commands I know so far :D"
)
async def help(ctx):
    helpEmbed = discord.Embed(
        title="Commands",
        description="These are the commands I know so far :D",
        color=discord.Color.dark_orange(),
    )
    helpEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    helpEmbed.add_field(
        name="Rock Paper Scissors [-rps]",
        value="This command allows you to play rock paper scissors against the bot! How to use the command: `-rps value` exchange the value with **rock paper or scissors**!",
        inline=False,
    )
    helpEmbed.add_field(
        name="Coinflip [-coinflip]",
        value="This command lets you flip a coin",
        inline=False,
    )
    helpEmbed.add_field(
        name="Custom commands [-custom]",
        value="This command show the list of custom commands for friends!",
    )
    helpEmbed.add_field(
        name="IP Help [-serverIp]",
        value="This tells you what servers we have and their ips!",
        inline=False,
    )
    await ctx.respond(embed=helpEmbed)


# Cutsom Embed
@bot.command(aliases=["friend"])
async def custom(ctx):
    customEmbed = discord.Embed(
        title="Commands",
        description="These are the commands I know so far :D",
        color=discord.Color.blurple(),
    )
    customEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    customEmbed.add_field(
        name="City's Custom Command [-city]",
        value="This is a custom command for <@701981194971119690>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Marchly's Custom Command [-march]",
        value="This is a custom command for <@706876255064293416>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Ghost's Custom Command [-ghost]",
        value="This is a custom command for <@606870679543087154>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Shiv's Custom Command [-shiv]",
        value="This is a custom command for <@518744853832794112>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Stellar's Custom Command [-stellar]",
        value="This is a custom command for <@820304171764416582>! Try it to see what is does!!",
        inline=False,
    )
    customEmbed.add_field(name="F O O T [-foot]", value="F O O T", inline=False)
    customEmbed.add_field(
        name="El Pepe's custom command [-elpepe]",
        value="This is a custom command for <@852834698300620820>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="ACE's custom command [-ace, /ace]",
        value="This is a custom command for <@886078239833980958>! Try it to see what is does!",
        inline=False,
    )
    await ctx.send(embed=customEmbed)


@bot.slash_command(description="This shows all my friend's commands!")
async def friends(ctx):
    customEmbed = discord.Embed(
        title="Commands",
        description="These are the commands I know so far :D",
        color=discord.Color.blurple(),
    )
    customEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    customEmbed.add_field(
        name="City's Custom Command [-city]",
        value="This is a custom command for <@701981194971119690>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Marchly's Custom Command [-march]",
        value="This is a custom command for <@706876255064293416>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Ghost's Custom Command [-ghost]",
        value="This is a custom command for <@606870679543087154>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Shiv's Custom Command [-shiv]",
        value="This is a custom command for <@518744853832794112>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Stellar's Custom Command [-stellar]",
        value="This is a custom command for <@820304171764416582>! Try it to see what is does!!",
        inline=False,
    )
    customEmbed.add_field(name="F O O T [-foot]", value="F O O T", inline=False)
    customEmbed.add_field(
        name="El Pepe's custom command [-elpepe]",
        value="This is a custom command for <@852834698300620820>! Try it to see what is does! can use it",
        inline=False,
    )
    customEmbed.add_field(
        name="ACE's custom command [-ace, /ace]",
        value="This is a custom command for <@886078239833980958>! Try it to see what is does!",
        inline=False,
    )
    await ctx.respond(embed=customEmbed)


# Edit command


@bot.group()
async def edit(ctx):
    pass


@edit.command()
async def servername(ctx, *, input):
    await ctx.guild.edit(name=input)
    await ctx.send("Success! The Guild name is now " + "**" + input + "**")


@edit.command()
async def createText(ctx, *, input):
    await ctx.guild.create_text_channel(name=input)
    await ctx.send(
        "Success! A new Text channel called " + "**" + input + "** has been created!"
    )


@edit.command()
async def createVoice(ctx, *, input):
    await ctx.guild.create_voice_channel(name=input)
    await ctx.send(
        "Success! A new Voice channel called " + "**" + input + "** has been created!"
    )


@edit.command()
async def createRole(ctx, *, input):
    await ctx.guild.create_role(name=input)
    await ctx.send(
        "Success! A new Role called " + "**" + input + "** has been created!"
    )


# Ip embed


@bot.command(aliases=["ip", "server", "serverip"])
async def serverIp(ctx):
    ipEmbed = discord.Embed(
        title="Server IPs",
        description="We currently have 2 servers!",
        color=discord.Color.green(),
    )
    ipEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    ipEmbed.add_field(
        name="1.18.2 Modded SMP",
        value="**IP: StarCraftReal.aternos.me:27226**. This is an smp with a lot of mods, including Origins, Gravestones, Waystones and more! Check <#971649825630203945> for the modlist! **Cracked is enabled on this server!**",
        inline=False,
    )
    ipEmbed.add_field(
        name="1.19 Vanilla SMP",
        value="**IP: OMGLETSGOOOOO.aternos.me**, This is a vanilla 1.19 server! **Cracked is not enabled on this server**",
        inline=False,
    )
    ipEmbed.set_footer(text="Ask us if you want any more smps!")
    await ctx.send(embed=ipEmbed)


@bot.slash_command(
    aliases=["ip", "server"], description="This shows all the servers we have!"
)
async def serverip(ctx):
    ipEmbed = discord.Embed(
        title="Server IPs",
        description="We currently have 2 servers!",
        color=discord.Color.green(),
    )
    ipEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    ipEmbed.add_field(
        name="1.18.2 Modded SMP",
        value="**IP: StarCraftReal.aternos.me:27226**. This is an smp with a lot of mods, including Origins, Gravestones, Waystones and more! Check <#971649825630203945> for the modlist! **Cracked is enabled on this server!**",
        inline=False,
    )
    ipEmbed.add_field(
        name="1.19 Vanilla SMP",
        value="**IP: OMGLETSGOOOOO.aternos.me**, This is a vanilla 1.19 server! **Cracked is not enabled on this server**",
        inline=False,
    )
    ipEmbed.set_footer(text="Ask us if you want any more smps!")
    await ctx.respond(embed=ipEmbed)


# custom commands


@bot.command()
async def foot(ctx):
    await ctx.send("https://i.kym-cdn.com/photos/images/original/001/526/968/043.jpg")


@bot.command()
async def shiv(ctx):
    await ctx.send(
        "https://tenor.com/view/kidnapping-roblox-roblox-kidnapping-lol-uwu-gif-24871536"
    )


@bot.command()
async def stellar(ctx):
    await ctx.send("https://tenor.com/view/among-us-gif-24283650")
    await ctx.send(
        "https://tenor.com/view/sushichaeng-among-us-among-us-meme-shocked-confused-gif-22454610"
    )


@bot.command()
async def elpepe(ctx):
    await ctx.send("https://tenor.com/view/stare-staring-cat-gif-20275090")


@bot.command()
async def march(ctx):
    await ctx.send("> 'no' - Marchly , 2022")


@bot.command()
async def ghost(ctx):
    await ctx.send(
        "GHOST IS A LITTLE SUSSY BAKA AMOGUS UWU https://tenor.com/view/oops-haha-epic-fail-escalator-sliding-gif-15280329"
    )


@bot.command()
async def city(ctx):
    await ctx.send("city is sus AMOGUS https://c.tenor.com/o9bbZuiIt0AAAAAd/amogus.gif")
    print("yes")


@bot.command(description="ACE's Custom Command")
async def ace(ctx):
    await ctx.respond("bob, you truly are a god")
    await ctx.send(
        "https://cdn.discordapp.com/attachments/979007072060469318/987741354618662953/IMG_0650.png"
    )


# Events


@bot.event
async def on_message(msg):
    username = msg.author.display_name
    if msg.author == bot.user:
        return
    else:
        if msg.content == "hello":
            await msg.channel.send("Hello " + username)


@bot.event
async def on_ready():
    activity = discord.Game(name="!help")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="/help")
    )
    print("Bot is ready!")


@bot.event
async def on_member_join(member):
    guild = member.guild
    guildname = guild.name
    dmchannel = await member.create_dm()
    await dmchannel.send(
        f"Welcome to {guildname}! Read <#971339877004218419> and have fun! Also you're supposed to complete the steps to be able to see <#938455379950567444> where you can choose your version and get access to the rest of the server!"
    )


# slah commands
@bot.slash_command(description="City's Custom Command")
async def city(ctx):
    await ctx.respond(f"city is sus AMOGUS")
    await ctx.send("https://c.tenor.com/o9bbZuiIt0AAAAAd/amogus.gif")


@bot.slash_command(description="F O O T")
async def foot(ctx):
    await ctx.respond(
        "https://i.kym-cdn.com/photos/images/original/001/526/968/043.jpg"
    )


@bot.slash_command(description="Shiv's Custom Command")
async def shiv(ctx):
    await ctx.respond(
        "https://tenor.com/view/kidnapping-roblox-roblox-kidnapping-lol-uwu-gif-24871536"
    )


@bot.slash_command(description="Stellar's Custom Command")
async def stellar(ctx):
    await ctx.respond("https://tenor.com/view/among-us-gif-24283650")
    await ctx.send(
        "https://tenor.com/view/sushichaeng-among-us-among-us-meme-shocked-confused-gif-22454610"
    )


@bot.slash_command(description="El Pepe's Custom Command")
async def elpepe(ctx):
    await ctx.respond("https://tenor.com/view/stare-staring-cat-gif-20275090")


@bot.slash_command(description="Marchly's Custom Command")
async def march(ctx):
    await ctx.respond("https://c.tenor.com/5CVn4YakwxcAAAAM/cta-cat.gif")


@bot.slash_command(description="Ghost's Custom Command")
async def ghost(ctx):
    await ctx.respond("GHOST IS A LITTLE SUSSY BAKA AMOGUS UWU")
    await ctx.send(
        "https://tenor.com/view/oops-haha-epic-fail-escalator-sliding-gif-15280329"
    )


@bot.slash_command(description="ACE's Custom Command")
async def ace(ctx):
    await ctx.respond("Bob, you truly are a god")
    await ctx.send(
        "https://tenor.com/view/naruto-uzumaki-uzumaki-naruto-naruto-uzumaki-baryon-mode-gif-23142269"
    )


# RPS


@bot.slash_command(description="Rock Paper Scissors")
async def rps(
    ctx,
    options: Option(str, "choose your option", choices=["rock", "paper", "scissors"]),
):
    hands = ["rock", "paper", "scissors", "rock", "paper", "scissors"]
    opt = options or None
    bothand = random.choice(hands)
    await ctx.respond("I chose " + bothand)
    if opt == bothand:
        await ctx.send("Its a Draw! Shall we play again?")
    # elif opt == None:
    #     await ctx.respond("bruh you chose nothing, SO I GUES I WIN HAHA")
    elif opt == "rock":
        if bothand == "paper":
            await ctx.send("HAH I WON")
            await ctx.send(
                "https://tenor.com/view/dancing-cat-dancing-kitten-60fps-boogie-cat-gif-24303276"
            )
        else:
            await ctx.send(
                "DUDE MY INTERNET WAS LAGGING I SHOULD HAVE WON THA- i mean yay you won haha"
            )

    elif opt == "paper":
        if bothand == "rock":
            await ctx.send("I FRICKING HATE YOU SO MUC- you won")
            await ctx.send(
                "https://tenor.com/view/i-hate-you-anakin-star-wars-gif-10358450"
            )
        else:
            await ctx.send("WHEEE I WONNN")
            await ctx.send(
                "https://tenor.com/view/dance-dog-dancing-pet-boy-123asd-gif-18609627"
            )

    elif opt == "scissors":
        if bothand == "paper":
            await ctx.send(
                "yay you won '*how much longer do i have to do this again?*'"
            )
        else:
            await ctx.send("SUCK IT LOSER I WON")


@bot.slash_command(description="Defender's *SECRET* command")
async def defender(ctx):
    userid = ctx.author.id
    if userid == 832156730502414346:
        await ctx.respond(
            "https://tenor.com/view/get-real-real-get-fornite-impossible-gif-24471055"
        )
    else:
        await ctx.respond("This isn't your command. smh")


from config import TOKEN


@bot.slash_command(description="Allows admins to change the bot's status")
async def changestatus(ctx, status):
    userid = ctx.author.id
    username = ctx.author.display_name

    if userid == 832156730502414346:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status)
        )
        statusEmbed = discord.Embed(
            title="Change Defender bot's status", color=discord.Color.gold()
        )
        statusEmbed.add_field(
            name="ok", value="Changed DefenderBot's Status to " + status
        )
        await ctx.respond(embed=statusEmbed)
    elif userid == 706876255064293416:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status)
        )
        statusEmbed = discord.Embed(
            title="Change Defender bot's status", color=discord.Color.gold()
        )
        statusEmbed.add_field(
            name="ok", value="Changed DefenderBot's Status to " + status
        )
        await ctx.respond(embed=statusEmbed)
    elif userid == 701981194971119690:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status)
        )
        statusEmbed = discord.Embed(
            title="Change Defender bot's status", color=discord.Color.gold()
        )
        statusEmbed.add_field(
            name="ok", value="Changed DefenderBot's Status to " + status
        )
        await ctx.respond(embed=statusEmbed)
    elif userid == 939701768491782204:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status)
        )
        statusEmbed = discord.Embed(
            title="Change Defender bot's status", color=discord.Color.gold()
        )
        statusEmbed.add_field(
            name="ok", value="Changed DefenderBot's Status to " + status
        )
        await ctx.respond(embed=statusEmbed)
    else:

        statusEmbed = discord.Embed(title="why", color=discord.Color.gold())
        statusEmbed.add_field(name="no " + username, value="bruh")
        await ctx.respond(embed=statusEmbed)

@bot.slash_command(desciption = "is this a SCERET?")
async def secret_omg(ctx):
    await ctx.respond("omg you discovered secret, dm <@832156730502414346> to get a custom role!", ephemeral=True)

# class nitroButton(Button):
#     def __init__(self, label):
#         super().__init__(label= label, style = discord.ButtonStyle.blurple, emoji="<:nitro:989116809892491314>", custom_id="fakeNitro")
#     async def callback(self, button, interaction):
#         button.label = "Claimed Nitro"
#         button.disabled = True
#         await interaction.response.edit_message(view=self)
#         await interaction.followup.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713", ephemeral = True)

class MyView(View):

    def __init__(self, ctx):
        super().__init__(timeout = 180)
        self.ctx = ctx

    @discord.ui.button(label= "Click here to get FREE NITRO", style = discord.ButtonStyle.blurple, emoji="<:nitro:989116809892491314>", custom_id="fakeNitro")
    async def button_callback(self, button, interaction):
        button.label = "Claimed Nitro"
        button.disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send("https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713", ephemeral = True)
    async def on_timeout(self):
        await self.ctx.send("You took too long smh")
    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("This isn't your nitro!", ephemeral = True)
            return False
        else:
            return True
@bot.slash_command()
async def nitro(ctx):
    # button = Button(label= label, style = discord.ButtonStyle.blurple, emoji="<:nitro:989116809892491314>", custom_id="fakeNitro")
    view = MyView(ctx)
    nitroEmbed = discord.Embed(title = "Get Free Nitro!", description = "Click on the button to get free nitro!")
    await ctx.respond(embed = nitroEmbed, view=view)
bot.run(TOKEN)
