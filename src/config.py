"""Конфигурация проекта: пути и глобальные константы"""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
MODELS_DIR = PROJECT_ROOT / "models"
METRICS_DIR = PROJECT_ROOT / "metrics"
VISUALIZATION_DIR = PROJECT_ROOT / "visualization"

DATA_FILE = DATA_DIR / "steam_games_2026.csv"

RANDOM_STATE = 42
TARGET = "24_peak_players"