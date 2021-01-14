import pandas as pd

# Divider
d = "-" * 79  

url = "https://byui-cse.github.io/cse110-course/lesson11/life-expectancy.csv"
df = pd.read_csv(url)

print("Lowest and Highest Life expectancy: ")

lowest_LifeYear = df["Life expectancy (years)"].min()
print(f"Lowest Life expectancy (years): {lowest_LifeYear}")

highest_LifeYear = df["Life expectancy (years)"].max()
print(f"Highest Life expectancy (years): {highest_LifeYear}")

print("\n", d, "\n")

sorted_Life = (
    df.sort_values("Life expectancy (years)")
    .reset_index()
    .drop(columns="index", axis=1)
)

# The lowest life expectancy for year and country
lowest = sorted_Life[["Year", "Entity"]].iloc[0]
lowest_year = lowest[0]
lowest_country = lowest[1]

print(
    f"The lowest Life expectancy (year) was the year {lowest_year} in {lowest_country}."
)

# The highest life expectancy for year and country
highest = sorted_Life[["Year", "Entity"]].iloc[-1]
highest_year = highest[0]
highest_country = highest[1]

print(
    f"The highest Life expectancy (year) was the year {highest_year} in {highest_country}."
)

print("\n", d, "\n")

# Average from the year the user puts in.
user_year = int(input("Will you please choose a year to view? "))

life_expectancy_list = []
ntity_list = []
tup_list = []

for i in range(len(sorted_Life["Year"])):
    if user_year == sorted_Life["Year"][i]:
        life_expectancy = sorted_Life["Life expectancy (years)"][i]
        ntity = sorted_Life["Entity"][i]

        life_expectancy_list.append(life_expectancy)
        ntity_list.append(ntity)


for country, age in zip(ntity_list, life_expectancy_list):
    combo = (country, age)
    tup_list.append(combo)


def sort_lists(list_of_tuples):
    list_of_tuples.sort(key=lambda x: x[1])
    return list_of_tuples


user_year_average = sum(life_expectancy_list) / len(life_expectancy_list)

fin = sort_lists(tup_list)

minimum = fin[0]
maximum = fin[-1]

print(
    f"""
\nThe average life expectancy during the year {user_year} was {user_year_average:.1f}
\nMore information about the year:
The countries with the minimum and maximum life expectancies for {user_year} were:
Minimum: {minimum[0]} with a life expectancy of {minimum[1]:.01f} years.
Maximum: {maximum[0]} with a life expectancy of {maximum[1]:.01f} years.
"""
)