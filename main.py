import json
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.apihelper import ApiTelegramException
import requests

# Replace this with your Bot Token from BotFather
BOT_TOKEN = "7699208754:AAFlNIo-PsNOaM2pn6UUKYe0j_lou1wI5wI"
bot = telebot.TeleBot(BOT_TOKEN)

# Load the JSON configuration with UTF-8 encoding
with open("bot_config.json", "r", encoding="utf-8") as file:
    config = json.load(file)

# Access data from the JSON
BOT_TOKEN = config["bot_token"]
RESPONSES = config["responses"]
BUTTONS = config["buttons"]
COMMANDS = config["commands"]
HELP_LINK = config["help_link"]
DEFAULT_CITY = config["default_city"]

# Helper function to determine the topic
def determine_topic(message):
    text = message.text.lower()
    if "html" in text:
        return "html"
    elif "css" in text:
        return "css"
    elif "python" in text or "tkinter" in text:
        return "python"
    elif "javascript" in text:
        return "javascript"
    elif "database" in text or "databases" in text:
        return "databases"
    elif "algorithm" in text or "algorithms" in text:
        return "algorithms"
    elif "more" in text:
        return "more"
    elif "help" in text:
        return "help"
    elif "hello" in text:
        return "hello"

#def_second_function for css
def condiction_1 (message1):
    text = message1.text.lower()
    if " flexbpox" in text:
        return "flexbox"
    elif " grid" in text:
        return " grid"
    elif "what is gap" in text:
        return " gap"
    elif "class" in text :
        return "class"
    elif "id" in text:
        return "id"
    elif "margin" in text :
        return "margin"
    elif "rule css" in text :
        return "rule css"
    elif "how to add css" in text:
        return "how to add css"
    elif "padding" in text:
        return "padding"
    return None  # No specific topic detected

#def_second_function for HTML

def condiction_2(message2):
    text = message2.text.lower()
    if "table" in text:
        return "table"
    elif "structure" in text:
        return "structure"
    elif "element" in text:
        return "html element"
    elif "code block" in text:
        return "code block"
    elif "heading" in text:
        return "paragrap"
    
    
    return None

#def_second_function for python
def condiction_3(message3):
    text = message3.text.lower()
    if "date type" in text:
        return "data type"
    elif "for loop" in text:
        return " for loop"
    elif "while loop" in text:
        return"while loop"
    elif "function" in text:
        return "function"
    elif "array" in text:
        return "array"
    elif "string" in text:
        return "string"
    return None

# Start command handler
@bot.message_handler(commands=["start"])
def start(message):
    # Create a reply markup with buttons
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    # Add emojis to visually enhance buttons
    html_button = KeyboardButton("🖍 HTML")
    css_button = KeyboardButton("🎨 CSS")
    python_button = KeyboardButton("🐍 Python")
    javascript_button = KeyboardButton("📜 JavaScript")
    databases_button = KeyboardButton("💾 Databases")
    algorithms_button = KeyboardButton("🔣 Algorithms")
    more_button = KeyboardButton("❓ More")
    help_button = KeyboardButton("❓ Help")

    markup.add(
        html_button, css_button, python_button,
        javascript_button, databases_button, algorithms_button,
        help_button, more_button
    )


    # Send message with enhanced buttons 
    bot.send_message(
        message.chat.id,
        "Welcome! Select a topic to ask about:\n- HTML\n- CSS\n- Python\n- JavaScript\n- Databases\n- Algorithms\nOr type your question, and I'll do my best to help!",
        reply_markup=markup,
    )


# Message handler for topic selection@bot.message_handler(func=lambda message: message.text in ["HTML", "CSS", "Python", "JavaScript", "Databases", "Algorithms", "More", "Help"])
def handle_topic_selection(message):
    topic = message.text.lower()
    if topic == "more":
        bot.send_message(message.chat.id, RESPONSES["More"])
    else:
        bot.send_message(message.chat.id, RESPONSES[topic])


#Message for topic selecion 2
@bot.message_handler(func=lambda message2: message2.text in ["table", "structure", "element", "code block","heading","paragrap"])
def handle_topic_selection(message2):
    topic = message2.text
    bot.send_message(message2.chat.id, RESPONSES[topic])

# css
@bot.message_handler(func=lambda message1: message1.text in ["flexbox","grid","gap","class","id","margin","rule css","padding","how to add css"])
def handle_topic_selection(message1):
    topic = message1.text
    bot.send_message(message1.chat.id, RESPONSES[topic])
#  py
@bot.message_handler(func=lambda message3: message3.text in ["data type","for loop","while loop","function","array","string"])
def handle_topic_selection(message3):
    topic = message3.text
    bot.send_message(message3.chat.id, RESPONSES[topic])


# Command: /info
@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(
        message,
        "🤖 A Telegram Chat Bot is a software application that operates on the Telegram messaging platform, designed to automate tasks, provide services, or engage users through text or multimedia. Bots can simulate conversations, perform predefined tasks, and offer user-centric solutions seamlessly within Telegram."
    )

# Command: /status
@bot.message_handler(commands=["status"])
def send_status(message):
    bot.reply_to(message, "The status of a Telegram bot generally refers to its activity, health, or operational state. A bot's status helps users and developers understand its current functionality and any potential issues. ✅")


@bot.message_handler(commands=["video"])
def send_status(message):
    bot.reply_to(message, "https://www.youtube.com/playlist?list=PL938URpgZ7qYQrfk-HHvzYJMsd576-P66")

# Command: /weather
@bot.message_handler(commands=["weather"])
def send_weather(message):
    # Default city or user-provided city
    city = "Phnom Penh"  # Default city
    if len(message.text.split()) > 1:
        city = " ".join(message.text.split()[1:])  # Extract city from command

    api_key = "7f59948b973042e8bfd22815241211"  # Your WeatherAPI key
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    data = response.json()

    # Check if the request was successful
    if "error" not in data:
        weather_data = (
            f"Weather in {city}:\n"
            f"Temperature: {data['current']['temp_c']}°C\n"
            f"Description: {data['current']['condition']['text']}"
        )
    else:
        weather_data = "Sorry, I couldn't fetch the weather data. Please check the city name."

    bot.reply_to(message, weather_data)
    
# Fallback message handler for any question
@bot.message_handler(func=lambda message: True)
def handle_question(message):
    topic = determine_topic(message)
    if topic:
        # Respond with a predefined answer
        bot.send_message(message.chat.id, RESPONSES[topic])
    else:
        # Respond with a generic message and provide a helpful link
        bot.send_message(
            message.chat.id,
            "I'm sorry, I can currently only help with HTML, CSS, Python, JavaScript, Databases, Algorithms, and general knowledge. Feel free to ask me anything, and I'll try my best to help!"
        )
        # Provide a link to a general help document
        help_link = "https://www.w3schools.com/"  # Replace with your actual link
        bot.send_message(
            message.chat.id,
            f"Download the guide here: [General Help Guide]({help_link})",
            parse_mode="Markdown"
        )

# Start polling
if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
