import os
import csv
import logging
from datetime import datetime, timedelta

import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DELAY = 2

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("email_generation.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

EMAIL_TEMPLATES = {
    "letter1": {
        "subject": "{personalization_short}",
        "body": (
            "Привет, {name}!\n\n"
            "{personalization} — это отличный ход. "
            "Кстати, мы в Polza Agency как раз помогаем B2B-компаниям "
            "привлекать клиентов через холодные рассылки.\n\n"
            "Бесплатно сделаем аудит вашей текущей стратегии и покажем, "
            "как можно увеличить поток лидов.\n\n"
            "Есть ли у вас время на короткий звонок в ближайшие дни?"
        )
    },
    "letter2": {
        "subject": "Идея для {industry} / Результат, который мы получили",
        "body": (
            "Привет, {name}!\n\n"
            "Я писал вам на днях насчет автоматизации аутрича. "
            "Возможно, сейчас не самое подходящее время, но хочу поделиться кейсом.\n\n"
            "Недавно мы запустили рассылку для компании из вашей отрасли. "
            "За 4 недели они получили 20+ квалифицированных лидов и 3 новых клиента.\n\n"
            "Сделали это без спама — только персонализированный подход "
            "и умные цепочки писем.\n\n"
            "Думаю, вашему бизнесу тоже может быть полезно. "
            "Давайте обсудим это на 15-минутном созвоне?"
        )
    },
    "letter3": {
        "subject": "Будем на связи / Полезный материал для вас",
        "body": (
            "Привет, {name}!\n\n"
            "Заметил, что вы не ответили на мои предыдущие письма. "
            "Возможно, сейчас вы заняты или не ищете подрядчиков для аутрича.\n\n"
            "На всякий случай отправляю наш гайд "
            "\"5 ошибок в холодных рассылках, которые убивают конверсию\". "
            "Думаю, вам будет полезно.\n\n"
            "Если когда-нибудь решите попробовать автоматизированный подход "
            "к лидогенерации — мы всегда открыты к диалогу.\n\n"
            "Желаю успехов в развитии бизнеса!\n\n"
            "P.S. Если не хотите получать больше писем, "
            "просто напишите \"стоп\" — и я вас сразу удалю из списка."
        )
    }
}

def get_contact_firstname(contact_str):
    if not contact_str or contact_str == "-":
        return "Коллега"
    parts = contact_str.replace("(", " ").replace(")", " ").split()
    for part in parts:
        if part.endswith("ва") or part.endswith("на") or part.endswith("ий") or part.endswith("ой") or part.endswith("ов") or part.endswith("ин"):
            continue
        if len(part) > 1 and part[0].isupper():
            return part
    return parts[0] if parts else "Коллега"

def generate_personalized_email(company, letter_key):
    template = EMAIL_TEMPLATES[letter_key]
    first_name = get_contact_firstname(company.get("Контактное лицо (должность)", ""))
    personalization = company.get("Персонализация", "")
    industry = company.get("Отрасль", "вашей отрасли")

    personalization_short = personalization[:45] if len(personalization) > 45 else personalization

    subject = template["subject"].format(
        name=first_name,
        personalization_short=personalization_short,
        industry=industry
    )

    body = template["body"].format(
        name=first_name,
        personalization=personalization,
        industry=industry
    )

    return subject, body

def generate_ai_personalized_email(company, letter_key):
    if not OPENAI_API_KEY:
        return generate_personalized_email(company, letter_key)

    name = company.get("Контактное лицо (должность)", "")
    first_name = get_contact_firstname(name)
    company_name = company.get("Название", "")
    personalization = company.get("Персонализация", "")
    industry = company.get("Отрасль", "")

    if letter_key == "letter1":
        prompt = (
            f"Напиши холодное письмо для B2B-аутрич агентства Polza Agency. "
            f"Компания: {company_name}. Контакт: {first_name}. "
            f"Персонализация: {personalization}. "
            f"Тема: макс 50 символов, интригующая. "
            f"Приветствие: Привет, {first_name}!. "
            f"Используй персонализацию как крючок. "
            f"Расскажи о Polza Agency (помогаем B2B-компаниям с лидогенерацией). "
            f"CTA: созвон на 15 минут. Тон: дружелюбный, экспертный. "
            f"Максимум 120 слов. Напиши только письмо, в формате:\n"
            f"Тема: ...\nТело:\n..."
        )
    elif letter_key == "letter2":
        prompt = (
            f"Напиши follow-up письмо (день +3) для B2B-компании {company_name} "
            f"от Polza Agency. Контакт: {first_name}. Отрасль: {industry}. "
            f"Тема: новый угол. Приветствие: Привет, {first_name}!. "
            f"Упомяни прошлое письмо, приведи кейс (как помогли похожей компании "
            f"получить 20+ лидов за 4 недели). CTA: обсудить на созвоне. "
            f"Максимум 120 слов. Формат:\nТема: ...\nТело:\n..."
        )
    else:
        prompt = (
            f"Напиши финальное follow-up письмо (день +8) для {company_name} "
            f"от Polza Agency. Контакт: {first_name}. "
            f"Тема: мягкий выход. Признай, что возможно сейчас не время. "
            f"Предложи гайд \"5 ошибок в холодных рассылках\". "
            f"Завершение дружелюбное, без давления. Максимум 120 слов. "
            f"Добавь P.S. с опцией отписки. Формат:\nТема: ...\nТело:\n..."
        )

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
            temperature=0.7
        )
        result = response.choices[0].message.content.strip()
        lines = result.split("\n", 2)
        subject = lines[0].replace("Тема:", "").strip() if "Тема:" in lines[0] else ""
        body = lines[2] if len(lines) > 2 else result
        return subject, body
    except Exception as e:
        logging.error(f"OpenAI error for {company_name}: {e}")
        return generate_personalized_email(company, letter_key)

def generate_email_sequence(input_csv, output_csv, use_ai=True):
    companies = []
    with open(input_csv, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            companies.append(row)

    fieldnames = [
        "Название компании", "Персонализация",
        "Письмо 1 - Тема", "Письмо 1 - Тело",
        "Письмо 2 - Тема", "Письмо 2 - Тело",
        "Письмо 3 - Тема", "Письмо 3 - Тело"
    ]

    results = []
    for i, company in enumerate(companies[:5]):
        name = company.get("Название", "")
        logging.info(f"[{i+1}/5] Генерация писем для: {name}")

        row = {
            "Название компании": name,
            "Персонализация": company.get("Персонализация", "")
        }

        for lk in ["letter1", "letter2", "letter3"]:
            if use_ai:
                subj, body = generate_ai_personalized_email(company, lk)
            else:
                subj, body = generate_personalized_email(company, lk)

            num = lk.replace("letter", "")
            row[f"Письмо {num} - Тема"] = subj
            row[f"Письмо {num} - Тело"] = body
            logging.info(f"  Письмо {num}: {subj}")
            time.sleep(DELAY)

        results.append(row)

    for company in companies[5:]:
        name = company.get("Название", "")
        personalization = company.get("Персонализация", "")
        first_name = get_contact_firstname(company.get("Контактное лицо (должность)", ""))
        industry = company.get("Отрасль", "")

        row = {
            "Название компании": name,
            "Персонализация": personalization,
            "Письмо 1 - Тема": "{personalization_short}",
            "Письмо 1 - Тело": EMAIL_TEMPLATES["letter1"]["body"].format(
                name=first_name, personalization=personalization, industry=industry
            ),
            "Письмо 2 - Тема": f"Идея для {industry} / Результат, который мы получили",
            "Письмо 2 - Тело": EMAIL_TEMPLATES["letter2"]["body"].format(
                name=first_name, personalization=personalization, industry=industry
            ),
            "Письмо 3 - Тема": "Будем на связи / Полезный материал для вас",
            "Письмо 3 - Тело": EMAIL_TEMPLATES["letter3"]["body"].format(
                name=first_name, personalization=personalization, industry=industry
            ),
        }
        results.append(row)

    with open(output_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    logging.info(f"Готово! Цепочки писем сохранены в {output_csv}")
    return results

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else "companies_with_personalization.csv"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "email_sequences.csv"
    use_ai = "--no-ai" not in sys.argv
    generate_email_sequence(input_file, output_file, use_ai=use_ai)
