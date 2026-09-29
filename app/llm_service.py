import json
import os
from urllib import request


def _fallback(message: str, context: str) -> dict[str, str]:
    lower = message.lower()
    if "ноутбук" in lower:
        hint = "Предложите клиенту мышь, сумку для ноутбука или расширенную гарантию."
    elif "телефон" in lower or "смартфон" in lower or "iphone" in lower:
        hint = "Предложите чехол, защитное стекло или беспроводные наушники."
    else:
        hint = "Уточните потребность клиента и предложите релевантный сопутствующий товар из базы знаний."

    if "достав" in lower:
        answer = "Здравствуйте! Обычная доставка стоит 500 ₽, а при заказе от 5000 ₽ она бесплатная. Срок доставки — 1–3 дня."
    elif "гарант" in lower:
        answer = "Здравствуйте! Гарантия на ноутбуки и смартфоны составляет 12 месяцев. Буду рад помочь с выбором."
    elif "оплат" in lower:
        answer = "Здравствуйте! Заказ можно оплатить банковской картой онлайн или при получении. При курьерской доставке также доступна оплата наличными."
    else:
        answer = "Здравствуйте! Я сверился с нашей базой знаний. Подскажите, пожалуйста, какой товар вас интересует и что именно вы хотели бы уточнить?"
    return {"client_answer": answer, "manager_hint": hint}


def generate_answer(message: str, context: str) -> dict[str, str]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return _fallback(message, context)

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    prompt = f"""Ты AI-ассистент менеджера интернет-магазина.
Используй ТОЛЬКО факты из базы знаний. Не придумывай цены, сроки и условия.
Верни JSON с двумя строковыми полями: client_answer и manager_hint.
client_answer — короткий, вежливый и готовый к отправке ответ клиенту.
manager_hint — внутренняя подсказка менеджеру по уместной допродаже. Не показывай ее клиенту.
Если информации недостаточно, честно попроси уточнение.

База знаний:
{context}

Обращение клиента:
{message}
"""
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "Отвечай строго валидным JSON без markdown."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
    }).encode()
    req = request.Request(
        "https://api.openai.com/v1/chat/completions",
        data=payload,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=30) as response:
            body = json.loads(response.read().decode())
        return json.loads(body["choices"][0]["message"]["content"])
    except Exception:
        return _fallback(message, context)