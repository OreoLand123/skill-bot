from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

import func_bot

# CallbackData
cd_main_menu = CallbackData('main_menu_std', 'chapter')
cd_spend = CallbackData('spend_list', 'id', 'title', 'cost')
cd_purchase = CallbackData('purchase_accept', 'id', 'title', 'cost')


# Main menu
def get_main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('Как заработать? 📌', callback_data=cd_main_menu.new('earn')),
         InlineKeyboardButton('Потратить 💳', callback_data=cd_main_menu.new('spend'))],
        [InlineKeyboardButton('Проверить счёт 💰', callback_data=cd_main_menu.new('cheak'))],
    ])


# Back to main menu
def get_back() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('🔙 Назад', callback_data=cd_main_menu.new('menu'))]
    ])


# List of spend
def get_list_spend() -> InlineKeyboardMarkup:
    rec_id, titles, costs = func_bot.main_get(tables=['awards'], columns=['id', 'title', 'cost'])
    ikb = InlineKeyboardMarkup()
    for i, id in enumerate(rec_id):
        ikb.add(InlineKeyboardButton(titles[i] + ' ' + str(costs[i]) + " 💸",
                                     callback_data=cd_spend.new(id=id, title=titles[i], cost=costs[i])))
    ikb.add(InlineKeyboardButton('🔙 Назад', callback_data=cd_main_menu.new('menu')))
    return ikb


# Confirm with spend SkillCoins
def get_confirmation(rec_id: int, title: str, cost: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton('💸 Купить 💸', callback_data=cd_purchase.new(id=rec_id, title=title, cost=cost)),
         InlineKeyboardButton('❎ Отмена ❎', callback_data=cd_main_menu.new('spend'))]
    ])
