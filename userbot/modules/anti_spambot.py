# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# CYBERUSERBOT - FARIDDADASHZADE
#

from asyncio import sleep
from requests import get

from telethon.events import ChatAction
from telethon.tl.types import ChannelParticipantsAdmins, Message

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, ANTI_SPAMBOT, ANTI_SPAMBOT_SHOUT, bot


@bot.on(ChatAction)
async def anti_spambot(welcm):
    try:
        if not ANTI_SPAMBOT:
            return
        if welcm.user_joined or welcm.user_added:
            adder = None
            ignore = False
            users = None

            if welcm.user_added:
                ignore = False
                try:
                    adder = welcm.action_message.from_id
                except AttributeError:
                    return

            async for admin in bot.iter_participants(
                    welcm.chat_id, filter=ChannelParticipantsAdmins):
                if admin.id == adder:
                    ignore = True
                    break

            if ignore:
                return

            elif welcm.user_joined:
                users_list = hasattr(welcm.action_message.action, "users")
                if users_list:
                    users = welcm.action_message.action.users
                else:
                    users = [welcm.action_message.from_id]

            await sleep(5)
            spambot = False

            if not users:
                return

            for user_id in users:
                async for message in bot.iter_messages(welcm.chat_id,
                                                       from_user=user_id):

                    correct_type = isinstance(message, Message)
                    if not message or not correct_type:
                        break

                    join_time = welcm.action_message.date
                    message_date = message.date

                    if message_date < join_time:
                        # E??er mesaj kullan??c?? kat??lma tarihinden daha ??nce ise yoksay??l??r.
                        continue

                    check_user = await welcm.client.get_entity(user_id)

                    # Hata ay??klama. ??lerideki durumlar i??in b??rak??ld??. ###
                    print(
                        f"Kat??lan kullan??c??: {check_user.first_name} [ID: {check_user.id}]"
                    )
                    print(f"Sohbet: {welcm.chat.title}")
                    print(f"Zaman: {join_time}")
                    print(
                        f"G??nderdi??i mesaj: {message.text}\n\n[Zaman: {message_date}]"
                    )
                    ##############################################

                    try:
                        cas_url = f"https://combot.org/api/cas/check?user_id={check_user.id}"
                        r = get(cas_url, timeout=3)
                        data = r.json()
                    except BaseException:
                        print(
                            "CAS kontrol?? ba??ar??s??z, eski anti_spambot kontrol??ne d??n??l??yor."
                        )
                        data = None
                        pass

                    if data and data['ok']:
                        reason = f"[Combot Anti Spam taraf??ndan banland??.](https://combot.org/cas/query?u={check_user.id})"
                        spambot = True
                    elif "t.cn/" in message.text:
                        reason = "`t.cn` URL'leri tespit edildi."
                        spambot = True
                    elif "t.me/joinchat" in message.text:
                        reason = "Potansiyel reklam mesaj??"
                        spambot = True
                    elif message.fwd_from:
                        reason = "Ba??kas??ndan iletilen mesaj"
                        spambot = True
                    elif "?start=" in message.text:
                        reason = "Telegram botu `start` linki"
                        spambot = True
                    elif "bit.ly/" in message.text:
                        reason = "`bit.ly` URL'leri tespit edildi."
                        spambot = True
                    else:
                        if check_user.first_name in ("Bitmex", "Promotion",
                                                     "Information", "Dex",
                                                     "Announcements", "Info",
                                                     "Duyuru", "Duyurular"
                                                     "Bilgilendirme", "Bilgilendirmeler"):
                            if check_user.last_name == "Bot":
                                reason = "Bilinen SpamBot"
                                spambot = True

                    if spambot:
                        print(f"Potansiyel Spam Mesaj??: {message.text}")
                        await message.delete()
                        break

                    continue  # Bir sonraki mesaj?? kontrol et

            if spambot:
                chat = await welcm.get_chat()
                admin = chat.admin_rights
                creator = chat.creator
                if not admin and not creator:
                    if ANTI_SPAMBOT_SHOUT:
                        await welcm.reply(
                            "@admins\n"
                            "`ANTI SPAMBOT TESP??T ED??LD??!\n"
                            "BU KULLANICI BEN??M SPAMBOT ALGOR??TMALARIMLA E??LE????YOR!`"
                            f"SEBEP: {reason}")
                        kicked = False
                        reported = True
                else:
                    try:

                        await welcm.reply(
                            "`Potansiyel Spambot Tespit Edildi !!`\n"
                            f"`SEBEP:` {reason}\n"
                            "??u anl??k gruptan kickleniyor, bu ID ilerideki durumlar i??in kaydedilecek.\n"
                            f"`KULLANICI:` [{check_user.first_name}](tg://user?id={check_user.id})"
                        )

                        await welcm.client.kick_participant(
                            welcm.chat_id, check_user.id)
                        kicked = True
                        reported = False

                    except BaseException:
                        if ANTI_SPAMBOT_SHOUT:
                            await welcm.reply(
                                "@admins\n"
                                "`ANTI SPAMBOT TESP??T ED??LD??!\n"
                                "BU KULLANICI BEN??M SPAMBOT ALGOR??TMALARIMLA E??LE????YOR!`"
                                f"SEBEP: {reason}")
                            kicked = False
                            reported = True

                if BOTLOG:
                    if kicked or reported:
                        await welcm.client.send_message(
                            BOTLOG_CHATID, "#ANTI_SPAMBOT RAPORU\n"
                            f"Kullan??c??: [{check_user.first_name}](tg://user?id={check_user.id})\n"
                            f"Kullan??c?? IDsi: `{check_user.id}`\n"
                            f"Sohbet: {welcm.chat.title}\n"
                            f"Sohbet IDsi: `{welcm.chat_id}`\n"
                            f"Sebep: {reason}\n"
                            f"Mesaj:\n\n{message.text}")
    except ValueError:
        pass


CMD_HELP.update({
    'anti_spambot':
    "Kullan??m: Bu mod??l config.env dosyas??nda ya da env de??eri ile etkinle??tirilmi??se,\
        \ne??er bu spamc??lar UserBot'un anti-spam algoritmas??yla e??le??iyorsa, \
        \nbu mod??l gruptaki spamc??lar?? gruptan yasaklar (ya da adminlere bilgi verir)."
})
