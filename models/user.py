from sqlalchemy import Column, Integer, String
from . import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100))
    email = Column(String(100), unique=True)
    telefone = Column(String(15))
    senha = Column(String(20))
    is_admin = Column(Integer, default=0) # 0 para usuário comum, 1 para administrador
    posts = [] # Lista de postagens associadas a este usuário

