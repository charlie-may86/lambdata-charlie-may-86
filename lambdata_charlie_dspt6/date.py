import pandas as pd


def date_columns(X):
    '''Identifies a date column and split dates ("MM/DD/YYYY", etc.) into new
    columns that contain the year, month, and day.

    Args:
      X: The dataframe you are passing through.
        note: name of date column should be 'Date'.

    Returns:
      The dataframe you pass through with three new columns.

    Raises:
      KeyError: 'Date' - if date column is not named 'Date'.

    '''

    #create a year column
    X['year'] = pd.DatetimeIndex(X['Date']).year

    #create a month column
    X['month'] = pd.DatetimeIndex(X['Date']).month

    #create a day column
    X['day'] = pd.DatetimeIndex(X['Date']).day
