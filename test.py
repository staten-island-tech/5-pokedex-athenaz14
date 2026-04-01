""" sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]
def receipt(orders):
    the_receipt = {}
    for sushi in orders:
        if sushi["name"] in the_receipt:
            the_receipt[sushi['name']]['quantity'] +=1
        else:
            the_receipt[sushi["name"]] = {
                "price": sushi['price'],
                "quantity": 1
            }
    for sushi, value in the_receipt.items():
        price = value['price'] * value['quantity']
        print(sushi, value['quantity'], price)
    print(receipt)
receipt(sushi_orders) """

#for key, value in student.items():
wards = {
    "Cardiology":  ["Alice", "Bob", "Carol"],
    "Neurology":   ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Hank"],
    "Oncology":    ["Ivy", "Bob"]
}
staff = {}

for dept, docs in wards.items():
    for doc in docs:
        if doc not in staff:
            staff[doc] = [dept]
        else:
            staff[doc].append(dept)
print(staff["Bob"])

""" for dept, docs in wards.items():
    for doc in docs:
        if doc not in staff:
            staff[doc] = []
            staff[doc].append(dept)
print(staff["Bob"])
 """





"""             staff[docs[wards]]+=1
        else:
            staff[doc[wards]] = {
                "ward": _[wards]
                "doc": []
            }
        print(staff)
staff("Alice") """