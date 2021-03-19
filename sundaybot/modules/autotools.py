

import asyncio
import time
from telethon.errors import FloodWaitError
from telethon.tl import functions
from uniborg.util import edit_or_reply, sunday_on_cmd, sudo_cmd
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.executors.asyncio import AsyncIOExecutor
from sundaybot.function.auto_tools import auto_name, auto_bio, auto_pic
from sundaybot import ALIVE_NAME, CMD_HELP

scheduler = AsyncIOScheduler(executors={'default': AsyncIOExecutor()})

@sunday.on(sunday_on_cmd(pattern="autoname(?: |$)(.*)"))
@sunday.on(sudo_cmd(pattern="autoname(?: |$)(.*)", allow_sudo=True))
async def autoname(event):
    if event.fwd_from:
        return
    sed = await sunday.edit_or_reply(event, "`Started AutoName Your Name Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Use .stop Cmd`")
    scheduler.add_job(auto_name, 'interval', args=[event.pattern_match.group(1)], minutes=5, id='autoname')
    
@sunday.on(sunday_on_cmd(pattern="autopic$"))
@sunday.on(sudo_cmd(pattern="autopic$", allow_sudo=True))
async def autopic(event):
    if event.fwd_from:
        return
    sed = await sunday.edit_or_reply(event, "`Started AutoPic Your Name Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Use .stop Cmd`")
    scheduler.add_job(auto_pic, 'interval', minutes=5, id='autopic')

@sunday.on(sunday_on_cmd(pattern="autobio(?: |$)(.*)"))
@sunday.on(sudo_cmd(pattern="autobio(?: |$)(.*)", allow_sudo=True))
async def autobio(event):
    if event.fwd_from:
        return
    sed = await sunday.edit_or_reply(event, "`Started AutoBio Your Bio Will Be Changed Every 1 Min, According To TimeZone Given. To Terminate This Process Use .stop Cmd`")
    scheduler.add_job(auto_bio, 'interval', args=[event.pattern_match.group(1)], minutes=5, id='autobio')

@sunday.on(sunday_on_cmd(pattern="stop$"))
@sunday.on(sudo_cmd(pattern="stop$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    sed = await sunday.edit_or_reply(event, "`Checking Recived Input :/`")
    try:
        scheduler.remove_all_jobs()
    except:
        await event.edit("`Are You Fking Insane?`")
        return
    logger.info("Auto Tools Has Been Terminated")
    await sed.edit("`All Auto Tools Has Been Terminated`")
    
scheduler.start()

CMD_HELP.update(
    {
        "autotools": "**AutoTools**\
\n\n**Syntax : **`.autoname`\
\n**Usage :** Change your Name With Time.\
\n\n**Syntax : **`.autopic`\
\n**Usage :** Change your Picture With Time.\
\n\n**Syntax : **`.autobio <text>`\
\n**Usage :** Change your Bio With Time.\
\n\n**Syntax : **`.stop`\
\n**Usage :** Stops All The Auto Processes"
    }
)
