import random
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
    "flexbox": 
        "CSS Flexbox is a layout model that allows you to design responsive web pages easily. "
        "It enables you to align and distribute space among items in a container, even when their sizes are unknown or dynamic.",
    "grid":  "CSS Grid is a powerful layout system for creating two-dimensional layouts. "
        "It allows you to divide a page into rows and columns and place items within the grid. It's especially useful for complex web layouts.",
    "gap": "The gap property in CSS is used to specify the space between items in a container, typically in a flexbox or grid layout."
            "It is a shorthand for defining the spacing between rows and columns in a grid or between flex items.",
    "class":"class (.)  Can be applied to multiple elements.",
    "id":"ID (#): Must be unique to one element.",
    "element": """An HTML element is defined by a start tag, some content, and an end tag:

<tagname> Content goes here... </tagname>
The HTML element is everything from the start tag to the end tag:
""",
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
  "more": """Here are the available commands:
- /start - Start the bot
- /info - Information about the bot
- /status - Check the bot's status
- /video - watch video
- /weather - Check weather
""",
"help": """ 🔴➡️ question guideline: 

        🔸 what is HTML 🕵️ ?                                                            
        🔸 what is CSS 🤓?                                
        🔸 what is python 🐍?
        🔸 what is javascript 🤔?
        🔸 what is databases 🌐?
        🔸 what is algorithms 🚀?

    🎯 About HTML:                                                🎯 About CSS:
        🔹 Structure HTML                       🔹 What is flexbox ?                                                                                                                  
        🔹 Table of HTML                                       🔹 What is grid ?                                               
        🔹 Element of HTML                                          🔹 Class & ID                                          
        🔹 Code block                                                      🔹 What is gap?
        🔹 HTML Heading & Paragrap                       🔹 Rule CSS
        🔹 Video about HTML & CSS                          🔹 How to add CSS?
""",
"code block":"""Ordered list:
html
<pre>
<ol>
  <li>Item 1</li>
  <li>Item 2</li>
</ol>
Unordered list:
html
<ul>
  <li>Item A</li>
  <li>Item B</li>
</ul>
</pre>
""",
    
   "rule css" : """A CSS rule is a statement that defines the style properties for a particular HTML element or group of elements. It consists of two main parts:

            1.Selector: Specifies which HTML elements the rule applies to.

            2.Declaration Block: Contains one or more property-value pairs that define the style.""",
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
    elif "id" in text :
        return "id"
    elif "rule css" in text :
        return "rule css"

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
    return None

def condiction_3(message_help):
    text = message_help.text.lower()
    if "structure" in text:
        return "structure"

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
@bot.message_handler(func=lambda message2: message2.text in ["table", "structure", "element", "code block"])
def handle_topic_selection(message2):
    topic = message2.text
    bot.send_message(message2.chat.id, RESPONSES[topic])


@bot.message_handler(func=lambda message1: message1.text in ["flexbox","grid","gap","class","id","rule css"])
def handle_topic_selection(message1):
    topic = message1.text
    bot.send_message(message1.chat.id, RESPONSES[topic])

@bot.message_handler(func=lambda message_help: message_help.text in ["structure", "table"])
def handle_topic_selection(message_help):
    topic = message_help.text
    bot.send_message(message_help.chat.id, RESPONSES[topic])

# structure
@bot.message_handler(commands=["structure"])
def send_structure(message_help):
    bot.reply_to(message_help, "structure:"
    """<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <!-- Page content goes here -->
</body>
</html>
""")
    
#table

@bot.message_handler(commands=["table"])
def send_table(message_help):
    bot.reply_to(message_help, "table:"
    """<table>
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
 """)
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