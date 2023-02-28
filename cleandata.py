import pandas as pd

def main():
    df1 = pd.read_csv(r"vnindex1.csv")
    df2 = pd.read_csv(r"vnindex2.csv")
    df2 = df2[:-1] # trung ngay 25/3/2021

    df = pd.concat([df2, df1]) # merge
    df = df.iloc[::-1] #reverse dataframe
    df = df.reset_index()
    df = df.drop("index", axis=1)

    # Drop commas
    for index, day in df.iterrows():
        day["Price"] = day["Price"].replace(",", "")
        day["Open"] = day["Open"].replace(",", "")
        day["High"] = day["High"].replace(",", "")
        day["Low"] = day["Low"].replace(",", "")

    # Save in a csv
    df.to_csv("final.csv")
    


if __name__ == "__main__":
    main()