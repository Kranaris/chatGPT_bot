from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json

def get_start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton("/start")],
        [KeyboardButton("/help")]
    ], resize_keyboard=True)
    return kb


def get_cancel() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('/canсel'))


def get_voice_ikb() -> InlineKeyboardMarkup:
    ikb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Да", callback_data=json.dumps({"action": "yes"}))],
        [InlineKeyboardButton("Нет. Повторить запрос", callback_data=json.dumps({"action": "no"}))],
    ])
    return ikb
