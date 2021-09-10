"""
CYBERUSERBOT 
FARIDXZ
"""

from telethon.tl.types import ChannelParticipantsAdmins as cp
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from time import sleep

dayandir = False
msjcgr = None
taglimit = 500

@register(outgoing=True, pattern="^.tag(?: |$)(.*)")
async def _(q):
	global dayandir
	global msjcgr
	if q.fwd_from:
		return
	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	msjcgr = True
	await q.delete()
	async for i in bot.iter_participants(chat):
		if dayandir:
			dayandir=False
			msjcgr = None
			break
		if a_ == taglimit:
			dayandir=False
			msjcgr = None
			break
		a_+=1
		await q.client.send_message(q.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		if taglimit <= 500:
			sleep(1)
		if taglimit > 500:
			sleep(2)


@register(outgoing=True, pattern="^.alladmin(?: |$)(.*)")
async def _(q):
	global dayandir
	global msjcgr

	if q.fwd_from:
		return
	if q.pattern_match.group(1):
		seasons = q.pattern_match.group(1)
	else:
		seasons = ""

	chat = await q.get_input_chat()
	a_=0
	msjcgr = True
	await q.delete()
	async for i in bot.iter_participants(chat, filter=cp):
		if dayandir:
			dayandir=False
			msjcgr = None
			break
		if a_ == taglimit:
			dayandir=False
			msjcgr = None
			break
		a_+=1
		await q.client.send_message(q.chat_id, "[{}](tg://user?id={}) {}".format(i.first_name, i.id, seasons))
		if taglimit <= 500:
			sleep(1)
		if taglimit > 500:
			sleep(2)

@register(outgoing=True, pattern="^.stop$")
async def _(q):
	global dayandir
	if msjcgr == None:
		await q.edit("`Siz tag prosesini başlatmamısınız.`")
		return

	dayandir = True
	await q.edit("`Tag prosesi dayandırıldı!`")
	

@register(outgoing=True, pattern=".taglimit(?: |$)(.*)$")
async def _(q):
	global taglimit
	if q.pattern_match.group(1):
		pass

	else:
		return await q.edit("`Xahiş edirəm bir dəyər verin.`")

	try:
		limit=int(q.pattern_match.group(1))
	except:
		await q.edit("`Xahiş edirəm bir dəyər verin.`")
		return

	taglimit=limit
	await q.edit("`Tag etmə limitiniz {}-ə ayarlandı.`".format(str(limit)))
