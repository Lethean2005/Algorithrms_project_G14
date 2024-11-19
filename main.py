import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.apihelper import ApiTelegramException
import requests

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
