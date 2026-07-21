def food_recommendation():

    while True:

        print("\n==================================")
        print("AI FOOD RECOMMENDATION SYSTEM")
        print("==================================")


        # Meal Selection
        meal = input("""
Which meal are you looking for?

1. Breakfast
2. Lunch
3. Dinner
4. Snack
5. Exit

Enter your choice: 
""").lower()


        if meal == "5" or meal == "exit":
            print("\nThank you for using AI Food Recommendation System!")
            break


        # Food Type Selection
        food_type = input("""
What type of food do you prefer?

1. Vegetarian
2. Non-Vegetarian
3. Return to Meal Selection

Enter your choice: 
""").lower()


        if food_type == "3":
            continue


        # Budget Selection
        budget = input("""
What is your budget?

1. Low
2. Medium
3. High
4. Return to Food Type

Enter your choice:
""").lower()


        if budget == "4":
            continue


        print("\n----------------------------------")
        print("Recommended Meal:")
        print("----------------------------------")


        # Breakfast Recommendation
        if meal == "breakfast" or meal == "1":

            if food_type == "vegetarian" or food_type == "1":

                if budget == "low" or budget == "1":
                    print("Banana and Tea")

                elif budget == "medium" or budget == "2":
                    print("Vegetable Omelette, Toast, and Fresh Juice")

                elif budget == "high" or budget == "3":
                    print("Avocado Toast, Fruit Bowl, and Smoothie")

                else:
                    print("Invalid Budget")

            else:

                if budget == "low" or budget == "1":
                    print("Egg Sandwich and Tea")

                elif budget == "medium" or budget == "2":
                    print("Chicken Sandwich and Fresh Juice")

                elif budget == "high" or budget == "3":
                    print("Chicken Pancakes and Smoothie")



        # Lunch Recommendation
        elif meal == "lunch" or meal == "2":

            if food_type == "vegetarian" or food_type == "1":

                if budget == "low" or budget == "1":
                    print("Rice, Lentils, and Salad")

                elif budget == "medium" or budget == "2":
                    print("Vegetable Pasta and Garlic Bread")

                elif budget == "high" or budget == "3":
                    print("Vegetable Curry, Rice, and Dessert")

            else:

                if budget == "low" or budget == "1":
                    print("Chicken Rice")

                elif budget == "medium" or budget == "2":
                    print("Chicken Rice Bowl with Salad")

                elif budget == "high" or budget == "3":
                    print("Grilled Chicken, Rice, and Dessert")



        # Dinner Recommendation
        elif meal == "dinner" or meal == "3":

            if food_type == "vegetarian" or food_type == "1":

                if budget == "low" or budget == "1":
                    print("Vegetable Curry and Rice")

                elif budget == "medium" or budget == "2":
                    print("Vegetable Soup and Pasta")

                elif budget == "high" or budget == "3":
                    print("Special Vegetarian Platter")

            else:

                if budget == "low" or budget == "1":
                    print("Chicken Sandwich")

                elif budget == "medium" or budget == "2":
                    print("Grilled Chicken with Rice")

                elif budget == "high" or budget == "3":
                    print("Steak, Vegetables, and Dessert")


        elif meal == "snack" or meal == "4":

            if food_type == "vegetarian" or food_type == "1":
                print("🍎 Fruit Salad and Juice")

            else:
                print("🌯 Chicken Wrap and Juice")


        else:
            print("Invalid meal choice.")


        print("\n----------------------------------")
        print("What would you like to do next?")
        print("1. Get another recommendation")
        print("2. Exit")

        choice = input("Enter your choice: ")


        if choice == "1":
            continue

        elif choice == "2":
            print("\nThank you for using AI Food Recommendation System!")
            break

        else:
            print("\nInvalid choice. Closing program...")
            break

food_recommendation()