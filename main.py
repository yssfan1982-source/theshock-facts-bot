import telebot
from telebot import types
import http.server
import socketserver
import threading
import os

# --- إعداد منفذ Render لضمان استمرارية البوت ---
def run_dummy_server():
    PORT = int(os.environ.get("PORT", 8080))
    Handler = http.server.SimpleHTTPRequestHandler
    # السماح بإعادة استخدام المنفذ لتجنب أخطاء التعليق
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

threading.Thread(target=run_dummy_server, daemon=True).start()

# --- إعداد البوت ---
TOKEN = '8788666843:AAEMthDUv8sNO8nF1rg0fzVo3eYi6EB_K24'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    # استخدام الأزرار الشفافة Inline لتفادي مشاكل التعليق ومطابقة النصوص
    markup = types.InlineKeyboardMarkup(row_width=1)
    
    btn1 = types.InlineKeyboardButton('🏛️ المحطة 1: عصر الانسجام', callback_data='station_1')
    btn2 = types.InlineKeyboardButton('💡 المحطة 2: الأئمة والآل', callback_data='station_2')
    btn3 = types.InlineKeyboardButton('⚖️ المحطة 3: حقيقة المحاكمة', callback_data='station_3')
    btn4 = types.InlineKeyboardButton('⚠️ المحطة 4: تلف الأمة المعاصر', callback_data='station_4')
    btn5 = types.InlineKeyboardButton('📜 بيان المشروع والمصادر', callback_data='project_info')
    
    markup.add(btn1, btn2, btn3, btn4, btn5)
    
    welcome_msg = (
        "✨ **بوت (حقائق الصدق) | مشروع كشف الحقائق** ✨\n\n"
        "مرحباً بك في الموسوعة الرقمية لتصحيح المسار التاريخي للأمة.\n"
        "هدفنا: إظهار الحقيقة المجردة بعيداً عن الجفاء وتزييف الفكر.\n\n"
        "👇 اضغط على أحد الأزرار أدناه لتصفح المحطات والمصادر:"
    )
    bot.send_message(message.chat.id, welcome_msg, reply_markup=markup, parse_mode='Markdown')

# --- معالج الضغط على الأزرار الشفافة ---
@bot.callback_query_handler(func=lambda call: True)
def callback_listener(call):
    # إشعار تليجرام بأن الضغطة تمت بنجاح لمنع تعليق الزر
    bot.answer_callback_query(call.id)
    
    if call.data == 'station_1':
        msg = (
            "🏛️ **المحطة الأولى: 500 عام من الاستقرار الذهبي**\n\n"
            "قبل ظهور فتنة المنهاج، عاشت الأمة في تناغم تام:\n"
            "✅ لم يختلف الأشاعرة والماتريدية مع المذاهب الأربعة.\n"
            "✅ كانت مودة العترة النبوية أصلاً لا يقبل التشكيك.\n"
            "✅ ساد 'أدب الإجماع' واختفى 'شذوذ المنهاج'.\n\n"
            "📚 **المراجع:** تاريخ الإسلام (الذهبي)، البداية والنهاية (ابن كثير)."
        )
        bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')

    elif call.data == 'station_2':
        msg = (
            "💡 **المحطة الثانية: مواقف الأئمة الأربعة العملية**\n\n"
            "الأئمة الأربعة لم يكونوا مجرد فقهاء، بل كانوا جنوداً في نصرة العترة:\n"
            "• **أبو حنيفة:** نصر ثورة الإمام زيد بالمال والفتوى.\n"
            "• **الشافعي:** صلى خلف السيدة نفيسة وأوصى ببركتها.\n"
            "• **مالك:** تلمذ على الصادق وأجله إجلالاً عظيماً.\n\n"
            "📚 **المراجع:** سير أعلام النبلاء (الذهبي)، وفيات الأعيان (ابن خلكان)."
        )
        bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')

    elif call.data == 'station_3':
        msg = (
            "⚖️ **المحطة الثالثة: كشف مستور محاكمات ابن تيمية**\n\n"
            "سجن ابن تيمية كان بقرار 'سني جماعي' من قضاة المذاهب الأربعة:\n"
            "• **ابن مخلوف (المالكي) وابن جماعة (الشافعي):** أدانوه بسبب الجفاء في حق النبي ﷺ وآل بيته وبسبب فتنة التجسيم.\n"
            "• **السبب الحقيقي:** حماية عقيدة الأمة ووحدتها من الفكر المنفرد.\n\n"
            "📚 **المراجع:** الدرر الكامنة (ابن حجر)، دفع شبه من شبه وتمرد (الحصني الدمشقي)."
        )
        bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')

    elif call.data == 'station_4':
        msg = (
            "⚠️ **المحطة الرابعة: الواقع المعاصر و'تلف' الأمة**\n\n"
            "كيف تحول الفكر التيمي إلى أداة لتمزيق الأمة اليوم؟\n"
            "1️⃣ **استهداف الأزهر والزيتونة:** محاولة تبديع وتكفير المدارس العريقة التي حافظت على الإسلام لقرون.\n"
            "2️⃣ **صناعة الحواجز:** جعلوا 'ذكر فضائل آل البيت' تهمة بالتشيع، ليحرموا الأمة من مصدر بركتها.\n"
            "3️⃣ **فوضى الفتوى:** ضرب إجماع المذاهب الأربعة بدعوى 'اتباع الدليل' لتمكين الجهلاء من الفتوى.\n\n"
            "📚 **المراجع:** إحياء المقبور (الغماري)، مقالات الكوثري، فتاوى الأزهر الشريف."
        )
        bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')

    elif call.data == 'project_info':
        msg = (
            "📜 **بيان مشروع كشف الحقائق**\n\n"
            "نحن لا ننتصر لفريق، بل ننتصر للحقيقة.\n"
            "الميزان الصحيح: **عترةٌ تُحب، ومذاهبُ تُتبع**.\n\n"
            "🔗 لزيارة القناة ومتابعة السلاسل البحثية كاملة، تفضل بالانضمام إلينا."
        )
        bot.send_message(call.message.chat.id, msg, parse_mode='Markdown')

# تنظيف أي تداخلات قديمة للويب هوك وإطلاق البوت بثبات
bot.remove_webhook()
bot.infinity_polling(timeout=10, long_polling_timeout=5)
