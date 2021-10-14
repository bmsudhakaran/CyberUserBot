import asyncio, sys, datetime, importlib, inspect
import logging, math, os, re
from pathlib import Path
from time import gmtime, strftime
from userbot import *
from telethon import events
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

on = bot.on

def on(**args):
    def decorator(func):
        async def wrapper(event):
            await func(event)

        client.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorater
