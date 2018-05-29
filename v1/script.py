#import matplotlib
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
#import matplotlib.style as style
#style.use('fivethirtyeight')

print("Welcome to Project QuantifiedChase\n")


goalsleep = 8
goalfitness = 30
goalnutrition = 2040
goalmindfulness = 5
goalproductivity = 3

achievedsleep = float(input("How much sleep did you get last night?: "))
achievedfitness = int(input("How many minutes did you workout today?: "))
achievednutrition = int(input("How many calories did you eat today?: "))
achievedmindfulness = int(input("How many minutes did you meditate today?: "))
achievedproductivity = int(input("How many tasks did you complete today?: "))

sleep = int(achievedsleep / goalsleep * 100)
fitness = int(achievedfitness / goalfitness * 100)
nutrition = int(achievednutrition / goalnutrition * 100)
mindfulness = int(achievedmindfulness / goalmindfulness * 100)
productivity = int(achievedproductivity / goalproductivity * 100)

#import matplotlib.pyplot as plt; plt.rcdefaults()

objects = ('Sleep', 'Fitness', 'Nutrition', 'Mindfulness', 'Productivity')
y_pos = np.arange(len(objects))
performance = [sleep,fitness,nutrition,mindfulness,productivity]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Percent of Goal')
plt.title('Todays Dashboard')


plt.show()

print("script done")
