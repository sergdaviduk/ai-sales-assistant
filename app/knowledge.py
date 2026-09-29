KNOWLEDGE_BASE = [
    {
        "topic": "Ноутбуки",
        "keywords": ["ноутбук", "ноутбуки", "laptop"],
        "facts": "Гарантия на ноутбуки — 12 месяцев. К ноутбуку можно предложить мышь, сумку и расширенную гарантию.",
    },
    {
        "topic": "Смартфоны",
        "keywords": ["смартфон", "телефон", "iphone", "android"],
        "facts": "Гарантия на смартфоны — 12 месяцев. Дополнительно можно предложить чехол, защитное стекло и беспроводные наушники.",
    },
    {
        "topic": "Доставка",
        "keywords": ["доставка", "доставить", "привезти", "курьер"],
        "facts": "Обычная доставка стоит 500 ₽. При заказе от 5000 ₽ доставка бесплатная. Срок доставки — 1–3 дня.",
    },
    {
        "topic": "Оплата",
        "keywords": ["оплата", "оплатить", "карта", "наличные"],
        "facts": "Оплатить заказ можно банковской картой онлайн или при получении. Наличная оплата доступна при курьерской доставке.",
    },
]


def find_context(message: str) -> tuple[str, str]:
    text = message.lower()
    matched = [item for item in KNOWLEDGE_BASE if any(k in text for k in item["keywords"])]
    if not matched:
        matched = KNOWLEDGE_BASE
    context = "\n".join(f'{item["topic"]}: {item["facts"]}' for item in matched)
    source = ", ".join(item["topic"] for item in matched)
    return context, source