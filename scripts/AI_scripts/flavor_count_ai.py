import pandas as pd
import sqlite3
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

class PredictionResults:
    @staticmethod
    def run_prediction():
        conn = sqlite3.connect("site.db")
        query = "SELECT id, lava, hot_fudge, blizzard, chocolate, vanilla FROM flavor_count"
        data_set = pd.read_sql_query(query, conn)
        conn.close()

        if data_set.empty: 
            return [], None 

        data_set = pd.concat([data_set] * 2, ignore_index=True)
        independent = data_set[['lava', 'hot_fudge', 'blizzard', 'chocolate', 'vanilla']].values
        y_train, y_test, x_train, x_test = train_test_split(independent, independent, test_size=0.50, random_state=0)
        sc = StandardScaler()
        x_train = sc.fit_transform(x_train)
        x_test = sc.transform(x_test)
        regressor = RandomForestRegressor(random_state=0)
        regressor.fit(x_train, y_train)
        y_pred = regressor.predict(x_test)
        mse = mean_squared_error(y_test, y_pred)

        results_list = []
        for i in range(len(y_test)):
            row_id = data_set.iloc[i, 0]  
            lava = y_test[i, 0]
            ai_lava = y_pred[i, 0]
            hot_fudge = y_test[i, 1]
            ai_hot_fudge = y_pred[i, 1]
            blizzard = y_test[i, 2]
            ai_blizzard = y_pred[i, 2]
            chocolate = y_test[i, 3]
            ai_chocolate = y_pred[i, 3]
            vanilla = y_test[i, 4]
            ai_vanilla = y_pred[i, 4]            
            results_list.append([row_id, lava, ai_lava, hot_fudge, ai_hot_fudge, blizzard, ai_blizzard, chocolate, ai_chocolate, vanilla, ai_vanilla])
        return results_list, mse