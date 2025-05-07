
# 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
#
# qwen/qwen3-4b:free

import telebot
import requests
import json
import time
import threading

# Конфигурация
BOT_TOKEN = "7837655156:AAEYFtHrBHTXM1fs5Am-JxzyBtXQj_U8z5c"
OPENROUTER_API_KEY = "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"
MODEL_NAME = "qwen/qwen3-4b:free"

bot = telebot.TeleBot(BOT_TOKEN)


class ThinkingIndicator:
	def __init__(self, bot, chat_id):
		self.bot = bot
		self.chat_id = chat_id
		self.message_id = None
		self.stop_event = threading.Event()

	def start(self):
		"""Показывает сообщение 'Бот думает...'"""
		msg = self.bot.send_message(self.chat_id, "🤖 Котик думает...")
		self.message_id = msg.message_id

	def stop(self):
		"""Удаляет сообщение 'Бот думает...'"""
		if self.message_id:
			try:
				self.bot.delete_message(self.chat_id, self.message_id)
			except:
				pass  # Если сообщение уже удалено
		self.stop_event.set()


def generate_with_ai(prompt):
	headers = {
		"Authorization": f"Bearer {OPENROUTER_API_KEY}",
		"Content-Type": "application/json"
	}

	payload = {
		"model": MODEL_NAME,
		"messages": [{"role": "user", "content": prompt}],
		"temperature": 0.7
	}

	try:
		response = requests.post(
			"https://openrouter.ai/api/v1/chat/completions",
			headers=headers,
			data=json.dumps(payload),
			timeout=30)

		if response.status_code == 200:
			return response.json()['choices'][0]['message']['content']
		return "Не удалось получить ответ от ИИ"

	except Exception as e:
		return f"Ошибка: {str(e)}"


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_chat_action(message.chat.id, 'typing')
	time.sleep(1)
	welcome_text = """
Привет! Я умный бот с функциями:
- Отвечаю на приветствия
- Рассказываю анекдоты (/anekdot)
- Могу поддержать беседу

Используй /help для списка команд
"""
	bot.send_message(message.chat.id, welcome_text)


@bot.message_handler(commands=['anekdot'])
def tell_joke(message):
	indicator = ThinkingIndicator(bot, message.chat.id)
	indicator.start()

	try:
		prompt = "Расскажи свежий анекдот (только текст, без пояснений)"
		joke = generate_with_ai(prompt)
		bot.send_message(message.chat.id, joke)
	finally:
		indicator.stop()


@bot.message_handler(func=lambda message: True)
def handle_message(message):
	if "привет" in message.text.lower():
		bot.send_chat_action(message.chat.id, 'typing')
		time.sleep(1)
		bot.send_message(message.chat.id, "Привет-привет! 😊")
	else:
		indicator = ThinkingIndicator(bot, message.chat.id)
		indicator.start()

		try:
			response = generate_with_ai(message.text)
			bot.send_message(message.chat.id, response)
		finally:
			indicator.stop()


bot.infinity_polling()