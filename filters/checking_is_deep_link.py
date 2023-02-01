from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsDeeplink(BoundFilter):
    async def check(self, message: types.Message):
        return len(message.text.split()) == 2