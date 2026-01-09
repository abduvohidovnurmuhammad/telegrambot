import telebot

# Bot tokeningiz
TOKEN = "8133175969:AAEyFLseZkNofcEOSrA9CGP1eOMw0WylmpA"
bot = telebot.TeleBot(TOKEN)

# Faqat public kanal tekshiriladi
PUBLIC_CHANNEL = "@sahfa_books"

WELCOME_TEXT = (
    "Assalomu alaykum!\n\n"
    "Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling 👇\n\n"
   
)

# Public kanaldagi obunani tekshiradigan funksiya
def check_sub(user_id):
    try:
        status = bot.get_chat_member(PUBLIC_CHANNEL, user_id).status
        return status != "left"
    except:
        return False

# /start komandasi
@bot.message_handler(commands=['start'])
def start(msg):
    user_id = msg.from_user.id

    if check_sub(user_id):
        bot.send_message(msg.chat.id, "🎉 Rahmat! Siz public kanalda obunasiz.")
    else:
        markup = telebot.types.InlineKeyboardMarkup()

        # private kanal (faqat ko'rsatish)
        markup.add(
            telebot.types.InlineKeyboardButton(
                "1️⃣ Private kanalga obuna bo‘lish",
                url="https://t.me/+VMDEmsIqlTUzYjBi"
            )
        )

        # public kanal (tekshiradi)
        markup.add(
            telebot.types.InlineKeyboardButton(
                "2️⃣ Public kanalga obuna bo‘lish",
                url="https://t.me/sahfa_books"
            )
        )

        # tekshirish tugmasi
        markup.add(
            telebot.types.InlineKeyboardButton(
                "✔️ Obunani tekshirish",
                callback_data="check"
            )
        )

        bot.send_message(msg.chat.id, WELCOME_TEXT, reply_markup=markup)

# "Tekshirish" tugmasi bosilganda
@bot.callback_query_handler(func=lambda call: call.data == "check")
def callback_check(call):
    user_id = call.from_user.id

    if check_sub(user_id):
        bot.edit_message_text(
            "🎉 Tabriklaymiz!\n\n"
        "Siz barcha shartlarni muvaffaqiyatli bajardingiz va "
        "Asmo Box × Sahfa Books tomonidan maxsus PROMOKOD sohibiga aylandingiz!\n\n"
        "🎁 Promokod: 134B7-ASMO10\n\n"
        "Bu promokod orqali keyingi xaridingizda maxsus chegirmadan foydalanishingiz mumkin.\n\n"
        "👉 Promokoddan foydalanish uchun quyidagi havola orqali o‘ting:\n"
        "🔗 https://uzum.uz/ru/product/bloknot-moya-kaaba-1917547?skuId=6749819\n\n"
        "🛍 Xaridingiz uchun rahmat! Sizni yana mamnun qilishdan xursandmiz 💙",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
    else:
        bot.answer_callback_query(call.id, "❌ Hali public kanalda obuna bo‘lmagansiz!")

bot.polling()
