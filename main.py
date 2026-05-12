import telebot
from telebot import types
import http.server
import socketserver
import threading
import os

# --- إعداد منفذ وهمي لمنصة Render لضمان استمرار البوت ---
def run_dummy_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()

# تشغيل السيرفر الوهمي في خلفية الكود
threading.Thread(target=run_dummy_server, daemon=True).start()

# --- إعداد البوت الخاص بك ---
TOKEN = '8788666843:AAEMthDUv8sNO8nF1rg0fzVo3eYi6EB_K24'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('علوم العترة')
    btn2 = types.KeyboardButton('حديث الكساء')
    btn3 = types.KeyboardButton('الإمام جعفر الصادق')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "أهلاً بك في بوت حقائق الصدق. اختر أحد الأقسام التالية:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == 'علوم العترة':
        bot.reply_to(message, "قريباً سيتم إضافة محتوى علوم العترة هنا.")
    elif message.text == 'حديث الكساء':
        bot.reply_to(message, "قريباً سيتم إضافة شرح حديث الكساء.")
    elif message.text == 'الإمام جعفر الصادق':
        bot.reply_to(message, "قريباً سيتم إضافة سيرة الإمام الصادق عليه السلام.")

# تشغيل البوت
print("البوت يعمل الآن...")
bot.infinity_polling()
