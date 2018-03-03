import pandas as pnd
import matplotlib.pyplot as plo

print("\nData science program")
print("Pokemon Dataset , source : https://www.kaggle.com/abcsds/pokemon/data")
ofil = pnd.read_csv("Pokemon.csv")

print("\n\n Mean of dataset \n")
print(ofil.mean())

print("\n\n Median of dataset \n")
print(ofil.median())

print("\n\n Mode of dataset")
print(ofil.mode())

print("Graph plots will be shown \n")

print("Figure 1 - General plotting of data on graph")
ofil.plot()  # plots all columns against index

print("Figure 2 - Scatter graph with x axis as Attack and y axis as Defence")
ofil.plot(kind='scatter',x='Attack',y='Defense') # scatter plot

print("Figure 3 - Density graph")
ofil.plot(kind='density')  # estimate density function

print("Figure 4 - Histogram graph")
ofil.plot(kind='hist') # histogram plot

print("Figure 5 - Box graph")
ofil.plot(kind='box') # Box plot

plo.show() #visualization
