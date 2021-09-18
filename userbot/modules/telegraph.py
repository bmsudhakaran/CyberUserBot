# Copyright (C) 2021 CYBER USERBOT.
#
# Licensed under the General Public License, Version 3.0;
# you may not use this file except in compliance with the License.

# CYBERUSERBOT - FaridDadashzade
#

import os

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file

from userbot import TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp


telegraph = Telegraph()
r = telegraph.create_account(short_name="telegraph")
auth_url = r["auth_url"]


@register(outgoing=True, pattern=r"^\.tg (med|text)$")
async def telegraph(graph):
    await graph.edit("`Hazırlanır...`")
    if not graph.text[0].isalpha() and graph.text[0] not in ("/", "#", "@", "!"):
        if graph.fwd_from:
            return
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
            os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        if graph.reply_to_msg_id:
            r_message = await graph.get_reply_message()
            input_str = graph.pattern_match.group(1)
            if input_str == "med":
                downloaded_file_name = await bot.download_media(
                    r_message, TEMP_DOWNLOAD_DIRECTORY
                )
                await graph.edit(f"Yükləndi `{downloaded_file_name}`.")
                if downloaded_file_name.endswith(".webp"):
                    resize_image(downloaded_file_name)
                try:
                    media_urls = upload_file(downloaded_file_name)
                except exceptions.TelegraphException as exc:
                    await graph.edit("Xəta: " + str(exc))
                    os.remove(downloaded_file_name)
                else:
                    os.remove(downloaded_file_name)
                    await graph.edit(
                        f"Uğurla yükləndi!\n[telegra.ph](https://telegra.ph{media_urls[0]}).",
                        link_preview=True,
                    )
            elif input_str == "text":
                user_object = await bot.get_entity(r_message.sender_id)
                title_of_page = user_object.first_name
                page_content = r_message.message
                if r_message.media:
                    if page_content != "":
                        title_of_page = page_content
                    downloaded_file_name = await bot.download_media(
                        r_message, TEMP_DOWNLOAD_DIRECTORY
                    )
                    m_list = None
                    with open(downloaded_file_name, "rb") as fd:
                        m_list = fd.readlines()
                    for m in m_list:
                        page_content += m.decode("UTF-8") + "\n"
                    os.remove(downloaded_file_name)
                page_content = page_content.replace("\n", "<br>")
                response = telegraph.create_page(
                    title_of_page, html_content=page_content
                )
                await graph.edit(
                    "Uğurla yükləndi!\n"
                    f"[telegra.ph](https://telegra.ph/{response['path']}).",
                    link_preview=True,
                )
        else:
            await graph.edit("`Daimi bir telegra.ph bağlantısı əldə etmək üçün bir mesaja cavab verin.`")


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


CmdHelp('telegraph').add_command(
    'tg', '<med/text>', 'Mesaja yanıt verərək .tg text (yazı) və ya .tg med (mediya) yazaraq Telegrapha yükləyin.'
).add()    
