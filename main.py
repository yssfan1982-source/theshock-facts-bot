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
    btn1 = types.KeyboardButton('الـ 500 عام الذهبية')
    btn2 = types.KeyboardButton('الأئمة الأربعة والآل')
    btn3 = types.KeyboardButton('كشف مستور المحاكمات')
    btn4 = types.KeyboardButton('أصل فتنة التجسيم')
    btn5 = types.KeyboardButton('أعلام العترة')
    btn6 = types.KeyboardButton('أقوال وحكم')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    
    welcome_msg = (
        "✨ بوت (حقائق الصدق) | مشروع كشف الحقائق ✨\n\n"
        "منصة توثيقية تعيد قراءة التاريخ الإسلامي بعيداً عن الجفاء وتزييف الحقائق.\n"
        "اختر المقال البحثي الذي تود الاطلاع على مصادره:"
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    
    if message.text == 'الـ 500 عام الذهبية':
        msg = (
            "📜 **المقال الأول: عصر ما قبل المنهاج**\n\n"
            "عاشت الأمة 500 عام من الانسجام تحت مظلة المذاهب الأربعة والعترة النبوية قبل ظهور فتنة 'الجفاء'.\n\n"
            "📚 **المصادر والمراجع:**\n"
            "• **تاريخ الإسلام** للذهبي: (بيان استقرار المذاهب والأعصار).\n"
            "• **البداية والنهاية** لابن كثير: (حوادث القرون 3-7 هـ).\n"
            "• **الخطط المقريزية**: (في وصف تلاحم المجتمع مع آل البيت)."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'الأئمة الأربعة والآل':
        msg = (
            "💡 **المقال الثاني: مواقف الأئمة الأربعة العملية**\n\n"
            "نصر الأئمة العترة فعلياً؛ فأبو حنيفة نصر زيد بن علي، والشافعي قصد نفيسة العلم.\n\n"
            "📚 **المصادر والمراجع:**\n"
            "• **سير أعلام النبلاء** للذهبي: (تراجم الأئمة الأربعة وعلاقتهم بالآل).\n"
            "• **مناقب الخوارزمي**: (تفصيل نصرة أبي حنيفة للإمام زيد).\n"
            "• **وفيات الأعيان** لابن خلكان: (توثيق صلاة الشافعي خلف السيدة نفيسة)."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'كشف مستور المحاكمات':
        msg = (
            "⚖️ **المقال الثالث: حقيقة محاكمات ابن تيمية**\n\n"
            "سجن ابن تيمية كان بقرار فقهي سني من قضاة المذاهب الأربعة (ابن مخلوف وابن جماعة).\n\n"
            "📚 **المصادر والمراجع:**\n"
            "• **الدرر الكامنة** لابن حجر العسقلاني: (تفصيل المحاكمة وسببها).\n"
            "• **البداية والنهاية** لابن كثير: (حوادث سنة 705 هـ وما بعدها).\n"
            "• **دفع شبه من شبه وتمرد** للحصني الدمشقي: (بيان موقف العلماء من جفاء المنهاج)."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'أصل فتنة التجسيم':
        msg = (
            "⚠️ **أصل الفتنة: التنزيه vs التجسيم**\n\n"
            "الصراع بين الأشاعرة وبين فكر ابن تيمية حول حقيقة الذات الإلهية.\n\n"
            "📚 **المصادر والمراجع:**\n"
            "• **دفع شبه التشبيه** لابن الجوزي (الحنبلي): (في الرد على المجسمة).\n"
            "• **الفرق بين الفرق** للبغدادي: (تأصيل عقيدة أهل السنة والجماعة).\n"
            "• **طبقات الشافعية الكبرى** للسبكي: (بيان انحرافات ابن تيمية العقدية)."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'أعلام العترة':
        msg = "🌟 **محطات العترة:**\n• الإمام الصادق (ع)\n• الإمام زيد بن علي (ع)\n• السيدة نفيسة (ع)\n"
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'أقوال وحكم':
        quotes = ["💎 \"الميزان الصحيح: عترةٌ تُحب، ومذاهبُ تُتبع.\"", "💎 \"الدين حبٌ واتباع، لا نقدٌ وجفاء.\""]
        bot.reply_to(message, random.choice(quotes))

bot.remove_webhook()
bot.infinity_polling()
