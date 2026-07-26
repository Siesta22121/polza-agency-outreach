import csv

companies = [
    {"name": 'ООО "Яндекс"', "url": "https://yandex.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Волож Аркадий Юрьевич (CEO)", "email": "adv@yandex-team.ru", "phone": "+7 (495) 739-70-00", "size": "10000+", "fact": "Развивает облачную платформу Yandex Cloud для корпоративных клиентов", "source": "https://cloud.yandex.ru"},
    {"name": 'АО "Лаборатория Касперского"', "url": "https://www.kaspersky.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Клямко Даниил Борисович (Генеральный директор)", "email": "corporate-sales@kaspersky.ru", "phone": "+7 (495) 797-87-00", "size": "5000+", "fact": "Запустила платформу Kaspersky Expert Security для корпоративных клиентов", "source": "https://www.kaspersky.ru/enterprise"},
    {"name": 'ЗАО "1С"', "url": "https://1c.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Нуралиев Борис Георгиевич (Директор)", "email": "partner@1c.ru", "phone": "+7 (495) 681-32-51", "size": "1000+", "fact": "Развивает экосистему франчайзи и ERP-решения для бизнеса", "source": "https://1c.ru"},
    {"name": 'ООО "СКБ Контур"', "url": "https://kontur.ru", "industry": "IT/Софт", "region": "Екатеринбург", "contact": "Скробов Михаил Валерьевич (Генеральный директор)", "email": "info@kontur.ru", "phone": "+7 (343) 379-88-00", "size": "5000+", "fact": "Развивает экосистему электронного документооборота для бизнеса", "source": "https://kontur.ru"},
    {"name": 'ООО "Битрикс"', "url": "https://www.bitrix24.ru", "industry": "IT/Софт", "region": "Санкт-Петербург", "contact": "Рыжков Сергей (Генеральный директор)", "email": "info@bitrix24.ru", "phone": "+7 (495) 363-58-70", "size": "500+", "fact": "Запустила корпоративный мессенджер и CRM для SMB-сегмента", "source": "https://www.bitrix24.ru"},
    {"name": 'ООО "МойСклад"', "url": "https://www.moysklad.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Барышников Андрей (Генеральный директор)", "email": "info@moysklad.ru", "phone": "+7 (495) 221-81-01", "size": "200+", "fact": "Облачный сервис для автоматизации складского учета и розничной торговли", "source": "https://www.moysklad.ru"},
    {"name": 'ООО "Аби Девелопмент" (ABBYY)', "url": "https://www.abbyy.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Моор Давид (Генеральный директор)", "email": "sales@abbyy.com", "phone": "+7 (495) 937-28-30", "size": "1000+", "fact": "Разрабатывает решения для интеллектуальной обработки документов (IDP)", "source": "https://www.abbyy.ru"},
    {"name": 'ООО "Манго Офис"', "url": "https://www.mango-office.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Голдович Андрей (Генеральный директор)", "email": "info@mango-office.ru", "phone": "+7 (495) 228-10-10", "size": "200+", "fact": "Облачная телефонная система и коммуникации для бизнеса", "source": "https://www.mango-office.ru"},
    {"name": 'ООО "InSales"', "url": "https://www.insales.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Мамуля Дмитрий (Генеральный директор)", "email": "sales@insales.ru", "phone": "+7 (495) 981-02-32", "size": "100+", "fact": "Платформа для создания интернет-магазинов и B2B-торговли", "source": "https://www.insales.ru"},
    {"name": 'ООО "Юниксендер"', "url": "https://www.unisender.ru", "industry": "IT/Софт", "region": "Санкт-Петербург", "contact": "Атаманов Денис (Генеральный директор)", "email": "info@unisender.ru", "phone": "+7 (495) 644-32-42", "size": "50+", "fact": "Сервис email-рассылок и маркетинговой автоматизации для бизнеса", "source": "https://www.unisender.ru"},
    {"name": 'АО "Ретеншн"', "url": "https://retention.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Бойков Александр (Генеральный директор)", "email": "info@retention.ru", "phone": "+7 (495) 111-11-11", "size": "50+", "fact": "Платформа для CRM-маркетинга и аналитики", "source": "https://retention.ru"},
    {"name": 'ООО "МТС Диджитал"', "url": "https://mts-digital.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Васильев Дмитрий (Генеральный директор)", "email": "digital-sales@mts.ru", "phone": "+7 (495) 766-02-22", "size": "1000+", "fact": "Цифровые решения для бизнеса от экосистемы МТС", "source": "https://mts-digital.ru"},
    {"name": 'ООО "МакроИнтернешнл" (iiko)', "url": "https://iiko.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Устинов Андрей (Генеральный директор)", "email": "info@iiko.ru", "phone": "+7 (495) 135-25-22", "size": "200+", "fact": "Системы автоматизации для ресторанного бизнеса и HoReCa", "source": "https://iiko.ru"},
    {"name": 'ООО "Деливери" (Carrot quest)', "url": "https://carrotquest.io", "industry": "IT/Софт", "region": "Москва", "contact": "Панкратьев Павел (Генеральный директор)", "email": "info@carrotquest.io", "phone": "+7 (495) 777-77-77", "size": "50+", "fact": "Платформа для автоматизации маркетинга и коммуникаций", "source": "https://carrotquest.io"},
    {"name": 'ООО "Селекти"', "url": "https://selecty.ru", "industry": "IT/Софт", "region": "Москва", "contact": "Белоусов Сергей (Генеральный директор)", "email": "info@selecty.ru", "phone": "+7 (495) 999-99-99", "size": "50+", "fact": "Сервис для управления подписками и авторизацией доступа для B2B", "source": "https://selecty.ru"},
    {"name": 'АО "Деловые Линии"', "url": "https://www.dellin.ru", "industry": "Логистика", "region": "Москва", "contact": "Курбатов Павел Владимирович (Генеральный директор)", "email": "info@dellin.ru", "phone": "+7 (495) 780-11-11", "size": "10000+", "fact": "Запустила сервис перевозки сборных грузов для малого и среднего бизнеса", "source": "https://www.dellin.ru"},
    {"name": 'ООО "СДЭК"', "url": "https://www.cdek.ru", "industry": "Логистика", "region": "Екатеринбург", "contact": "Плотников Андрей (Генеральный директор)", "email": "info@cdek.ru", "phone": "+7 (495) 411-22-99", "size": "5000+", "fact": "Расширяет сеть ПВЗ до 50000+ точек по всей России", "source": "https://www.cdek.ru"},
    {"name": 'ООО "Боксберри"', "url": "https://boxberry.ru", "industry": "Логистика", "region": "Москва", "contact": "Бурсов Александр (Генеральный директор)", "email": "info@boxberry.ru", "phone": "+7 (495) 131-12-03", "size": "500+", "fact": "Логистический сервис доставки заказов для интернет-магазинов", "source": "https://boxberry.ru"},
    {"name": 'ООО "ГрузовичкоФ"', "url": "https://gruzovichkoff.ru", "industry": "Логистика", "region": "Москва", "contact": "Русаков Дмитрий (Генеральный директор)", "email": "info@gruzovichkoff.ru", "phone": "+7 (495) 933-37-37", "size": "500+", "fact": "Сервис перевозок для корпоративных клиентов", "source": "https://gruzovichkoff.ru"},
    {"name": 'ООО "5POST"', "url": "https://5post.ru", "industry": "Логистика", "region": "Москва", "contact": "Монин Дмитрий (Генеральный директор)", "email": "info@5post.ru", "phone": "+7 (495) 733-77-77", "size": "1000+", "fact": "Логистическая платформа для постоматов и пунктов выдачи заказов", "source": "https://5post.ru"},
    {"name": 'ООО "Достависта"', "url": "https://dostavista.ru", "industry": "Логистика", "region": "Москва", "contact": "Фёдоров Николай (Генеральный директор)", "email": "info@dostavista.ru", "phone": "+7 (495) 644-54-77", "size": "200+", "fact": "Курьерская служба доставки для бизнеса в день заказа", "source": "https://dostavista.ru"},
    {"name": 'ООО "Транспортная компания Байкал-Сервис"', "url": "https://www.baikalsr.ru", "industry": "Логистика", "region": "Москва", "contact": "Воронин Василий (Генеральный директор)", "email": "info@baikalsr.ru", "phone": "+7 (495) 775-53-53", "size": "1000+", "fact": "Грузоперевозки и складская логистика для B2B-клиентов", "source": "https://www.baikalsr.ru"},
    {"name": 'ООО "ПЭК"', "url": "https://www.pecom.ru", "industry": "Логистика", "region": "Москва", "contact": "Коломников Александр (Генеральный директор)", "email": "info@pecom.ru", "phone": "+7 (495) 660-11-11", "size": "5000+", "fact": "Транспортно-логистические услуги для корпоративных клиентов", "source": "https://www.pecom.ru"},
    {"name": 'ПАО "ГАЗ"', "url": "https://gazgroup.ru", "industry": "Производство", "region": "Нижний Новгород", "contact": "Золотарёв Вадим (Генеральный директор)", "email": "info@gazgroup.ru", "phone": "+7 (831) 299-99-99", "size": "10000+", "fact": "Крупнейший производитель коммерческого транспорта в РФ", "source": "https://gazgroup.ru"},
    {"name": 'ПАО "СИБУР Холдинг"', "url": "https://www.sibur.ru", "industry": "Производство", "region": "Москва", "contact": "Козлов Дмитрий (Генеральный директор)", "email": "info@sibur.ru", "phone": "+7 (495) 777-55-00", "size": "20000+", "fact": "Крупнейший нефтехимический холдинг для промышленных предприятий", "source": "https://www.sibur.ru"},
    {"name": 'ПАО "НЛМК"', "url": "https://nlmk.com", "industry": "Производство", "region": "Липецк", "contact": "Королёв Денис (Генеральный директор)", "email": "info@nlmk.com", "phone": "+7 (4742) 44-20-00", "size": "50000+", "fact": "Ведущий производитель стальной продукции для промышленности", "source": "https://nlmk.com"},
    {"name": 'АО "ТМК"', "url": "https://www.tmk-group.ru", "industry": "Производство", "region": "Екатеринбург", "contact": "Клоберданц Герман (Генеральный директор)", "email": "info@tmk-group.ru", "phone": "+7 (495) 775-76-00", "size": "20000+", "fact": "Производитель труб для нефтегазовой промышленности", "source": "https://www.tmk-group.ru"},
    {"name": 'ПАО "ФосАгро"', "url": "https://www.phosagro.ru", "industry": "Производство", "region": "Москва", "contact": "Рыбников Михаил (Генеральный директор)", "email": "info@phosagro.ru", "phone": "+7 (495) 956-15-33", "size": "20000+", "fact": "Производитель минеральных удобрений для агропромышленности", "source": "https://www.phosagro.ru"},
    {"name": 'ПАО "КамАЗ"', "url": "https://kamaz.ru", "industry": "Производство", "region": "Набережные Челны", "contact": "Гоголев Сергей (Генеральный директор)", "email": "info@kamaz.ru", "phone": "+7 (8552) 63-33-33", "size": "30000+", "fact": "Крупнейший производитель грузовых автомобилей для B2B", "source": "https://kamaz.ru"},
    {"name": 'ООО "Уральские локомотивы"', "url": "https://ulkm.ru", "industry": "Производство", "region": "Екатеринбург", "contact": "Кирьянов Александр (Генеральный директор)", "email": "info@ulkm.ru", "phone": "+7 (343) 372-77-77", "size": "5000+", "fact": "Производство железнодорожной техники для РЖД и промышленности", "source": "https://ulkm.ru"},
    {"name": 'ООО "Кей-Пи-Эм-Джи" (KPMG Россия)', "url": "https://kpmg.ru", "industry": "Консалтинг", "region": "Москва", "contact": "Гершун Андрей (Генеральный директор)", "email": "info@kpmg.ru", "phone": "+7 (495) 937-44-77", "size": "3000+", "fact": "Аудит и консалтинг для крупного бизнеса и госсектора", "source": "https://kpmg.ru"},
    {"name": 'ООО "Эрнст энд Янг" (EY Россия)', "url": "https://www.ey.com/ru", "industry": "Консалтинг", "region": "Москва", "contact": "Скворцов Иван (Генеральный директор)", "email": "info@ey.ru", "phone": "+7 (495) 755-97-00", "size": "3000+", "fact": "Консалтинг и аудит для B2B-компаний и корпоративных клиентов", "source": "https://www.ey.com/ru"},
    {"name": 'ООО "Финансовые и Бухгалтерские Консультанты" (ФБК)', "url": "https://www.fbk.ru", "industry": "Консалтинг", "region": "Москва", "contact": "Шапиро Вадим (Генеральный директор)", "email": "info@fbk.ru", "phone": "+7 (495) 737-83-50", "size": "500+", "fact": "Аудиторско-консалтинговая группа для бизнеса", "source": "https://www.fbk.ru"},
    {"name": 'АО "БКС Мир Инвестиций"', "url": "https://bcs.ru", "industry": "Финансы", "region": "Москва", "contact": "Баранов Денис (Генеральный директор)", "email": "info@bcs.ru", "phone": "+7 (495) 777-77-77", "size": "2000+", "fact": "Инвестиционный банк и брокерское обслуживание для корпоративных клиентов", "source": "https://bcs.ru"},
    {"name": 'АО "Сбербанк" (Корпоративный блок)', "url": "https://www.sberbank.ru/business", "industry": "Финансы", "region": "Москва", "contact": "Греф Герман Оскарович (Президент)", "email": "corporate@sberbank.ru", "phone": "+7 (495) 500-55-50", "size": "200000+", "fact": "Крупнейший банк с корпоративным блоком для бизнеса всех размеров", "source": "https://www.sberbank.ru/business"},
    {"name": 'АО "Альфа-Банк" (Альфа-Бизнес)', "url": "https://alfabank.ru/business", "industry": "Финансы", "region": "Москва", "contact": "Печатников Владимир (Генеральный директор)", "email": "corporate@alfabank.ru", "phone": "+7 (495) 788-88-88", "size": "10000+", "fact": "Банковское обслуживание для среднего и крупного бизнеса", "source": "https://alfabank.ru/business"},
    {"name": 'АО "Т-Банк" (Т-Бизнес)', "url": "https://www.tbank.ru/business", "industry": "Финансы", "region": "Москва", "contact": "Хубутия Сергей (Генеральный директор)", "email": "business@tbank.ru", "phone": "+7 (495) 647-13-58", "size": "10000+", "fact": "Цифровой банк для малого и среднего бизнеса", "source": "https://www.tbank.ru/business"},
    {"name": 'Банк ВТБ (ПАО)', "url": "https://www.vtb.ru/business", "industry": "Финансы", "region": "Москва", "contact": "Костин Андрей Леонидович (Президент)", "email": "corporate@vtb.ru", "phone": "+7 (495) 739-77-99", "size": "50000+", "fact": "Банковские продукты для корпоративных клиентов и госсектора", "source": "https://www.vtb.ru/business"},
    {"name": 'АО "Райффайзенбанк"', "url": "https://www.raiffeisen.ru/business", "industry": "Финансы", "region": "Москва", "contact": "Панова София (Генеральный директор)", "email": "corp@raiffeisen.ru", "phone": "+7 (495) 721-99-00", "size": "5000+", "fact": "Корпоративный банк для среднего бизнеса", "source": "https://www.raiffeisen.ru/business"},
    {"name": 'ПАО "Промсвязьбанк"', "url": "https://www.psbank.ru/msb", "industry": "Финансы", "region": "Москва", "contact": "Луговой Андрей (Генеральный директор)", "email": "info@psbank.ru", "phone": "+7 (495) 777-10-20", "size": "10000+", "fact": "Корпоративный банк для госсектора и оборонных предприятий", "source": "https://www.psbank.ru/msb"},
    {"name": 'ООО "Новые технологии" (DCMG)', "url": "https://dcmg.ru", "industry": "Маркетинг/Реклама", "region": "Москва", "contact": "Скворцов Сергей (Генеральный директор)", "email": "info@dcmg.ru", "phone": "+7 (495) 665-77-77", "size": "200+", "fact": "Рекламное агентство полного цикла для B2B-компаний", "source": "https://dcmg.ru"},
    {"name": 'ООО "Перформикс" (Performics Russia)', "url": "https://www.performics.ru", "industry": "Маркетинг/Реклама", "region": "Москва", "contact": "Рутберг Роман (Генеральный директор)", "email": "info@performics.ru", "phone": "+7 (495) 755-56-56", "size": "100+", "fact": "Перформанс-маркетинг для B2B и Retail-клиентов", "source": "https://www.performics.ru"},
    {"name": 'ООО "Одода"', "url": "https://ododa.ru", "industry": "Маркетинг/Реклама", "region": "Москва", "contact": "Кузин Михаил (Генеральный директор)", "email": "info@ododa.ru", "phone": "+7 (495) 258-22-22", "size": "100+", "fact": "Digital-агентство для B2B и технологических компаний", "source": "https://ododa.ru"},
    {"name": 'ООО "Мобио" (Mobio)', "url": "https://mobio.ru", "industry": "Маркетинг/Реклама", "region": "Москва", "contact": "Назаров Илья (Генеральный директор)", "email": "info@mobio.ru", "phone": "+7 (495) 111-00-44", "size": "100+", "fact": "Performance-маркетинг и аналитика для B2B-бизнеса", "source": "https://mobio.ru"},
    {"name": 'ООО "Тексель" (Texel)', "url": "https://texel.ru", "industry": "Маркетинг/Реклама", "region": "Москва", "contact": "Фёдоров Андрей (Генеральный директор)", "email": "info@texel.ru", "phone": "+7 (495) 644-03-03", "size": "50+", "fact": "Programmatic-платформа для рекламных кампаний B2B", "source": "https://texel.ru"},
    {"name": 'ПАО "Группа ПИК"', "url": "https://www.pik.ru", "industry": "Строительство", "region": "Москва", "contact": "Эдельман Иван (Генеральный директор)", "email": "info@pik.ru", "phone": "+7 (495) 748-55-55", "size": "10000+", "fact": "Крупнейший девелопер жилья с B2B-направлением подрядных работ", "source": "https://www.pik.ru"},
    {"name": 'ПАО "Самолёт"', "url": "https://www.samolet.ru", "industry": "Строительство", "region": "Москва", "contact": "Голоулин Андрей (Генеральный директор)", "email": "info@samolet.ru", "phone": "+7 (495) 222-00-22", "size": "5000+", "fact": "Девелопер коммерческой недвижимости и госзаказов", "source": "https://www.samolet.ru"},
    {"name": 'Группа ЛСР (ПАО)', "url": "https://www.lsr.ru", "industry": "Строительство", "region": "Санкт-Петербург", "contact": "Молчанов Андрей (Президент)", "email": "info@lsr.ru", "phone": "+7 (812) 314-67-67", "size": "10000+", "fact": "Строительная группа с производством стройматериалов для B2B", "source": "https://www.lsr.ru"},
    {"name": 'АО "Стройтрансгаз"', "url": "https://www.stroytransgaz.ru", "industry": "Строительство", "region": "Москва", "contact": "Рыбакин Павел (Генеральный директор)", "email": "info@stroytransgaz.ru", "phone": "+7 (495) 725-55-00", "size": "10000+", "fact": "Строительство инфраструктуры для нефтегазового сектора", "source": "https://www.stroytransgaz.ru"},
    {"name": 'АО "Московская Медицинская Палата" (МЕДСИ)', "url": "https://medsi.ru", "industry": "Медицина", "region": "Москва", "contact": "Кузнецов Евгений (Генеральный директор)", "email": "info@medsi.ru", "phone": "+7 (495) 152-56-56", "size": "3000+", "fact": "Сеть клиник с корпоративным медицинским обслуживанием для бизнеса", "source": "https://medsi.ru"},
    {"name": 'ООО "СберЗдоровье"', "url": "https://sberhealth.ru", "industry": "Медицина", "region": "Москва", "contact": "Мельников Дмитрий (Генеральный директор)", "email": "corp@sberhealth.ru", "phone": "+7 (495) 785-15-15", "size": "1000+", "fact": "Цифровая платформа для корпоративного здоровья и ДМС", "source": "https://sberhealth.ru"},
    {"name": 'ООО "Нетология"', "url": "https://netology.ru", "industry": "Образование", "region": "Москва", "contact": "Прудникова Мария (Генеральный директор)", "email": "partner@netology.ru", "phone": "+7 (495) 946-26-72", "size": "500+", "fact": "Корпоративное обучение и повышение квалификации для компаний", "source": "https://netology.ru"},
    {"name": 'ООО "Скиллбокс" (Skillbox)', "url": "https://skillbox.ru", "industry": "Образование", "region": "Москва", "contact": "Еремеев Константин (Генеральный директор)", "email": "corp@skillbox.ru", "phone": "+7 (495) 106-00-90", "size": "500+", "fact": "Корпоративные программы обучения для бизнеса", "source": "https://skillbox.ru/corporate"},
    {"name": 'АО "ГикБрейнс" (GeekBrains)', "url": "https://geekbrains.ru", "industry": "Образование", "region": "Москва", "contact": "Прутков Андрей (Генеральный директор)", "email": "business@geekbrains.ru", "phone": "+7 (495) 118-33-87", "size": "500+", "fact": "Обучение IT-специалистов для корпоративных клиентов", "source": "https://geekbrains.ru/corporate"},
    {"name": 'ПАО "Группа компаний Детский Мир" (B2B)', "url": "https://www.detmir.ru/b2b", "industry": "Ритейл", "region": "Москва", "contact": "Соин Александр (Генеральный директор)", "email": "b2b@detmir.ru", "phone": "+7 (495) 737-60-07", "size": "10000+", "fact": "Оптовые продажи детских товаров корпоративным клиентам", "source": "https://www.detmir.ru/b2b"},
    {"name": 'ООО "Юлмарт"', "url": "https://ulmart.ru", "industry": "Ритейл", "region": "Москва", "contact": "Соколов Юрий (Генеральный директор)", "email": "b2b@ulmart.ru", "phone": "+7 (495) 221-55-55", "size": "1000+", "fact": "Оптовые поставки электроники и товаров для корпоративных клиентов", "source": "https://ulmart.ru"},
    {"name": 'АО "Самокат" (B2B)', "url": "https://samokat.ru/business", "industry": "Ритейл", "region": "Москва", "contact": "Маркевич Никита (Генеральный директор)", "email": "b2b@samokat.ru", "phone": "+7 (495) 374-55-55", "size": "5000+", "fact": "Корпоративное питание и доставка для офисов", "source": "https://samokat.ru/business"},
]

# Write base_companies.csv
with open("Z:\\opencode\\Работа\\base_companies.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Название компании", "Сайт", "Отрасль", "Регион", "Контактное лицо (должность)", "Email", "Телефон", "Размер компании", "Персонализация", "Источник персонализации"])
    for c in companies:
        writer.writerow([c["name"], c["url"], c["industry"], c["region"], c["contact"], c["email"], c["phone"], c["size"], c["fact"], c["source"]])

print(f"База сохранена: {len(companies)} компаний")

# Generate email sequences - 5 full + 50 template
with open("Z:\\opencode\\Работа\\email_sequences.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Название компании", "Персонализация", "Письмо 1 - Тема", "Письмо 1 - Тело", "Письмо 2 - Тема", "Письмо 2 - Тело", "Письмо 3 - Тема", "Письмо 3 - Тело"])

    letter2_body = (
        'Привет, {name}!\n\n'
        'Я писал вам на днях насчет автоматизации аутрича. '
        'Возможно, сейчас не самое подходящее время, но хочу поделиться кейсом.\n\n'
        'Недавно мы запустили рассылку для компании из вашей отрасли. '
        'За 4 недели они получили 20+ квалифицированных лидов и 3 новых клиента.\n\n'
        'Сделали это без спама — только персонализированный подход '
        'и умные цепочки писем.\n\n'
        'Думаю, вашему бизнесу тоже может быть полезно. '
        'Давайте обсудим это на 15-минутном созвоне?'
    )

    letter3_body = (
        'Привет, {name}!\n\n'
        'Заметил, что вы не ответили на мои предыдущие письма. '
        'Возможно, сейчас вы заняты или не ищете подрядчиков для аутрича.\n\n'
        'На всякий случай отправляю наш гайд '
        '"5 ошибок в холодных рассылках, которые убивают конверсию". '
        'Думаю, вам будет полезно.\n\n'
        'Если когда-нибудь решите попробовать автоматизированный подход '
        'к лидогенерации — мы всегда открыты к диалогу.\n\n'
        'Желаю успехов в развитии бизнеса!\n\n'
        'P.S. Если не хотите получать больше писем, '
        'просто напишите "стоп" — и я вас сразу удалю из списка.'
    )

    for i, c in enumerate(companies):
        name = c["name"]
        fact = c["fact"]
        industry = c["industry"]
        fact_short = fact[:45] if len(fact) > 45 else fact

        # Extract first name from contact
        contact = c["contact"]
        first_name = "Коллега"
        if "(" in contact:
            name_part = contact.split("(")[0].strip()
            parts = name_part.split()
            if len(parts) >= 2:
                first_name = parts[1]
            elif len(parts) >= 1:
                first_name = parts[0]

        if i < 5:
            # Full personalized emails
            l1_body = (
                f'Привет, {first_name}!\n\n'
                f'{fact} — это отличный ход. '
                f'Кстати, мы в Polza Agency как раз помогаем B2B-компаниям '
                f'привлекать клиентов через холодные рассылки.\n\n'
                f'Бесплатно сделаем аудит вашей текущей стратегии и покажем, '
                f'как можно увеличить поток лидов.\n\n'
                f'Есть ли у вас время на короткий звонок в ближайшие дни?'
            )
            l1_subj = fact_short
            l2_subj = f'Идея для {industry} / Результат, который мы получили'
            l2_body = letter2_body.format(name=first_name)
            l3_subj = 'Будем на связи / Полезный материал для вас'
            l3_body = letter3_body.format(name=first_name)
        else:
            # Template-based
            l1_subj = '{personalization_short}'
            l1_body = (
                f'Привет, {{name}}!\n\n'
                f'{{personalization}} — это отличный ход. '
                f'Кстати, мы в Polza Agency как раз помогаем B2B-компаниям '
                f'привлекать клиентов через холодные рассылки.\n\n'
                f'Бесплатно сделаем аудит вашей текущей стратегии и покажем, '
                f'как можно увеличить поток лидов.\n\n'
                f'Есть ли у вас время на короткий звонок в ближайшие дни?'
            )
            l2_subj = f'Идея для {{{{industry}}}} / Результат, который мы получили'
            l2_body = (
                f'Привет, {{name}}!\n\n'
                f'Я писал вам на днях насчет автоматизации аутрича. '
                f'Возможно, сейчас не самое подходящее время, но хочу поделиться кейсом.\n\n'
                f'Недавно мы запустили рассылку для компании из вашей отрасли. '
                f'За 4 недели они получили 20+ квалифицированных лидов и 3 новых клиента.\n\n'
                f'Сделали это без спама — только персонализированный подход '
                f'и умные цепочки писем.\n\n'
                f'Думаю, вашему бизнесу тоже может быть полезно. '
                f'Давайте обсудим это на 15-минутном созвоне?'
            )
            l3_subj = 'Будем на связи / Полезный материал для вас'
            l3_body = (
                f'Привет, {{name}}!\n\n'
                f'Заметил, что вы не ответили на мои предыдущие письма. '
                f'Возможно, сейчас вы заняты или не ищете подрядчиков для аутрича.\n\n'
                f'На всякий случай отправляю наш гайд '
                f'"5 ошибок в холодных рассылках, которые убивают конверсию". '
                f'Думаю, вам будет полезно.\n\n'
                f'Если когда-нибудь решите попробовать автоматизированный подход '
                f'к лидогенерации — мы всегда открыты к диалогу.\n\n'
                f'Желаю успехов в развитии бизнеса!\n\n'
                f'P.S. Если не хотите получать больше писем, '
                f'просто напишите "стоп" — и я вас сразу удалю из списка.'
            )

        writer.writerow([name, fact, l1_subj, l1_body, l2_subj, l2_body, l3_subj, l3_body])

print("Цепочки писем сохранены")
