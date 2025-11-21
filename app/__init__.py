from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate  # <-- importar

db = SQLAlchemy()
csrf = CSRFProtect()
migrate = Migrate()  # <-- criar objeto

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')

    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)  # <-- inicializar migração

    from .routes import main
    app.register_blueprint(main)

    return app
