import colorama
from colorama.initialise import colorama_text
import discord, asyncio
import shutil
import subprocess
import psutil
import logging
from sys import argv
from os import system
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system

def logo():
    try:
        msg = Fore.RED + """
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
\\|       \ |  |  |  |     /       ||           |    /       | /      ||   _  \     |  | |   _  \  |           |(_ ) //
\\|  .--.  ||  |  |  |    |   (----``---|  |----`   |   (----`|  ,----'|  |_)  |    |  | |  |_)  | `---|  |----` |/  //
\\|  |  |  ||  |  |  |     \   \        |  |         \   \    |  |     |      /     |  | |   ___/      |  |          //
\\|  '--'  ||  `--'  | .----)   |       |  |     .----)   |   |  `----.|  |\  \----.|  | |  |          |  |          //
\\|_______/  \______/  |_______/        |__|     |_______/     \______|| _| `._____||__| | _|          |__|          //
----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------
 """
        for l in msg:
            print(l, end="")
    except KeyboardInterrupt:

        sys.exit()
logo()


print(Fore.YELLOW + '                                          [?]  Github.com/DustScript  [?]  ')


print('  ')
print(Fore.YELLOW + '----------------------------------------------[-] Dust Comandos Dell [-]-----------------------------------------------'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print(''.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print(Fore.GREEN + '                         CMD    [1] dust : (Digite "dust" para Deletar mensagens mamaco)'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print(Fore.GREEN + '                         CMD    [2] dust2 : (Digite "dust2" para Deletar todas mensagens da dm seu virgem )'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print(''.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX)) 
print(Fore.YELLOW + '-----------------------------------------------------------------------------------------------------------------------'.format(Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX))
print('  ')

client = discord.Client()
token = "Insert your Token"

def murder(cmd):
    subprocess.call(cmd, shell=True)
@client.event

async def on_ready():
    width = shutil.get_terminal_size().columns
    def ui():
        print()
        print(Fore.WHITE + "Developer/Dust' #1533".center(width))
        print()
        print(Fore.BLUE +  "[-] [Hakai 44] Perfil logado - Delet Message : {0} [-]".format(client.user).center(width))
        print()
        print(Fore.WHITE +  "[-] Crow Labs [-]".center(width))
    ui()

@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel
        if commands[0] == 'dust':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == 'dust2':
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                print(msg)
                        except:
                             pass

client.run(token, bot=False)