from telebot import TeleBot 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton 
 
# Telegram bot token (replace with your bot's token) 
BOT_TOKEN = '7916798453:AAET_y-YRy2aSkSxrPej1ugMENbBw3VLQ6s' 
 
# Bot initialization 
bot = TeleBot(BOT_TOKEN) 
 
# Start command handler 
@bot.message_handler(commands=['start']) 
def send_welcome(message): 
    # Caption for the image 
    caption = ( 
        "⦿━━━━━━━━━━━━━━━━━━━━━⦿\n" 
        "ᴛʜɪs ɪs ᴄʜᴛ ᴡєʙ ʙσᴛ ʙʏ @cyber_ansh\n" 
        "ᴛʜɪs ɪs σηʟʏ ᴛєsᴛɪηɢ ʙσᴛ\n" 
        "ᴄʟɪᴄᴋ ʟɪᴠє ᴄʜᴧᴛ ʙυᴛᴛση ᴄʜᴧᴛ ʟɪᴠє\n" 
        "ʏσυ ᴄᴧη ʙυʏ ᴘꝛєϻɪυϻ ᴘσꝛᴛғσʟɪσ ᴡєʙsɪᴛє  ᴛєϻᴘʟᴧᴛєs\n" 
        "⦿━━━━━━━━━━━━━━━━━━━━━⦿" 
    ) 
     
    # Inline keyboard buttons 
    keyboard = InlineKeyboardMarkup() 
    keyboard.row( 
        InlineKeyboardButton("ᴄʜᴧηηєʟ ᴊσɪη", url="https://t.me/ans_X_bot"), 
        InlineKeyboardButton("ᴡєʙsɪᴛє", url="https://anshu908.github.io/web-service-miini/") 
    ) 
    keyboard.add( 
        InlineKeyboardButton("ᴄσηᴛᴧᴄᴛ", url="https://t.me/cyber_ansh") 
    ) 
     
    # Sending the image with caption and buttons 
    try: 
        bot.send_photo( 
            chat_id=message.chat.id,  
            photo="https://envs.sh/9-x.jpg",  # Use valid URL or local path 
            caption=caption,  
            reply_markup=keyboard 
        ) 
    except Exception as e: 
        bot.send_message(chat_id=message.chat.id, text=f"Error occurred: {str(e)}") 
 
# Callback query handler for inline buttons 
@bot.callback_query_handler(func=lambda call: True) 
def handle_query(call): 
    if call.data == "help": 
        bot.send_message(call.message.chat.id, "This is the help section.") 
    elif call.data == "about": 
        bot.send_message(call.message.chat.id, "About us: We provide awesome services!") 
 
# Polling to keep the bot running 
print("Bot is running...") 
bot.infinity_polling()
