"""db.py
SQLite データベース接続とテーブル定義（SQLAlchemy ORM）
まだ Shopee API を呼ぶ前段階として、スキーマだけ作成します。
"""

import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

# .env から DB_URL を取得（無ければデフォルト sqlite:///shopee.db）
DB_URL = os.getenv("DB_URL", "sqlite:///shopee.db")

engine = create_engine(DB_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, future=True)

Base = declarative_base(metadata=MetaData())

class Order(Base):
    __tablename__ = "orders"

    order_sn: str = Column("order_sn", String, primary_key=True)
    status: str = Column(String, nullable=False)
    buyer_username: str = Column(String)
    total_amount: float = Column(Float)
    create_time: int = Column(Integer)
    update_time: int = Column(Integer)


def init_db():
    """テーブルを作成（存在しない場合のみ）"""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    # テーブルを作成して接続テスト
    init_db()
    print("✅ SQLite 初期化完了 →", DB_URL)

