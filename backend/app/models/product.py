from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.database import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primery_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    image_url = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    products = relationship('Product', back_populates='category')

    category = relationship('Category', back_populates='products')

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price='{self.price})>"