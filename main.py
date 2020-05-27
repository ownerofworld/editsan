from telegram import File, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import os
import requests
from subprocess import Popen, PIPE
import json

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',

                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "999846356:AAFovHyEha6j4q_1G4-PLjU8xeaM8QttjMM"

try:  
  os.system('mkdir downloads')
  os.system('cd downloads')
except:
  pass

def photo(bot, update):
    try:  
      media_id = update.effective_message.photo[-1].file_id
      newFile = bot.getFile(media_id)
      fileName = os.path.split(newFile.file_path)[-1]
      newFile.download(fileName)
      bot.sendMessage(chat_id=update.message.chat_id, text="Downloaded, Trying To Upload On AnonFile")
      stdout = Popen(f'curl -F "file=@{fileName}" https://api.anonfiles.com/upload', shell=True, stdout=PIPE).stdout
      output = stdout.read()
      visit = json.loads(output)
      full_link = visit['data']['file']['url']['full']
      short_link = visit['data']['file']['url']['short']
      messagee = f'''❤️ <b>Succesfully Uploaded</b>

      Short Link :- {short_link}
      Full Link :- {full_link}
      '''

      update.message.reply_text(messagee, parse_mode=ParseMode.HTML)
    except:
      update.message.reply_text("Kindly Send Me Photos Less Then 20 MB")
    try:
      os.remove(fileName)
    except:
      pass
    
def documentt(bot, update):
  try:
      media_id = update.effective_message.document.file_id
      newFile = bot.getFile(media_id)
      fileName = os.path.split(newFile.file_path)[-1]
      newFile.download(fileName)
      bot.sendMessage(chat_id=update.message.chat_id, text="Downloaded, Trying To Upload On AnonFile")
      stdout = Popen(f'curl -F "file=@{fileName}" https://api.anonfiles.com/upload', shell=True, stdout=PIPE).stdout
      output = stdout.read()
      visit = json.loads(output)
      full_link = visit['data']['file']['url']['full']
      short_link = visit['data']['file']['url']['short']
      messagee = f'''❤️ <b>Succesfully Uploaded</b>

      Short Link :- {short_link}
      Full Link :- {full_link}
      '''

      update.message.reply_text(messagee, parse_mode=ParseMode.HTML)
    except:
      update.message.reply_text("Kindly Send Me Photos Less Then 20 MB")
  try:
      os.remove(fileName)
  except:
      pass
def main():
  updater = Updater(TOKEN)
  dp = updater.dispatcher
  dp.add_handler(MessageHandler(Filters.photo, photo))
  updater.start_polling()
  logging.info("Starting Long Polling!")
  updater.idle()

if __name__=='__main__':
  main()
