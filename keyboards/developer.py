from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Main menu
def get_main_menu_developer():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("➕ Добавить админа ➕", callback_data="admins_add"),
         InlineKeyboardButton("🖋 Редактировать админа 🖋", callback_data="admins_edit")],
        [InlineKeyboardButton('📂 Получить файл DB 📂', callback_data='get_file_db')],
    ])


# Back to main menu
back_main_menu_but = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("🏠 Назад в главное меню 🏠", callback_data="back_dev_main_menu")]
])

# Accept or reject add admin
confirm_add_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("✅ Принять ✅", callback_data="accept_add_admin"),
     InlineKeyboardButton("❌ Отменить ❌", callback_data="reject_add_admin")]])


# Admins list
def create_list_admins_ikb(records_name, rec_id):
    ikb = InlineKeyboardMarkup()
    for i, name in enumerate(records_name):
        ikb.add(InlineKeyboardButton("💼 " + name + " 💼", callback_data=f"admins_{rec_id[i]}"))
    ikb.add(InlineKeyboardButton("🏠 Назад в главное меню 🏠", callback_data="back_dev_main_menu"))
    return ikb


# Full admin info
edit_admin_ikb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("🪪 Имя 🪪", callback_data="input_name"), InlineKeyboardButton("🆔", callback_data="input_id")],
    [InlineKeyboardButton("🔙 Назад", callback_data="admins_edit")],
    [InlineKeyboardButton("Удалить ➕🗑", callback_data="del_admins")]])


# Back to full admin info
def back_edit_admin_ikb(rec_id):
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔙 Назад", callback_data=f"admins_{rec_id}")]])
    return ikb
