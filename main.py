import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #pip install matplotlib
#pip install requests, pip insll json_normalize
from pandas import json_normalize
import requests
from datetime import date
def case06():
    x = np.arange(-10,11)
    y = x ** 2
    #plt.plot(x, y)
    #plt.show()
    #print(x)
    #print(y)
    y_2 = -x ** 2
    #plt.plot(x, y, "--", linewidth=8, color="red") #whether linewidth or color comes first, it doesnt matter
    #plt.plot(x, y_2, ":", color="#00FF00") #use color.adobe.com website to check for color codes
    plt.plot(x, y, marker="o", markerfacecolor="red", markersize=10)
    plt.show() # -- is for dashed lines, : is for dotted line, check textbooks for others

def case07():
    #scatterplot
    x = np.random.rand(30)
    y = np.random.rand(30)
    z = np.random.rand(30)
    colours = np.random.choice(["blue", "black", "red"], 30)
    plt.scatter(x, y, marker="o", color=colours, s=z * 100)
    plt.show()

def case08():
    #histogram
    x = np.random.randn(1000)
    #plt.hist(x)
    #-
    #plt.hist(x, bins=30)
    # -
    #bins = np.arange(-4, 4, .1)
    #plt.hist(x, bins=bins)
    # -
    plt.hist(x, color="#00FF00", edgecolor='black', linewidth=1.5)
    plt.show()

def case09():
    #bar chart
    pays = ["France", "Italie", "Belgique", "Allemagne"]
    unemployment = [9.3, 9.7, 6.5, 3.4]
    #plt.bar(pays, unemployment)
    #plt.barh(pays, unemployment)
    #plt.show()

    #several variables
    countries = ["France", "Italie", "Belgique", "Allemagne"]
    unemp_f = [9.1, 11.2, 6.4, 2.9]
    unemp_h = [9.5, 9, 6.6, 3.8]
    # Position on the x-axis for each label
    position = np.arange(len(countries))
    # Bar widths
    width = .35
    # Creating the figure and a set of subgraphics
    fig, ax = plt.subplots()
    r1 = ax.bar(position - width / 2, unemp_f, width)
    r2 = ax.bar(position + width / 2, unemp_h, width)
    # Modification of the marks on the x-axis and their labels
    ax.set_xticks(position)
    ax.set_xticklabels(countries)
    plt.show()

def case10():
    countries = ["France", "Italie", "Belgique", "Allemagne"]
    no_unemp_f = [1.307, 1.185, .577, .148]
    no_unemp_h = [1.46, 1.338, .878, .179]
    plt.bar(countries, no_unemp_f)
    plt.bar(countries, no_unemp_h, bottom=no_unemp_f)
    plt.show()

def case11():
    #legend
    x = np.arange(-10, 11)
    y = x ** 2
    y_2 = x ** 3
    plt.plot(x, y, label="square ($x^2$)")
    plt.plot(x, y_2, label="cube ($x^3$)")
    plt.legend()
    plt.legend()
    path = 'C:\\Users\\Dell\\OneDrive\\Desktop\\Python Projects\\0_figures' + 'Figure_1.png'
    plt.savefig(path) #saving the figure
    plt.show()

def case12():
    path = "C:\\Users\\Dell\\OneDrive\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\02-customer_missing.csv"
    df=pd.read_csv(path)
    #print(df)
    df2 =df.replace('-','No data')
    df3= df2.fillna('No data') #if it is null value, replace it with no data
    df4= df3.replace('--', 'No data')
    df5 = df4.replace(' ','No data')
    print(df5)

def case13():
    #replacing only in a selected column
    path = "C:\\Users\\Dell\\OneDrive\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\02-customer_missing.csv"
    df=pd.read_csv(path)
    #'name' column only
    df['name'] = df['name'].fillna('No data')
    df['name'] = df['name'].replace({
        '-': 'No data',
        '--': 'No data',
        ' ': 'No data'
    })
    print(df)

def case14():
    path = "C:\\Users\\Dell\\OneDrive\\Desktop\\0_1.24 Sem\\Computer tools\\Data\\02-customer_missing.csv"
    df=pd.read_csv(path)
    #print(df)
    #df['duration']= calculateAge(date(1992, 2,3))
    for x in df.index:
        jdate= df.at[x,'date_join']
        y = int(jdate[0:4])
        m = int(jdate[5:7])
        d = int(jdate[8:10])
        duration_value = calculateAge(date(y, m, d))
        df.at[x, 'duration'] = duration_value
        print(df)
def calculateAge(birthDate):
    days_in_year =365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age

def case15():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(BASE_URL + "/products")
    data = response.json()
    df = json_normalize(data)
    print(df[['id','title','category']])

def challenge():
    BASE_URL = 'https://fakestoreapi.com'
    response = requests.get(BASE_URL + "/products")
    data = response.json()
    df = json_normalize(data)
    #print(df[['category']])
    df2 = df[['category']].drop_duplicates()
    print(df2.values.tolist())

if __name__ == '__main__':
    #case06()
    #case07()
    #case08()
    #case09()
    #case10()
    #case11()
    #case12()
    #case13()
    #case14()
    #case15()
    challenge()