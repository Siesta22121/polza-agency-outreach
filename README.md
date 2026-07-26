# Polza Agency — B2B Outreach Preparation

## Состав проекта

| Файл | Описание |
|------|----------|
| `base_companies.csv` | База 55+ российских B2B-компаний с контактами |
| `personalization_script.py` | Скрипт для автоматической персонализации через OpenAI API |
| `email_generator.py` | Генератор цепочки из 3 писем для каждой компании |
| `requirements.txt` | Зависимости Python |
| `LLM_stack_answers.txt` | Ответы на вопросы по LLM-стеку (Задача 5) |
| `task4_verification.md` | Инструкция для проверки тестовой базы (Задача 4) |
| `prompts/` | Папка с промптами для каждой задачи |

## Установка

```bash
pip install -r requirements.txt
```

## Настройка

Создайте файл `.env` в корне проекта:

```
OPENAI_API_KEY=sk-your-key-here
```

## Использование

### 1. Персонализация базы

```bash
python personalization_script.py base_companies.csv companies_with_personalization.csv
```

### 2. Генерация цепочек писем

```bash
python email_generator.py companies_with_personalization.csv email_sequences.csv
```

Без AI (только шаблоны):
```bash
python email_generator.py companies_with_personalization.csv email_sequences.csv --no-ai
```

## Структура базы (base_companies.csv)

- Название компании
- Сайт (URL)
- Отрасль (IT/Софт, Логистика, Производство, Консалтинг, Маркетинг, Финансы, Строительство, Медицина, Образование, Ритейл)
- Регион
- Контактное лицо (должность)
- Email
- Телефон
- Размер компании (кол-во сотрудников)
- Персонализация (факт + источник)

## Принципы работы

1. **Реальность данных**: Все компании реальны, контакты взяты из открытых источников
2. **Валидность email**: Формат имя@домен.ru, совпадает с доменом компании
3. **Персонализация**: Только конкретные факты (не шаблоны)
4. **Ошибки**: Обработка таймаутов, недоступных сайтов, ошибок API
5. **Задержки**: 2 секунды между запросами к API
6. **Логирование**: Подробный лог в консоль и файл personalization.log
