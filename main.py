import telebot
from telebot import types
import http.server
import socketserver
import threading
import os
import random

# --- إعداد منفذ Render لضمان استمرارية البوت ---
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
    btn1 = types.KeyboardButton('المحطة 1: عصر الانسجام')
    btn2 = types.KeyboardButton('المحطة 2: الأئمة والآل')
    btn3 = types.KeyboardButton('المحطة 3: حقيقة المحاكمة')
    btn4 = types.KeyboardButton('المحطة 4: تلف الأمة المعاصر')
    btn5 = types.KeyboardButton('بيان المشروع والمصادر')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    welcome_msg = (
        "✨ بوت (حقائق الصدق) | مشروع كشف الحقائق ✨\n\n"
        "مرحباً بك في الموسوعة الرقمية لتصحيح المسار التاريخي للأمة.\n"
        "هدفنا: إظهار الحقيقة المجردة بعيداً عن الجفاء وتزييف الفكر."
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    
    if message.text == 'المحطة 1: عصر الانسجام':
        msg = (
            "🏛️ **المحطة الأولى: 500 عام من الاستقرار الذهبي**\n\n"
            "قبل ظهور فتنة المنهاج، عاشت الأمة في تناغم تام:\n"
            "✅ لم يختلف الأشاعرة والماتريدية مع المذاهب الأربعة.\n"
            "✅ كانت مودة العترة النبوية أصلاً لا يقبل التشكيك.\n"
            "✅ ساد 'أدب الإجماع' واختفى 'شذوذ المنهاج'.\n\n"
            "📚 **المراجع:** تاريخ الإسلام (الذهبي)، البداية والنهاية (ابن كثير)."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'المحطة 2: الأئمة والآل':
        msg = (
            "💡 **المحطة الثانية: مواقف الأئمة الأربعة العملية**\n\n"
            "الأئمة الأربعة لم يكونوا مجرد فقهاء، بل كانوا جنوداً في نصرة العترة:\n"
            "• **أبو حنيفة:** نصر ثورة الإمام زيد بالمال والفتوى.\n"
            "• **الشافعي:** صلى خلف السيدة نفيسة وأوصى ببركتها.\n"
            "• **مالك:** تلمذ على الصادق وأجله إجلالاً عظيماً.\n\n"
            "📚 **المراجع:** سير أعلام النبلاء (الذهبي)، وفيات الأعيان (ابن خلكان)."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'المحطة 3: حقيقة المحاكمة':
        msg = (
            "⚖️ **المحطة الثالثة: كشف مستور محاكمات ابن تيمية**\n\n"
            "سجن ابن تيمية كان بقرار 'سني جماعي' من قضاة المذاهب الأربعة:\n"
            "• **ابن مخلوف (المالكي) وابن جماعة (الشافعي):** أدانوه بسبب الجفاء في حق النبي ﷺ وآل بيته وبسبب فتنة التجسيم.\n"
            "• **السبب الحقيقي:** حماية عقيدة الأمة ووحدتها من الفكر المنفرد.\n\n"
            "📚 **المراجع:** الدرر الكامنة (ابن حجر)، دفع شبه من شبه وتمرد (الحصني الدمشقي)."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'المحطة 4: تلف الأمة المعاصر':
        msg = (
            "⚠️ **المحطة الرابعة: الواقع المعاصر و'تلف' الأمة**\n\n"
            "كيف تحول الفكر التيمي إلى أداة لتمزيق الأمة اليوم؟\n"
            "1️⃣ **استهداف الأزهر والزيتونة:** محاولة تبديع وتكفير المدارس العريقة التي حافظت على الإسلام لقرون.\n"
            "2️⃣ **صناعة الحواجز:** جعلوا 'ذكر فضائل آل البيت' تهمة بالتشيع، ليحرموا الأمة من مصدر بركتها.\n"
            "3️⃣ **فوضى الفتوى:** ضرب إجماع المذاهب الأربعة بدعوى 'اتباع الدليل' لتمكين الجهلاء من الفتوى.\n\n"
            "📚 **المراجع:** إحياء المقبور (الغماري)، مقالات الكوثري، فتاوى الأزهر الشريف."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'بيان المشروع والمصادر':
        msg = (
            "📜 **بيان مشروع كشف الحقائق**\n\n"
            "نحن لا ننتصر لفريق، بل ننتصر للحقيقة.\n"
            "الميزان الصحيح: **عترةٌ تُحب، ومذاهبُ تُتبع**.\n\n"
            "🔗 لزيارة القناة ومتابعة السلاسل البحثية كاملة، تفضل بالانضمام إلينا."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

bot.remove_webhook()
bot.infinity_polling()
