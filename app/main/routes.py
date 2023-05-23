from app.main import main


@main.route('/')
def index():
    return 'This is the main blueprint'

