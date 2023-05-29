from flask import Flask

from config import Config
from app.extensions import db,bcrypt,login_manager


#Flask application factoy function
def create_app(config_class=Config):
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Initialize flask extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    
    ##Register blueprints here
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    from app.posts import posts as posts_bp
    app.register_blueprint(posts_bp)


    from app.auth import auth as auth_pb
    app.register_blueprint(auth_pb)

    from app.questions import query as query_pb
    app.register_blueprint(query_pb)
    

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the flaskApplication</h1>'
    
    return app

