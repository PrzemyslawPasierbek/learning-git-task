#1
shopping_list = {
"bakery" : ["bread", "rolls", "donuts"],
"vege_shop" : ["rucolas", "carrots", "celerys"]
}

print("Shoppinglist")
for shop in shopping_list:
    print()
    for products in shopping_list.values():
        print()
    amount_products = len(products)
    print(f"I will go the {shop} and I will buy {products}")
print(f"Amount of products are {amount_products}")