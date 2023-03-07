from aiogram.types import InlineKeyboardMarkup,  InlineKeyboardButton

# Кнопки админа
kb_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Добавить ➕", callback_data="add"), InlineKeyboardButton("Редактировать 🖋", callback_data="edit")],
    [InlineKeyboardButton("Добавить SkillCoins 💎", callback_data="coins_add")]
])

# Назад и Удалить
butt_back_and_del_search = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Удалить ➕🗑", callback_data="del_search")],
    [InlineKeyboardButton("🔙 Назад в меню", callback_data="back_menu_edit")]
])


def create_ikb_back_edit_menu(type_class: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Показать всех 🔍", callback_data="all_" + type_class), InlineKeyboardButton("🔙 Назад в меню", callback_data='back_menu_edit')]
    ])


#Назад в обычное меню
back_add_menu_btn = InlineKeyboardButton("🔙 Назад в меню", callback_data="back_menu")
back_add_menu = InlineKeyboardMarkup(inline_keyboard=[[back_add_menu_btn]])


#Создание кнопок списка
def create_ikb_records_list(rec_id, records_names, type_class, option=None, std_id=None) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    for i, name in enumerate(records_names):
        ikb.add(InlineKeyboardButton(name + " 🪪", callback_data=f"{type_class}_{rec_id[i]}"))
    back_edit = InlineKeyboardButton("🔙 Назад в меню", callback_data="back_menu_edit")
    if type_class == "awards" or type_class == "tasks":
        ikb.add(back_edit)
    elif type_class != 'prof':
        if option == 'search':
            ikb.row(InlineKeyboardButton("Показать всех 🔍", callback_data="all_" + type_class), InlineKeyboardButton("🔙 Назад в меню", callback_data="back_menu_edit"))
        elif option == 'edit':
            ikb.add(back_edit)
    elif type_class == "prof":
        if option == 'add':
            ikb.add(back_add_menu_btn)
        elif option == 'edit':
            ikb.add(InlineKeyboardButton("🔙 Назад", callback_data=f"{'std'}_{std_id}"))
    return ikb


def create_ikb_info_list(rec_id: int, columns: dict, table: str) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    count = 0
    for feat in columns:
        count += 1
        btn = InlineKeyboardButton(columns[feat], callback_data=f"feat_{rec_id}_{feat}_{columns[feat]}_{table}")
        if count % 2 == 0:
            ikb.add(prev_btn, btn)
        prev_btn = btn
    if table == 'teachers':
        ikb.add(prev_btn)
    if table == "teachers":
        ikb.row(InlineKeyboardButton("🔙 Назад в меню", callback_data="back_menu_edit"))
    else:
        ikb.row(InlineKeyboardButton("Удалить ➕🗑", callback_data="del"), InlineKeyboardButton("🔙 Назад в меню", callback_data="back_menu_edit"))

    return ikb

    
#Кнопки учителя студента и типа
back_main_menu_btn = InlineKeyboardButton("В главное меню 🏠", callback_data="back_main_menu")
add_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Куратор 💼", callback_data="add_teachers"), InlineKeyboardButton("Студент 👤", callback_data="add_students")],
    [InlineKeyboardButton("Награду 💰", callback_data="add_awards"), InlineKeyboardButton("Задания 📎", callback_data="add_tasks")],
    [InlineKeyboardButton("В главное меню 🏠", callback_data="back_main_menu")]
])

#Кнопки учителя студента поиска
edit_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Куратор 💼", callback_data="edit_tch"), InlineKeyboardButton("Студент 👤", callback_data="edit_std")],
    [InlineKeyboardButton("Награду 💰", callback_data="awards_edit"), InlineKeyboardButton("Задания 📎", callback_data="tasks_edit")],
    [back_main_menu_btn]
])

#Кнопки выбора поиска
student_and_teacher_search = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("Куратора 💼", callback_data="teacher_search"), InlineKeyboardButton("Студента 👤", callback_data="student_search")],
    [InlineKeyboardButton("🔙 Назад в меню", callback_data="back_menu_edit")]
])


#Кнопки да и нет
yes_and_no = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("✅", callback_data="yes"), InlineKeyboardButton("❌", callback_data="no")],
])

#Кнопки принять и отменить для добавления студентов
accept_and_reject = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("✅ Принять ✅", callback_data="accept"), InlineKeyboardButton("❌ Отмена ❌", callback_data="reject")]
])


def create_ikb_back_rec_info(rec_id, table):
    if table == "students":
        type_class = "std"
    elif table == "teachers":
        type_class = "tch"
    elif table == "awards":
        type_class = "awards"
    else:
        type_class = "tasks"
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔙 Назад", callback_data= f"{type_class}_{rec_id}")]])
    return ikb

accept_and_reject_edit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton("✅ Принять ✅", callback_data="accept_edit"), InlineKeyboardButton("❌ Отмена ❌", callback_data="reject_edit")]])

# Add SkillCoins

def students_list(rec_id=None, rec_names=None, is_all=False) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    if rec_id and rec_names:
        for i, name in zip(rec_id, rec_names):
            ikb.add(InlineKeyboardButton(name, callback_data=f'choose_std_{i}_{name}'))
    if is_all:
        ikb.add(InlineKeyboardButton("🔙 Назад", callback_data='back_main_menu'))
    else:
        ikb.row(InlineKeyboardButton("Показать всех 🔍", callback_data='allstd4tch'), InlineKeyboardButton("🔙 Назад", callback_data='back_main_menu'))
    return ikb


def tasks_list(rec_id=None, rec_title=None, rec_cost=None) -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup()
    if rec_id and rec_title and rec_cost:
        for i, title, cost in zip(rec_id, rec_title, rec_cost):
            ikb.add(InlineKeyboardButton(title, callback_data=f'choose_task_{i}_{title}_{cost}'))
    ikb.add(InlineKeyboardButton("🔙 Назад", callback_data='back_main_menu'))
    return ikb


def accept_add_coins():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("✅ Добавить ✅", callback_data="coins_add_accept"), InlineKeyboardButton("❌ Отмена ❌", callback_data="back_main_menu")],
    ])