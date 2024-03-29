# importing
from code import interact
from concurrent.futures import wait
from profile import run
from ssl import Options
from types import NoneType
from webbrowser import BackgroundBrowser, BaseBrowser
from dotenv import load_dotenv
from discord.ui import Select

# from click import pass_context

# from tkinter.ttk import Style
import discord, os, asyncio
import random
from discord.ui import Button, View, Select
from discord.ext import commands, tasks
from discord.commands import Option, slash_command
from discord.ext.commands import has_permissions, MissingPermissions
from discord import (
    CategoryChannel,
    Member,
    Permissions,
    default_permissions,
    TextChannel,
)

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(
    command_prefix=">>>", help_command=None, intents=intents
)


# Commands


@bot.slash_command(description="Flip a coin")
async def coinflip(ctx):
    num = random.randint(1, 2)
    if num == 1:
        await ctx.respond("Heads")
    else:
        await ctx.respond("Tails")


# Help Embed


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
        name="Rock Paper Scissors [/rps]",
        value="This command allows you to play rock paper scissors against the bot! How to use the command: `-rps value` exchange the value with **rock paper or scissors**!",
        inline=False,
    )
    helpEmbed.add_field(
        name="Coinflip [/coinflip]",
        value="This command lets you flip a coin",
        inline=False,
    )
    helpEmbed.add_field(
        name="Custom commands [/friends]",
        value="This command show the list of custom commands for friends!",
    )
    helpEmbed.add_field(
        name="IP Help [/serverip]",
        value="This tells you what servers we have and their ips!",
        inline=False,
    )
    helpEmbed.add_field(
        name="Change Bot Status [/changestatus]",
        value="Allows certain people to change the bot's status",
        inline=False,
    )
    helpEmbed.set_footer(text="rip techno :((((((((((")
    await ctx.respond(embed=helpEmbed, ephemeral=True)


# Cutsom Embed


@bot.slash_command(description="This shows all my friend's commands!")
async def friends(ctx):
    customEmbed = discord.Embed(
        title="Commands",
        description="These are my friends' commands!",
        color=discord.Color.blurple(),
    )
    customEmbed.set_thumbnail(url="https://i.imgflip.com/60v6pm.jpg")
    customEmbed.add_field(
        name="City's Custom Command [/city]",
        value="This is a custom command for <@701981194971119690>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Marchly's Custom Command [/march]",
        value="This is a custom command for <@706876255064293416>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Ghost's Custom Command [/ghost]",
        value="This is a custom command for <@606870679543087154>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Shiv's Custom Command [/shiv]",
        value="This is a custom command for <@518744853832794112>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Stellar's Custom Command [/stellar]",
        value="This is a custom command for <@820304171764416582>! Try it to see what is does!!",
        inline=False,
    )
    customEmbed.add_field(name="F O O T [/foot]", value="F O O T", inline=False)
    customEmbed.add_field(
        name="El Pepe's custom command [/elpepe]",
        value="This is a custom command for <@852834698300620820>! Try it to see what is does! can use it",
        inline=False,
    )
    customEmbed.add_field(
        name="ACE's custom command [-ace, /ace]",
        value="This is a custom command for <@886078239833980958>! Try it to see what is does!",
        inline=False,
    )
    customEmbed.add_field(
        name="Hal's Custom Command [/hal]",
        value="This is a custom command for <@922536626108911667>",
        inline=False,
    )
    customEmbed.add_field(
        name="Kori's Custom Command[/kori]",
        value="This is a custom command for <@982213873551699969>",
        inline=False,
    )
    customEmbed.set_footer(text="rip techno :(((((((((")
    await ctx.respond(embed=customEmbed)


# Ip embed


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
        name="1.19.1 Modded SMP",
        value="**IP: DefendersDen.aternos.me**, This is an smp with a lot of mods, including Origins, Gravestones, Inventorio and more! You can download it on [Curse](https://www.curseforge.com/minecraft/modpacks/defenders-smp) or [Modrinth](https://modrinth.com/modpack/defenders-smp)! **Cracked is not enabled on this server!**",
        inline=False,
    )
    ipEmbed.set_footer(text="Ask us if you want any more smps!")
    await ctx.respond(embed=ipEmbed)


# Create Stuff

create = discord.SlashCommandGroup(
    "create", "Commands that can help moderators create channels automaticaly."
)


@create.command(description="Creates a text channel!")
@default_permissions(manage_channels=True)
async def channel(ctx, name):
    await ctx.respond(f"A Text channel with the name {name}!", ephemeral=True)
    await ctx.guild.create_text_channel(name=name)


@create.command(description="Creates a voice channel for you!")
@default_permissions(manage_channels=True)
async def vc(ctx, name):
    await ctx.respond(f"Created a vc with name: {name}", ephemeral=True)
    await ctx.guild.create_voice_channel(name=name)


@create.command(description="Creates a forum channel for you!")
@default_permissions(manage_channels=True)
async def forum(ctx, name):
    await ctx.respond(f"Created a forum channel with name: {name}", ephemeral=True)
    await ctx.guild.create_forum_channel(name=name)


@create.command(description="Creates a stage channel for you!")
@default_permissions(manage_channels=True)
async def stage(ctx, name):
    await ctx.respond(f"Created a stage channel with the name: {name}!", ephemeral=True)
    await ctx.guild.create_stage_chanel(name=name)

@create.command(description = "Creates a role for you!")
async def role(ctx,name):
    await ctx.respond(f"Created a role with the name: {name}!", ephemeral = True)
    await ctx.guild.create_role(name=name)

bot.add_application_command(create)

# Events
@bot.event
async def on_ready():
    f = open("status.txt", "r")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name="Haters be hatin'"
        ),
        status=discord.Status.dnd,
    )
    # await bot.change_presence(status=discord.Status.do_not_disturb)
    print("Bot is ready!")


# @bot.event
# async def on_member_join(member):
#     await bot.wait_until_ready()
#     guild = bot.get_guild(938444786145325097)
#     guildname = guild.name
#     channel = guild.get_channel(971410967021895710)
#     rulesChannel = guild.get_channel(971339877004218419)
#     rolesChannel = guild.get_channel(978996415504199720)
#     partnersChannel = guild.get_channel(980821704945324062)
#     botChannel = guild.get_channel(987381424418091068)
#     ticketChannel = guild.get_channel(980039998738944080)
#     dmchannel = await member.create_dm()
#     await dmchannel.send(
#         f"Welcome to {guildname}! Read {rulesChannel.mention}! Have Fun!"
#     )
#     embed = discord.Embed(
#         title="Welcome to Defender's Den!",
#         description=f"""**Thanks for joining!**\n\n**Please read the {rulesChannel.mention}**\n\n
#         **Go to {rolesChannel.mention} to customize your roles.**\n\n
#         **If you have any questions, feel free to direct message a staff member or open a ticket in {ticketChannel.mention}.**\n\n 
#         **See how my bot is updated in {botChannel.mention}**\n\n
#         **Check out our partners in {partnersChannel.mention}\n\n**""",
#         color=discord.Color.brand_green(),
#     )
#     embed.add_field(
#         name="PSST Check out the GitHub Page for my bot!:",
#         value="https://github.com/DefenderYAY/DefenderBot!",
#         inline=False,
#     )
#     embed.set_footer(text="Have Fun!")
#     await channel.send(f"Welcome {member.mention}", embed=embed)


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


@bot.slash_command(description="Hal's Custom Command!")
async def hal(ctx):
    await ctx.respond(
        "https://tenor.com/view/cat-the-cat-he-dance-he-dance-gif-24077288"
    )


@bot.slash_command(description="Kori's Custom Command")
async def kori(ctx):
    await ctx.respond(
        "https://c.tenor.com/XgAG1LXjpcYAAAAC/apartamento-qualquer-banner-banner.gif"
    )
    await ctx.send(
        "My self korilic. I identify as a garlic but I hate garlic eww...\nthe most cool staff member (definitely not a cap)"
    )


@bot.slash_command(description="Ret's Funny Taunt")
async def ret(ctx):
    await ctx.respond("https://tenor.com/view/scout-laugh-gif-21799013")
    await ctx.send("we have an embed fail! chat f for sad.")


@bot.slash_command(description="EXACTLY! NUVEY")
async def legendary(ctx):
    await ctx.respond("EXACTLY!!! NUVEY")


@bot.slash_command(description="Bigtub's Laundry??")
async def bigtub(ctx):
    await ctx.respond(
        "https://media.discordapp.net/attachments/1002526675269079070/1002833325154648104/IMG_8004.png"
    )


@bot.slash_command(description="IM ANGY")
async def angy(ctx):
    await ctx.respond(
        "https://media.discordapp.net/attachments/1002526675269079070/1002832758676144159/unknown.png"
    )


@bot.slash_command(description="He's Back Boys", name="aspect_zero")
async def aspectzero(ctx):
    await ctx.respond(
        """"I have returned"
        -AspectZero
    """
    )

@bot.slash_command(description = "GOO GOO GAA GAA IM A BABY")
async def googoogaagaa(ctx):
    await ctx.respond("https://cdn.upload.systems/uploads/KIJYL5au.mp4")

@bot.slash_command(description = "A Turtorial: 'How to play League'(not fake)")
async def leagueoflegends(ctx):
    await ctx.respond("You have sinned, and you will hence recieve a punishement worthy of playing LoL. **Public Shaming**", ephemeral = True)
    await ctx.send(f"Its seems {ctx.author} has used /leagueoflegends! Well...")
    await ctx.send("https://www.wikihow.com/Take-a-Relaxing-Shower")

# RPS WHEEEEE


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


@bot.slash_command(description="Allows admins to change the bot's status")
async def changestatus(ctx, status):
    userid = ctx.author.id
    username = ctx.author.display_name
    f = open("status.txt", "w")
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
        f.write(status)
        await ctx.respond(embed=statusEmbed)

    elif userid == 706876255064293416:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status),
            status=discord.Status.dnd,
        )
        statusEmbed = discord.Embed(
            title="Change Defender bot's status", color=discord.Color.gold()
        )
        statusEmbed.add_field(
            name="ok", value="Changed DefenderBot's Status to " + status
        )
        f.write(status)
        await ctx.respond(embed=statusEmbed)

    elif userid == 701981194971119690:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status),
            status=discord.Status.dnd,
        )
        statusEmbed = discord.Embed(
            title="Change Defender bot's status", color=discord.Color.gold()
        )
        statusEmbed.add_field(
            name="ok", value="Changed DefenderBot's Status to " + status
        )
        f.write(status)
        await ctx.respond(embed=statusEmbed)
    elif userid == 939701768491782204:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status),
            status=discord.Status.dnd,
        )
        statusEmbed = discord.Embed(
            title="Change Defender bot's status", color=discord.Color.gold()
        )
        statusEmbed.add_field(
            name="ok", value="Changed DefenderBot's Status to " + status
        )
        f.write(status)
        await ctx.respond(embed=statusEmbed)

    elif userid == 606870679543087154:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.playing, name=status),
            status=discord.Status.dnd,
        )
        statusEmbed = discord.Embed(
            title="Change Defender bot's status", color=discord.Color.gold()
        )
        statusEmbed.add_field(
            name="ok", value="Changed DefenderBot's Status to " + status
        )
        f.write(status)
        await ctx.respond(embed=statusEmbed)

    else:

        statusEmbed = discord.Embed(title="why", color=discord.Color.gold())
        statusEmbed.add_field(name="no " + username, value="bruh")
        await ctx.respond(embed=statusEmbed)
    f.close()


class MyView(View):
    def __init__(self, ctx):
        super().__init__(timeout=180)
        self.ctx = ctx

    @discord.ui.button(
        label="Click here to get FREE NITRO",
        style=discord.ButtonStyle.blurple,
        emoji="<:nitro:989116809892491314>",
        custom_id="fakeNitro",
    )
    async def button_callback(self, button, interaction):
        button.label = "Claimed Nitro"
        button.disabled = True
        await interaction.response.edit_message(view=self)
        await interaction.followup.send(
            "https://tenor.com/view/rickroll-roll-rick-never-gonna-give-you-up-never-gonna-gif-22954713",
            ephemeral=True,
        )

    # async def on_timeout(self):
    #     if discord.InteractionResponded == True:
    #         return
    #     else:
    #         await self.ctx.send("You took too long smh")

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message(
                "This isn't your nitro!", ephemeral=True
            )
            return False
        else:
            return True


@bot.slash_command(description="is this FREE NITRO?!1!?")
async def nitro(ctx):
    # button = Button(label= label, style = discord.ButtonStyle.blurple, emoji="<:nitro:989116809892491314>", custom_id="fakeNitro")
    view = MyView(ctx)
    nitroEmbed = discord.Embed(
        title="Get Free Nitro!", description="Click on the button to get free nitro!"
    )
    await ctx.respond(embed=nitroEmbed, view=view)


@bot.slash_command(pass_context=True)
async def ayowtf(ctx):
    channel = bot.get_channel(979007072060469318)
    await channel.send("amongus")


@bot.slash_command(description="This shows all the partners we have!")
async def partners(ctx):
    PartnerEmbed = discord.Embed(
        title="Our Partners",
        description="These are our Partners",
        color=discord.Colour.green(),
    )
    PartnerEmbed.add_field(
        name="CityBot Home",
        value="This is City's Bot's Server! Join Here: https://discord.gg/vUNVYa4Nuy",
        inline=False,
    )
    PartnerEmbed.add_field(
        name="City's Cabaret",
        value="This is City's Extra Server! Join Here: https://discord.gg/sEztMEDFyp",
        inline=False,
    )
    await ctx.respond(embed=PartnerEmbed)


@bot.slash_command(description="Quotes your message!")
async def quote(ctx, message):
    author = ctx.author
    await ctx.respond("Done! You made me say " + message, ephemeral=True)
    await ctx.send(
        f""""{message}"
        -{author}
        """
    )


@bot.slash_command(
    description="Makes me say a message in a channel! This is definitely NOT a bad idea :D"
)
@default_permissions(manage_messages=True)
async def say(ctx, message):
    if "nigger" in message.lower() or "retard" in message.lower() or "faggot" in message.lower() or "nigga" in message.lower() or "fag" in message.lower():
        await ctx.respond("I will not say this because your message contains slurs! Please be better!", ephemeral = True)
    else:
        await ctx.respond("Done! You made me say " + message, ephemeral=True)
        await ctx.send(message)


@bot.slash_command(description="I will send an embed with YOUR message on it!")
async def embed(ctx, message):
    author = ctx.author
    avatar = ctx.author.avatar
    await ctx.respond(
        "Done! I have sent an embed which says " + message, ephemeral=True
    )
    messageEmbed = discord.Embed(
        title=None, description=message, color=discord.Color.nitro_pink()
    )
    messageEmbed.set_author(name=author, icon_url=avatar)
    await ctx.send(embed=messageEmbed)


@bot.slash_command(description="🥖")
async def bread(ctx):
    await ctx.respond("🥖🥖🥖🥖🥖🥖🥖🥖🥖🥖")


@bot.slash_command(description="Shows you a users status", name="user_status")
async def userstatus(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    elif member.status == discord.Status.online:
        gembed = discord.Embed(title=f"{member.name} is online")
        await ctx.respond(embed=gembed)
    elif member.status == discord.Status.offline:
        gembed = discord.Embed(title=f"{member.name} is offline")
        await ctx.respond(embed=gembed)
    elif member.status == discord.Status.dnd:
        gembed = discord.Embed(title=f"{member.name} wants you to not not disturb them")
        await ctx.respond(embed=gembed)
    elif member.status == discord.Status.idle:
        gembed = discord.Embed(
            title=f"{member.name} has been afk for 10 minutes or more"
        )
        await ctx.respond(embed=gembed)
    elif member.status == discord.Status.invisible:
        gembed = discord.Embed(title=f"{member.name} is secretly online! shh")
        await ctx.respond(embed=gembed)


@bot.slash_command(
    description="A few instructions on how you can start the smp", name="start_smp"
)
async def smp(ctx):
    smpStartEmbed = discord.Embed(
        title="Instructions on how to start the smp!",
        color=discord.Colour.brand_green(),
    )
    smpStartEmbed.add_field(
        name="DM Defender",
        value="You can always dm <@832156730502414346> and ask him to start the smp **WHEN HE IS ONLINE**",
        inline=False,
    )
    smpStartEmbed.add_field(
        name="Start it yourself!",
        value="To start the SMP when the <@832156730502414346> isnt online, create a ticket and send your aternos username there! Please do **NOT** create a ticket asking us to start the smp!",
    )
    smpStartEmbed.set_thumbnail(
        url="https://upload.wikimedia.org/wikipedia/en/5/51/Minecraft_cover.png"
    )
    await ctx.respond(embed=smpStartEmbed)


@bot.slash_command(
    description="Revive the chat", name="revive", guild_ids=[938444786145325097]
)
@default_permissions(ban_members=True)
@discord.ext.commands.cooldown(1, 3600, type=discord.ext.commands.BucketType.default)
async def revivechat(ctx, reason):
    username = ctx.author
    avatar = ctx.author.avatar
    embed = discord.Embed(
        title=None, description=reason, color=discord.Color.brand_red()
    )
    embed.set_author(name=username, icon_url=avatar)
    await ctx.respond("Reviving chat for " + reason, ephemeral=True)
    await ctx.send("<@&981927410876448838>", embed=embed)


# loops


# @tasks.loop(seconds=18000)
# async def send_message():
#     await bot.wait_until_ready()
#     channel = bot.get_channel(979007072060469318)
#     print(channel)
#     partnersHourlyEmbed = discord.Embed(
#         title="Our Partners",
#         description="These are our Partners",
#         color=discord.Colour.green(),
#     )
#     partnersHourlyEmbed.add_field(
#         name="CityBot Home",
#         value="This is City's Bot's Server! Join Here: https://discord.gg/vUNVYa4Nuy",
#         inline=False,
#     )                                                                                                                         Taken Out Because It is too distracting
#     partnersHourlyEmbed.add_field(
#         name="City's Cabaret",
#         value="This is City's Private Server! Join Here: https://discord.gg/sEztMEDFyp",
#         inline=False,
#     )
#     partnersHourlyEmbed.add_field(
#         name="Darkcord",
#         value="<@982213873551699969>'s server! Join Here: https://discord.gg/CrdAvMYC5M",
#         inline=False,
#     )
#     partnersHourlyEmbed.set_footer(text="rip techno :((((((((")
#     await channel.send(embed=partnersHourlyEmbed)


# send_message.start()
# Polls


class PollCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.numbers = [
            "1️⃣",
            "2️⃣",
            "3️⃣",
            "4️⃣",
            "5️⃣",
            "6️⃣",
            "7️⃣",
            "8️⃣",
            "9️⃣",
            "🔟",
        ]
        self._last_member = None

    @discord.slash_command(description="Create a Poll!")
    @default_permissions(manage_messages=True)
    async def poll(self, ctx, minutes: int, title, things: str):
        things = things.split(",")
        print(things)
        if len(things) == 0:
            pollEmbed = discord.Embed(
                title=title, description=f"There are **{minutes}** minutes remaining!"
            )
            await ctx.respond(
                f"Done! Created a poll with title: {title}!", ephemeral=True
            )
            msg = await ctx.send(embed=pollEmbed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
        else:
            pollEmbed = discord.Embed(
                title=title, description=f"There are **{minutes}** minutes remaining!"
            )
            for number, option in enumerate(things):
                pollEmbed.add_field(
                    name=f"{self.numbers[number]}", value=f"**{option}**", inline=False
                )
            await ctx.respond(
                f"Done! Created a poll with title: {title}, and your options!",
                ephemeral=True,
            )
            msg = await ctx.send(embed=pollEmbed)
            for x in range(len(pollEmbed.fields)):
                await msg.add_reaction(self.numbers[x])
        self.poll_updater.start(ctx, minutes, title, things, msg)

    @discord.slash_command(description="Say Hello!")
    async def hello(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.respond("Done!", ephemeral=True)
            await ctx.send(f"Hello {member.name}~")
        else:
            await ctx.respond("Done!", ephemeral=True)
            await ctx.send(f"Hello {member.name}... This feels familiar.")
        self._last_member = member

    @tasks.loop(minutes=1)
    async def poll_updater(self, ctx, minutes, title, things, msg):
        counter = self.poll_updater.current_loop
        remaining = minutes - counter

        pollEmbedv2 = discord.Embed(
            title=title, description=f"There are **{remaining}** minutes remaining!"
        )
        for number, option in enumerate(things):
            pollEmbedv2.add_field(
                name=f"{self.numbers[number]}", value=f"**{option}**", inline=False
            )

        await msg.edit(embed=pollEmbedv2)

        if remaining == 0:
            counts = []
            msg = discord.utils.get(bot.cached_messages, id=msg.id)
            reactions = msg.reactions

            for reaction in reactions:
                counts.append(reaction.count)
            most_react = max(counts)
            i = 0
            for count in counts:
                if count == most_react:
                    i = i + 1
            if i > 1:
                await ctx.send("The Vote Has Resulted in a draw!")
            else:
                max_index = counts.index(most_react)
                if len(things) == 0:
                    await ctx.send(
                        "Looks like the time's up! Let's See what the people think!"
                    )
                    winneremoji = reactions[max_index]
                    if winneremoji.emoji == "👍":
                        await ctx.send("That's What I Thought!")
                    elif winneremoji.emoji == "👎":
                        await ("Turns out People don't like this!")
                else:
                    winner = things[max_index]
                    winneremoji = reactions[max_index]

                    await ctx.send(
                        "Looks like the time's up! Let's See what the people think!"
                    )
                    await ctx.send(
                        f"{winneremoji.emoji} **{winner}** has won the poll!"
                    )
                self.poll_updater.stop()


bot.add_cog(PollCommand(bot))

load_dotenv(".env")
bot.run(os.getenv("token"))
