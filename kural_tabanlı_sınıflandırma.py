import seaborn as sns
import pandas as pd
from pandas.api.types import CategoricalDtype
df = pd.read_csv(r"C:\Users\Sony\PycharmProjects\pythonProject1\Homeworks\persona.csv")
df.head()

def simple_control(dataframe):
    """
       A small function to understand the data

       Parameters
       ----------
       dataframe : DataFrame
           Type the name of your dataframe
       -------

       """
    print("----------shape--------")
    print(dataframe.shape)
    print("----------dtypes--------")
    print(dataframe.dtypes)
    print("----------Head--------")
    print(dataframe.head())
    print("----------describe--------")
    print(dataframe.describe())
simple_control(df)


def cat_control(dataFrame):
    """
    We examine the numbers of classes
    """
    cat_df = [i for i in dataFrame.columns if dataFrame[i].dtypes in ["category","bool","object"]]
    cat_df.append("PRICE")
    for col in cat_df:
        print(col)
        print(dataFrame[col].unique())
        print(dataFrame[col].value_counts())
        print(dataFrame[col].value_counts().count())
        print("---------------------------")
    return cat_df
cat_control(df)

def sum_mean(dataframe,grp,target):
    """
    We look at the mean and total values of SOURCE and COUNTRY variables.
    """
    print(dataframe.groupby(grp)[target].sum())
    print(dataframe.groupby(grp)[target].mean())
sum_mean(df,"SOURCE","PRICE")
sum_mean(df,"COUNTRY","PRICE")

#Let's group the sources and countries and examine the average prices.
fan0 = ["SOURCE","COUNTRY"]
df.groupby(fan0)["PRICE"].mean()

#Let's calculate the average price for all variables
fan1 = ["COUNTRY", "SOURCE", "SEX", "AGE"]
agg_df=df.groupby(fan1)["PRICE"].mean()

#Let's sort by price and arrange the indexes
agg_df = agg_df.sort_values(ascending=False)
agg_df = agg_df.reset_index()
agg_df.index

#Let's add agg_df and make it categorical
agg_df["newage"] =pd.cut(agg_df["AGE"],[0,18,24,30,40,70],labels=["0_18","19_24","25_30","31_40","41_70"])
agg_df["newage"]=agg_df["newage"].astype("object")

#let's define new level based customers
agg_df["customers_level_based"] = agg_df.COUNTRY+"_"+agg_df.SOURCE+"_"+agg_df.SEX+"_"+agg_df["newage"]
agg_df["customers_level_based"] = [col.upper() for col in agg_df.customers_level_based]
fan2 = ["customers_level_based","PRICE"]
agg_df = agg_df[fan2]
agg_df =agg_df.groupby("customers_level_based").mean()
agg_df = agg_df.sort_values(by = "PRICE",ascending=False)
agg_df = agg_df.reset_index()

#Let's segment new customers
agg_df["segment"] = pd.qcut(agg_df["PRICE"],4,labels=["D","C","B","A"])
new_user = "TUR_ANDROID_FEMALE_31_40"
new_user1 = "FRA_IOS_MALE_25_30"

#let's assign new customers and estimate how much they can bring
agg_df[agg_df["customers_level_based"] == new_user]
agg_df[agg_df["customers_level_based"] == new_user1]
agg_df