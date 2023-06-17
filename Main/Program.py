import json
import datetime


class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def getName(self):
        return self.name

    def getQuantity(self):
        return self.quantity

    def subtractQuantity(self, i):
        self.quantity -= i

    def getPrice(self):
        return self.price

    def toJSON(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "price": self.price
        }

    def __str__(self):
        string = "Produto: {}; Quantidade: {} kg; Valor: {} R$/kg".format(self.name, self.quantity,
                                                                          round(self.price, 2))
        return string


class Stock:
    def __init__(self):
        self.stockList = {}

    def add(self, productID, product):
        self.stockList[productID] = product

    def getProduct(self, id):
        return self.stockList.get(id)

    def getIDlist(self):
        return self.stockList.keys()

    def startStock(self):
        try:
            with open("stocklist.json", "r") as file:
                jsonMap = json.load(file)

            for key, value in jsonMap.items():
                name = value["name"]
                quantity = value["quantity"]
                price = value["price"]
                self.add(int(key), Product(name, quantity, price))

        except FileNotFoundError:
            print("Erro ao carregar o estoque a partir de stocklist.json")

    def endStock(self):
        with open("stocklist.json", "w") as file:
            json.dump(self.stockList, file, default=lambda product: product.toJSON())

    def __str__(self):
        string = ""
        for key, value in self.stockList.items():
            if value.getQuantity() > 0:
                string += "ID: {} - {}\n".format(key, value)
        return string


def registerProduct(stock):
    id = int(input("Insira a ID do prodruto: "))

    if not id in stock.getIDlist():
        name = str(input("Insira o nome do produto: "))
        quantity = float(input("Insira a quantidade do produto em kg: "))

        if quantity > 0:
            price = float(input("Insira o preço do produto por kg: "))

            if price > 0:
                stock.add(id, Product(name, quantity, price))
                print("Produto cadastrado com sucesso!")

            else:
                print("Preço inválido")

        else:
            print("Quantidade inválida")

    else:
        print("ID já existente")


def printStock(stock):
    if len(stock.getIDlist()) > 0:
        print(stock)

    else:
        print("Não há itens no estoque")


def registerPurchase(stock):
    id = int(input("Insira a ID do prodruto: "))
    product = stock.getProduct(id)

    if product is not None:
        print(product)
        quantity = float(input("Insira a quantidade de kg desejada: "))

        if quantity > 0:
            if product.getQuantity() >= quantity:
                purchasePrice = product.getPrice() * quantity

                while True:
                    print("\nO valor da compra é de: R$", purchasePrice)
                    print("Deseja adicionar ao carrinho?\n1 - Sim\n2 - Não")
                    keyboard = int(input())

                    if keyboard == 1:
                        print("Compra adicionada!")
                        product.subtractQuantity(quantity)
                        return purchasePrice

                    elif keyboard == 2:
                        print("Compra cancelada")
                        break

                    else:
                        print("Input inválido")

            else:
                print("Quandidade em estoque insuficiente")

        else:
            print("Quantidade inválida")

    else:
        print("ID inválida")

    return 0


def checkout(cartTotal):
    if cartTotal != 0:
        print("O total da compra foi de: R$", round(cartTotal, 2))
        totalSells.append(cartTotal)

    else:
        print("Não há itens no carrinho")

    return 0


def endSells(totalSells):
    print("O total do caixa foi de: R$", round(sum(totalSells), 2))

    try:
        with open("sellslog.json", "r") as file:
            jsonMap = json.load(file)

    except FileNotFoundError:
        jsonMap = {}

    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    jsonMap.update({now: sum(totalSells)})

    with open("sellslog.json", "w") as file:
        json.dump(jsonMap, file)


stock = Stock()
stock.startStock()
cartTotal = 0
totalSells = []

while True:
    print("\n---------------menu---------------")
    print(
        "1 - Cadastrar produto no estoque\n2 - Lista produtos do estoque\n3 - Registrar compra\n4 - Finalizar carrinho\n5 - Fechamento de caixa")
    keyboard = int(input())
    print()

    if keyboard in range(1, 6):
        if keyboard == 1:
            registerProduct(stock)

        elif keyboard == 2:
            printStock(stock)

        elif keyboard == 3:
            cartTotal += registerPurchase(stock)
            print("\nO total do carrinho é de: R$", round(cartTotal, 2))

        elif keyboard == 4:
            cartTotal = checkout(cartTotal)

        elif keyboard == 5:
            endSells(totalSells)
            stock.endStock()
            break

    else:
        print("Input inválido")
