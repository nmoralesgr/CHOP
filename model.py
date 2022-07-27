meals = {
  "Arroz con pollo" : ''' You should try Arroz con pollo! Here is the recipe:
2 tsp adobo seasoning ($0.20),
1.5 lbs boneless chicken thighs ($6.49),
2 2/3 Tbsp cooking oil, divided ($0.11),
1/4 cup sofrito ($0.36),
1 red bell pepper, small dice, divided ($0.98),
1/2 yellow onion, small dice ($0.19),
3 cloves garlic, minced ($0.24),
2 Tbsp tomato sauce ($0.06),
1/2 cup pimiento stuffed Spanish olives ($1.16),
2 cups rice ($0.74),
2 1/2 cups chicken stock ($1.12),
1/4 tsp salt ($0.02),
1 1/2 tsp sazón seasoning ($0.19),
1/2 cup frozen green peas ($0.33),
1/4 cup cilantro (optional garnish) ($0.11). It only costs $12.30 to make this meal!''',

"Menemen" : ''' You should try Menemen! Here is the Recipe!:
2 Tbsp olive oil ($0.25),
1 yellow onion ($0.37),
1 bell pepper (any color) ($0.98),
1/2 tsp dried oregano ($0.05),
1/4 tsp crushed red pepper (or Aleppo pepper) ($0.03),
1 15oz. can diced tomatoes ($0.79)
1 tsp salt ($0.05),
1/4 tsp freshly cracked black pepper ($0.02),
4 large eggs, lightly beaten ($0.78),
1/4 cup chopped parsley ($0.40),
1 cup crumbled feta (optional) ,($1.64) It only costs 5.36 to make!''',

"Kale Pasta Salad": ''' You should try Kale Pasta Salad! Here is the Recipe: 1/3 cup olive oil ($0.85),
3 Tbsp balsamic vinegar ($0.42),
2 Tbsp mayonnaise ($0.15),
1/2 Tbsp Dijon mustard ($0.09),
1 clove garlic, minced ($0.08),
1/2 tsp dried basil ($0.05),
1/4 tsp salt ($0.02),
1/4 tsp freshly cracked black pepper ($0.02). It only costs $7.88 to make!''',


"BBQ Kebabs": ''' You should try Barbeque styled Kebabs!
Here is the Recipe: 2 small red onions (or one large) ($0.76),
1 fresh pineapple ($1.99), 
1.3 lbs. Simply Nature Organic Chicken Breasts ($8.21),
2 Tbsp cooking oil, divided ($0.08),
1 tsp smoked paprika ($0.10),
1 tsp sweet paprika ($0.10),
1/2 tsp garlic powder ($0.05),
1/4 tsp salt ($0.02),
1/4 tsp freshly cracked black pepper ($0.02),
1/2 cup Burman's Original BBQ Sauce ($0.21),
2 green onions, sliced ($0.12). It only costs $11.66 to make! ''',

"Vegetarian French Dip Sandwiches": ''' You should try vegetarian french dip sanwiches! Here is the recipe:
  1 yellow onion ($0.32)
3 portobello mushroom caps (about ½ lb.) ($3.99)
2 Tbsp butter ($0.20)
1/8 tsp salt ($0.01)
1/8 tsp freshly cracked black pepper ($0.01)
1/4 tsp dried thyme ($0.02)
1/4 tsp dried oregano ($0.02)
2 cups vegetable broth* ($0.26)
1 Tbsp soy sauce ($0.06)
1/2 Tbsp brown sugar ($0.02)
1/8 tsp garlic powder ($0.01)
4 6-inch French or Hoagie rolls ($1.66)
4 slices provolone ($1.00). It only costs $6.58 to make!''',


}

cost = {
"Arroz con pollo": 12.30,
"Menemen": 5.36,
"Kale Pasta Salad": 7.88,
"BBQ Kebabs": 11.66,
"Vegetarian French Dip Sandwiches" : 6.58
}

images_dict = {
"Arroz con pollo" : "static/images/arroz-con-pollo.jpg",
"Menemen" : "static/images/Menemen-Square.jpeg",
"Kale Pasta Salad" : "static/images/kale-pasta-salad.jpg",
"BBQ Kebabs": "static/images/steak-kebabs-26.jpg",
"Vegetarian French Dip Sandwiches": "static/images/Vegetarian-French-Dip-Sandwiches-V1.jpg"

}

def budget_calc(budget):
  #while the user has enough money to buy more food, we keep printing new meals
  user_meals = {} 
  mealnumber = 1 
  
  for meal in cost:
    if budget >= cost[meal]:
      # user_meals[mealnumber] = meal
      # user_meals [str(mealnumber) + "description"] = meals[meal]
      user_meals[meal] = meals[meal]
      budget -= cost[meal]
    mealnumber += 1 
  return user_meals 
#  else:
#    return "We don't have any results for this yet! Please try inserting different values!"

def images_calc():
  return images_dict


