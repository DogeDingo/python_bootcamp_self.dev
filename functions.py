chaos = ["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for x in chaos:
    split = x.split(":")
    text = split[0]
    price = int(split[1])
    if "new" in text:
        order.append(price)
    elif "old" in text:
        if price > 0 and price <= 20:
            price = price * 0.8
            order.append(price)
        elif price > 20 and price <= 50:
            price = price * 0.6
            order.append(price)
        elif price > 50:
            price = price * 0.4
            order.append(price)
print(order)

#     if "new price: " in x:
#         # a = (x[-2] + x[-1])
#         # order.append(a)
#     elif "old price: " in x:
#         s = (x[-2] + x[-1])
#         new_price = int(s)
#         if new_price > 0 and new_price <= 20:
#             new_price = new_price * 0.8
#             order.append(new_price)
#         elif new_price > 20 and new_price <= 50:
#             new_price = new_price * 0.6
#             order.append(new_price)
#         elif new_price > 50:
#             new_price = new_price * 0.4
#             order.append(new_price)
#
# print(order)
