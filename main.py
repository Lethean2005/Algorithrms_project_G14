import telebot
import random
import requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.apihelper import ApiTelegramException


# Replace this with your Bot Token from BotFather
BOT_TOKEN = "7699208754:AAFlNIo-PsNOaM2pn6UUKYe0j_lou1wI5wI"
bot = telebot.TeleBot(BOT_TOKEN)

# Predefined responses for topics
RESPONSES = {
    "hello": "Hello! How are you? I'm here to assist you with HTML, CSS, Python, JavaScript, Databases, Algorithms, and more!",
    "html": "HTML (HyperText Markup Language) is the standard markup language for creating web pages. How can I assist you with HTML?",
    "css": "CSS (Cascading Style Sheets) is used to style HTML elements. How can I help with CSS?",
    "python": "Python is a versatile programming language, and Tkinter is its built-in library for creating GUIs. What do you want to know about Python or Tkinter?",
    "javascript": "JavaScript is a programming language used for creating interactive effects within web browsers. How can I help with JavaScript?",
    "databases": "Databases store and manage data. You can use SQL, NoSQL, or other database technologies. What do you want to know about databases?",
    "algorithms": "Algorithms are a set of instructions to solve a problem. They are fundamental to computer science. How can I assist you with algorithms?",
    "structure": """<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <!-- Page content goes here -->
</body>
</html>
""",
"table": """<table>
<thead>
    <tr>
        <th>Header 1</th>
        <th>Header 2</th>
        <th>Header 3</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>Row 1, Column 1</td>
        <td>Row 1, Column 2</td>
        <td>Row 1, Column 3</td>
    </tr>
    <tr>
        <td>Row 2, Column 1</td>
        <td>Row 2, Column 2</td>
        <td>Row 2, Column 3</td>
    </tr>
</tbody>
</table>
 """,
    "More": """Here are the available commands:
- /start - Start the bot
- /info - Information about the bot
- /status - Check the bot's status
- /data - Get a random data
- /weather - Check weather
"""
    
}

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
    elif "hello" in text:
        return "hello"
    return None  # No specific topic detected


#def_second_function for HTML

def condiction_2(message2):
    text = message2.text.lower()
    if "table" in text:
        return "table"
    elif "structure" in text:
        return "structure"
    elif "more" in text:
        return "more"
    return None

# Start command handler
@bot.message_handler(commands=["start"])
def start(message):
    # Create a reply markup with buttons
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    html_button = KeyboardButton("HTML")
    css_button = KeyboardButton("CSS")
    python_button = KeyboardButton("Python")
    javascript_button = KeyboardButton("JavaScript")
    databases_button = KeyboardButton("Databases")
    algorithms_button = KeyboardButton("Algorithms")
    help_button = KeyboardButton("More")
    markup.add(html_button, css_button, python_button, javascript_button, databases_button, algorithms_button, help_button)

    # Send welcome message with buttons
    bot.send_message(
        message.chat.id,
        "Welcome! Select a topic to ask about:\n- HTML\n- CSS\n- Python (Tkinter)\n- JavaScript\n- Databases\n- Algorithms\nOr type your question, and I'll do my best to help!",
        reply_markup= markup,
    )

# Message handler for topic selection
@bot.message_handler(func=lambda message: message.text in ["HTML", "CSS", "Python", "JavaScript", "Databases", "Algorithms"])
def handle_topic_selection(message):
    topic = message.text.lower()
    if topic == "help":
        bot.send_message(message.chat.id, RESPONSES["More"])
    else:
        bot.send_message(message.chat.id, RESPONSES[topic])


#Message for topic selecion 2
@bot.message_handler(func=lambda message2: message2.text in ["table", "structure", "More"])
def handle_topic_selection(message2):
    topic = message2.text
    bot.send_message(message2.chat.id, RESPONSES[topic])

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

# Command: /data
@bot.message_handler(commands=["data"])
def send_data(message):
    data = [
        """
        1. User Data 
        2. Interaction Data 
        3. Bot Data 
        4. Group and Channel Data (if the bot operates in groups or channels) 
        5. Analytics and Performance Data 
        """
    ]
    bot.reply_to(message, random.choice(data))

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

# Start polling
if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()
