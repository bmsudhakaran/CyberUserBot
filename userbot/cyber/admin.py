# Copyright 2021 (C) FaridDadashzade
#
# CyberUserBot - FaridDadashzade

from telethon import events
from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChatAdminRights,
    ChatBannedRights,
    MessageEntityMentionName,
)


from . import *

# ----------------------------------------------------- #

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)


# ----------------------------------------------------- #





# ----------------------------------------------------- #

@tgbot.on(events.NewMessage(pattern="^/ban(?: |$)(.*)"))
async def ban(event):
    noob = event.sender_id
    userids = []
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("Sən admin deyilsən!")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply("Bunu etmək üçün admin olmalıyam!")
        return

    user, reason = await get_user_from_event(event)
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await event.reply("Xəta.")
        return
    try:
        reply = await event.get_reply_message()
        if reply:
            pass
    except BadRequestError:
        await event.reply(
            "`Xəta.`"
        )
        return
    if reason:
        await event.reply(f"`{str(user.id)}` ban edildi.\n\nSəbəb: {reason}")
    else:
        await event.reply(f"`{str(user.id)}` ban edildi!")


@tgbot.on(events.NewMessage(pattern="^/unban(?: |$)(.*)"))
async def nothanos(event):
    userids = []
    noob = event.sender_id
    async for user in tgbot.iter_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    ):
        userids.append(user.id)
    if noob not in userids:
        await event.reply("Sən admin deyilsən!")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await event.reply("Bunu etmək üçün admin olmalıyam!")
        return
    user = await get_user_from_event(event)
    user = user[0]
    if user:
        pass
    else:
        return
    try:
        await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
        await event.reply("`İstifadəçi yenidən qrupa qatıla bilər!`")
    except BadRequestError:
        await event.reply("`Bunu etmək üçün admin olmalısınız!`")
        return
      
      
# ----------------------------------------------------- #
      
