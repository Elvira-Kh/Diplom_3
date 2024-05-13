import os

class Token:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')  # Исправлено на правильное имя переменной

    def export_token(self):
        if self.github_token:
            os.environ['GITHUB_TOKEN'] = self.github_token  # Исправлено на правильное имя переменной
            os.environ['WDM_PROVIDERS'] = 'github'
        else:
            raise ValueError('GitHub токен не установлен в переменных окружения.')
