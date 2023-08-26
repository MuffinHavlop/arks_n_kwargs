def burger_order(Size, *ingridients, **details):
    print(f"Your burger order is a {Size}, with the following ingridients: ")
    for ingridient in ingridients:
        print(f"- {ingridient}")
    print ("Details of the order are: ")
    for catagory, content in details.items():
        print(f"- {catagory}: {content}")

burger_order("large", "Onion", "Patty", "Lettuce", "Tomato", "mayonese", delivery = True, tip = 5)
