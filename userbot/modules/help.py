# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^\.help(?: |$)(.*)")
async def help(event):
    """ For .help command,"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit("Silakan tentukan nama modul yang valid.")
    else:
        head = "**Help for** [Miku Chan♥️](https://github.com/tegarseptian033/ProjectBish-1)"
        head2 = "Silakan tentukan modul mana yang ingin Anda Gunakan !!"
        head3 = "Contoh: .help <module name>"
        head4 = "Daftar untuk semua perintah tersedia di bawah ini: "
        string = ""
        sep1 = "••••••••••••••••••••••••••••••••••••••••••••••"
        sep2 = "==============================="
        for i in CMD_HELP:
            string += "`" + str(i)
            string += "`  |  "
        await event.edit(f"{head}\
              \n{sep2}\
              \n{head2}\
              \n{head3}\
              \n{sep2}\
              \n{head4}\
              \n\n{string}\
              \n{sep1}")
