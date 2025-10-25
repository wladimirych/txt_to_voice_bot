import telepot
from telepot.loop import MessageLoop
from gtts import gTTS
import os
import time
import logging

# Настройка логирова
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

TOKEN = 'your_tg_token'
bot = telepot.Bot(TOKEN)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    logger.info(f"📨 Получено сообщение: type={content_type}, chat_id={chat_id}")

    if content_type == 'text':
        text = msg['text']
        logger.info(f"📝 Текст сообщения: {text}")
        text_to_voice(text, chat_id)
    else:
        logger.warning(f"⚠️ Неподдерживаемый тип сообщений: {content_type}")


def text_to_voice(text, chat_id):
    try:
        logger.info(f"🔊 Генерация аудио для текста: {text[:50]}...")
        tts = gTTS(text=text, lang='ru')
        tts.save('voice.mp3')

        logger.info(f"📤 Отправка аудио в чат {chat_id}")
        with open('voice.mp3', 'rb') as audio:
            bot.sendAudio(chat_id, audio)

        os.remove('voice.mp3')
        logger.info(f"✅ Аудио успешно отправлено в чат {chat_id}")
    except Exception as e:
        logger.error(f"❌ Ошибка при обработке: {e}", exc_info=True)


MessageLoop(bot, handle).run_as_thread()
logger.info("🤖 Бот успешно запущен и ожидает сообщения...")

while True:
    time.sleep(8)