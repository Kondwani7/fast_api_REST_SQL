from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column,Text
#creating a table
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    price = Column(Integer, nullable=False)
    discount = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Proudct name={self.name} price={self.price}>"