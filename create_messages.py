from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import random

# Esta función nos permite crear un mensaje HTML para enviar
# Puede editar todos los campos del mensaje utilizando la sintaxis HTML

def create_item_html(items):
    response = []
    print(f'{5 * "*"} Creating post {5 * "*"}')

    # Barajamos los elementos
    random.shuffle(items)

    # Itera sobre los items
    for item in items:
        # Si el producto tiene una oferta activa
        if 'off' in item:
            # Crea botón de compra
            keyboard = [
                [InlineKeyboardButton("🛒 Acquista ora 🛒", callback_data='buy', url=item["url"])],
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            # Crea el cuerpo del mensaje

            html = ""
            html += f"🎁 <b>{item['title']}</b> 🎁\n\n"

            if 'description' in list(item.keys()):
                html += f"{item['description']}\n"

            html += f"<a href='{item['image']}'>&#8205</a>\n"

            if 'savings' in list(item.keys()):
                html += f"❌ Non più: {item['original_price']}€ ❌\n\n"

            html += f"💰 <b>Al prezzo di: {item['price']}</b> 💰\n\n"

            if 'savings' in list(item.keys()):
                html += f"✅ <b>Risparmi: {item['savings']}€</b> ✅\n\n"

            html += f"<b><a href='{item['url']}'></a></b>"

            response.append(html)
            response.append(reply_markup)
    return response
