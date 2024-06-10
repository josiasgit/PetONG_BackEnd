from flask import Flask
from controllers.user_controller import user_bp
from controllers.post_controller import post_bp
from models import create_tables,create_seeds  # Importe a função create_tables
from flask_cors import CORS

app = Flask(__name__)
# Adicione o CORS ao app
CORS(app)

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)

if __name__ == "__main__":
    create_tables()  # Chame a função para criar as tabelas
    create_seeds()  # Chame a função para criar os seeds
    app.run(host="0.0.0.0", port=5000, debug=True)