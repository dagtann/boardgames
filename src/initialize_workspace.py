import numpy as np
import pandas as pd
import sqlalchemy as sqla

%matplotlib

PATH_DB = "sqlite:////Users/dag/github/boardgames/dta/raw/"
NAME_DB = "database.sqlite"

db = sqla.create_engine(PATH_DB + NAME_DB)
board_df = pd.read_sql("select * from BoardGames", db)

board_df.shape
board_df.info()


board_df["game.type"].value_counts()
board_df["details.yearpublished"].min()
board_df["details.yearpublished"].max()
board_df.boxplot(column=["details.yearpublished"], grid=False)

