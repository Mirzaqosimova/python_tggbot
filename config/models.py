import datetime
import sqlalchemy
from sqlalchemy import ARRAY, DateTime, ForeignKey, String

from config.const import *
from config.database import metadata
from config.enums import LanguageEnum, BotStatus

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("full_name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("chat_id", sqlalchemy.BigInteger),
    sqlalchemy.Column("phone_number", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("lang", sqlalchemy.Enum(LanguageEnum), nullable=True),
    sqlalchemy.Column("status", sqlalchemy.Enum(BotStatus), nullable=True),
    sqlalchemy.Column("created_at",DateTime, default=datetime.datetime.utcnow),
)

category = sqlalchemy.Table(
    "categorys",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("file_id", sqlalchemy.BigInteger),
    sqlalchemy.Column("created_at",DateTime, default=datetime.datetime.utcnow),
)

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String, nullable=True),
    sqlalchemy.Column("price", sqlalchemy.BigInteger,nullable=True),
    sqlalchemy.Column("category_id",sqlalchemy.Integer, ForeignKey('categorys.id'),nullable=True),
    sqlalchemy.Column("files", ARRAY(String), nullable=True),
    sqlalchemy.Column("created_at",DateTime, default=datetime.datetime.utcnow),
)