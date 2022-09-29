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


class Status(Base):
    __tablename__ = 'status'
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column("Pavadinimas", String)
    price = Column("Kaina", Float)


class Order(Base):
    __tablename__ = 'my_order'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    customer = relationship("Customer")
    status_id = Column(Integer, ForeignKey("status.id"))
    status = relationship("Status")
    order_date = Column("Data", String)


class OrderLine(Base):
    __tablename__ = 'order_line'
    order_id = Column(Integer, ForeignKey('my_order.id'))
    order = relationship('Order')
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship("Product")
    quantity = Column(Integer)
