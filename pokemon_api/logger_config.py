import logging
from logging.handlers import RotatingFileHandler

# Configurar el sistema de logs
log_file = "app.log"

# Crear un manejador de logs con rotación (máx. 1MB por archivo, 3 copias de respaldo)
log_handler = RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=1)
log_handler.setLevel(logging.INFO)

# Formato del log
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)

# Configurar el logger principal
logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)
