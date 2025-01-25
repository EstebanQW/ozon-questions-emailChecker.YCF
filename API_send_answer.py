import requests
import json
import time
from login import *


# Вызывает функцию отправки ответа на вопрос по API, если есть текст ответа
def send_answer(
    from_mail: str, subject_tema: str, content_telo: str, cookie: str
) -> None:
    if content_telo:
        print(f"По API ОТВЕТ id: {subject_tema} текст: '{content_telo}'")
        return answer_question(subject_tema, content_telo, cookie)
    else:
        print(f"По API НЕ отправляю.")


url = "https://seller.ozon.ru/api/v1/create-answer"


# Отправляет ответ на вопрос по API и возвращает результат отправки
def answer_question(id: str, text: str, cookie: str) -> str:
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "ru",
        "content-type": "application/json",
        "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "x-o3-app-name": "seller-ui",
        "x-o3-company-id": company_id,
        "x-o3-language": "ru",
        "x-o3-page-type": "questions",
        "Referer": "https://seller.ozon.ru/app/reviews/questions",
        "Referrer-Policy": "strict-origin-when-cross-origin",
        "cookie": cookie,
    }
    body = {
        "text": text,
        "question_id": id,
        "sc_company_id": company_id,
        "company_type": "seller",
    }
    for attempt in range(3):
        try:
            response = requests.post(url, headers=headers, data=json.dumps(body))
            print(
                f"Запрос отправлен статус-код: {response.status_code}. Ответ json: {response.json()}"
            )
            break
        except requests.exceptions.RequestException as e:
            if attempt < 2:
                print(
                    f"Ошибка при отправке запроса: {e}. Повторная попытка через 10 секунд..."
                )
                time.sleep(10)
            else:
                print(f"Все попытки завершились неудачно. ID вопроса = {id}")
                return "ERROR"
    return "OK"
