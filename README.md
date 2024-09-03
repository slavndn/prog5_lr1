# Лабораторная работа 1 - Славный Даниил Михайлович 
1. Создал папку **rootserver** 
2. Создал файл **myremotemodule.py** внутри **rootserver**
3. Добавил в файл следующий код:
```
def myfoo():
    author = "" # Здесь обознаться своё имя (авторство модуля)
    print(f"{author}'s module is imported")
```
4. В папке **rootserver** создал файл **activation_script.py**
5. Вставил в него следующий код, который включает функции *url_hook* и классы *URLLoader*, *URLFinder*. Также я использовал библиотеку **requests**
```
import sys
import requests
import importlib.util

class URLLoader:
    def __init__(self, url):
        self.url = url

    def get_code(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Проверка на ошибки
        return response.text

def url_hook(path):
    if path.startswith("http://"):
        return URLLoader(path)
    return None

# url_hook в sys.path_hooks
sys.path_hooks.append(url_hook)
sys.path.append("http://localhost:8000")  
```
6. Перешел в директорию **rootserver**
```
cd C:\home\study\prog5\lr1\rootserver
```
7. Запускаю HTTP сервер:
```
python -m http.server
```
8. На втором терминале перехожу в папку **rootserver** и запускаю **activation_script.py**
```
python -i activation_script.py
```
9. Пробую импортировать свой модуль
```
import myremotemodule
myremotemodule.myfoo()
```
10. Вывод
```
PS C:\home\study\prog5\lr1\rootserver> python -i activation_script.py 
Failed calling sys.__interactivehook__
Traceback (most recent call last):
  File "<frozen site>", line 461, in register_readline
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1322, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 1262, in _find_spec
  File "<frozen importlib._bootstrap_external>", line 1528, in find_spec
  File "<frozen importlib._bootstrap_external>", line 1502, in _get_spec
AttributeError: 'URLLoader' object has no attribute 'find_spec'
>>> import myremotemodule
>>> myremotemodule.myfoo()
slavniyivt's module is imported
>>>
```
! Скриншоты ! 
![image](https://github.com/user-attachments/assets/73a095e8-dca7-4414-8813-55c1a1938768)
![image](https://github.com/user-attachments/assets/17246c08-44b6-4dfb-90d5-8017c385e497)
![image](https://github.com/user-attachments/assets/507f3c9d-379d-43a2-af41-60f99649d5ca)
![image](https://github.com/user-attachments/assets/322ea459-d4cd-443a-9536-58e9def9e2ef)
![image](https://github.com/user-attachments/assets/9a0dce69-3340-459a-b33e-f5767f6910fd)





