from fastapi import HTTPException
from task.helpers import process_json_content, get_animal_sound


async def sound_by_animal_from_file(file):
    # Чтение содержимого загруженного файла
    content = await file.read()
    content_str = content.decode("utf-8")

    # Обробка вмісту JSON файлу
    data = await process_json_content(content_str)

    # Блок валідацій полів файлу
    if "field1" not in data:
        raise HTTPException(status_code=400, detail="Field 'field1' is missing")
    if data["field1"] != "value1":
        raise HTTPException(status_code=400, detail="Field 'field1' is strange (!= value1)")

    if "animal" not in data:
        raise HTTPException(status_code=400, detail="Field 'animal' is missing")

    # Отримуємо значення поля "animal" та повертаємо потрібний звук за допомогою функції get_animal_sound
    animal = data["animal"]
    sound = await get_animal_sound(animal)
    # Формуємо респонс з тварини та відповідного звуку
    return {"animal": animal, "sound": sound}