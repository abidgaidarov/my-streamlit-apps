import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

st.write("""

# Чаевые в ресторане

### Исследование датасета с информацией об оставленных чаевых

""")

st.write("#### 1. Импортируем и посмотрим первые 5 строчек датафрейма")

tips = pd.read_csv('tips_data.csv')

st.dataframe(tips.head(5))

st.write(" #### 2. Построим гистограмму распределения общего счета")
fig, ax = plt.subplots(figsize=(10,3))
plt.hist(tips['total_bill'])
plt.title('Гистограмма распределения общего счета')
plt.xlabel('Общий счет')
plt.ylabel('Частота')
st.pyplot(fig)


st.write(" #### 2. Построим scatterplot, показывающий связь между total_bill and tip")
fig, ax = plt.subplots(figsize=(10,3))
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Scatterplot, показывающий связь между total_bill and tip')
plt.xlabel('Общий счет')
plt.ylabel('Чаевые')
st.pyplot(fig)


st.write(" #### 3. Построим график, связывающий total_bill, tip, и size")
fig, ax = plt.subplots(figsize=(10,3))
sns.scatterplot(data=tips, x='total_bill', y='tip', size='size', hue='size', marker='X')
st.pyplot(fig)


st.write(" #### 4. Покажим связь между днем недели и размером счета")

day = tips.pivot_table(index='day', values='total_bill', aggfunc='median')
day = day.reindex(['Thur', 'Fri', 'Sat', 'Sun'])
st.dataframe(day)

fig, ax = plt.subplots(figsize=(10,3))
sns.lineplot(data=day, x=day.index, y='total_bill')
plt.title('Связь между днем недели и размером счета')
st.pyplot(fig)


st.write(" #### 5. Построим scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу")

fig, ax = plt.subplots(figsize=(10,3))
sns.scatterplot(tips, x='day', y='tip', hue='sex', marker='x')
plt.title('Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу', fontsize=9)
st.pyplot(fig)

tip_day = tips.pivot_table(index='day', columns='sex', values='tip', aggfunc='median')
tip_day = tip_day.reindex(['Thur', 'Fri', 'Sat', 'Sun'])
st.dataframe(tip_day)

fig, ax = plt.subplots(figsize=(10,3))
sns.scatterplot(data=tip_day, x=tip_day.index, y='Female', label='Female')
sns.scatterplot(data=tip_day, x=tip_day.index, y='Male', label='Male')
plt.title('Scatter plot с днем недели по оси y, чаевыми по оси x, и цветом по полу', fontsize=9)
plt.legend()
st.pyplot(fig)


st.write(" #### 6. Построим box plot c суммой всех счетов за каждый день, разбивая по time (Dinner/Lunch)")

sum_bill = tips.pivot_table(index='day', values='total_bill', columns='time', aggfunc='sum')
sum_bill = sum_bill.reindex(['Thur', 'Fri', 'Sat', 'Sun'])
st.dataframe(sum_bill)

fig, ax = plt.subplots(figsize=(10,3))
sns.boxplot(data=tips, y='total_bill', x='time')
st.pyplot(fig)


st.write(" #### 7. Нарисуйте 2 гистограммы чаевых на обед и ланч. Расположите их рядом по горизонтали.")
fig, ax = plt.subplots(figsize=(10,3))

ax1 = plt.subplot(1, 2, 2)
plt.hist(data=tips[tips['time'] == 'Dinner'], x='tip', bins=20)
ax1.set_xlabel('Размер чаевых')
ax1.set_title('Dinner')

ax2 = plt.subplot(1, 2, 1, sharey=ax1)
plt.hist(data=tips[tips['time'] == 'Lunch'], x='tip', bins=20)
ax2.set_ylim(bottom=0, top=35)
ax2.set_xlim(left=0, right=10)
ax2.set_title('Lunch')
ax2.set_xlabel('Размер чаевых')

fig.suptitle('2 гистограммы чаевых на обед и ланч', fontsize=16)

st.pyplot(fig)



st.write(" #### 8. Нарисуйте 2 scatterplots (для мужчин и женщин), показав связь размера счета и чаевых, дополнительно разбив по курящим/некурящим. Расположите их по горизонтали")
fig, ax = plt.subplots(figsize=(10,3))

ax1 = plt.subplot(1, 2, 2)
sns.scatterplot(data=tips[tips['sex'] == 'Male'], x='tip', y='total_bill', hue='smoker')
ax1.set_xlabel('Размер чаевых')
ax1.set_title('Male')
ax1.axes.get_yaxis().set_visible(False)

ax2 = plt.subplot(1, 2, 1, sharey=ax1)
sns.scatterplot(data=tips[tips['sex'] == 'Female'], x='tip', y='total_bill', hue='smoker')
#ax2.set_ylim(bottom=0, top=35)
#ax2.set_xlim(left=0, right=10)
ax2.set_title('Female')
ax2.set_xlabel('Размер чаевых')

fig.suptitle('2 scatterplots (для мужчин и женщин), и связь размера счета и чаевых', fontsize=12)

st.pyplot(fig)