from pyrogram import Client, filters
import pytgcalls
import subprocess, pafy, os
if os.path.exists('newton.raw'):
    os.remove('newton.raw')
app = Client('Newton',2622293,'519569630746dfca366a4545197e5e11')
@app.on_message()
async def join(_, message):
    if message.text == '/call':
        if message.from_user.id == 989310142:
            if message.reply_to_message:
                if 'https://youtu.be/' in message.reply_to_message.text:
                    if os.path.exists('newton.raw'):
                        os.remove('newton.raw')
                    await message.reply_text('جاري التحميل : '+pafy.new(message.reply_to_message.text).title)
                    subprocess.call('ffmpeg -i "$(youtube-dl -x -g "'+message.reply_to_message.text+'")" -f s16le -ac 2 -ar 48000 -acodec pcm_s16le newton.raw', shell=True)
                    await pytgcalls.GroupCall(app,input_filename='newton.raw').start(-1001131674840)
                    await message.reply_text('تم التشغل ...')
                else:
                    await message.reply_text('الرابط غير مدعوم')
            else:
                await message.reply_text('لم يتم ارسال رابط او الرد عليه')
        else:
            await message.reply_text("الامر غير صالح لك")
    elif message.text == '/stop':
        await message.reply_text('تم الايقاف')
        os.remove('newton.raw')
        os.remove('group_call.log')
app.run()