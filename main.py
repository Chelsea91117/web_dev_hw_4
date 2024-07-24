from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)
sync_session = Session()


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    title = Column(String(16))
    description = Column(String(250))
    products = relationship('Product', back_populates='category')


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    price = Column(Float(precision=2))
    is_available = Column(Boolean)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='products')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Задача 1: Наполнение данными
# Добавьте в базу данных следующие категории и продукты

category_1 = Category(title="Electronics", description="Gadgets and devices")
category_2 = Category(title="Books", description="Printed books and e-books")
category_3 = Category(title="Clothing", description="Men's and women's clothing")
sync_session.add_all([category_1, category_2, category_3])
sync_session.commit()

product_1 = Product(title='Smartphone', price=299.99, is_available=True, category_id=category_1.id)
product_2 = Product(title='Laptop', price=499.99, is_available=True, category_id=category_1.id)
product_3 = Product(title='Science Fiction Novel', price=15.99, is_available=True, category_id=category_2.id)
product_4 = Product(title='Jeans', price=40.50, is_available=True, category_id=category_3.id)
product_5 = Product(title='T-shirt', price=20.00, is_available=True, category_id=category_3.id)
sync_session.add_all([product_1, product_2, product_3, product_4, product_5])
sync_session.commit()

# Задача 2: Чтение данных
# Извлеките все записи из таблицы categories.
# Для каждой категории извлеките и выведите все связанные с ней продукты, включая их названия и цены.

# categories = sync_session.query(Category).all()
# for category in categories:
#     print(f"Category: {category.title} - {category.description}")
#     for product in category.products:
#         print(f"    Product: {product.title}, Price: {product.price}")

# Задача 3: Обновление данных
# Найдите в таблице products первый продукт с названием "Смартфон". Замените цену этого продукта на 349.99.

# product_s = sync_session.query(Product).filter_by(title="Smartphone").first()
# if product_s:
#     product_s.price = 349.99
#     sync_session.commit()
#     print(f'{product_s.title} has new price: {product_s.price}')
# else:
#     print('Was not found')

# Задача 4: Агрегация и группировка
# Используя агрегирующие функции и группировку, подсчитайте общее количество продуктов в каждой категории.

# total_products = sync_session.query(Product.category_id, func.count(Product.id).label('product_count')).group_by(Product.category_id).all()
# for category_id, product_count in total_products:
#     print(f"Category ID: {category_id}, Total Products: {product_count}")

