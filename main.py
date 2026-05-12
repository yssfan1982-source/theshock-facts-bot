import telebot
from telebot import types
import http.server
import socketserver
import threading
import os

# --- إعداد منفذ وهمي لمنصة Render ---
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
        "منصة معرفية تعنى بنشر علوم العترة الطاهرة وسيرة أهل البيت عليهم السلام.\n"
        "يرجى اختيار القسم الذي ترغب في تصفحه:"
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == 'علوم العترة':
        msg = (
            "📖 **حديث الثقلين: المرجعية التي رسمت مسار التاريخ الإسلامي**\n\n"
            "\"إني تارك فيكم ما إن تمسكتم به لن تضلوا بعدي أبداً: كتاب الله وعترتي أهل بيتي\"\n\n"
            "1️⃣ **الربط الوجودي:** العترة عدل القرآن، ولا يستقيم فهم النص بدونهم.\n"
            "2️⃣ **الاستمرارية:** 'لن تضلوا' تعني مرجعية دائمة لا تنقطع.\n"
            "3️⃣ **الصراع الإصلاحي:** العترة هي الرمز الذي تلتف حوله الجماهير لاستعادة التوازن.\n\n"
            "💡 **لماذا الثقلين؟** الثقل هو الأمانة التاريخية والمعرفية الكبرى."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'حديث الكساء':
        msg = (
            "🛡️ **حديث الكساء: آية التطهير ودلالة الاصطفاء**\n\n"
            "\"اللهم هؤلاء أهل بيتي وخاصتي وحامتي، أذهب عنهم الرجس وطهرهم تطهيراً\"\n\n"
            "📍 **سياق الحدث:** في بيت السيدة فاطمة الزهراء (ع)، حين جلل النبي ﷺ علي وفاطمة والحسن والحسين بالكساء، ليكون إعلاناً نبوياً لتحديد الهوية المرجعية.\n\n"
            "✨ **آية التطهير:** نزلت {إِنَّمَا يُرِيدُ اللَّهُ...} في هذا المشهد كصك إلهي يحصر أهل البيت في هؤلاء الخمسة، مما يجعلهم المرجعية المعصومة.\n\n"
            "📜 **الأبعاد التاريخية:**\n"
            "- **التحديد الحصري:** الحديث أغلق الباب أمام المحاولات السياسية لتوسيع المفهوم.\n"
            "- **المكانة:** روي عن أمهات المؤمنين وكبار الصحابة، مما يجعله حجة دامغة.\n\n"
            "📚 **المصادر:** صحيح مسلم، مسند أحمد، سنن الترمذي."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

    elif message.text == 'الإمام جعفر الصادق':
        msg = (
            "💡 **الإمام جعفر الصادق (عليه السلام)**\n\n"
            "الإمام السادس ومؤسس المذهب الجعفري.\n\n"
            "بانتظار إضافة المحتوى المفصل لهذا القسم..."
        )
        bot.reply_to(message, msg, parse_mode='Markdown')

# تشغيل البوت
bot.remove_webhook()
bot.infinity_polling()
