import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("carSales.csv")
print(df.head(10),"\n")

# total number of cars and brands
brand_car=df.groupby("Brand")["Car_Name"].count()
print(f"The number of cars in each brand are {brand_car}")

total_number_of_car=df["Car_Name"].count()
print(f"The total numbers of car are :: {total_number_of_car}\n")

total_number_of_brand=df["Brand"].nunique()
print(f"The total numbers of brands are:: {total_number_of_brand}\n")

# total number of car types (Fuel types, Transmission, Seller types)
fuel_type=df.groupby("Fuel_Type")["Car_Name"].count()
print(f"These are fule Types \n{fuel_type}\n")

transmission=df.groupby("Transmission")["Car_Name"].count()
print(f"No of Transmission are \n{transmission}\n")

seller_type=df.groupby("Seller_Type")["Car_Name"].count()
print(f"seller types are \n{seller_type}\n")

# Summary statistics
summary=df.describe().round(2)
print(summary,"\n")


# most expensive and cheapest cars
expensive=df.loc[df["Price"].idxmax(),["Car_Name","Price","Brand"]]
cheapest=df.loc[df["Price"].idxmin(),["Car_Name","Price","Brand"]]
    
print(f"The most Expensive Car is {expensive["Car_Name"]} brand name is {expensive["Brand"]} with the Price of {expensive["Price"]}")
print(f"The most Cheapest Car is {cheapest["Car_Name"]} brand name is {cheapest["Brand"]} with the Price of {cheapest["Price"]}")

# Average price by Brand, Fuel_Type, Transmission


brand_avg=df.groupby(["Brand","Fuel_Type","Transmission"])["Price"].mean().round(2).reset_index()

print(f"\n{brand_avg}\n")


# Correlation between Mileage, Engine_Size, and Price
correlation =df[["Mileage","Engine_Size","Price"]].corr().round(2)
print(correlation,"\n")

# average selling price by brand
avg_selling_price_brand=df.groupby("Brand")["Price"].mean().round(2)
print(f"The average selling price is :: \n{avg_selling_price_brand}\n")


# Top 5 brands by average selling price

top_5=avg_selling_price_brand.nlargest(5)
print(top_5)


# Cars older than 2015 but still expensive (> $20,000)

year=df[(df["Year"]<2015) & (df["Price"]>20000)]

if year.empty:
    print("No cars older than 2015 with price > $20,000 found.")
else:
    print(year)

# Correlation between Mileage, Engine_Size, and Price graph

sns.heatmap(correlation,annot=True,cmap="coolwarm")
plt.show()

# change the colors of bars
unique_brand=df["Brand"].unique()
if(len(unique_brand)<10):
    palette=sns.color_palette("tab10",len(unique_brand))
elif(len(unique_brand)<20):
    palette=sns.color_palette("tab20",len(unique_brand))
else:
    palette=sns.color_palette("husl",len(unique_brand))
brand_color={brand: palette[ i % len(palette)]for i,brand in enumerate(unique_brand)}
colors=[brand_color[b] for b in df["Brand"]]


# Bar chart – Average Price by Brand
plt.bar(avg_selling_price_brand.index,avg_selling_price_brand.values,color=colors)
plt.axhline(avg_selling_price_brand.mean(),linestyle="--",linewidth=2,color="black",label="average")
plt.title("BAR CHART WHICH SHOWES THE BRAND AVERAGE PRICE")
plt.xlabel("Brand")
plt.ylabel("AVERAGE PRICE")
plt.legend()
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()

# bar chart of top_5
plt.bar(top_5.index,top_5.values,color=colors)
plt.show()
# Scatter Plot – Price vs Mileage

plt.scatter(df["Price"],df["Mileage"],color="red",s=100)
plt.title("SCATTER CHART WHICH SHOWES THE PRICE VS MILEAGE")
plt.xlabel("PRICE")
plt.ylabel("MILAGE")
plt.grid(True,linestyle="--",alpha=0.5)
plt.show()

# Pie Chart – Cars by Fuel Type
plt.pie(fuel_type,autopct="%1.1f%%",startangle=90,labels=fuel_type.index)
plt.axis("equal")
plt.tight_layout()
plt.title("Pie chart")
plt.show()

# Line Plot – Average Price by Year (to see trends)

avg_price_by_year = df.groupby("Year")["Price"].mean()
plt.plot(avg_price_by_year.index, avg_price_by_year.values, color="red", marker="o")
plt.title("Average Car Price by Year")
plt.xlabel("Year")
plt.ylabel("Average Price")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

