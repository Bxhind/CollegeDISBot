#There's a simple discord bot who works with db wia postgre psycopg2
#______                                 ___________                      ________   
#      \\ \\ \        // / || |   || | |___     ___|  || \ \\     || |  ||  ____\ \\
#   /\  \\ \\ \      // /  || |   || |     || |       || |\ \\    || |  || |     \ \\
#   \/   || \\ \    // /   || |   || |     || |       || | \ \\   || |  || |     | ||
#       //   \\ \  // /    || |___|| |     || |       || |  \ \\  || |  || |     | ||
#       \\    \\ \// /     || |___|| |     || |       || |   \ \\ || |  || |     | ||
#   /\   \\   // /\\ \     || |   || |     || |       || |    \ \\|| |  || |     | ||
#   \/   //  // /  \\ \    || |   || |  ___|| |___    || |     \ \\| |  || |_____/ //
#       //  // /    \\ \   || |   || | |___________|  || |      \ \\ |  || |___ / //
    
import disnake
import asyncio, tracemalloc, os, platform, json

from disnake.ext import commands, tasks

init_extension = []
for filename in os.listdir('./cogs'):
    if filename.endswith(".py"):
        init_extension.append(F"cogs.{filename[:-3]}")

with open("access.json") as file:
    access = json.load(file)

prefix = access['prefix']
token = access['token']

Bot = commands.Bot(command_prefix= prefix, intents= disnake.Intents.all())

@Bot.event
async def on_ready():
    print(f"We have logged in as {Bot.user}\n")
    await Bot.change_presence(
        status=disnake.Status.online,
        activity=disnake.Activity(
            type=disnake.ActivityType.listening, name="создателя."))


if __name__ == "__main__":
    for extension in init_extension:
        Bot.load_extension(extension)
        print(f"{extension} load", end= "\n")
    Bot.run(token)
    