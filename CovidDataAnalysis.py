import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print('Libraries are imported successfully.')

corona_dataset_csv = pd.read_csv("Datasets/covid19_Confirmed_dataset.csv")
corona_dataset_csv.head(10)

corona_dataset_csv.shape #size of covid dataset

#Removing less useful columns
corona_dataset_csv.drop(["Lat","Long"],axis=1, inplace= True)
corona_dataset_csv.head(10)

corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
corona_dataset_aggregated.head()
corona_dataset_aggregated.shape #size after removing latitude and longitude

#Testing plotting for China, Italy, and Spain
corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Spain"].plot()
plt.legend()

corona_dataset_aggregated.loc['China'].plot()
corona_dataset_aggregated.loc["China"][:3].plot()
corona_dataset_aggregated.loc["China"].diff().plot() #Plotting derivitive to see change

corona_dataset_aggregated.loc["China"].diff().max()
corona_dataset_aggregated.loc["Italy"].diff().max()
corona_dataset_aggregated.loc["Spain"].diff().max()

#Corona_dataset_aggregated has the max infection rate of every country.
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
corona_dataset_aggregated["max_infection_rate"] = max_infection_rates

corona_dataset_aggregated.head()
#Creating dataset with just the max infection rate
corona_data = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])
corona_data.head()


#Importing world hapiness report
hapiness_report_csv = pd.read_csv("Datasets/worldwide_happiness_report.csv")
hapiness_report_csv.head()

#Removing less useful columns
useless_cols =["Overall rank", "Score", "Generosity", "Perceptions of corruption"]
hapiness_report_csv.drop(useless_cols, axis=1, inplace=True)
hapiness_report_csv.head()
hapiness_report_csv.set_index("Country or region", inplace = True)
hapiness_report_csv.head()

#Merging Datasets
corona_data.head()
corona_data.shape

hapiness_report_csv.shape


#Using inner join because hapiness dataset contains more countries
data=corona_data.join(hapiness_report_csv,how="inner")
data.head()

#Corrilation Matrix
data.corr()

#Visualizing Results
data.head()

#GDP vs Infection Rate
x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))


#Social Support vs Infection Rate
x = data["Social support"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))

#Healthy Life Expectancy vs Infection Rate
x = data["Healthy life expectancy"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))
sns.regplot(x,np.log(y))