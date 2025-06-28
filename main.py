import os
import sys
from flask import Flask
from src.app_info.extensions import mail, bcrypt, jwt_manager
from src.config.app_config import configure_current_application

sys.path.insert(0, 'src/')

app = Flask(__name__)
# Set debug mode explicitly
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

with app.app_context():
    configure_current_application()
    mail.init_app(app)
    bcrypt.init_app(app)
    jwt_manager.init_app(app)


@app.route('/')
def hello():
    return '<h1>Hello World!</h1><br><i>Server is running</i>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
