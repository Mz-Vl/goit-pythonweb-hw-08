from datetime import datetime
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import func


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(20), nullable=False)
    birth_date: Mapped[Date] = mapped_column(Date, nullable=False)
    additional_data: Mapped[str] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column('created_at', DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column('updated_at', DateTime, default=func.now(), onupdate=func.now())