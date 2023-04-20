-- INSERT INTO auth_user (username, password, first_name, last_name, is_staff, email, is_superuser, is_active, date_joined) VALUES ('yoni','pbkdf2_sha256$390000$dihFNmTJCPBMD9ykqUexgb$NIDkfRi5Sc9+waDfo1M3x5zwVVmCLPZDIPRCZJJnSUw=', 'yehonatan', 'amir', True, 'yoni@email.com', True, True, '2023-04-20 18:47:57.955801');

-- food_ordering_guest_category
INSERT INTO food_ordering_guest_category (name, image) VALUES ('starters', 'starters.jpeg');
INSERT INTO food_ordering_guest_category (name, image) VALUES ('mains', 'mains.jpeg');
INSERT INTO food_ordering_guest_category (name, image) VALUES ('drinks', 'desserts.jpeg');
INSERT INTO food_ordering_guest_category (name, image) VALUES ('desserts', 'drinks.jpeg');

-- food_ordering_guest_dish
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Avocado Salad', 35, 'Fresh avocado slices mixed with tomatoes, red onion, and cilantro, dressed in a tangy lime vinaigrette.', 'AvocadoSalad.jpeg', False, True, 1);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Anti Pasti', 29, 'A selection of marinated vegetables, cheeses, and olives.', 'AntiPasti.jpeg', True, True, 1);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Eggs Salad', 35, 'Boiled eggs mixed with mayonnaise, mustard, and seasonings, served on a bed of lettuce.', 'EggSalad.jpeg', False, True, 1);
INSERT INTO food_ordering_guest_dish (name, price, description, image, is_gluten_free, is_vageterian, category_id) VALUES ('Chicken Wings', 42, 'Crispy fried or baked chicken wings coated in a spicy or savory sauce. Served with celery sticks and blue cheese or ranch dressing.', 'Wings.jpeg', False, False, 1);

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
