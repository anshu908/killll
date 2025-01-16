from flask import Flask, request
from telebot import TeleBot, types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

# Telegram bot token (replace with your bot's token)
BOT_TOKEN = '7916798453:AAET_y-YRy2aSkSxrPej1ugMENbBw3VLQ6s'

# Webhook URL (Replace with your deployed Koyeb domain)
WEBHOOK_URL = 'https://giant-nicoli-matrix9-003b1d95.koyeb.app/'

# Bot initialization
bot = TeleBot(BOT_TOKEN)

# Flask app initialization
app = Flask(__name__)

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


# Webhook route for handling updates
@app.route('/', methods=['POST'])
def webhook():
    try:
        json_string = request.get_data().decode('utf-8')
        update = types.Update.de_json(json_string)
        bot.process_new_updates([update])
    except Exception as e:
        return f"Error processing update: {e}", 500
    return "OK", 200


# Set webhook
@app.route('/set_webhook', methods=['GET'])
def set_webhook():
    try:
        set_hook = bot.set_webhook(WEBHOOK_URL)
        if set_hook:
            return "Webhook set successfully!", 200
        else:
            return "Failed to set webhook", 500
    except Exception as e:
        return f"Error setting webhook: {e}", 500


# Verify webhook
@app.route('/verify_webhook', methods=['GET'])
def verify_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json(), 200
        else:
            return f"Failed to verify webhook: {response.text}", 500
    except Exception as e:
        return f"Error verifying webhook: {e}", 500


if __name__ == '__main__':
    # Run Flask app on port 8080
    app.run(host='0.0.0.0', port=8080)
