-- INSERT INTO auth_user (username, password, first_name, last_name, is_staff, email, is_superuser, is_active, date_joined) VALUES ('yoni','pbkdf2_sha256$390000$dihFNmTJCPBMD9ykqUexgb$NIDkfRi5Sc9+waDfo1M3x5zwVVmCLPZDIPRCZJJnSUw=', 'yehonatan', 'amir', True, 'yoni@email.com', True, True, '2023-04-20 18:47:57.955801');

-- food_ordering_guest_category
INSERT INTO food_ordering_guest_category (name, image) VALUES ('starters', 'starters.jpeg');
INSERT INTO food_ordering_guest_category (name, image) VALUES ('mains', 'mains.jpeg');
INSERT INTO food_ordering_guest_category (name, image) VALUES ('desserts', 'desserts.jpeg');
INSERT INTO food_ordering_guest_category (name, image) VALUES ('drinks', 'drinks.jpeg');

-- food_ordering_guest_dish
-- starters
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Avocado Salad', 35, 'Fresh avocado slices mixed with tomatoes, red onion, and cilantro, dressed in a tangy lime vinaigrette.', 'AvocadoSalad.jpeg', False, True, 1);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Anti Pasti', 29, 'A selection of marinated vegetables, cheeses, and olives.', 'AntiPasti.jpeg', True, True, 1);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Eggs Salad', 35, 'Boiled eggs mixed with mayonnaise, mustard, and seasonings, served on a bed of lettuce.', 'EggSalad.jpeg', False, True, 1);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Chicken Wings', 42, 'Crispy fried or baked chicken wings coated in a spicy or savory sauce. Served with celery sticks and blue cheese or ranch dressing.', 'Wings.jpeg', False, False, 1);
-- mains
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Steak', 130, 'Our stake entrecote dish comes with a generous portion of juicy, grilled steak, served with a side of crispy fries and a fresh garden salad.', 'Stake.jpeg', True, False, 2);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Chicken', 90, 'Our whole chicken dish is a delicious and satisfying meal. Roasted to perfection, the juicy chicken is served with a side of seasoned vegetables and creamy mashed potatoes.', 'Chicken.jpeg', True, False, 2);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Shnitzel', 74, 'Our schnitzel dish features a tender and crispy breaded cutlet, served with a side of savory mashed potatoes and steamed vegetables.', 'Shnitzel.jpeg', False, False, 2);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Tomato Pasta', 52, 'Our tomato pasta dish features al dente pasta in a rich tomato sauce, topped with freshly grated parmesan cheese and chopped basil.', 'TomatoPasta.jpeg', False, True, 2);
-- desserts
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Ice Cream', 30, 'Our ice cream dessert is the perfect way to end your meal. A generous scoop of creamy vanilla ice cream is served with a warm, gooey chocolate sauce and topped with whipped cream and a cherry.', 'IceCream.jpeg', False, True, 3);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Cheese Cake', 47, 'Our cheesecake dessert is a classic favorite. A smooth and creamy New York-style cheesecake sits atop a graham cracker crust, drizzled with a sweet fruit compote and finished with a dollop of whipped cream.', 'CheeseCake.jpeg', False, True, 3);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Chocolate Cake', 47, 'Our chocolate cake dessert is a chocolate lovers dream. Rich layers of moist chocolate cake are stacked and filled with creamy chocolate ganache, then topped with a smooth chocolate buttercream frosting and a sprinkle of chocolate shavings.', 'ChocolateCake.jpeg', False, True, 3);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Crack Pai', 42, 'Our crack pie dessert is a decadent treat made with a buttery oatmeal cookie crust and a gooey, rich filling of brown sugar, cream, and eggs. Its served with a dollop of whipped cream and a sprinkle of powdered sugar on top.', 'CrackPai.jpeg', False, True, 3);
-- drinks
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('CocaCola', 14, 'Carbonated beverage with cola flavor.', 'CocaCola.jpeg', True, True, 4);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('CocaCola Zero', 14, 'Sugar-free carbonated beverage with cola flavor.', 'ZeroCocaCola.jpeg', True, True, 4);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Fanta', 14, 'Carbonated beverage with orange flavor.', 'Fanta.jpeg', True, True, 4);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Sprait', 14, 'Carbonated beverage with lime flavor.', 'Sprait.jpeg', True, True, 4);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Water', 10, 'Mineral water.', 'Water.jpeg', True, True, 4);

-- food_ordering_guest_cart
INSERT INTO food_ordering_guest_cart (user_id) VALUES (1);

-- food_ordering_guest_items
-- INSERT INTO food_ordering_guest_items (dish_id, cart_id, amount) VALUES (1,1,1);
-- INSERT INTO food_ordering_guest_items (dish_id, cart_id, amount) VALUES (2,1,1);
-- INSERT INTO food_ordering_guest_items (dish_id, cart_id, amount) VALUES (3,1,2);
-- INSERT INTO food_ordering_guest_items (dish_id, cart_id, amount) VALUES (4,1,1);

-- food_ordering_guest_delivery
-- INSERT INTO food_ordering_guest_delivery (is_deliverd, address, comment, order_id) VALUES (True,'Hapragim 18','Privet House','');
-- INSERT INTO food_ordering_guest_delivery (is_deliverd, address, comment, order_id) VALUES (False,'Derech Hashalom 50','Leave The Door Man','');
-- INSERT INTO food_ordering_guest_delivery (is_deliverd, address, comment, order_id) VALUES (True,'Oziel 101','Come Fast','');
-- INSERT INTO food_ordering_guest_delivery (is_deliverd, address, comment, order_id) VALUES (True,'Harakefet 4','Thank You','');


-- @login_required
-- def add_dish_to_cart(request):
--   if request.method == 'POST':
--     cart = Cart.objects.get(user_id=request.user.id)
--     dish_id = request.POST.get('dish_id')
--     dish_item = Items(cart_id=cart.id, dish_id = dish_id, amount=request.POST.get('amount'))
--     dish_item.save()
--     return redirect('my-cart')
