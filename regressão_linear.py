import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
import random 
x = np.array([100,150,200,250,300,350,400,450]).reshape(-1,1)
y = np.array([27.77777778,41.66666667,55.55555556,69.44444444,83.33333333,97.22222222,111.1111111,125]).reshape(-1,1)
'''
x = np.array(range(0,100)).reshape(-1,1)
y = np.empty(len(x))
for i in range(len(x)):
    y[i] = randint(0,100)+i*2
y = y.reshape(-1,1)
'''

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)  #separando 20% para treinar
regressor = LinearRegression()
regressor.fit(X_train, y_train) #treinando o algoritimo
y_pred = regressor.predict(X_test)
plt.plot(x,y, 'bo')
#plt.plot(X_test, y_pred, color='red', linewidth=2) #valores testados no grafico com os valores previstos
a = regressor.coef_
b = regressor.intercept_
print("y = ",a,"*x", "+",b) #equação da reta otima
y1 = []
for i in x:
    y1.append((a[0]*i)+b[0])
print('Raiz quadrada do erro-médio',np.sqrt(metrics.mean_squared_error(y_test, y_pred)*100), "%") #porcentagem do erro testado em relção ao previsto
plt.plot(x,y1, color = 'green')
print(regressor.score(X_test,y_test))
plt.show()
