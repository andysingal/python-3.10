import shelve

non_alcoholic_drinks = ['Coke','Juice','Water','Tea']
alcoholic_drinks = ['Bear','Wine','Vodka']
vegetables = ['onion','garlic','cucumber']
fruits = ['apple','orange','banana','grape']

# dict_key = input("Enter a key: ")
with shelve.open('food',writeback=True) as food_file:
    # food_file['non_alcoholic_drinks'] = non_alcoholic_drinks
    # food_file['alcoholic_drinks'] = alcoholic_drinks
    # food_file['vegetables'] = vegetables
    # food_file['fruits'] = fruits
    #
    # if dict_key in food_file:
    #     print(food_file[dict_key])
    # else:
    #     print("The key does not exist")
    food_file['fruits'] = fruits
    food_file.sync()
    fruits.append('Avacado')

    for food in food_file:
        print(food,food_file[food])



