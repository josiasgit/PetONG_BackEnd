from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Importe aqui os modelos para garantir que as tabelas sejam criadas corretamente
from .user import User
from .post import Post

# Adicione este bloco para criar as tabelas
def create_tables():
    Base.metadata.drop_all(bind=engine) # Remova esta linha para não apagar os dados
    Base.metadata.create_all(bind=engine) # Crie as tabelas

# Adicione este bloco com os seeds para popular o banco de dados
from models import session
from models.user import User
from models.post import Post

def create_seeds():
    # Adicionando um usuário de exemplo
    user = User(nome='Fernando',email='fernando@gmail.com',telefone='123456789',senha='123456',is_admin=1)
    
    session.add(user)
    session.commit()
    
    # Adicionando 2 post de exemplo para usuario 1
    post1 = Post(titulo='Primeira postagem',conteudo='Conteúdo da primeira postagem',imagem_url='https://via.placeholder.com/150',user_id=user.id)    
    session.add(post1)
    session.commit()
    
    post2 = Post(titulo='Segunda postagem',conteudo='Conteúdo da segunda postagem',imagem_url='https://via.placeholder.com/150',user_id=user.id)
    session.add(post2)
    session.commit()
    
   # Criando três usuários com is_admin=0
    user1 = User(nome='Maria', email='maria@gmail.com', telefone='987654321', senha='senha123', is_admin=0)
    user2 = User(nome='João', email='joao@gmail.com', telefone='555555555', senha='senha456', is_admin=0)
    user3 = User(nome='Ana', email='ana@gmail.com', telefone='111111111', senha='senha789', is_admin=0)

    session.add_all([user1, user2, user3])
    session.commit()
    
    # Adicionando postagens para os usuários
    post_maria = Post(titulo='Título do post da Maria', conteudo='Conteúdo do post da Maria', imagem_url='https://via.placeholder.com/150', user_id=user1.id)
    session.add(post_maria)
    session.commit()
    
    post_joao = Post(titulo='Título do post do João', conteudo='Conteúdo do post do João', imagem_url='https://via.placeholder.com/150', user_id=user2.id)
    session.add(post_joao)
    session.commit()
    
    post_ana = Post(titulo='Título do post da Ana', conteudo='Conteúdo do post da Ana', imagem_url='https://via.placeholder.com/150', user_id=user3.id)
    session.add(post_ana)
    session.commit()
    
    

# Base.metadata.create_all(engine)
