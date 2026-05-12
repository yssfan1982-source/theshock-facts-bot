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
    markup.add(btn1, btn2, btn3)
    
    welcome_msg = (
        "✨ أهلاً بك في بوت (حقائق الصدق) ✨\n\n"
        "هذا البوت مخصص لنشر علوم العترة الطاهرة وسيرة أهل البيت عليهم السلام.\n"
        "يرجى اختيار القسم الذي ترغب في تصفحه من القائمة أدناه:"
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == 'علوم العترة':
        msg = (
            "📖 **علوم العترة الطاهرة**\n\n"
            "قال رسول الله (ص): 'إني تارك فيكم الثقلين: كتاب الله، وعترتي أهل بيتي'.\n\n"
            "علوم العترة هي المنهج الصافي لفهم القرآن والسنة النبوية. تشمل هذه العلوم:\n"
            "1. التفسير الباطني والظاهري للقرآن.\n"
            "2. الأحكام الشرعية المستنبطة من نهجهم.\n"
            "3. الأخلاق والمعارف الإلهية التي ورثوها عن جدهم المصطفى (ص)."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'حديث الكساء':
        msg = (
            "🛡️ **حديث الكساء الشريف**\n\n"
            "هو الحديث المتواتر الذي يثبت فضائل أهل بيت النبوة (خمسة أصحاب الكساء).\n\n"
            "يروي هذا الحديث جمع النبي (ص) لعلي وفاطمة والحسن والحسين عليهم السلام تحت الكساء، "
            "ونزول آية التطهير: {إِنَّمَا يُرِيدُ اللَّهُ لِيُذْهِبَ عَنْكُمُ الرِّجْسَ أَهْلَ الْبَيْتِ وَيُطَهِّرَكُمْ تَطْهِيرًا}."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'الإمام جعفر الصادق':
        msg = (
            "💡 **الإمام جعفر الصادق (عليه السلام)**\n\n"
            "هو الإمام السادس من أئمة أهل البيت، ومؤسس المذهب الجعفري.\n\n"
            "في عهده ازدهرت العلوم الإسلامية والطبيعية، وتخرج من مدرسته آلاف العلماء في شتى المجالات "
            "(مثل الكيمياء لـ جابر بن حيان، والفقه والتوحيد).\n"
            "يُعرف بـ 'صادق العترة' لأمانته وعمق علمه الذي ملأ الآفاق."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

# تشغيل البوت
print("البوت يعمل الآن ومستعد لنشر علوم العترة...")
bot.remove_webhook()
bot.infinity_polling()
