# Copyright 2021 (C) FaridDadashzade.

from telethon import Button, custom
from userbot import bot, DEFAULT_NAME, SAHIB_ID, SUPPORT
from userbot import *
from . import *


CYBER_NAME = f"[{DEFAULT_NAME}](tg://user?id={SAHIB_ID})"

SAHIB = SUPPORT

async def qur(cyber, ad, deyer):
    try:
        cyber.set(ad, deyer)
    except BaseException:
        return await cyber.edit("`Xəta.`")
      
      
def geri(ad):
    button = [Button.inline("« Geri", data=f"{ad}")]
    return button
