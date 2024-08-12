
from config import config
from src import init_app

# Obtener la configuración adecuada
configuration = config['development']

# Inicializar la aplicación Flask
app = init_app(configuration)


if __name__ == '__main__':
    app.run()
