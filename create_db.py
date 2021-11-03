from database import Base, engine
from models import Product

print("Creating database...")

Base.metadata.create_all(engine)