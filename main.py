from models import Base, engine, Customer, Product, Status, Order, OrderLine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
""":type: sqlalchemy.orm.Session"""

if __name__ == '__main__':
    Base.metadata.create_all(engine)

while True:
    choice = int(input("Pridėti:\n1 - pirkėją\n2 - produktą\n3 - statusą\n4 - užsakymą\n5 - rodyti užsakymą\n"))
    match choice:
        case 1:
            f_name = input("Vardas: ")
            l_name = input("Pavardė: ")
            email = input("El. pašto adresas: ")
            customer = Customer(f_name, l_name, email)
            session.add(customer)
            session.commit()
            print("Klientas įvestas")
        case 2:
            name = input("Produkto pavadinimas: ")
            price = float(input("Kaina: "))
            product = Product(name, price)
            session.add(product)
            session.commit()
            print("Produktas įvestas")
        case 3:
            name = input("Statuso pavadinimas: ")
            status = Status(name)
            session.add(status)
            session.commit()
            print("Statusas įvestas")
        case 4:
            order_date = input("Data: ")
            customers = session.query(Customer).all()
            for customer in customers:
                print(customer)
            customer_id = int(input("Įveskite kliento ID: "))
            statusai = session.query(Status).all()
            for status in statusai:
                print(status)
            status_id = int(input("Įveskite statuso ID: "))
            order = Order(customer_id, status_id, order_date)
            session.add(order)
            session.commit()
            print("Užsakymas įvestas")
        case 5:
            orders = session.query(Order).all()
            for order in orders:
                print(order)
            order_id = int(input("Įveskite užsakymo ID: "))
            active_order = session.query(Order).get(order_id)
            print(f"Užsakymas nr. {active_order.id}:")
            print(f"Klientas: {active_order.customer}")
            print(f"Būklė: {active_order.status}")
            print("Užsakyti produktai:")
            total = 0
            for line in active_order.order_lines:
                suma = line.product.price * line.quantity
                total += suma
                print(f"{line.product} - {line.quantity}, suma: {suma}")
            print(f"Bendra suma: {total}")
            while True:
                choice2 = input("a - keisti statusą\nb - pridėti produktus\nc - išeiti iš užsakymo\n")
                match choice2:
                    case "a":
                        statusai = session.query(Status).all()
                        for status in statusai:
                            print(status)
                        status_id = int(input("Įveskite statuso ID: "))
                        active_order.status_id = status_id
                        session.commit()
                    case "b":
                        products = session.query(Product).all()
                        for product in products:
                            print(product)
                        product_id = int(input("Įveskite produkto ID: "))
                        quantity = int(input("Įveskite kiekį: "))
                        order_line = OrderLine(active_order.id, product_id, quantity)
                        active_order.order_lines.append(order_line)
                        session.commit()
                    case "c":
                        break
