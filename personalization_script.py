import os
import time
import csv
import logging
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DELAY = 2
MAX_RETRIES = 3

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("personalization.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def fetch_page(url):
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(url, timeout=10, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            })
            if resp.status_code == 200:
                return resp.text
        except requests.RequestException as e:
            logging.warning(f"Попытка {attempt+1}/{MAX_RETRIES}: {url} - {e}")
            time.sleep(DELAY)
    return None

def parse_page_for_facts(html):
    soup = BeautifulSoup(html, "html.parser")
    texts = []
    for tag in soup.find_all(["h1", "h2", "h3", "p", "a"]):
        txt = tag.get_text(strip=True)
        if len(txt) > 20:
            texts.append(txt)
    return " ".join(texts[:50])

def get_personalization_from_openai(company_name, url, industry):
    if not OPENAI_API_KEY:
        return "OPENAI_API_KEY не установлен"
    prompt = (
        f"Компания: {company_name}\n"
        f"Сайт: {url}\n"
        f"Отрасль: {industry}\n\n"
        "Найди один конкретный, реальный факт об этой компании для персонализации "
        "холодного письма. Факт должен быть уникальным (не шаблонным). "
        "Ответь одним предложением (до 20 слов). Без кавычек."
    )
    try:
        import openai
        openai.api_key = OPENAI_API_KEY
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"OpenAI API error for {company_name}: {e}")
        return f"Ошибка API: {e}"

def process_companies(input_csv, output_csv):
    companies = []
    with open(input_csv, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            companies.append(row)

    fieldnames = list(companies[0].keys()) if companies else []
    if "Персонализация" not in fieldnames:
        fieldnames.append("Персонализация")
    if "Источник" not in fieldnames:
        fieldnames.append("Источник")

    for i, company in enumerate(companies):
        name = company.get("Название", "Unknown")
        url = company.get("Сайт", "")
        industry = company.get("Отрасль", "")
        logging.info(f"[{i+1}/{len(companies)}] Обработка: {name}")

        if not url:
            company["Персонализация"] = "Сайт не указан"
            company["Источник"] = "-"
            continue

        html = fetch_page(url)
        if not html:
            company["Персонализация"] = "Сайт недоступен"
            company["Источник"] = url
            logging.warning(f"Сайт недоступен: {url}")
            continue

        fact = get_personalization_from_openai(name, url, industry)
        company["Персонализация"] = fact
        company["Источник"] = url

        logging.info(f"Факт: {fact}")
        time.sleep(DELAY)

    with open(output_csv, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(companies)

    logging.info(f"Готово! Результат сохранён в {output_csv}")
    return companies

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else "base_companies.csv"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "companies_with_personalization.csv"
    process_companies(input_file, output_file)
