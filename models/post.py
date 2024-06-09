from sqlalchemy import Column, Integer, String
from . import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100))
    conteudo = Column(String(500))
    imagem_url = Column(String(100))
    user_id = Column(Integer) # Usuário que escreveu a postagem