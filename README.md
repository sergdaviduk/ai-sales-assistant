# AI Sales Assistant for amoCRM — prototype

Прототип AI-помощника менеджера: принимает обращение клиента, сверяется с небольшой базой знаний и возвращает два блока — готовый ответ клиенту и внутреннюю подсказку по допродаже.

## Возможности
- FastAPI + Pydantic
- локальная база знаний
- поиск релевантного контекста по ключевым словам
- demo-режим без API-ключа
- простой веб-интерфейс в стиле рабочего окна менеджера

## Запуск

### macOS / Linux
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Откройте `http://127.0.0.1:8000`.

## API
`POST /api/v1/assistant`

```json
{
  "message": "Здравствуйте! Хочу купить ноутбук. Сколько стоит доставка?"
}
```

Пример ответа:
```json
{
  "client_answer": "Здравствуйте! Обычная доставка стоит 500 ₽, а при заказе от 5000 ₽ она бесплатная. Срок доставки — 1–3 дня.",
  "manager_hint": "Предложите клиенту мышь, сумку для ноутбука или расширенную гарантию.",
  "source": "Ноутбуки, Доставка"
}
```

## Как развить дальше
Можно подключить реальную интеграцию с amoCRM через API/webhook, заменить локальную базу знаний на RAG/vector DB, добавить авторизацию, логирование, retry/rate limits и мониторинг.
