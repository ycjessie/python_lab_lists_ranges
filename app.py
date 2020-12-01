students = ['Jessie', 'Tina', 'Sofia','Peter','Sam']
foods=('dumplings','fried rice','beef noodles','tofu')
cohort=[]
for n,f in zip(students,foods):
    cohort.append({"student":n,"fav_food":f})

for c in cohort:
    print(c)