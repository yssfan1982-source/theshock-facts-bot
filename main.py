import telebot
from telebot import types
import http.server
import socketserver
import threading
import os
import random

# --- إعداد منفذ وهمي لمنصة Render ---
def run_dummy_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# --- إعداد البوت ---
TOKEN = '8788666843:AAEMthDUv8sNO8nF1rg0fzVo3eYi6EB_K24'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('علوم العترة')
    btn2 = types.KeyboardButton('حديث الكساء')
    btn3 = types.KeyboardButton('الإمام جعفر الصادق')
    btn4 = types.KeyboardButton('أقوال وحكم')
    markup.add(btn1, btn2, btn3, btn4)
    
    welcome_msg = "✨ أهلاً بك في بوت (حقائق الصدق) ✨\n\nمنصة معرفية لنشر علوم أهل البيت (ع).\nاختر قسماً من القائمة:"
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == 'علوم العترة':
        msg = "📖 **حديث الثقلين: المرجعية والمسار التاريخي**\n\n\"إني تارك فيكم ما إن تمسكتم به لن تضلوا بعدي أبداً: كتاب الله وعترتي أهل بيتي\""
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'حديث الكساء':
        msg = "🛡️ **حديث الكساء: آية التطهير ودلالة الاصطفاء**\n\nنزلت فيه آية التطهير {إِنَّمَا يُرِيدُ اللَّهُ...} لتعيين المرجعية المعصومة."
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'الإمام جعفر الصادق':
        msg = (
            "💡 **الإمام جعفر الصادق (ع): رائد النهضة العلمية**\n\n"
            "أسس جامعة المدينة المنورة التي ضمت 4000 طالب، وشملت دروسه الكيمياء والطب والفلك بالإضافة للفقه.\n\n"
            "🧪 **جابر بن حيان:** تلميذه الذي نقل عنه أصول الكيمياء.\n"
            "📚 **الأصول الأربعمائة:** هي تدوينات تلاميذه التي حفظت التراث النبوي."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'أقوال وحكم':
        quotes = [
            "💎 \"العلم خزانة، ومفاتيحها السؤال.\"",
            "💎 \"من قنع بما رزقه الله فهو من أغنى الناس.\"",
            "💎 \"لكل شيء زكاة، وزكاة العلم أن يعلمه أهله.\"",
            "💎 \"ما قدم عبد على الله بشيء أحب إليه من حسن الخلق.\""
        ]
        bot.reply_to(message, message.chat.id, random.choice(quotes))

bot.remove_webhook()
bot.infinity_polling()
