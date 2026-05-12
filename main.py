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
    btn1 = types.KeyboardButton('علوم العترة والكساء')
    btn2 = types.KeyboardButton('الإمام جعفر الصادق')
    btn3 = types.KeyboardButton('الإمام زيد بن علي')
    btn4 = types.KeyboardButton('السيدة نفيسة (ع)')
    btn5 = types.KeyboardButton('ابن تيمية والمنهاج')
    btn6 = types.KeyboardButton('أقوال وحكم')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    
    welcome_msg = (
        "✨ أهلاً بك في بوت (حقائق الصدق) ✨\n\n"
        "منصة 'مشروع كشف الحقائق' لإعادة الأمور إلى نصابها؛ فالدين حبٌ واتباع، لا نقدٌ وجفاء.\n"
        "اختر المحطة المعرفية التي تريد تصفحها:"
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    # --- قسم علوم العترة والكساء ---
    if message.text == 'علوم العترة والكساء':
        msg = (
            "📖 **المحطة الأولى: الثقلين والكساء**\n\n"
            "\"إني تارك فيكم ما إن تمسكتم به لن تضلوا بعدي أبداً: كتاب الله وعترتي أهل بيتي\"\n\n"
            "📍 **حديث الكساء:** هو التحديد العملي للهوية المرجعية (علي، فاطمة، الحسن، الحسين) بنص آية التطهير.\n"
            "⚖️ **الميزان:** عترةٌ تُحب، ومذاهبُ تُتبع.. هكذا اجتمعت الأمة."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    # --- قسم الإمام جعفر الصادق ---
    elif message.text == 'الإمام جعفر الصادق':
        msg = (
            "💡 **جعفر الصادق: المنبع الذي سقى المذاهب وجفاه المنهاج**\n\n"
            "مؤسس أكبر جامعة إسلامية (4000 طالب). تلمذ على يديه أبو حنيفة ومالك.\n\n"
            "⚠️ **سقطة المنهاج:** حاول ابن تيمية التقليل من تلمذة الأئمة على يديه لفك الارتباط بين العترة والجمهور.\n"
            "🔬 **الريادة:** أستاذ جابر بن حيان في الكيمياء، ومرجع علوم الطب والتوحيد."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    # --- قسم الإمام زيد بن علي (المحطة الجديدة) ---
    elif message.text == 'الإمام زيد بن علي':
        msg = (
            "⚔️ **الإمام زيد بن علي: حليف القرآن الذي نصرته المذاهب وغيبه المنهاج**\n\n"
            "1️⃣ **لماذا حليف القرآن؟** لملازمته المصحف تدبراً وعملاً، ووراثته لعلم جده علي (ع).\n\n"
            "2️⃣ **نصرة المذاهب:** الإمام **أبو حنيفة** نصر ثورته بالمال وقال: 'ضاهى خروجه خروج رسول الله ﷺ يوم بدر'.\n\n"
            "3️⃣ **تغييب المنهاج:** تعرض إرثه لمحاولات التهميش في تيار المنهاج لإضعاف رمزية الثورة ضد الظلم.\n\n"
            "📚 **المصادر:** تاريخ الطبري، سير أعلام النبلاء للذهبي، مناقب الخوارزمي."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    # --- قسم السيدة نفيسة (المحطة الجديدة) ---
    elif message.text == 'السيدة نفيسة (ع)':
        msg = (
            "✨ **السيدة نفيسة: نفيسة العلم التي صلى عليها الشافعي وجفاها فكر المنع**\n\n"
            "1️⃣ **نفيسة العلم:** حفيدة الحسن (ع)، كانت مرجعاً فقهياً وقبلةً للعلماء.\n\n"
            "2️⃣ **الشافعي في حضرتها:** كان يزورها ويسمع منها الحديث، وأوصى أن تُصلي عليه عند وفاته، ففعلت.\n\n"
            "3️⃣ **مواجهة الجفاء:** يحاول الفكر التيمي المعاصر تصوير الارتباط بها كبدعة، متجاهلين أن الإمام الشافعي هو من أسس هذا الارتباط.\n\n"
            "📚 **المصادر:** وفيات الأعيان لابن خلكان، سير أعلام النبلاء، الخطط المقريزية."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    # --- قسم ابن تيمية والمنهاج ---
    elif message.text == 'ابن تيمية والمنهاج':
        msg = (
            "📚 **سقطات 'المنهاج'.. نقد الفضائل وجفاء المنهج**\n\n"
            "1️⃣ **تضعيف الثوابت:** أنكر أحاديث صحيحة (أنا مدينة العلم) لأنها تخدم الخصوم.\n"
            "2️⃣ **الجفاء السياسي:** اتهم الإمام علي بطلب 'الرياسة' والسلطة، وهو قول شاذ.\n"
            "3️⃣ **المحاكمة:** سُجن بقرار إجماعي من قضاة المذاهب الأربعة صيانةً للعقيدة من الفرقة."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    # --- قسم أقوال وحكم ---
    elif message.text == 'أقوال وحكم':
        quotes = [
            "💎 \"العلم خزانة، ومفاتيحها السؤال.\" - الإمام الصادق",
            "💎 \"من قنع بما رزقه الله فهو من أغنى الناس.\" - الإمام الصادق",
            "💎 \"بالصبر واليقين تُنال الإمامة في الدين.\" - ابن تيمية",
            "💎 \"أحبوا الله لما يغدوكم به من نعمه، وأحبوني لحب الله، وأحبوا أهل بيتي لحبي.\" - حديث شريف"
        ]
        bot.reply_to(message, random.choice(quotes))

bot.remove_webhook()
bot.infinity_polling()
