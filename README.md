To set up the project:
1. Pull the project
2. Run command: "pip install -r requirements.txt"
3. Wait until packages are installed
4. Run command: "uvicorn main:app --reload"
5. Go to the path: "http://127.0.0.1:8000/docs#/" in a browser
6. Create a file to be tested with text "{"field1": "value1", "animal": "alien"}", for example
7. In Swagger, click on "Try it out" button on the "Sound By Animal" endpoint
8. Then click "Choose file" button
9. Choose test file created before in file system
10. Click "Execute" button

Коментар щодо імплеменатції:
Я обрав фреймворк FastApi тому, що:
* Багато працював з ним останнім часом
* FastAPI надає можливість переглянути Swagger одразу після створення ендпоінту, що дуже зручно і для тестування функціоналу, і для перегляду
* FastAPI надає можливість швидко налаштувати завантаження та обробку файлів через ендпоінт, що підходить для виконання поставленої задачі

Щодо структури проєкту:
* Під час практикування з FastApi, саме таку структуру вдалось виробити для зручного написання коду.
* В helpers.py знаходяться допоміжні функції, які викликаютсья функціями за файлу services.py
* В router.py налаштовані ендпоінти
* В services.py знаходятся функції, що викликаються при відправці запросу по ендпоінту

Щодо того, що можна було зробити по-іншому:
* Можна було створити клас з тваринами та звуками, що вони створюють, а методами класу вже виводити звуки по назві тварини
* Можна додати тести
* Можна додати кращу перевірку назви тварини (бо зараз, якщо написати вірне ім`я, але, наприклад, з великої літери, то буде помилка, що тварина невідома). Можно приводити всі імена до нижнього регістру, а далі перевіряти, наприклад
* Можна було створити невеличку БД з тваринами та звуками, що вони роблять, та використовувати БД як референс для валідації імен тварин та звуків
* Ще можна додати логіку зберігання назв тварин, які не входять до списку з задачі, коли викликається помилка "Unknown animal". Щоб розширити БД назв тварин
* Можна ще зробити валідацію поля "field1" та значення, що в нього записане (додав це)
* Можна ще зробити валідацію файлу на етапі завантаження (Чи валідний формат запису JSON файлу. Якщо так - працюємо з цим файлом, якщо ні - повернемо помилку) UPDЖ додав цю перевірку