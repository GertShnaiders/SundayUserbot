import asyncio

from sundaybot import CMD_HELP
from sundaybot.utils import sunday_on_cmd


# @command(pattern="^.cmds", outgoing=True)
@sunday.on(sunday_on_cmd(pattern=r"cmds"))
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls sundaybot/modules"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**List of Plugins:**\n - {o}\n\n**HELP:** __If you want to know the commands for a plugin, do:-__ \n `.help <plugin name>` **without the < > brackets.**\n__All modules might not work directly. Visit__ @SundayUserBot_Official __for assistance.__"
    await event.edit(OUTPUT)


CMD_HELP.update(
    {
        "cmd_list": "**Cmd_list**\
\n\n**Syntax : **`.cmds`\
\n**Usage :** This plugin lists all the plugins which are in your userbot."
    }
)
