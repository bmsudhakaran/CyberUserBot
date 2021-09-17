# Copyright (C) 2021 CyberUserBot.
#
# Oğurlayan bizə ata desin.


from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl import functions
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.messages import GetFullChatRequest

from userbot import CMD_HELP
from userbot.cmdhelp import CmdHelp
from userbot.events import register as cyber
from userbot import bot, BLACKLIST_CHAT

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Yanlış kanal/qrup`")
            return None
        except ChannelPrivateError:
            await event.reply(
                "`Bu qrup gizli qrupdur ya da mən burada ban edilmişəm.`"
            )
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Belə bir supergroup yoxdur.`")
            return None
        except (TypeError, ValueError):
            await event.reply("`Yanlış kanal/qrup`")
            return None
    return chat_info


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = " ".join(names)
    return full_name


@cyber(outgoing=True, disable_errors=True, groups_only=True, pattern=r"^\.inviteall (.*)")
async def get_users(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await event.edit("```Bunu C Y B Ξ R Support 🇦🇿 qrupunda edə bilməzsiniz.```")
    sender = await event.get_sender()
    me = await event.client.get_me()
    if not sender.id == me.id:
        cyber = await event.edit("`Qrupu axtarıram...`")
    else:
        cyber = await event.edit("`İstifadəçilər əlavə edilir...`")
    farid = await get_chatinfo(event)
    chat = await event.get_chat()
    if event.is_private:
        return await cyber.edit("`Bağışlayın qeyd etdiyiniz qrupda istifadəçi yoxdur.`")
    s = 0
    f = 0
    error = "None"

    await cyber.edit("**C Y B Ξ R SCRAPER**\n\n`İstifadəçilər əlavə edilir...`")
    async for user in event.client.iter_participants(farid.full_chat.id):
        try:
            if error.startswith("Too"):
                return await cyber.edit(
                    f"**C Y B Ξ R**\n `Böyük ehtimalla spam olmusunuz @spambot-a /start yazın.` \nXəta: \n`{error}` \n\n `{s}` istifadəçi əlavə edildi.\n `{f}` istifadəçini əlavə etmək olmadı."
                )
            await event.client(
                functions.channels.InviteToChannelRequest(channel=chat, users=[user.id])
            )
            s = s + 1
            await cyber.edit(
                f"**C Y B Ξ R**\n\n`{s}` istifadəçi əlavə edildi.\n`{f}` istifadəçini əlavə etmək olmadı\n\n**Xəta:** `{error}`"
            )
        except Exception as e:
            error = str(e)
            f = f + 1
    return await cyber.edit(
        f"**C Y B Ξ R** \n\nUğurla `{s}` istifadəçi əlavə edildi.\nUğursuz olan istifadəçilərin sayı: `{f}`"
    )


CmdHelp('scraper').add_command(
    'inviteall', '<daşıyacağınız qrupun istifadəçi adı>', 'Qeyd etdiyiniz qrupdaki istifadəçiləri olduğunuz qrupa əlavə edər.'
).add()
