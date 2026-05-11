import telebot
from telebot import types

# التوكن الخاص بك الذي زودتني به
API_TOKEN = '8788666843:AAEMthDUv8sNO8nF1rg0fzVo3eYi6EB_K24'

bot = telebot.TeleBot(API_TOKEN)

# 1. استجابة أمر البدء وتجهيز الأزرار
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    item1 = types.KeyboardButton("🌿 علوم العترة")
    item2 = types.KeyboardButton("📖 حديث الكساء")
    item3 = types.KeyboardButton("🎓 الإمام جعفر الصادق")
    item4 = types.KeyboardButton("⚖️ حقائق الصدق")
    
    markup.add(item1, item2, item3, item4)
    
    welcome_text = (
        f"مرحباً بك يا {message.from_user.first_name} في بوت (حقائق الصدق) 🌿\n\n"
        "هذا البوت مخصص لنشر علوم أهل البيت عليهم السلام والبحث في الحقائق التاريخية.\n"
        "اختر من القائمة أدناه لتبدأ الرحلة:"
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# 2. برمجة ما يحدث عند الضغط على كل زر
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "🌿 علوم العترة":
        bot.send_message(message.chat.id, "قريباً: سيتم عرض أبحاث وشروحات عن علوم العترة الطاهرة.")
        
    elif message.text == "📖 حديث الكساء":
        text_ksaa = (
            "عن جابر بن عبد الله الأنصاري عن فاطمة الزهراء (عليها السلام) قالت: "
            "دخل علي أبي رسول الله في بعض الأيام فقال: السلام عليك يا فاطمة..."
        )
        bot.send_message(message.chat.id, text_ksaa)
        
    elif message.text == "🎓 الإمام جعفر الصادق":
        info_sadiq = "الإمام جعفر بن محمد الصادق (عليه السلام) هو مؤسس المذهب الجعفري وناشر علوم الطب والكيمياء والفقه."
        bot.send_message(message.chat.id, info_sadiq)
        
    elif message.text == "⚖️ حقائق الصدق":
        bot.send_message(message.chat.id, "هذا القسم مخصص لمشروعك 'كشف الحقائق التاريخية' الذي تعمل عليه حالياً.")

# 3. تشغيل البوت باستمرار
bot.polling(none_stop=True)
