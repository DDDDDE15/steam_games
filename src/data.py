"""Загрузка и базовая очистка данных"""
import pandas as pd
import numpy as np
from src.config import DATA_FILE

def load_raw_data() -> pd.DataFrame:
    """
    Загрузка сырого csv в DataFrame
    :return:
        df: сырой датафрейм с колонками в нижнем регистре.
    """
    df = pd.read_csv(DATA_FILE)
    df.columns = df.columns.str.lower()
    return df

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Базовая очистка данных.
    Выполняет:
    1. Удаляет невышедшие игры (нет владельцев, отзывов и онлайна).
    2. Удаляет колонку steam_deck_status (во всех строках Unknown).
    3. Парсит release_date в datetime.
    4. Создаёт производные признаки: release_year, is_free.

    Важно: пропуски в числовых признаках НЕ заполняются здесь.
    Их заполнение — в пайплайне через SimpleImputer, чтобы
    избежать утечки данных между train и val.


    :param df:
        df: сырой датафрейм с колонками в нижнем регистре.
    :return:
        df: очищенный датафрейм.
    """
    # 1. Убираем невышедшие игры
    condition = (
            ((df['estimated_owners'].isna()) | (df['estimated_owners'] == 0)) &
            ((df['total_reviews'].isna()) | (df['total_reviews'] == 0)) &
            ((df['24h_peak_players'].isna()) | (df['24h_peak_players'] == 0)))
    df = df.loc[~condition].copy()

    # 2. Убираем бесполезную колонку
    df.drop(columns=['steam_deck_status'], inplace=True)

    # 3. Парсим дату
    df['release_date'] = pd.to_datetime(df['release_date'])

    # 4. Производные признаки
    df['is_free'] = df['price_usd'] == 0
    df['release_year'] = df['release_date'].dt.year.astype('Int64')
    df.loc[df["release_date"].isna(), "release_year"] = pd.NA

    # Рейтинг 0 — это ошибка сбора, а не «самый плохой рейтинг».
    # Заменяем на NaN, чтобы SimpleImputer в пайплайне заполнил его корректно.
    df["review_score_pct"] = df["review_score_pct"].replace(0, np.nan)
    df["review_score_pct"] = df["review_score_pct"].astype("float").astype("Int64")



    return df
