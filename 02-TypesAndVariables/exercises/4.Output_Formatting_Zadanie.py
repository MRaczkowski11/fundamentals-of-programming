# Program using f-strings========================================================================================================================================================================================================

name = "Adam"
age = 22
height = 180

print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {age + 6} years old.")                     

# Program obliczający dochód na osobę========================================================================================================================================================================================================

father_income = 5450
mother_income = 4920
family_members = 5

total_income = father_income + mother_income                        #Obliczanie całkowitego dochodu rodziny poprzez dodanie dochodów ojca i matki
income_per_person = total_income / family_members                      #Obliczanie dochodu na osobę poprzez podzielenie całkowitego dochodu rodziny przez liczbę członków rodziny

print(f'Total family income is {total_income}, and income per person is {income_per_person}.')                 #Wyświetlanie całkowitego dochodu rodziny oraz dochodu na osobę z użyciem f-stringów

# Program pokazujący values and variables========================================================================================================================================================================================================

a = 3
b = 5

print(f'{a}+{b}={a + b}')        
print(f'{a}-{b}={a - b}')
print(f'{a}*{b}={a * b}')
print(f'{a}/{b}={a / b}')
