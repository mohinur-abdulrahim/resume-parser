from environs import Env
from pydantic import BaseModel


class Bot(BaseModel):
    """
    Bot configuration
    """
    token: str
    admins: list


class Database(BaseModel):
    """
    Database configuration
    """
    host: str
    port: int
    username: str = None
    password: str = None
    database: str


class Config(BaseModel):
    """
    Configuration model
    """
    bot: Bot
    db: Database = None


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(bot=Bot(token=env.str("BOT_TOKEN"), admins=env.list("ADMINS")))
