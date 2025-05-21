import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general = pd.read_csv("test/general.csv")
prenatal = pd.read_csv("test/prenatal.csv")
sports = pd.read_csv("test/sports.csv")

prenatal.columns = general.columns
sports.columns = general.columns

hospitals = pd.concat([general, prenatal, sports], ignore_index=True)
hospitals = hospitals.drop(columns='Unnamed: 0')

hospitals = hospitals.dropna(how='all')

hospitals['gender'] = hospitals['gender'].replace({'man' : 'm', 'male' : 'm', 'female' : 'f',
                                                   'woman' : 'f'})
hospitals['gender'] = hospitals['gender'].fillna('f')

hospitals.loc[:, 'bmi' : 'months'] = hospitals.loc[:, 'bmi' : 'months'].fillna(0)

bins = [0, 15, 35, 55, 70, 80]
plt.hist(hospitals['age'], bins=bins)
plt.show()

print("The answer to the 1st question: 15-35")

plt.pie(hospitals['diagnosis'].value_counts() / len(hospitals), labels=list(hospitals['diagnosis'].value_counts().index), autopct='%.1f%%')
plt.show()

print('The answer to the 2nd question: pregnancy')

plt.violinplot(hospitals['height'])
plt.show()

print('The answer to the 3rd question: because we have prenatal specialization, which is responsible for small values, and specializations for adults, which correspond to bigger values')

# print(f"The answer to the 1st question is {hospitals.hospital.value_counts().idxmax()}")
#
# nr_of_stomach_issues = hospitals[hospitals.hospital == 'general'].diagnosis.value_counts()['stomach']
# nr_of_general = hospitals[hospitals.hospital == 'general'].count()['hospital']
# print(f"The answer to the 2nd question is {(nr_of_stomach_issues / nr_of_general).round(3)}")
#
# nr_of_dislocations = hospitals[hospitals.hospital == 'sports'].diagnosis.value_counts()['dislocation']
# nr_of_sports = hospitals[hospitals.hospital == 'sports'].count()['hospital']
# print(f"The answer to the 3rd question is {(nr_of_dislocations / nr_of_sports).round(3)}")
#
# general_age_median = hospitals[hospitals.hospital == 'general']['age'].median()
# sports_age_median = hospitals[hospitals.hospital == 'sports']['age'].median()
# print(f"The answer to the 4th question is {int(general_age_median - sports_age_median)}")
#
# print(f"The answer to the 5th question is {hospitals[hospitals['blood_test'] == 't']['hospital'].value_counts().idxmax()},"
#       f"{hospitals[hospitals['blood_test'] == 't']['hospital'].value_counts().max()} tests")
