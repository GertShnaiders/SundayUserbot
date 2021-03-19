

from sundaybot.Configs import Config
import time
from telethon import __version__ as tv
import sys
import platform
from git import Repo
from sundaybot import ALIVE_NAME
from sundaybot import bot
from sundaybot.modules import currentversion

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def friday(event):
    await event.reply(f"`Yo ! {bot.me.first_name} , I am Alive. Need Help ? Maybe You Should Pm Me.`")
