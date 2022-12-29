import re 
import os
from pytgcalls import GroupCallFactory
from pyrogram import Client, filters
from pyrogram.types import Message
# from py_youtube import ytdl
from py_youtube import ytdl 

API_ID = os.environ.get("API_ID",11973721)
API_HASH = os.environ.get("API_HASH","5264bf4663e9159565603522f58d3c18")
SESSION_NAME = os.environ.get("SESSION_NAME","BQBMOPAM9e7_BXQzX9V6HtORfNj02_pqSw9jKvwzX_EtEK2083CTBOTsuiqAHZ9x1reOUEfvY2VMR14McoYh-FfmYmK_gcixijSCMzojE5GNekocsZ-14eOWPisl_xg9E0DRyxOSKWzP7dTYiXUhI1UQfz1xdA7DIbZzTgr73UvPr_Ipvq1YnTxQn_kFzeSRc8OXD8AhNZ1ayaOdm76tioan99_wluQznX5AI3aywIu78C21E9va4BuwVIMXL9BWKsXoqgO-4n_NcEkqHuMgHwAB_buLbuU_ou0jxIW7_Jh_be0dH4mJKyXioNl09q_EerdcWz_3LyFgnNVZozPDzWMYUvF4PAA")
CHAT = os.environ.get("CHAT","1391556668")
ADMIN = int(os.environ.get("ADMIN", -1001715180239))

app = Client(SESSION_NAME, API_ID, API_HASH)

group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)
VIDEO_CALL = {}

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["start"]))
async def start(client, m: Message):
	await m.reply("Hello Start Stream Video Using Command /play(reply_to_message) and /stop\n  ")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["play"]))
async def play(client, m: Message):
	if (m.reply_to_message):
			link = m.reply_to_message.text
			youtube_regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
			youtube_regex_match = re.match(youtube_regex, link)
			if youtube_regex_match:
				             try:
				             	video_url = ytdl(link).besturl()
				             except Exception as e:
				             	await m.reply(f"**Error** -- `{e}`")
				             	return
				             try:
				             	group_call = group_call_factory.get_group_call()
				             	await group_call.join(CHAT)
				             	await group_call.start_video(video_url,enable_experimental_lip_sync=True)
				             	VIDEO_CALL[CHAT] = group_call
				             	await m.reply("**Started  Streaming!**")
				             except Exception as e:
				             	await m.reply(f"**Error** -- `{e}`")
				             	
					
			else:
			         	try:
			         		group_call = group_call_factory.get_group_call()
			         		await group_call.join(CHAT)
			         		await group_call.start_video(link,enable_experimental_lip_sync=True)
			         		VIDEO_CALL[CHAT] = group_call
			         		await m.reply("** Started Streaming!**")
			         	except Exception as e:
			         	    	await m.reply(f"**Error** -- `{e}`")
				             	
@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["livestream"]))
async def livestream(client, m: Message):
	if (m.reply_to_message):
			link = m.reply_to_message.text
			youtube_regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
			youtube_regex_match = re.match(youtube_regex, link)
			if youtube_regex_match:
				             try:
				             	video_url = ytdl(link).besturl()
				             except Exception as e:
				             	await m.reply(f"**Error** -- `{e}`")
				             	return
				             try:
				             	group_call = group_call_factory.get_group_call()
				             	await group_call.join(CHAT)
				             	await group_call.start_video(video_url,enable_experimental_lip_sync=False)
				             	VIDEO_CALL[CHAT] = group_call
				             	await m.reply("**Started  Streaming!**")
				             except Exception as e:
				             	await m.reply(f"**Error** -- `{e}`")
				             	
					
			else:
			         	try:
			         		group_call = group_call_factory.get_group_call()
			         		await group_call.join(CHAT)
			         		await group_call.start_video(link,enable_experimental_lip_sync=False)
			         		VIDEO_CALL[CHAT] = group_call
			         		await m.reply("** Started Streaming!**")
			         	except Exception as e:
			         	    	await m.reply(f"**Error** -- `{e}`")




@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["stop"]))
async def stop (client, m: Message):
	try:
	       await VIDEO_CALL[CHAT].stop()
	       await m.reply("** Stopped Streaming!**")
	except Exception as e:
		await m.reply(f"**Error** - `{e}`")
