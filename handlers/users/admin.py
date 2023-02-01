from aiogram import executor, types

from data.strings import INPUT_TO_SHOW
from filters.check_admin import IsAdmin
from loader import dp, bot, db


# ----------   ADMIN side   ----------, text=INPUT_TO_SHOW

@dp.message_handler(IsAdmin(), text=INPUT_TO_SHOW, state='*')
async def info(message: types.Message):
    # text = INVITES_INFO + '\n'
    # for user, count in db.get_top_invites_count():
    #     text += '\n'
    #     text = text + LINK_USER + str(user) + ' ---- ' + str(count)
    text = 'admin'
    await message.answer(text=text)

#
# @dp.message_handler(commands=['start'])
# async def on_startup(message: types.Message):
#     if not db.is_exist_user(message.from_user.id):
#         try:
#             deep_link = message.text.split()[1]
#         except:
#             deep_link = ''
#
#         try:
#             db.add_user(
#                 identifier=message.from_user.id,
#                 referral=deep_link,
#                 active=1
#             )
#
#         except Exception as err:
#             await message.reply(err)
#
#         # ADMINGA xabar beramiz
#         msg = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> bazaga qo'shildi."
#         await bot.send_message(chat_id=ADMINS[0], text=msg)
#         if deep_link:
#             msg_to_ref = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a> sizning linkingiz orqali botga ulandi."
#             await bot.send_message(chat_id=int(deep_link), text=msg_to_ref)
#             db.update_invites_count(deep_link)
#         await bot.send_message(chat_id=message.from_user.id, text="Harakatni tanlang", reply_markup=menu_keyboard)
#
#     else:
#         await message.answer("Sizni botimizda yana ko'rib turganimizdan xursandmiz!")
#         await bot.send_message(chat_id=message.from_user.id, text="Harakatni tanlang", reply_markup=menu_keyboard)
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
