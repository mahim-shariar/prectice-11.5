from django.shortcuts import render


def index(request):
    meals = [
        {
            "strMeal": "BeaverTails",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "idMeal": "52928",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"
        },
        {
            "strMeal": "Breakfast Potatoes",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "idMeal": "52965",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        },
        {
            "strMeal": "Canadian Butter Tarts",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "idMeal": "52923",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        },
        {
            "strMeal": "Montreal Smoked Meat",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "idMeal": "52927",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        },
        {
            "strMeal": "Nanaimo Bars",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "idMeal": "52924",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        },
        {
            "strMeal": "Pate Chinois",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "idMeal": "52930",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        },
        {
            "strMeal": "Pouding chomeur",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "idMeal": "52932",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        },
        {
            "strMeal": "Poutine",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "idMeal": "52804",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        },
        {
            "strMeal": "Rappie Pie",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "idMeal": "52933",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        },
        {
            "strMeal": "Split Pea Soup",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "idMeal": "52925",
            "strDetails": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates! Lorem ipsum dolor sit amet consectetur adipisicing elit. Magni, voluptates!"

        }
    ]

    return render(request, 'index.html', {'meals': meals})
