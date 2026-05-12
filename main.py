import telebot
from telebot import types
import http.server
import socketserver
import threading
import os
import random

# --- إعداد منفذ وهمي لمنصة Render لضمان استمرار البوت ---
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
    btn1 = types.KeyboardButton('استقرار الـ 500 عام')
    btn2 = types.KeyboardButton('فتنة "المنهاج" والجفاء')
    btn3 = types.KeyboardButton('حقيقة المحاكمة والسجن')
    btn4 = types.KeyboardButton('أعلام العترة والمذاهب')
    btn5 = types.KeyboardButton('أقوال وحكم')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    welcome_msg = (
        "✨ بوت (حقائق الصدق) | مشروع كشف الحقائق ✨\n\n"
        "هدفنا توضيح كيف حافظت المذاهب الأربعة على وحدة الأمة لقرون، وكيف أحدث فكر ابن تيمية شرخاً تاريخياً أضاع البوصلة.\n"
        "اختر المحطة المعرفية:"
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    
    if message.text == 'استقرار الـ 500 عام':
        msg = (
            "🏛️ **500 عام من الانسجام المذهبي**\n\n"
            "منذ تدوين المذاهب الأربعة وحتى القرن السابع الهجري، عاشت الأمة في استقرار فقهي وعقدي:\n\n"
            "✅ **وحدة المرجعية:** كانت المذاهب الأربعة هي الحصن الذي يجمع الأمة، مع تقدير كامل لمدرسة العترة النبوية.\n"
            "✅ **أدب الخلاف:** لم يخرج أحد عن الإجماع في مسائل العقيدة الكبرى أو مقام النبوة والزيارة.\n"
            "✅ **الجسر العلمي:** كان الأئمة (أبو حنيفة، مالك، الشافعي، أحمد) يرون في آل البيت منبع العلم والقدوة."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'فتنة "المنهاج" والجفاء':
        msg = (
            "⚠️ **ظهور فكر الجفاء وشق عصا الإجماع**\n\n"
            "أتى ابن تيمية بآراء شذت عن المذاهب الأربعة، مما أحدث بلبلة أضاعت الأمة:\n\n"
            "❌ **نقد الفضائل:** في 'منهاج السنة'، قلل من شأن إسلام الإمام علي (ع) ووصفه بـ'إسلام صبي'، واتهمه بالقتال لأجل السلطة (الرياسة).\n"
            "❌ **تضعيف الصحاح:** هاجم أحاديث الثقلين والموالاة التي أجمع عليها الحفاظ، لفك ارتباط الأمة بعترتها.\n"
            "❌ **الجفاء النبوي:** أثار فتنة 'منع شد الرحال' لزيارة القبر الشريف، وهو ما اعتبره الفقهاء خرقاً للأدب مع النبي ﷺ."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'حقيقة المحاكمة والسجن':
        msg = (
            "⚖️ **المحاكمة: المذاهب الأربعة في مواجهة التفرد**\n\n"
            "سجن ابن تيمية لم يكن ظلماً سياسياً، بل كان قراراً فقهياً جماعياً صيانةً للأمة:\n\n"
            "👤 **القضاة:** (ابن مخلوف المالكي، ابن جماعة الشافعي، وقضاة الحنفية والحنابلة).\n"
            "📝 **السبب:** أجمع القضاة على أن آراءه تشكل خطراً على السلم المجتمعي وتخالف العقيدة المستقرة.\n"
            "🔒 **النتيجة:** صدر الحكم بسجنه كـ'حجر شرعي' لمنع نشر الفكر الذي يفرق الأمة ويجفو مقام النبوة والعترة."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'أعلام العترة والمذاهب':
        msg = (
            "🌟 **الآل والأصحاب: ميزان الحق**\n\n"
            "• **الإمام الصادق:** المنبع الذي تلمذ عليه الأئمة وجفاه 'المنهاج'.\n"
            "• **الإمام زيد:** حليف القرآن الذي نصره أبو حنيفة وغيبه 'المنهاج'.\n"
            "• **السيدة نفيسة:** العلم الذي قصده الشافعي وحاربه فكر 'المنع' الحديث."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'أقوال وحكم':
        quotes = [
            "💎 \"الميزان الصحيح: عترةٌ تُحب، ومذاهبُ تُتبع.\" - شعار المشروع",
            "💎 \"زكاة العلم أن يعلمه أهله.\" - الإمام الصادق",
            "💎 \"الدين حبٌ واتباع، لا نقدٌ وجفاء.\""
        ]
        bot.reply_to(message, random.choice(quotes))

bot.remove_webhook()
bot.infinity_polling()
