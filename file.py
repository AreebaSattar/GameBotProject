import socket
import json
from game_state import GameState
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import joblib


import numpy as np

datFramTemp = pd.read_csv('bot.csv')
datFramTemp = datFramTemp[datFramTemp["has_round_started"]]

datFramTemp = datFramTemp[~((datFramTemp[['Player1_buttons_up', 'Player1_buttons_down', 'Player1_buttons_right',
            'Player1_buttons_left', 'Player1_buttons_X', 'Player1_buttons_Y',
            'Player1_buttons_A', 'Player1_buttons_B', 'Player1_buttons_L',
            'Player1_buttons_R']] == False).all(axis=1))]
print(pd.DataFrame(datFramTemp))
print(datFramTemp.head())

string_cols = datFramTemp.select_dtypes(include='object').columns
for ij in string_cols:
    labels, unique = pd.factorize(datFramTemp[ij])
    datFramTemp[ij] = labels.astype(float)

print(datFramTemp.shape)
XvAlss = datFramTemp[['Player1_health', 'Player2_health', 'Player1_is_jumping', 'Player1_is_crouching',
         'Player1_is_player_in_move', 'Player1_move_id', 'Player1_ID', 'Player2_ID','Player2_is_jumping','Player2_is_crouching','Player2_is_player_in_move','Player2_move_id']]
Yi = datFramTemp[['Player1_buttons_up', 'Player1_buttons_down', 'Player1_buttons_right', 'Player1_buttons_left',
         'Player1_buttons_X', 'Player1_buttons_Y', 'Player1_buttons_A', 'Player1_buttons_B',
         'Player1_buttons_L', 'Player1_buttons_R']]

print(datFramTemp.isnull().sum())
X_trainn, X_test, y_train, y_test = train_test_split(XvAlss, Yi, test_size=0.2, random_state=42)
train_data = pd.concat([X_trainn, y_train], axis=1).dropna()
X_trainn = train_data.drop(Yi.columns, axis=1)
y_train = train_data[Yi.columns]
print(X_test.columns)

M = RandomForestClassifier()
M.fit(X_trainn, y_train)

predictt = M.predict(X_test)
accuracy = np.mean(predictt == y_test)
print("Accuracy:", accuracy)

Filee= 'Model_Saveddd.pkl'
pickle.dump(M, open(Filee, 'wb'))
ff = 'model.joblib'
joblib.dump(M, ff)

