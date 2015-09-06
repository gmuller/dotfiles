import sys
from tabulate import tabulate
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()

section = sys.argv[1]
parser.read("workout_config.py")
options = parser.options(section)
workouts = []
for option in options:
    weight = parser.get(section, option)
    start = (option, weight)
    workouts.append(start)

warmup_perc = [(0.4, 5), (0.5, 5), (0.6, 3)]
week_one_perc = [(0.75, 5), (0.8, 5), (0.85, 5)]
week_two_perc = [(0.80, 3), (0.85, 3), (0.90, 3)]
week_three_perc = [(0.75, 5), (0.85, 3), (0.95, 1)]
week_four_perc = [(0.6, 5), (0.65, 5), (0.70, 5)]

all_perc = [week_one_perc, week_two_perc, week_three_perc, week_four_perc]

bastard = True

def roundnear(x, base=5):
    return int(base * round(float(x)/base))

def getweights(percentages, base_weight):
    calc_weights = []
    for perc in percentages:
        weight = roundnear(perc[0] * int(base_weight))
        calc_weights.append(str(perc[1]) + " x " + str(weight))
    return calc_weights

f = open(section + ".html", "w")
i = 1
for week in all_perc:
    if bastard: week.reverse()
    work = {}
    for workout in workouts:
        wu_weight = getweights(warmup_perc, workout[1])
        work_weight = getweights(week, workout[1])
        wu_weight.extend(work_weight)
        work[workout[0]] = wu_weight
    f.write("<h2>Week " + str(i) + "</h2>")
    f.write(tabulate(work,  headers="keys", tablefmt="html"))
    f.write("\n\n")
    i = i + 1
f.close()
