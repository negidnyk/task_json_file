from fastapi import HTTPException
import json


# Функція для обробки вмісту JSON файлу
async def process_json_content(content):
    try:
        data = json.loads(content)
        print(data)
        return data
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Error decoding JSON")


# Визначення звуків тварин
async def get_animal_sound(animal):
    sounds = {
        "dog": "bark",
        "cat": "meow",
        "cow": "moo",
        "rat": "pipi",
        "alien": "KILL"
    }
    if animal in sounds:
        return sounds[animal]
    else:
        raise HTTPException(status_code=400, detail="Unknown animal")