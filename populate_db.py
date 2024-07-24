from LittleLemonDRF.models import Category, MenuItem

# Create categories
soups = Category.objects.create(title='Soups')
veg_appetizers = Category.objects.create(title='Veg Appetizers')
non_veg_appetizers = Category.objects.create(title='Non-Veg Appetizers')
bar_snacks = Category.objects.create(title='Bar Snacks')
veg_curries = Category.objects.create(title='Veg Curries')
chicken_curries = Category.objects.create(title='Chicken Curries')
goat_and_lamb_curries = Category.objects.create(title='Goat and Lamb Curries')
sea_food = Category.objects.create(title='Sea Food')
rice_and_noodles = Category.objects.create(title='Rice and Noodles')
biryani = Category.objects.create(title='Biryani')
tandoori_and_grill = Category.objects.create(title='Tandoori and Grill')
naan_and_roti = Category.objects.create(title='Naan and Roti')
desserts = Category.objects.create(title='Desserts')
beverages = Category.objects.create(title='Beverages')

# Create menu items for Soups
MenuItem.objects.create(title='Chicken Creamy Baby Corn Soup', price=6.99, description='Slow reduced Indian & Chinese style Chicken stock thickened by creamy baby corn puree, garnished with spring onion and cilantro', category=soups)
MenuItem.objects.create(title='Chicken Manchow Soup', price=6.99, description='Shredded chicken, vegetables, and noodles, simmered in a rich broth spiced with garlic, ginger, soy sauce, and chili sauce, garnished with fresh herbs.', category=soups)
MenuItem.objects.create(title='Hot And Sour Veg Soup', price=5.99, description='Hot and Sour Soup is the PERFECT combo of spicy and savory, made with tofu, and veggies in a savory seasoned broth with soy sauce and vinegar.', category=soups)

# Create menu items for Veg Appetizers
MenuItem.objects.create(title='Baby corn 65', price=11.99, description='Tender baby corn coated in a spicy and crispy batter, deep-fried to perfection, and served with a tangy and flavorful sauce, creating an irresistible appetizer with a delightful crunch.', category=veg_appetizers)
MenuItem.objects.create(title='Baby corn Manchuria', price=11.99, description='Crispy fried baby corn in a sweet and spicy thick sauce along with onions and bell pepper (capsicum).An extremely popular Asian.', category=veg_appetizers)
MenuItem.objects.create(title='Crispy Corn 65', price=10.99, description='Baby corns are coated in a spicy batter and deep-fried till crisp and this is one of the delicious starter.', category=veg_appetizers)

# Create menu items for Non-Veg Appetizers
MenuItem.objects.create(title='Chicken Lollipops', price=15.99, description='(Med to Extra spicy) Chicken wings marinated with chili lime and deep-fried.', category=non_veg_appetizers)
MenuItem.objects.create(title='Vanjaram Fish Fry', price=18.99, description='(Med to Extra spicy) King Fish fry with hand-blended homestyle spices.', category=non_veg_appetizers)
MenuItem.objects.create(title='Chili Chicken', price=14.99, description='(Med to Extra spicy) Cubes of chicken pieces tossed into spicy ginger garlic soya flavored.', category=non_veg_appetizers)

# Create menu items for Bar Snacks
MenuItem.objects.create(title='Home Style Samosa (3 pieces)', price=9.99, description='Boiled mashed potatoes and fresh mint, stuffed with a tortilla sheet.', category=bar_snacks)
MenuItem.objects.create(title='Mix Vegetable Pakora', price=11.99, description='', category=bar_snacks)

# Create menu items for Veg Curries
MenuItem.objects.create(title='Channa Korma', price=13.99, description='Channa boiled and cooked with garam masala thickened by coconut and poppy seed paste.', category=veg_curries)
MenuItem.objects.create(title='Channa Masala', price=13.99, description='Chickpeas cooked in a spicy and tangy tomato-based sauce and one of the most popular dish across India.', category=veg_curries)
MenuItem.objects.create(title='Daal Makhani', price=14.99, description='A luscious and creamy lentil curry prepared with slow-cooked black lentils, aromatic spices, and a rich tomato-based gravy.', category=veg_curries)

# Create menu items for Chicken Curries
MenuItem.objects.create(title='Achari Chicken Masala', price=15.99, description='Succulent chicken cooked in a tangy and flavorful Achari (pickle) masala, infused with aromatic spices and pickling agents.', category=chicken_curries)
MenuItem.objects.create(title='Butter Chicken', price=15.99, description='Freshly ripened tomatoes and whole spices boiled together and finish with butter and cream.', category=chicken_curries)
MenuItem.objects.create(title='Chicken Korma', price=15.99, description='Chicken boiled and cooked with garam masala thickened by coconut and poppy seed paste.', category=chicken_curries)

# Create menu items for Goat and Lamb Curries
MenuItem.objects.create(title='Andhra Style Goat Curry', price=17.99, description='Cubes of Goat cooked with fresh ripe tomato onion grains, fresh green chilies and cilantro.', category=goat_and_lamb_curries)
MenuItem.objects.create(title='Andhra Style Lamb Curry', price=18.99, description='Cubes of Lamb cooked with fresh ripe tomato onion grains, fresh green chilies and cilantro.', category=goat_and_lamb_curries)
MenuItem.objects.create(title='Daal Cha Goat Curry', price=17.99, description='Dalcha Goat Curry is a delightful fusion of two distinct but equally delicious dishes: "Dalcha" and "Goat Curry."', category=goat_and_lamb_curries)

# Create menu items for Sea Food
MenuItem.objects.create(title='Saag Shrimp', price=17.99, description='Saag Shrimp is a delectable South Indian dish that combines succulent shrimp with a creamy and flavorful spinach-based gravy.', category=sea_food)
MenuItem.objects.create(title='Shrimp Tikka Masala', price=17.99, description='Shrimp Tikka Masala is a delightful fusion dish that combines tender, succulent shrimp with a rich and creamy tomato-based gravy.', category=sea_food)

# Create menu items for Rice and Noodles
MenuItem.objects.create(title='Egg Fried Rice', price=15.99, description='A delectable combination of fluffy rice stir-fried with scrambled eggs, fresh vegetables, and a medley of savory sauces.', category=rice_and_noodles)
MenuItem.objects.create(title='Chicken Fried Rice', price=16.99, description='Fragrant stir-fried rice loaded with tender chicken pieces and mixed vegetables.', category=rice_and_noodles)
MenuItem.objects.create(title='Hakka Paneer Veg Noodles', price=16.99, description='A delightful medley of paneer (Indian cottage cheese), fresh vegetables, and Hakka noodles stir-fried to perfection.', category=rice_and_noodles)

# Create menu items for Biryani
MenuItem.objects.create(title='Fish Biryani', price=18.99, description='Fish Dum Biryani is goodness of rice and meat that comes in layers!', category=biryani)
MenuItem.objects.create(title='Lamb Boneless Biryani', price=19.99, description='Lamb Boneless Dum biryani is goodness of rice and meat that comes in layers!', category=biryani)
MenuItem.objects.create(title='Shrimp Biryani', price=18.99, description='Shrimp Dum biryani is goodness of rice and meat that comes in layers!', category=biryani)

# Create menu items for Tandoori and Grill
MenuItem.objects.create(title='Masala Papad (2 Pieces)', price=7.99, description='Crispy papad topped with spiced onion-tomato mixture.', category=tandoori_and_grill)
MenuItem.objects.create(title='Tandoori Chicken Wings (10 Pieces)', price=23.99, description='Meat marinated in home style roasted spices cooked into clay pot oven or grill.', category=tandoori_and_grill)
MenuItem.objects.create(title='Tandoori Goat Chops', price=23.99, description='Meat marinated in home style roasted spices cooked into clay pot oven or grill.', category=tandoori_and_grill)

# Create menu items for Naan and Roti
MenuItem.objects.create(title='Paneer Kulcha', price=5.99, description='', category=naan_and_roti)
MenuItem.objects.create(title='Cheese Kulcha', price=5.99, description='', category=naan_and_roti)
MenuItem.objects.create(title='Peshawari Naan', price=4.99, description='', category=naan_and_roti)

# Create menu items for Desserts
MenuItem.objects.create(title='Carrot Halwa', price=4.99, description='', category=desserts)
MenuItem.objects.create(title='Kulfi Mango', price=5.99, description='', category=desserts)
MenuItem.objects.create(title='Pineapple Souffle', price=6.99, description='', category=desserts)

# Create menu items for Beverages
MenuItem.objects.create(title='Coke', price=2.49, description='', category=beverages)
MenuItem.objects.create(title='Sprite', price=2.49, description='', category=beverages)
MenuItem.objects.create(title='Sweet Tea', price=4.99, description='', category=beverages)

print("Database populated successfully!")