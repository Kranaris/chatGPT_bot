from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    BOT_TOKEN: str
    OPENAI_TOKEN: str
    ADMIN: str
    USERS: list[int]


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)

    users_str = env.str('USERS')
    users_dict = {}
    for item in users_str.split(','):
        key, value = item.split(':')
        users_dict[int(key)] = value

    return Config(tg_bot=TgBot(BOT_TOKEN=env('BOT_TOKEN'), OPENAI_TOKEN=env('OPENAI_TOKEN'), ADMIN=int(env('ADMIN')),
                               USERS=users_dict))
