Real Estate Telegram Bot

Description:  
A simple Telegram bot written in Python that allows users to search real estate listings by type, city, and price range.  
All data is stored locally in text files.

---

Features
 • Search properties by type (flats, houses, land)
 • Filter by city and price range
 • Simple file-based storage (no database needed)
 • Easy to modify and expand
 • Works on any device with Python3

---

Technologies:  
- Python 3  
- telebot (PyTelegramBotAPI)

---

Project Structure

<img width="240" height="206" alt="image" src="https://github.com/user-attachments/assets/cf77987e-fca3-4577-8a29-3656b9f6b580" />

---

Installation & Run:  
1. Clone the repository  
   ```bash
   git clone https://github.com/username/real-estate-bot.git
   cd real-estate-bot
   ```
2. Install dependencies  
   ```bash
   pip install pyTelegramBotAPI
   ```
3. Add a `.env` file with your bot token  
   ```json
   { "telegram_token": "YOUR_TELEGRAM_BOT_TOKEN" }
   ```
4. Run the bot  
   ```bash
   python main.py
   ```

---

#Bot Commands:

Command,Description

## /start,Greeting + menu
## /search,Start property search
## /help,Show available commands

---

Example User Flow

User: /search
Bot: “Choose property type: Flat / House / Land”
User: “Flat”
Bot: “Enter city:”
User: “Kyiv”
Bot: “Enter max price:”
User: “60000”
Bot: Results from data/flats.txt

---

License:  
This work is in the public domain.
Licensed under the MIT License — free to use, modify, and distribute

---

Author:  
Created by Alex Rudzenis for educational purposes.
