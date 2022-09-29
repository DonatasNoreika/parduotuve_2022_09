from models import engine, Customer, Product, Status
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

while True:
    choice = int(input("Pridėti:\n1 - pirkėją\n2 - produktą\n3 - statusą\n4 - užsakymą\n"))
    match choice:
        case 1:
            f_name = input("Vardas: ")
            l_name = input("Pavardė: ")
            email = input("El. pašto adresas: ")
            customer = Customer(f_name, l_name, email)
            session.add(customer)
            session.commit()
        case 2:
            name = input("Produkto pavadinimas: ")
            price = float(input("Kaina: "))
            product = Product(name, price)
            session.add(product)
            session.commit()
        case 3:
            name = input("Statuso pavadinimas: ")
            status = Status(name)
            session.add(status)
            session.commit()


if __name__ == '__main__':
    Base.metadata.create_all(engine)
