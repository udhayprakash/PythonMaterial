from sqlalchemy import create_engine, engine

engine = create_engine("sqlite:///:memory:", echo=True)
# echo=True will make SQLAlchemy to log all SQL commands it is doing while you apply commands.
# NOT recommended in production

# conn = engine.connect()

# trans = conn.begin()
# conn.execute('INSERT INTO "EX1" (name) '
#              'VALUES ("Hello")')
# trans.commit()

# Creating and Managing Session
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


# Creating Tables
from sqlalchemy.ext.declarative import declarative_base

# To map which table in the db will be related to each class in our files, we will use a SQLAlchemy system called Declarative.
Base = declarative_base()

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"User {self.name}"


# Finally, to create all tables
Base.metadata.create_all(engine)


# Adding new records, to table
user = User(name="John Snow", password="johnspassword")

# tO register the transaction
session.add(user)

print(user.id)  # None

# to commits (persists) those changes to the database.
session.commit()


# Making queries
query = session.query(User).filter_by(name="John")
print(f"{query.count() = }")
print(f"{query.first() = }")
print(f"{query.all()   = }")

session.query(User).filter(User.name == "John").first()

session.query(User).filter(User.name.like("%John%")).first()
