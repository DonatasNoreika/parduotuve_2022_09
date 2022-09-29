from sqlalchemy import (Column,
                        Integer,
                        String,
                        Float,
                        ForeignKey,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///parduotuve.db')
Base = declarative_base()


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    f_name = Column("Vardas", String)
    l_name = Column("Pavardė", String)
    email = Column("El. pašto adresas", String)

    def __init__(self, f_name, l_name, email):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

    def __repr__(self):
        return f"{self.id}: {self.f_name} {self.l_name}"

class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f"{self.id}: {self.name}"


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    price = Column("Kaina", Float)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order(Base):
    __tablename__ = 'my_order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer")
    status_id = Column(Integer, ForeignKey("status.id"))
    status = relationship("Status")
    order_date = Column("Data", String)

    def __init__(self, customer_id, status_id, order_date):
        self.customer_id = customer_id
        self.status_id = status_id
        self.order_date = order_date

    def __repr__(self):
        return f"{self.id}: {self.order_date}, {self.customer.f_name} {self.customer.l_name}, {self.status.name}"


class OrderLine(Base):
    __tablename__ = 'order_line'
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('my_order.id'))
    order = relationship('Order')
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("Product")
    quantity = Column(Integer)
