import random
import re
import os
import googletrans
from googletrans import Translator
from pykakasi import kakasi

current_sauce_mode = None
translator = Translator()


def get_response(message: str) -> str:
    p_message = message.lower()
    global current_sauce_mode

    if p_message == '!!help':
        return ("**## KOLEHIYO BOT COMMANDS**" +
                "```\n"
                " **GENERAL COMMANDS**\n" +
                " !!hello     - Will Respond to You\n" +
                " !!luwi      - Describes John Louie Ubias\n" +
                " !!domz      - Describes Dominic Ramos\n" +
                " !!migz      - Describes Miguel Pilapil\n" +
                " !!kurt      - Describes Kurt Robin Colonia\n" +
                " !!rots      - Describes Rotsen David\n" +
                " !!ru        - Rolls a Randon number from 0-1000\n" +
                " !!image     - Shows Random Images\n" +
                " !!nh        - Ask for Sauce\n" +
                " !!socials   - Check the Socials of the KOLEHIYO\n" +
                " !!ts        - Translates Eng-Jp and Jp-Eng\n" +

                " **MUSIC COMMANDS**\n" +
                "!!lyrics                - shows the lyrics of a song\n" +
                "!!nowplaying            - shows the song that is currently playing\n" +
                "!!play                  - plays the provided song\n" +
                "!!queue                 - shows the current queue\n" +
                "!!remove                - removes a song from the queue\n" +
                "!!shuffle               - shuffles songs you have added\n" +
                "!!skip                  - votes to skip the current song\n" +

                "```\n")

    if p_message == '!!hello':
        responses = [""]
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
        responses = ["TANG INA MO KURT ROBIN COLONIA", "NAG-COCODE TANG INA MO", "PAR SAGLET LANG HAH?!"]
        return random.choice(responses)

    if p_message == '!!rotz':
        responses = ["TANG INA MO ROTSEN DAVID", "TARA CSGO", "TARA VALORANT", "MISS KO NA SIYA SI"]
        return random.choice(responses)

    if p_message == '!!ru':
        random_number = random.randint(0, 1000)
        return f"{random_number} is the Number Homie"

    if p_message == '!!image':
        image_urls = [
        ]
        random_image_url = random.choice(image_urls)
        return random_image_url

    if p_message == '!!socials':
        return (

            "**KOLEHIYO SOCIALS**\n\n"

            "***JOHN LOUIE UBIAS***\n"
            "[FACEBOOK]\t\t<https://www.facebook.com/SenpaiLuwii>\n"
            "[INSTAGRAM]\t\t<https://www.instagram.com/itzluwi/>\n"
            "[TWITTER]\t\t<https://twitter.com/S_Luwi>\n"
            "[GITHUB]\t\t<https://github.com/SenpaiLuwi>\n\n"

            "***DOMINIC RAMOS***\n"
            "[FACEBOOK]\t\t<https://www.facebook.com/meeeeeeeeeeeeeeeengy>\n"
            "[FACEBOOK PAGE]\t\t<https://www.facebook.com/mengy07>\n"
            "[INSTAGRAM]\t\t<https://www.instagram.com/meeeeeeeeeeeeeeeengy/>\n"
            "[GITHUB]\t\t<https://github.com/Dramos02>\n\n"

            "***MIGUEL PILAPIL***\n"
            "[FACEBOOK]\t\t<https://www.facebook.com/ShappyYYy>\n"
            "[INSTAGRAM]\t\t<https://www.instagram.com/nonomigs__/>\n"
            "[TWITTER]\t\t<https://twitter.com/Daphr__>\n"
            "[GITHUB]\t\t<https://github.com/shap30>\n\n"

            "***KURT ROBIN COLONIA***\n"
            "[FACEBOOK]\t\t<https://www.facebook.com/teh.real.kurut0>\n"
            "[INSTAGRAM]\t\t<https://www.instagram.com/teh_real_kurut0/>\n"
            "[TWITTER]\t\t<https://twitter.com/teh_real_kurut0>\n"
            "[GITHUB]\t\t<https://github.com/krcolonia>\n\n"

            "***ROTSEN DAVID***\n"
            "[FACEBOOK]\t\t<https://www.facebook.com/rotsen.david.5>\n"
            "[FACEBOOK PAGE]\t\t<https://www.facebook.com/rezenro>\n"
            "[INSTAGRAM]\t\t<https://www.instagram.com/rotsen.rd/>\n"
            "[TWITTER]\t\t<https://twitter.com/rezenro>\n"
        )

    if current_sauce_mode is None and p_message == '!!nh':
        current_sauce_mode = 'sauce'
        return "What Sauce do you want to seek my lord? Type 's' if you have some and 'r' for randomized Luck!"

    if current_sauce_mode == 'sauce':
        if p_message == 's':
            current_sauce_mode = 's'
            return "Ok, Give the Sauce you Fucking Degenerate? (Ex: 177013 ( ͡° ͜ʖ ͡°))"
        elif p_message == 'r':
            current_sauce_mode = None
            return f"Here is the Link Enjoy!! <https://nhentai.net/g/random/>"
        else:
            return "Invalid choice. Please choose 's' for user input or 'r' for random sauce."

    if current_sauce_mode == 's' and re.match(r'^\d{6}$', p_message):
        sauce_number = p_message
        current_sauce_mode = None
        link = f"https://nhentai.net/g/{sauce_number}/"

        # Save the link to a text file
        with open('sos-dc.txt', 'a') as file:
            file.write(link + '\n')

        return f"Here is the Link Enjoy!! <{link}>"

    if p_message == '!!ts':
        current_sauce_mode = 'translate'
        return "What would you like to Translate?\n1. English to Japanese\n2. Japanese to English"

    if current_sauce_mode == 'translate':
        if p_message in ['1', '2']:
            translation_option = int(p_message)
            current_sauce_mode = f'translate_{translation_option}'
            if translation_option == 1:
                return "Enter the Text you Want to Translate from English to Japanese:"
            elif translation_option == 2:
                return "Enter the Text you Want to Translate from Japanese to English:"
            else:
                return "Invalid option. Please choose a valid translation option (1, 2)."

    if current_sauce_mode.startswith('translate_'):
        translation_option = int(current_sauce_mode.split('_')[1])
        if translation_option in [1, 2]:
            translated_text, romanji = translate_text(message, translation_option)
            current_sauce_mode = None
            output = f"The Translated Word:\n Word: **{message}**\n Translated Word: **{translated_text}**"
            if translation_option == 1:
                output += f"\n Romaji: **{romanji}**"
            return output

    return ""


def translate_text(text, translation_option):
    if translation_option == 1:
        translation = translator.translate(text, src='en', dest='ja')
        return translation.text, translate_to_romanji(translation.text)  # Translate to Romaji
    elif translation_option == 2:
        translation = translator.translate(text, src='ja', dest='en')
        romanji = translate_to_romanji(text)  # Translate to Romaji
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
