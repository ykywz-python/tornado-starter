import os.path
from time import strftime

from src.config.const import APP_NAME
from src.utils.path import resource_path, exe_path
from src.utils.pyinstaller_ import is_frozen


EXE_PATH = exe_path()
EXE_SOURCE_PATH = os.path.join(EXE_PATH, 'src')
RESOURCE_PATH = resource_path('src' if not is_frozen() else '')
DATA_PATH = os.path.join(EXE_PATH, f'{APP_NAME}_Data')

LOG_PATH = os.path.join(DATA_PATH, 'logs')
LOG_FILE = os.path.join(LOG_PATH, f'{strftime("%d-%m-%Y")}.log')
LOG_ERROR_FILE = os.path.join(LOG_PATH, f'{strftime("%d-%m-%Y")}-error.log')


# when in frozen
if is_frozen():
    CORE_PATH = os.path.join(DATA_PATH, 'core/dist/')
else:
    CORE_PATH = os.path.join(EXE_SOURCE_PATH, 'core/')