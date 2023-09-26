import random
import re
import os
import googletrans
from googletrans import Translator
from pykakasi import kakasi

current_sauce_mode = None
current_translate_mode = None
translator = Translator()
bot_choice = None


def get_response(message: str) -> str:
    p_message = message.lower()
    global current_sauce_mode
    global current_translate_mode
    global bot_choice

    if p_message == '!!help':
        return ("**## KOLEHIYO BOT COMMANDS**"
                "```\n"
                " **GENERAL COMMANDS**\n"
                " !!hello     - Will Respond to You\n"
                " !!luwi      - Describes John Louie Ubias\n"
                " !!domz      - Describes Dominic Ramos\n"
                " !!migz      - Describes Miguel Pilapil\n"
                " !!kurt      - Describes Kurt Robin Colonia\n"
                " !!rotz      - Describes Rotsen David\n"
                " !!ru        - Rolls a Randon number from 0-1000\n"
                " !!image     - Shows Random Images\n"
                " !!nh        - Ask for Sauce\n"
                " !!coin      - Rolls A Coin\n"
                " !!rps       - Plays a Game of Rock, Paper, and Scissors\n"
                " !!socials   - Check the Socials of the KOLEHIYO\n"
                " !!ts        - Translates Eng-Jp and Jp-Eng\n"
                " !!dc        - Disconnect Someone\n"

                " **MUSIC COMMANDS**\n"
                "**AS OF NOW INAAYOS PA PO**\n"
                "!!lyrics                - shows the lyrics of a song\n"
                "!!nowplaying            - shows the song that is currently playing\n"
                "!!play                  - plays the provided song\n"
                "!!queue                 - shows the current queue\n"
                "!!remove                - removes a song from the queue\n"
                "!!shuffle               - shuffles songs you have added\n"
                "!!skip                  - votes to skip the current song\n"

                "```\n")

    if p_message == '!!hello':
        responses = ["### WAZZUP HOMIE", "### SUPP CUH", "", "", "", ""]
        return random.choice(responses)

    if p_message == '!!luwi':
        responses = ["TANG INA MO JOHN LOUIE UBIAS", "21 CAN YOU DO SOMETHING FOR ME", "75/25 SA GENDER"]
        return random.choice(responses)

    if p_message == '!!domz':
        responses = ["TANG INA MO DOMINIC RAMOS", "TARA MUCK", "SANA OL MAY JOWA"]
        return random.choice(responses)

    if p_message == '!!migz':
        responses = ["TANG INA MO MIGUEL PILAPIL", "ISA AKONG RACISTT!!", "MERON AKONG SIDE CHICK!", "DI KO NA KAILANGAN MAG-ARAL HEHE"]
        return random.choice(responses)

    if p_message == '!!kurt':
        responses = ["TANG INA MO KURT ROBIN COLONIA", "NAG-COCODE TANG INA MO", "PAR SAGLET LANG HAH?!", "WALANG KWENTA BOT MO KURT"]
        return random.choice(responses)

    if p_message == '!!rotz':
        responses = ["TANG INA MO ROTSEN DAVID", "TARA CSGO", "TARA VALORANT", "MISS KO NA SIYA SI"]
        return random.choice(responses)

    if p_message == '!!ru':
        random_number = random.randint(0, 1000)
        return f"{random_number} is the Number Homie"

    if p_message == '!!coin':
        coin_sides = ["HEADS", "TAILS"]
        return f"The coin landed on: **{random.choice(coin_sides)}**"

    if p_message == '!!image':
        image_urls = [
            "https://imgur.com/Za67MfY", "https://imgur.com/AJtesSK", "https://imgur.com/Qb7MRoU", "https://imgur.com/Za67MfY", "https://imgur.com/fYPhNei",
            "https://imgur.com/GhQw3lI", "https://imgur.com/i22IeqH", "https://imgur.com/Lwz09BX", "https://imgur.com/KiYdtXD", "https://imgur.com/Jeieyjm",
            "https://imgur.com/FXWFPd4", "https://imgur.com/eMOTgkG", "https://imgur.com/1s8kLq1", "https://imgur.com/HMgv0bH", "https://imgur.com/YxGVV5O",
            "https://imgur.com/kGeiTCE", "https://imgur.com/d60Ul3o", "https://imgur.com/IjZliBy", "https://imgur.com/GanAgRN", "https://imgur.com/CHE5Wh6",
            "https://imgur.com/VLadjSP", "https://imgur.com/4FPbnTX", "https://imgur.com/T4pEonP", "https://imgur.com/YxGVV5O", "https://imgur.com/H0d8MEv",
            "https://imgur.com/sAitGU4", "https://imgur.com/uOAN101", "https://imgur.com/X3N4Lpd", "https://imgur.com/l51Rx6D", "https://imgur.com/16D3LHW",
            "https://imgur.com/fnKPUlu", "https://imgur.com/16D3LHW", "https://imgur.com/TgAaPCf", "https://imgur.com/yOmG2wj", "https://imgur.com/gUmlEcC",
            "https://imgur.com/gUmlEcC", "https://imgur.com/LLKKb7r", "https://imgur.com/KDE8aap", "https://imgur.com/O6UBoFN", "https://imgur.com/L3zcYs5",
            "https://imgur.com/CR2NKT8", "https://imgur.com/U3RjKej", "https://imgur.com/8QyRzMe", "https://imgur.com/TzjErkn", "https://imgur.com/YUYPlNS",
            "https://imgur.com/0Bz5T3h", "https://imgur.com/aMyrI1b", "https://imgur.com/mFLqBZd", "https://imgur.com/mFLqBZd", "https://imgur.com/jo8MKMj",
            "https://imgur.com/kOTM7do", "https://imgur.com/P8pTsry", "https://imgur.com/WEuZygk", "https://imgur.com/bQu1LG6", "https://imgur.com/1R4AN5y",
            "https://imgur.com/NEJP3Sc", "https://imgur.com/LJ1qgBK", "https://imgur.com/UBNYCvn", "https://imgur.com/DCVNY4Z", "https://imgur.com/5yqMjoY",
            #"", "", "", "", "",
            #"", "", "", "", "",
            #"", "", "", "", "",
            #"", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
            # "", "", "", "", "",
        ]
        random_image_url = random.choice(image_urls)
        return random_image_url

    if p_message == '!!socials':
        return (

            "**KOLEHIYO SOCIALS**\n\n"

            "***JOHN LOUIE UBIAS***\n"
            "*[FACEBOOK]*\n<https://www.facebook.com/SenpaiLuwii>\n\n"
            "*[INSTAGRAM]*\n<https://www.instagram.com/itzluwi/>\n\n"
            "*[TWITTER]*\n<https://twitter.com/S_Luwi>\n\n"
            "*[GITHUB]*\n<https://github.com/SenpaiLuwi>\n\n\n"

            "***DOMINIC RAMOS***\n"
            "*[FACEBOOK]*\n<https://www.facebook.com/meeeeeeeeeeeeeeeengy>\n\n"
            "*[FACEBOOK PAGE]*\n<https://www.facebook.com/mengy07>\n\n"
            "*[INSTAGRAM]*\n<https://www.instagram.com/meeeeeeeeeeeeeeeengy/>\n\n"
            "*[GITHUB]*\n<https://github.com/Dramos02>\n\n\n"

            "***MIGUEL PILAPIL***\n"
            "*[FACEBOOK]*\n<https://www.facebook.com/ShappyYYy>\n\n"
            "*[INSTAGRAM]*\n<https://www.instagram.com/nonomigs__/>\n\n"
            "*[TWITTER]*\n<https://twitter.com/Daphr__>\n\n"
            "*[GITHUB]*\n<https://github.com/shap30>\n\n\n"

            "***KURT ROBIN COLONIA***\n"
            "*[FACEBOOK]*\n<https://www.facebook.com/teh.real.kurut0>\n\n"
            "*[INSTAGRAM]*\n<https://www.instagram.com/teh_real_kurut0/>\n\n"
            "*[TWITTER]*\n<https://twitter.com/teh_real_kurut0>\n\n"
            "*[GITHUB]*\n<https://github.com/krcolonia>\n\n\n"

            "***ROTSEN DAVID***\n"
            "*[FACEBOOK]*\n<https://www.facebook.com/rotsen.david.5>\n\n"
            "*[FACEBOOK PAGE]*\n<https://www.facebook.com/rezenro>\n\n"
            "*[INSTAGRAM]*\n<https://www.instagram.com/rotsen.rd/>\n\n"
            "*[TWITTER]*\n<https://twitter.com/rezenro>\n"
        )

    if p_message == '!!rps':
        bot_choice = random.choice(["ROCK", "PAPER", "SCISSORS"])
        return "Tara Laro Rock-Paper-Scissors! Matalo BOBO! Enter your choice: ROCK, PAPER, or SCISSORS."

    if bot_choice and p_message in ["rock", "paper", "scissors"]:
        user_choice = p_message.upper()
        result = determine_rps_result(user_choice, bot_choice)
        bot_choice = None
        return result

    if current_sauce_mode is None and p_message == '!!nh':
        current_sauce_mode = 'sauce'
        return "What Sauce do you want to seek my lord? Type 's' if you have some and 'r' for randomized Luck!"

    if current_sauce_mode == 'sauce':
        if p_message == 's':
            current_sauce_mode = 's'
            return "Ok, Give the Sauce you Fucking Degenerate? (Ex: 177013 ( ͡° ͜ʖ ͡°))"
        elif p_message == 'r':
            current_sauce_mode = None
            return f"Here is the Link Enjoy!! <https://nhentai.net/random>"
        else:
            return "Invalid choice. Please choose 's' for user input or 'r' for random sauce."

    if current_sauce_mode == 's' and re.match(r'^\d{6}$', p_message):
        sauce_number = p_message
        current_sauce_mode = None
        link = f"https://nhentai.net/g/{sauce_number}/"

        with open('sos-dc.txt', 'a') as file:
            file.write(link + '\n')

        return f"Here is the Link Enjoy!! <{link}>"

    if p_message == '!!ts':
        current_translate_mode = 'translate'
        return "What would you like to Translate?\n1. English to Japanese\n2. Japanese to English"

    if current_translate_mode == 'translate':
        if p_message in ['1', '2']:
            translation_option = int(p_message)
            current_translate_mode = f'translate_{translation_option}'
            if translation_option == 1:
                return "Enter the Text you Want to Translate from English to Japanese:"
            elif translation_option == 2:
                return "Enter the Text you Want to Translate from Japanese to English:"
            else:
                return "Invalid option. Please choose a valid translation option (1, 2)."

    if current_translate_mode.startswith('translate_'):
        translation_option = int(current_translate_mode.split('_')[1])
        if translation_option in [1, 2]:
            translated_text, romanji = translate_text(message, translation_option)
            current_translate_mode = None
            output = f"The Translated Word:\n Word: **{message}**\n Translated Word: **{translated_text}**"
            if translation_option == 1:
                output += f"\n Romaji: **{romanji}**"
            return output

    return ""


def determine_rps_result(user_choice, bot_choice):
    if user_choice == bot_choice:
        return f"BAKET PAREHAS TAYONG NAKA **{bot_choice}**. TANG INA MO MADAYA!"

    if (
        (user_choice == "ROCK" and bot_choice == "SCISSORS")
        or (user_choice == "PAPER" and bot_choice == "ROCK")
        or (user_choice == "SCISSORS" and bot_choice == "PAPER")
    ):
        return f"PINILI KO AYYY **{bot_choice}**. EDI IKAW NA TANG INA MO KA"

    return f"PINILI KO AYYY **{bot_choice}**. BOBO PALAKAS KA MUNA!"


def translate_text(text, translation_option):
    if translation_option == 1:
        translation = translator.translate(text, src='en', dest='ja')
        return translation.text, translate_to_romanji(translation.text)  # Translate to Romaji
    elif translation_option == 2:
        translation = translator.translate(text, src='ja', dest='en')
        romanji = translate_to_romanji(text)
        return translation.text, romanji
    return "Invalid translation option."


def translate_to_romanji(text):
    kakasi_instance = kakasi()
    kakasi_instance.setMode("H", "a")
    kakasi_instance.setMode("K", "a")
    kakasi_instance.setMode("J", "a")
    conv = kakasi_instance.getConverter()
    romanji = conv.do(text)
    return romanji
