from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
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