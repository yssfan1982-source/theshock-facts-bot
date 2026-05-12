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
    btn1 = types.KeyboardButton('استقرار الـ 500 عام')
    btn2 = types.KeyboardButton('فتنة "المنهاج" والجفاء')
    btn3 = types.KeyboardButton('شهادات كبار الحفاظ')
    btn4 = types.KeyboardButton('حقيقة المحاكمة والسجن')
    btn5 = types.KeyboardButton('أعلام العترة والمذاهب')
    btn6 = types.KeyboardButton('أقوال وحكم')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    
    welcome_msg = (
        "✨ بوت (حقائق الصدق) | مستشارك في كشف الحقائق ✨\n\n"
        "هنا تجد الحقيقة المجردة: كيف حفظت المذاهب وحدة الأمة، وكيف شذّ 'المنهاج' عن الإجماع.\n"
        "اختر المحطة المعرفية:"
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    
    if message.text == 'استقرار الـ 500 عام':
        msg = (
            "🏛️ **500 عام من الانسجام المذهبي**\n\n"
            "منذ تدوين المذاهب الأربعة وحتى القرن السابع الهجري، عاشت الأمة في استقرار فقهي وعقدي تحت مظلة:\n"
            "✅ **أدب الخلاف:** احترام مرجعية العترة النبوية وتقدير الأئمة الأربعة لآل البيت.\n"
            "✅ **وحدة الصف:** لم يُعرف الجفاء السياسي أو تضعيف فضائل الإمام علي (ع) إلا مع ظهور آراء ابن تيمية المنفردة."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'شهادات كبار الحفاظ':
        msg = (
            "📜 **شهادات علماء السنة ضد فكر الجفاء**\n\n"
            "لم يكن نقد ابن تيمية طائفياً، بل كان نقداً من كبار أئمة السنة أنفسهم:\n\n"
            "🔹 **ابن حجر العسقلاني:** وصف بعض كلامه في 'المنهاج' بأنه جفاء في حق أمير المؤمنين.\n"
            "🔹 **الإمام الذهبي (تلميذه):** عاتبه في 'النصيحة الذهبية' على تطاوله على العلماء وتفرده بالرأي.\n"
            "🔹 **الحصني الدمشقي:** ألف كتاباً كاملاً للرد على ما اعتبره تنقصاً من مقام النبوة والعترة."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'فتنة "المنهاج" والجفاء':
        msg = (
            "⚠️ **شق عصا الإجماع وضياع الأمة**\n\n"
            "ابن تيمية خرق انسجام المذاهب بآراء أحدثت شرخاً تاريخياً:\n"
            "❌ **تضعيف الصحاح:** هاجم أحاديث الثقلين والموالاة لفك ارتباط الأمة بعترتها.\n"
            "❌ **الجفاء النبوي:** أثار فتنة 'منع الزيارة'، مما خرق الأدب المستقر مع الجناب النبوي لقرون."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'حقيقة المحاكمة والسجن':
        msg = (
            "⚖️ **المحاكمة: قرار فقهي سني خالص**\n\n"
            "سجن ابن تيمية كان بقرار من **قضاة المذاهب الأربعة** (ابن مخلوف، ابن جماعة، وغيرهم).\n"
            "📝 **السبب:** حماية وحدة الأمة وصيانة العقيدة من الأفكار التي تسبب الفرقة والجفاء."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'أعلام العترة والمذاهب':
        msg = "🌟 **الآل والأصحاب:**\n• الإمام الصادق: منبع المذاهب.\n• الإمام زيد: حليف القرآن.\n• السيدة نفيسة: العلم الذي قصده الشافعي."
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'أقوال وحكم':
        quotes = ["💎 \"الميزان الصحيح: عترةٌ تُحب، ومذاهبُ تُتبع.\"", "💎 \"الدين حبٌ واتباع، لا نقدٌ وجفاء.\""]
        bot.reply_to(message, random.choice(quotes))

bot.remove_webhook()
bot.infinity_polling()
