from sqlalchemy.orm import sessionmaker
from settings import db_name, db_password, db_user
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine


db_string = "postgresql://"+db_user+":"+db_password+"@postgresdb:5432/"+db_name

db = create_engine(db_string)
base = declarative_base()

class Queen(base):  
    __tablename__ = 'queen'

    id = Column(Integer, primary_key=True)
    n = Column(Integer)
    number_of_solutions = Column(Integer)

class BoardSolution(base):  
    __tablename__ = 'board_solution'

    id = Column(Integer, primary_key=True)
    board = Column(String)
    queen_id = Column(Integer, ForeignKey('queen.id'))


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)