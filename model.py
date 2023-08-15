import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor

def model(option, Low=0, Open=0, High=0, Volume=0, Marketcap=0):
    #reading database
    df = pd.read_csv("./coin_Bitcoin.csv")
    df = df.drop(["SNo", "Date","Name", "Symbol"], axis=1)

    if option == "get_database":
        return df

    #pre-processing and normalizing data
    mms = MinMaxScaler()
    mms_pred = MinMaxScaler()
    df["High"] = mms.fit_transform(df[["High"]])
    df["Low"] = mms.fit_transform(df[["Low"]])
    df["Open"] = mms.fit_transform(df[["Open"]])
    df["Close"] = mms_pred.fit_transform(df[["Close"]])
    df["Volume"] = mms.fit_transform(df[["Volume"]])
    df["Marketcap"] = mms.fit_transform(df[["Marketcap"]])

    if option == "pre_processing_data":
        return df
    
    #spliting data ain train and validation
    X = df.drop(["Close"], axis=1)
    y = df["Close"] 
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2, random_state=42)

    if option == "train_valid_split":
        return X_train, X_valid, y_train, y_valid

    #get database predict
    pipe = Pipeline([
        ("imputer", SimpleImputer()),
        ("tree", DecisionTreeRegressor())
    ])

    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_valid)

    df_predict = pd.DataFrame({
        "Expected": y_valid,
        "Returned": y_pred
    })

    if option == "database_predict":
        return df_predict

    pipe = Pipeline([
        ("imputer", SimpleImputer()),
        ("tree", DecisionTreeRegressor())
    ])

    pipe.fit(X_train, y_train)
    score = pipe.score(X_valid, y_valid)

    if option == "model_score":
        return score
    
    X_predict = pd.DataFrame({"High": [High],"Low": [Low],"Open": [Open], "Volume": [Volume], "Marketcap": [Marketcap]})
    X_predict["High"] = mms.fit_transform(X_predict[["High"]])
    X_predict["Low"] = mms.fit_transform(X_predict[["Low"]])
    X_predict["Open"] = mms.fit_transform(X_predict[["Open"]])
    X_predict["Volume"] = mms.fit_transform(X_predict[["Volume"]])
    X_predict["Marketcap"] = mms.fit_transform(X_predict[["Marketcap"]])

    if option == "predict":
        pred = pipe.predict(X_predict)[0]
        df_pred = pd.DataFrame({"Predicted value": [pred]})
        df_pred["Predicted value"] = mms_pred.inverse_transform(df_pred[["Predicted value"]])
        print(df_pred)
        return df_pred