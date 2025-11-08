import telebot

import json

def get_token():
    with open('.env', 'r') as f:
        python_object = json.load(f)
    token = python_object["telegram_token"]
    return token


TOKEN = get_token()

bot = telebot.TeleBot(TOKEN)

search_filters = {"Type of residence" : "",
                  "City": "",
                  "Price from" : 0,
                  "Price to" : 100000000000}

cities = []
residence_types = []
prices = []
price_from = (50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000)
price_to = (60000, 70000, 80000, 90000, 100000, 110000, 120000)
residence_unique = set()
cities_unique = set()

def update_residents():
    global cities, residence_types, prices, cities_unique, residence_unique
    with open ("objects/data.txt", "r", encoding = "utf-8") as file:
        i = 0
        for line in file:
            if i % 3 == 0:
                residence_types.append(line[:-1])
                residence_unique.add(line[:-1])
            elif i % 3 == 1:
                cities.append(line[:-1])
                cities_unique.add(line[:-1])
            elif i % 3 == 2:
                prices.append(int(line[:-1]))
            i += 1
    residence_types.sort()
    cities.sort()

def search(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "searching...")
    print(search_filters)
    print(residence_types)
    print(cities)
    print(prices)
    n = len(cities)
    for i in range(n):
        cond1 = search_filters["Price from"] <= prices[i] and prices[i] <= search_filters["Price to"]
        cond2 = search_filters["Type of residence"] == "" or search_filters["Type of residence"] == residence_types[i]
        cond3 = search_filters["City"] == "" or search_filters["City"] == cities[i]
        if cond1 and cond2 and cond3:
            path = "objects/" + str(i) + "/0.jpeg"
            with open (path, "rb") as photo:
                bot.send_photo(chat_id, photo)
            bot.send_message(chat_id, f"🏠Type of residence:  {residence_types[i]}\n🏙City:  {cities[i]}\n💵💰Price:  {prices[i]}")
            
@bot.message_handler(commands = ["start"])
def welcome(message):
    update_residents()
    menu_start(message)

@bot.callback_query_handler(func = lambda call: True)
def callback_handler(call):
    if call.data == "filter type":
        menu_type_of_residence(call.message)
    elif call.data == "filter city":
        menu_city(call.message)
    elif "filter city selected " in call.data:
        search_filters["City"] = call.data[21:]
        search_info(call.message)
    elif "filter option selected " in call.data:
        search_filters["Type of residence"] = call.data[23:]
        search_info(call.message)
    if call.data == "filter price from":
        menu_filer_price_from(call.message)
    if call.data == "filter price to":
        menu_filer_price_to(call.message)
    elif "filter price from selected " in call.data:
        search_filters["Price from"] = int(call.data[27:])
        search_info(call.message)
    elif "filter price to selected " in call.data:
        search_filters["Price to"] = int(call.data[25:])
        search_info(call.message)
    elif call.data == "search":
        search(call.message)
    elif call.data == "back to main menu":
        menu_start(call.message)
       
def menu_start(message):
    chat_id = message.chat.id
    markup = telebot.types.InlineKeyboardMarkup(row_width = 2)
    btn1 = telebot.types.InlineKeyboardButton("🏠Type of residence", callback_data = "filter type")
    btn2 = telebot.types.InlineKeyboardButton("🏙City", callback_data = "filter city")
    btn4 = telebot.types.InlineKeyboardButton("💵Price from", callback_data = "filter price from")
    btn5 = telebot.types.InlineKeyboardButton("💰Price to", callback_data = "filter price to")
    markup.add(btn1, btn2)
    markup.add(btn4, btn5)
    btn3 = telebot.types.InlineKeyboardButton("🔍Search", callback_data = "search")
    markup.add(btn3)
    bot.send_message(chat_id, "Select filters that apply:👇", reply_markup = markup)

def menu_type_of_residence(message):
    chat_id = message.chat.id
    markup_type_of_residenc = telebot.types.InlineKeyboardMarkup(row_width = 1)
    for option in residence_unique:
         btn = telebot.types.InlineKeyboardButton(option, callback_data = "filter option selected " + option)
         markup_type_of_residenc.add(btn)      
    bot.send_message(chat_id, "Select filters that apply:👇", reply_markup = markup_type_of_residenc)

def menu_city(message):
    chat_id = message.chat.id
    markup_city = telebot.types.InlineKeyboardMarkup(row_width = 1)
    for city in cities_unique:
         btn = telebot.types.InlineKeyboardButton(city, callback_data = "filter city selected " + city)
         markup_city.add(btn)      
    bot.send_message(chat_id, "Select filters that apply:👇", reply_markup = markup_city)

def menu_filer_price_from(message):
    chat_id = message.chat.id
    markup_price = telebot.types.InlineKeyboardMarkup(row_width = 1)
    for price in price_from:
         btn = telebot.types.InlineKeyboardButton(str(price), callback_data = "filter price from selected " + str(price))
         markup_price.add(btn)      
    bot.send_message(chat_id, "Select filters that apply:👇", reply_markup = markup_price)
    
def menu_filer_price_to(message):
    chat_id = message.chat.id
    markup_price = telebot.types.InlineKeyboardMarkup(row_width = 1)
    for price in price_to:
         btn = telebot.types.InlineKeyboardButton(str(price), callback_data = "filter price to selected " + str(price))
         markup_price.add(btn)      
    bot.send_message(chat_id, "Select filters that apply:👇", reply_markup = markup_price)
    
def search_info(message):
    chat_id = message.chat.id
    markup_search_info = telebot.types.InlineKeyboardMarkup(row_width = 1)
    btn = telebot.types.InlineKeyboardButton("⬅️To main menu", callback_data = "back to main menu")
    markup_search_info.add(btn)
    btn = telebot.types.InlineKeyboardButton("🔍Search", callback_data = "search")
    markup_search_info.add(btn)
    bot.send_message(chat_id, f"Your filters:\n🏠Type of residence:  {search_filters["Type of residence"]}\n🏙City:  {search_filters["City"]}\n💵Price from:  {search_filters["Price from"]}\n💰Price to:  {search_filters["Price to"]}", reply_markup = markup_search_info)

bot.polling()
