import os
from glob import glob


def get_files():
    """
    Return all csv files in ./data
    """
    return glob('./data/*.csv')


def calculate_confidence_levels(fsd=0):
    """
    TODO: Add comment
    """
    level = 'n/a'
    if fsd <= 13:
        level = 'high'
    elif fsd > 13 and fsd <= 20:
        level = 'medium'
    elif fsd > 20:
        level = 'low'
    return level


def get_confidence_level(df=None, column_name=None):
    """
    TODO: Add comment
    """
    confidence_levels = []
    for index, row in df.iterrows():
        fsd = row[column_name]
        level = calculate_confidence_levels(fsd)
        confidence_levels.append(level)
    return confidence_levels