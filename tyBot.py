import telebot
from telebot import types
import marlon

#Token From Botfather
bot = telebot.TeleBot('2080897192:AAE7dlr2bt_MZ3Fnz_0M1w4xH2ux5WfHgKA')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Browse', 'Support')

keyboard_mens = telebot.types.ReplyKeyboardMarkup()
keyboard_mens.row("Men's Tops", "Men's Bottoms", "Men's Outerwear", "Men's Footwear", "Back", "Accessories")

keyboard3 = telebot.types.ReplyKeyboardMarkup()
keyboard3.row('Nike', 'Adidas', 'Vans', 'Назад↪️')

keyboard4 = telebot.types.ReplyKeyboardMarkup()
keyboard4.row('Valentino Garavani', 'Bottega Veneta', 'Назад↪️')

ReplyKeyboardMarkup = keyboard1.resize_keyboard, keyboard_mens.resize_keyboard, keyboard3.resize_keyboard, keyboard4.resize_keyboard = True, True, True, True


# РАБОТА С КОМАНДАМИ
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Hello, {0.first_name}'.format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard1)


@bot.message_handler(commands=['Back'])
def back_home(message):
    bot.send_message(message.chat.id, '{0.first_name}, Welcome Home.'.format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard1)


@bot.message_handler(commands=["geophone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_phone, button_geo)
    bot.send_message(message.chat.id, "*Отправь мне свой номер телефона или поделись местоположением*",
                     reply_markup=keyboard, parse_mode="Markdown")


# обработка клавиатуры
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Browse':
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)            
            mens_button = types.InlineKeyboardButton("Men's")
            womens_button = types.InlineKeyboardButton("Women's")
            channel_button = types.InlineKeyboardButton("Channel")
            support_botton = types.InlineKeyboardButton("Support")
            wishlist_button = types.InlineKeyboardButton("My Wishlist")
            
            sitepage = types.InlineKeyboardButton(text="", url="")
            keyboard.add(mens_button, womens_button, channel_button, support_botton, wishlist_button)
            
            #bot.send_photo(message.chat.id, open('img/humanandwoman.jpg', 'rb'), reply_markup=keyboard2)
            bot.send_message(message.chat.id, 'Make Selection', reply_markup=keyboard, parse_mode="Markdown")
        elif message.text == "Men's":
            markup = types.ReplyKeyboardMarkup(row_width=2)                           
            mens_tops = types.InlineKeyboardButton("Men's Tops")
            mens_bottoms = types.InlineKeyboardButton("Men's Bottoms")
            mens_outerwear = types.InlineKeyboardButton("Men's Outerwear")
            mens_footwear = types.InlineKeyboardButton("Men's Footwear")
            back = types.InlineKeyboardButton("🔙")
            mens_accessories = types.InlineKeyboardButton("Accessories")
            wishlist = types.InlineKeyboardButton("My Wishlist")
            markup.add(mens_tops, mens_bottoms, mens_outerwear, mens_footwear, back, mens_accessories, wishlist)           
            bot.send_message(message.chat.id, 'Make Selection', reply_markup=markup, parse_mode="Markdown")

            
        elif message.text == "Women's":
            markup = types.ReplyKeyboardMarkup(row_width=2)
            tops = types.InlineKeyboardButton("Tops")
            bottoms = types.InlineKeyboardButton("Bottoms")
            outerwear = types.InlineKeyboardButton("Outerwear")
            footwear = types.InlineKeyboardButton("Footwear")
            back = types.InlineKeyboardButton("🔙")
            accessories = types.InlineKeyboardButton("Accessories")
            wishlist = types.InlineKeyboardButton("My Wishlist")
            markup.add(tops, bottoms, outerwear, footwear, back, accessories, wishlist)           
            bot.send_message(message.chat.id, 'Make Selection', reply_markup=markup, parse_mode="Markdown")            
        
        
        elif message.text == 'Marlon':
            markupmarlon = types.ReplyKeyboardMarkup(row_width=1)
            wish = types.InlineKeyboardButton("Add To Wishlist")
            markupmarlon.add(wish)
            
            m_dict = marlon.marlon
            
            global koland
            koland = 'yoyoyo'
            
            bot.send_message(message.chat.id, 'Marlon:')
            for m in m_dict:
                bot.send_photo(message.chat.id, open(m_dict[m], 'rb'))
                m_message = m
                bot.send_message(message.chat.id,
                             m,
                             parse_mode="Markdown", reply_markup=markupmarlon)
                             
         
        elif message.text == 'Add To Wishlist':
            brody = str(message.from_user.first_name) + ' is adding things to wishlist.'
                
            bot.send_message('-522309488', brody, parse_mode='html')
            
        elif message.text == 'Nike':
            markupnike = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Купить", callback_data='buy')
            item2 = types.InlineKeyboardButton("В корзину", callback_data='basket')
            markupnike.add(item1, item2, )
            bot.send_message(message.chat.id, 'Все модели Nike:')
            bot.send_photo(message.chat.id, open('img/nike/nike1.jpg', 'rb'))
            bot.send_message(message.chat.id,
                             '*Nike X Off-White*\nвысокие кроссовки, *размеры:37-44* Air Jordan 1 Retro High Off-White-UNC\n*154 810 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/nike/nike2.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Nike X Off-White* кроссовки, *размеры:37-44* \n*106 250 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/nike/nike3.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Nike x Sacai LDV* кроссовки, *размеры:37-44* \n*72 632 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

        elif message.text == 'Adidas':
            markupnike = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Купить",  callback_data='buy')
            item2 = types.InlineKeyboardButton("В корзину", callback_data='basket')

            markupnike.add(item1, item2)
            bot.send_message(message.chat.id, 'Все модели Adidas:')
            bot.send_photo(message.chat.id, open('img/adidas/adidas1.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Adidas Galaxy Spezial* кроссовки, *размеры:37-44* \n*13 927 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/adidas/adidas2.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Adidas Tokio Solar* кроссовки, *размеры:37-44* \n*8 647 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/adidas/adidas3.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Adidas Originals NMD_R1* кроссовки, *размеры:37-44* \n*23 657 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/adidas/adidas4.jpg', 'rb'))
            bot.send_message(message.chat.id,
                             '*Adidas Ozweego из коллаборации с Pusha T* кроссовки, *размеры:37-44* \n*8 716 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/adidas/adidas5.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Adidas ZX 6000 Juventus * кроссовки, *размеры:37-44* \n*12 255 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

        elif message.text == 'Vans':
            markupnike = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Купить", callback_data='buy')
            item2 = types.InlineKeyboardButton("В корзину", callback_data='basket')

            markupnike.add(item1, item2)
            bot.send_message(message.chat.id, 'Все модели Vans:')
            bot.send_photo(message.chat.id, open('img/vans/vans1.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Vans Old Skool* кеды, *размеры:37-44* \n*12 036 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/vans/vans2.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Vans Old Skool* кеды, *размеры:37-44* \n*6 558 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/vans/vans 3.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Vans Sk8-Hi MT* кроссовки, *размеры:37-44* \n*7 265 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

        elif message.text == 'Back':
            bot.send_message(message.chat.id, 'Welcome Home, {0.first_name}.'.format(
                message.from_user, bot.get_me()), parse_mode='html', reply_markup=keyboard1)

        elif message.text == 'Мужская обувь👞':
            bot.send_message(message.chat.id, '*Выберите бренд:* ', reply_markup=keyboard3, parse_mode="Markdown")

        elif message.text == 'Женская обувь👠':
            bot.send_message(message.chat.id, '*Выберите бренд:* ', reply_markup=keyboard4, parse_mode="Markdown")

        elif message.text == 'Valentino Garavani':
            markupnike = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Купить", callback_data='buy')
            item2 = types.InlineKeyboardButton("В корзину", callback_data='basket')

            markupnike.add(item1, item2)
            bot.send_photo(message.chat.id, open('img/Valentino Garavani/valentino1.jpg', 'rb'))
            bot.send_message(message.chat.id,
                             '*Valentino Garavani*,ботинки Uniqueform 80 на платформе\n*размеры:36-43* \n*65 340 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/Valentino Garavani/valentino2.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Valentino Garavani*,кроссовки Gumboy\n*размеры:36-43* \n*50 690 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

        elif message.text == 'Bottega Veneta':
            markupnike = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Купить", callback_data='buy')
            item2 = types.InlineKeyboardButton("В корзину", callback_data='basket')

            markupnike.add(item1, item2)
            bot.send_photo(message.chat.id, open('img/Bottega Veneta/Bottega Veneta1.jpg', 'rb'))
            bot.send_message(message.chat.id,
                             '*Bottega Veneta*,сетчатые туфли с завязками\n*размеры:38-42* \n*54 210 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)

            bot.send_photo(message.chat.id, open('img/Bottega Veneta/Bottega Veneta2.jpg', 'rb'))
            bot.send_message(message.chat.id, '*Bottega Veneta*,мюли на каблуке\n*размеры:39-43* \n*62 581 ₽*',
                             parse_mode="Markdown", reply_markup=markupnike)


        else:
            bot.send_message(message.chat.id, 'This has Not Been Set Yet', parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'sberbank':
                bot.send_message(call.message.chat.id, 'Ссылка для оплаты платежной системой Сбербанк:')
            elif call.data == 'kassa':
                bot.send_message(call.message.chat.id,
                                 'Ссылка для оплаты платежной системой Юкасса')
            elif call.data == 'buy':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='Недостаточно средств!🚫')

            elif call.data == 'basket':
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Add This And Message Group✅")
                brody = str(call.message.from_user.first_name) + ' is adding things to wishlist.'
                
                bot.send_message('-522309488', brody, parse_mode='html')
                #bot.send_message('-522309488','This is my test', parse_mode='html')
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
