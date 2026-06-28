# Анализ игр Steam (Pet-проект)

**Статус: В разработке** (активно ведутся исследования)

Данный проект представляет собой исследование факторов, влияющих на успех видеоигр в Steam, с использованием методов статистического анализа и визуализации данных.

## Цель проекта
Выявить скрытые зависимости и ключевые паттерны, которые делают игру популярной или высокооцененной. Исследование включает проверку гипотез о влиянии цены, жанра, скидок и других факторов.


## Используемые технологии
*   **Язык:** Python 3
*   **Библиотеки:** Pandas, NumPy, Matplotlib, Seaborn, SciPy, Pingouin, Scikit-posthocs
*   **Среда:** Jupyter Notebook

## Структура проекта
```text
steam_games/
├── .venv/                  # Виртуальное окружение Python
│   ├── Lib/
│   ├── Scripts/
│   └── share/
├── data/                   # Исходные и обработанные данные
├── notebooks/              # Jupyter-ноутбуки для экспериментов
├── outputs/                # Результаты работы программы
│   └── visualization/      # Сохраненные графики и визуализации
├── ANALYSE_PLAN.md         # План анализа данных
├── ML_PLAN.md              # План разработки моделей машинного обучения
├── README.md               # Документация проекта
└── requirements.txt        # Список зависимостей проекта
```

## Ключевые этапы исследования
1.  **Формулировка гипотез.** Сформулированы основные предположения о влиянии жанра, цены, скидок и мультиплеера на успех игры.
2.  **Предобработка данных.** Очистка данных, удаление невышедших игр, создание новых признаков (`is_free`, `release_year`).
3.  **Исследовательский анализ (EDA).** Анализ распределений, построение гистограмм, boxplot'ов, barplot'ов.
4.  **Статистическое тестирование.** Проверка гипотез с использованием непараметрических тестов (Mann-Whitney, Kruskal-Wallis).
5.  **Корреляционный анализ.** Построение матрицы корреляции и анализ взаимосвязей между метриками.

## Планы по развитию

###  Статистика и анализ
*   [ ] Завершить статистическое тестирование всех гипотез.
*   [ ] Завершить дополнительные аналитические блоки.

### Машинное обучение
*   [ ] Базовый ML-прототип — линейная регрессия (первый опыт) 
*   [ ] Улучшить модель: добавить новые признаки, проверить на переобучение
*   [ ] Попробовать другие алгоритмы (Random Forest, Gradient Boosting)

### Визуализация и отчетность
*   [ ] Оформить итоговый отчет в виде ноутбука.

## Данные

**Источник:** [Top 1000 Steam Games (2024–2026)](https://www.kaggle.com/datasets/waddahali/top-1000-steam-games-20242026)

Данные были взяты с Kaggle и содержат информацию о 1000 самых продаваемых и популярных играх в Steam, собранный в марте 2026 года.
CSV-файл содержит 12 структурированных столбцов.

**Важно:** 
- Сам файл с данными не включен в репозиторий из-за большого размера.
- Чтобы запустить проект, скачайте датасет по ссылке выше и поместите файл `steam_games_2026.csv` в папку `data/`.

**Описание данных:**

|Column|  Type  |Description|
|:---|:------:|---|
|AppID|  int   |Unique Steam application ID|
|Name|  str   |Full game title|
|Release_Date|  date  |Official release date (YYYY-MM-DD)|
|Primary_Genre|  str   |First genre listed (Action, Indie, RPG, etc.)|
|All_Tags|  str   |Up to 10 semicolon-separated community tags|
|Price_USD| float  |Current price in USD (0.00 = Free to Play)|
|Discount_Pct|  int   |Active discount % at time of scrape (0–95)|
|Review_Score_Pct|  int   |% of positive reviews (0–100)|
|Total_Reviews|  int   |Total user reviews|
|Steam_Deck_Status|  str   |Deck compatibility (Verified / Playable / Unsupported / Unknown)|
|Estimated_Owners|  int   |Estimated owners (Total Reviews × 30)|
|24h_Peak_Players|  int   |Peak concurrent players in last 24h (SteamSpy)|

## Как запустить проект
1.  Клонируйте репозиторий.
2.  Установите необходимые библиотеки: `pip install -r requirements.txt`.
3.  Запустите Jupyter Notebook: `jupyter notebook analysis.ipynb`

