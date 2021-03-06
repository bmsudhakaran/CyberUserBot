# Copyright (C) 2021 FaridDadashzade.
#
# CYBERUSERBOT - FaridDadashzade
#

from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import CMD_HELP, CYBER_EMOJI
from userbot.events import register

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("__cyber")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.cyber(?: |$)(.*)")
async def cyber(event):
    """ .cyber əmri üçün """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(LANG["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [sorted(list(CMD_HELP))[i:i + 3] for i in range(0, len(sorted(list(CMD_HELP))), 3)]
        
        for i in sayfa:
            string += f'{CYBER_EMOJI} '
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await event.edit(LANG["NEED_MODULE"] + '\n\n' + string)
