from database import Base

from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(80), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"


class Order(Base):
    ORDER_STATUS = (
        ("PENDING", "pending"),
        ("IN-TRANSIT", "in-Transit"),
        ("delivered", "delivered"),
    )

    PIZZA_SIZES = (
        ("SMALL", "small"),
        ("MEDIUM", "medium"),
        ("LARGE", "large"),
        ("EXTRA-LARGE", "extra-large"),
    )

    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    status = Column(
        ChoiceType(choices=ORDER_STATUS), default="PENDING",
    )
    pizza_size = Column(
        ChoiceType(choices=PIZZA_SIZES), default="SMALL"
    )
    user_id = Column(Integer, ForeignKey("user.id"))
    flavor = Column(String(50), nullable=False)
    user = relationship("User", back_populates="orders")

    def __repr__(self):
        return f"<Order {self.id}>"
