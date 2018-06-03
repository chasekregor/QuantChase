import os
import datetime
import pandas as pd
import numpy as np
import c3pyo as c3
from flask import Flask, render_template, json, request, redirect, url_for

app = Flask(__name__)

#today
def get_sleep_chart_json():

    #data
    sleepdata = pd.read_csv('data/Sleep Analysis.csv')
    sleep = sleepdata[['In bed start','In bed Finish','Minutes in bed','Minutes asleep']]
    sleep.columns = ['Inbedstart', 'InbedFinish','Minutesinbed','Minutesasleep']
    sleep = sleep[::-1].head(1)

    date = []
    for i in sleep.InbedFinish:
        date.append(i)

    minutesinbed = sleep.Minutesinbed
    sleep = []
    for i in minutesinbed:
        sleep.append(i / 60)

    avgsleep = np.average(sleep)

    #chart
    chart = c3.BarChart()
    chart.plot(sleep[::-1], label='Hours in Bed', color='5856d6')
    chart.ylabel('Sleep (hours)')
    chart.set_xticklabels(date[::-1])
    chart.bind_to('sleep_chart_div')


    return chart.json()

def get_food_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    nutrition = data[['Start','Finish','Carbohydrates (mg)','Protein (g)','Sugar (g)','Total Fat (g)','Caffeine (mg)','Dietary Calories (cal)','Resting Calories (kcal)','Dietary Water (L)']]
    nutrition = nutrition[::-1].head(1)
    nutrition.columns = ['Start', 'Finish','Carbohydrates','Proteins','Sugar','TotalFat','Caffeine','DietaryCalories','RestingCalories','DietaryWater']
    nutrition.Carbohydrates = nutrition.Carbohydrates * 0.001
    carbs = nutrition.Carbohydrates.tolist()
    proteins = nutrition.Proteins.tolist()
    fats = nutrition.TotalFat.tolist()
    dates = nutrition.Start.tolist()
    carbs = carbs[::-1]
    proteins = proteins[::-1]
    fats = fats[::-1]
    dates = dates[::-1]
    avgcarbs = np.average(carbs)
    avgproteins = np.average(proteins)
    avgfats = np.average(fats)

    #chart
    foodchart = c3.BarChart()
    foodchart.plot(carbs, label='Carbs (g)', color = '#ff3b30')
    foodchart.plot(proteins, label='Proteins (g)', color = '#4cd964')
    foodchart.plot(fats, label='Fats (g)', color = '#009dff')
    foodchart.stacked(True)
    foodchart.set_xticklabels(dates)
    foodchart.ylabel('Daily Intake (g)')
    foodchart.bind_to('food_chart_div')


    return foodchart.json()

def get_caloric_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    calories = data[['Start','Finish','Active Calories (kcal)','Resting Calories (kcal)','Dietary Calories (cal)']]
    calories = calories[::-1].head(1)
    calories.columns = ['Start','Finish','ActiveCalories','RestingCalories','DietaryCalories']
    calories.DietaryCalories = calories.DietaryCalories * 0.001
    calories['Net'] = calories['DietaryCalories'] - (calories['ActiveCalories'] + calories['RestingCalories'] )
    active = calories.ActiveCalories[::-1].tolist()
    resting = calories.RestingCalories[::-1].tolist()
    dietary = calories.DietaryCalories[::-1].tolist()
    net = calories.Net[::-1].tolist()
    dates = calories.Start[::-1].tolist()

    avgactive = np.average(active)
    avgresting = np.average(resting)
    avgdietary = np.average(dietary)
    avgnet = np.average(net)


    #chart
    caloricchart = c3.BarChart()
    caloricchart.plot(active, label='Active (kcal)', color='#ff9500')
    caloricchart.plot(resting, label='Resting (kcal)', color='#ffcc00')
    caloricchart.plot(dietary, label='Dietary (kcal)', color='#4cd964')
    caloricchart.plot(net, label='Net (kcal)', color='#ff3b30')
    caloricchart.set_xticklabels(dates)
    caloricchart.ylabel('Daily Energy (kcal)')
    caloricchart.bind_to('caloric_chart_div')


    return caloricchart.json()

def get_fitness_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    fitness = data[['Start','Cycling Distance (mi)','Distance (mi)','Steps (count)']]
    fitness = fitness[::-1].head(1)
    fitness.columns = ['Start', 'Cycling','WalkingandRunning','Steps']
    avgcycling = np.average(fitness.Cycling)
    avgwalkingandrunning = np.average(fitness.WalkingandRunning)

    #chart
    fitnesschart = c3.BarChart()
    fitnesschart.plot(fitness.Cycling[::-1], label='Cycling (mi)', color = '#007aff')
    fitnesschart.plot(fitness.WalkingandRunning[::-1], label='Walking and Running (mi)', color = '#ff9500')
    #chart.plot(fitness.Steps[::-1], label='Steps (counts )')
    fitnesschart.set_xticklabels(fitness.Start[::-1])
    fitnesschart.ylabel('Fitness')
    fitnesschart.bind_to('fitness_chart_div')


    return fitnesschart.json()

#yesterday
def get_yesterday_sleep_chart_json():

    #data
    sleepdata = pd.read_csv('data/Sleep Analysis.csv')
    sleep = sleepdata[['In bed start','In bed Finish','Minutes in bed','Minutes asleep']]
    sleep.columns = ['Inbedstart', 'InbedFinish','Minutesinbed','Minutesasleep']
    sleep = sleep[::-1][1:2]


    date = []
    for i in sleep.InbedFinish:
        date.append(i)

    minutesinbed = sleep.Minutesinbed
    sleep = []
    for i in minutesinbed:
        sleep.append(i / 60)

    avgsleep = np.average(sleep)


    avgsleep = np.average(sleep)
    #chart
    chart = c3.BarChart()
    chart.plot(sleep[::-1], label='Hours in Bed', color='5856d6')
    chart.ylabel('Sleep (hours)')
    chart.set_xticklabels(date[::-1])
    chart.bind_to('sleep_chart_div')


    return chart.json()

def get_yesterday_food_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    nutrition = data[['Start','Finish','Carbohydrates (mg)','Protein (g)','Sugar (g)','Total Fat (g)','Caffeine (mg)','Dietary Calories (cal)','Resting Calories (kcal)','Dietary Water (L)']]
    nutrition = nutrition[::-1][1:2]
    nutrition.columns = ['Start', 'Finish','Carbohydrates','Proteins','Sugar','TotalFat','Caffeine','DietaryCalories','RestingCalories','DietaryWater']
    nutrition.Carbohydrates = nutrition.Carbohydrates * 0.001
    carbs = nutrition.Carbohydrates.tolist()
    proteins = nutrition.Proteins.tolist()
    fats = nutrition.TotalFat.tolist()
    dates = nutrition.Start.tolist()
    carbs = carbs[::-1]
    proteins = proteins[::-1]
    fats = fats[::-1]
    dates = dates[::-1]
    avgcarbs = np.average(carbs)
    avgproteins = np.average(proteins)
    avgfats = np.average(fats)

    #chart
    foodchart = c3.BarChart()
    foodchart.plot(carbs, label='Carbs (g)', color = '#ff3b30')
    foodchart.plot(proteins, label='Proteins (g)', color = '#4cd964')
    foodchart.plot(fats, label='Fats (g)', color = '#009dff')
    foodchart.stacked(True)
    foodchart.set_xticklabels(dates)
    foodchart.ylabel('Daily Intake (g)')
    foodchart.bind_to('food_chart_div')


    return foodchart.json()

def get_yesterday_caloric_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    calories = data[['Start','Finish','Active Calories (kcal)','Resting Calories (kcal)','Dietary Calories (cal)']]
    calories = calories[::-1][1:2]
    calories.columns = ['Start','Finish','ActiveCalories','RestingCalories','DietaryCalories']
    calories.DietaryCalories = calories.DietaryCalories * 0.001
    calories['Net'] = calories['DietaryCalories'] - (calories['ActiveCalories'] + calories['RestingCalories'] )
    active = calories.ActiveCalories[::-1].tolist()
    resting = calories.RestingCalories[::-1].tolist()
    dietary = calories.DietaryCalories[::-1].tolist()
    net = calories.Net[::-1].tolist()
    dates = calories.Start[::-1].tolist()

    avgactive = np.average(active)
    avgresting = np.average(resting)
    avgdietary = np.average(dietary)
    avgnet = np.average(net)


    #chart
    caloricchart = c3.BarChart()
    caloricchart.plot(active, label='Active (kcal)', color='#ff9500')
    caloricchart.plot(resting, label='Resting (kcal)', color='#ffcc00')
    caloricchart.plot(dietary, label='Dietary (kcal)', color='#4cd964')
    caloricchart.plot(net, label='Net (kcal)', color='#ff3b30')
    caloricchart.set_xticklabels(dates)
    caloricchart.ylabel('Daily Energy (kcal)')
    caloricchart.bind_to('caloric_chart_div')


    return caloricchart.json()

def get_yesterday_fitness_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    fitness = data[['Start','Cycling Distance (mi)','Distance (mi)','Steps (count)']]
    fitness = fitness[::-1][1:2]
    fitness.columns = ['Start', 'Cycling','WalkingandRunning','Steps']
    avgcycling = np.average(fitness.Cycling)
    avgwalkingandrunning = np.average(fitness.WalkingandRunning)

    #chart
    fitnesschart = c3.BarChart()
    fitnesschart.plot(fitness.Cycling[::-1], label='Cycling (mi)', color = '#007aff')
    fitnesschart.plot(fitness.WalkingandRunning[::-1], label='Walking and Running (mi)', color = '#ff9500')
    #chart.plot(fitness.Steps[::-1], label='Steps (counts )')
    fitnesschart.set_xticklabels(fitness.Start[::-1])
    fitnesschart.ylabel('Fitness')
    fitnesschart.bind_to('fitness_chart_div')


    return fitnesschart.json()

#week
def get_week_sleep_chart_json():

    #data
    sleepdata = pd.read_csv('data/Sleep Analysis.csv')
    sleep = sleepdata[['In bed start','In bed Finish','Minutes in bed','Minutes asleep']]
    sleep.columns = ['Inbedstart', 'InbedFinish','Minutesinbed','Minutesasleep']
    sleep = sleep[::-1].head(7)

    date = []
    for i in sleep.InbedFinish:
        date.append(i)

    minutesinbed = sleep.Minutesinbed
    sleep = []
    for i in minutesinbed:
        sleep.append(i / 60)

    avgsleep = np.average(sleep)

    #chart
    chart = c3.BarChart()
    chart.plot(sleep[::-1], label='Hours in Bed', color='5856d6')
    chart.ylabel('Sleep (hours)')
    chart.set_xticklabels(date[::-1])
    chart.bind_to('sleep_chart_div')


    return chart.json()

def get_week_food_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    nutrition = data[['Start','Finish','Carbohydrates (mg)','Protein (g)','Sugar (g)','Total Fat (g)','Caffeine (mg)','Dietary Calories (cal)','Resting Calories (kcal)','Dietary Water (L)']]
    nutrition = nutrition[::-1].head(7)
    nutrition.columns = ['Start', 'Finish','Carbohydrates','Proteins','Sugar','TotalFat','Caffeine','DietaryCalories','RestingCalories','DietaryWater']
    nutrition.Carbohydrates = nutrition.Carbohydrates * 0.001
    carbs = nutrition.Carbohydrates.tolist()
    proteins = nutrition.Proteins.tolist()
    fats = nutrition.TotalFat.tolist()
    dates = nutrition.Start.tolist()
    carbs = carbs[::-1]
    proteins = proteins[::-1]
    fats = fats[::-1]
    dates = dates[::-1]
    avgcarbs = np.average(carbs)
    avgproteins = np.average(proteins)
    avgfats = np.average(fats)

    #chart
    foodchart = c3.BarChart()
    foodchart.plot(carbs, label='Carbs (g)', color = '#ff3b30')
    foodchart.plot(proteins, label='Proteins (g)', color = '#4cd964')
    foodchart.plot(fats, label='Fats (g)', color = '#009dff')
    foodchart.stacked(True)
    foodchart.set_xticklabels(dates)
    foodchart.ylabel('Daily Intake (g)')
    foodchart.bind_to('food_chart_div')


    return foodchart.json()

def get_week_caloric_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    calories = data[['Start','Finish','Active Calories (kcal)','Resting Calories (kcal)','Dietary Calories (cal)']]
    calories = calories[::-1].head(7)
    calories.columns = ['Start','Finish','ActiveCalories','RestingCalories','DietaryCalories']
    calories.DietaryCalories = calories.DietaryCalories * 0.001
    calories['Net'] = calories['DietaryCalories'] - (calories['ActiveCalories'] + calories['RestingCalories'] )
    active = calories.ActiveCalories[::-1].tolist()
    resting = calories.RestingCalories[::-1].tolist()
    dietary = calories.DietaryCalories[::-1].tolist()
    net = calories.Net[::-1].tolist()
    dates = calories.Start[::-1].tolist()

    avgactive = np.average(active)
    avgresting = np.average(resting)
    avgdietary = np.average(dietary)
    avgnet = np.average(net)


    #chart
    caloricchart = c3.BarChart()
    caloricchart.plot(active, label='Active (kcal)', color='#ff9500')
    caloricchart.plot(resting, label='Resting (kcal)', color='#ffcc00')
    caloricchart.plot(dietary, label='Dietary (kcal)', color='#4cd964')
    caloricchart.plot(net, label='Net (kcal)', color='#ff3b30')
    caloricchart.set_xticklabels(dates)
    caloricchart.ylabel('Daily Energy (kcal)')
    caloricchart.bind_to('caloric_chart_div')


    return caloricchart.json()

def get_week_fitness_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    fitness = data[['Start','Cycling Distance (mi)','Distance (mi)','Steps (count)']]
    fitness = fitness[::-1].head(7)
    fitness.columns = ['Start', 'Cycling','WalkingandRunning','Steps']
    avgcycling = np.average(fitness.Cycling)
    avgwalkingandrunning = np.average(fitness.WalkingandRunning)

    #chart
    fitnesschart = c3.BarChart()
    fitnesschart.plot(fitness.Cycling[::-1], label='Cycling (mi)', color = '#007aff')
    fitnesschart.plot(fitness.WalkingandRunning[::-1], label='Walking and Running (mi)', color = '#ff9500')
    #chart.plot(fitness.Steps[::-1], label='Steps (counts )')
    fitnesschart.set_xticklabels(fitness.Start[::-1])
    fitnesschart.ylabel('Fitness')
    fitnesschart.bind_to('fitness_chart_div')


    return fitnesschart.json()


#month
def get_month_sleep_chart_json():

    #data
    sleepdata = pd.read_csv('data/Sleep Analysis.csv')
    sleep = sleepdata[['In bed start','In bed Finish','Minutes in bed','Minutes asleep']]
    sleep.columns = ['Inbedstart', 'InbedFinish','Minutesinbed','Minutesasleep']
    sleep = sleep[::-1].head(30)

    date = []
    for i in sleep.InbedFinish:
        date.append(i)

    minutesinbed = sleep.Minutesinbed
    sleep = []
    for i in minutesinbed:
        sleep.append(i / 60)

    #chart
    chart = c3.BarChart()
    chart.plot(sleep[::-1], label='Hours in Bed', color='5856d6')
    chart.ylabel('Sleep (hours)')
    chart.set_xticklabels(date[::-1])
    chart.bind_to('sleep_chart_div')




    return chart.json()

def get_month_food_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    nutrition = data[['Start','Finish','Carbohydrates (mg)','Protein (g)','Sugar (g)','Total Fat (g)','Caffeine (mg)','Dietary Calories (cal)','Resting Calories (kcal)','Dietary Water (L)']]
    nutrition = nutrition[::-1].head(30)
    nutrition.columns = ['Start', 'Finish','Carbohydrates','Proteins','Sugar','TotalFat','Caffeine','DietaryCalories','RestingCalories','DietaryWater']
    nutrition.Carbohydrates = nutrition.Carbohydrates * 0.001
    carbs = nutrition.Carbohydrates.tolist()
    proteins = nutrition.Proteins.tolist()
    fats = nutrition.TotalFat.tolist()
    dates = nutrition.Start.tolist()
    carbs = carbs[::-1]
    proteins = proteins[::-1]
    fats = fats[::-1]
    dates = dates[::-1]


    #chart
    foodchart = c3.BarChart()
    foodchart.plot(carbs, label='Carbs (g)', color = '#ff3b30')
    foodchart.plot(proteins, label='Proteins (g)', color = '#4cd964')
    foodchart.plot(fats, label='Fats (g)', color = '#009dff')
    foodchart.stacked(True)
    foodchart.set_xticklabels(dates)
    foodchart.ylabel('Daily Intake (g)')
    foodchart.bind_to('food_chart_div')


    return foodchart.json()

def get_month_caloric_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    calories = data[['Start','Finish','Active Calories (kcal)','Resting Calories (kcal)','Dietary Calories (cal)']]
    calories = calories[::-1].head(30)
    calories.columns = ['Start','Finish','ActiveCalories','RestingCalories','DietaryCalories']
    calories.DietaryCalories = calories.DietaryCalories * 0.001
    calories['Net'] = calories['DietaryCalories'] - (calories['ActiveCalories'] + calories['RestingCalories'] )
    active = calories.ActiveCalories[::-1].tolist()
    resting = calories.RestingCalories[::-1].tolist()
    dietary = calories.DietaryCalories[::-1].tolist()
    net = calories.Net[::-1].tolist()
    dates = calories.Start[::-1].tolist()


    #chart
    caloricchart = c3.BarChart()
    caloricchart.plot(active, label='Active (kcal)', color='#ff9500')
    caloricchart.plot(resting, label='Resting (kcal)', color='#ffcc00')
    caloricchart.plot(dietary, label='Dietary (kcal)', color='#4cd964')
    caloricchart.plot(net, label='Net (kcal)', color='#ff3b30')
    caloricchart.set_xticklabels(dates)
    caloricchart.ylabel('Daily Energy (kcal)')
    caloricchart.bind_to('caloric_chart_div')


    return caloricchart.json()

def get_month_fitness_chart_json():

    #data
    data = pd.read_csv('data/Health Data.csv')
    fitness = data[['Start','Cycling Distance (mi)','Distance (mi)','Steps (count)']]
    fitness = fitness[::-1].head(30)
    fitness.columns = ['Start', 'Cycling','WalkingandRunning','Steps']


    #chart
    fitnesschart = c3.BarChart()
    fitnesschart.plot(fitness.Cycling[::-1], label='Cycling (mi)', color = '#007aff')
    fitnesschart.plot(fitness.WalkingandRunning[::-1], label='Walking and Running (mi)', color = '#ff9500')
    #chart.plot(fitness.Steps[::-1], label='Steps (counts )')
    fitnesschart.set_xticklabels(fitness.Start[::-1])
    fitnesschart.ylabel('Fitness')
    fitnesschart.bind_to('fitness_chart_div')


    return fitnesschart.json()

@app.route("/")
def today():

    sleepchart_json = get_sleep_chart_json()
    foodchart_json = get_food_chart_json()
    caloricchart_json = get_caloric_chart_json()
    fitnesschart_json = get_fitness_chart_json()

    #sleep
    sleepdata = pd.read_csv('data/Sleep Analysis.csv')
    sleep = sleepdata[['In bed start','In bed Finish','Minutes in bed','Minutes asleep']]
    sleep.columns = ['Inbedstart', 'InbedFinish','Minutesinbed','Minutesasleep']
    sleep = sleep[::-1].head(1)

    date = []
    for i in sleep.InbedFinish:
        date.append(i)

    minutesinbed = sleep.Minutesinbed
    sleep = []
    for i in minutesinbed:
        sleep.append(i / 60)

    avgsleep = np.average(sleep)

    #food
    data = pd.read_csv('data/Health Data.csv')
    nutrition = data[['Start','Finish','Carbohydrates (mg)','Protein (g)','Sugar (g)','Total Fat (g)','Caffeine (mg)','Dietary Calories (cal)','Resting Calories (kcal)','Dietary Water (L)']]
    nutrition = nutrition[::-1].head(1)
    nutrition.columns = ['Start', 'Finish','Carbohydrates','Proteins','Sugar','TotalFat','Caffeine','DietaryCalories','RestingCalories','DietaryWater']
    nutrition.Carbohydrates = nutrition.Carbohydrates * 0.001
    carbs = nutrition.Carbohydrates.tolist()
    proteins = nutrition.Proteins.tolist()
    fats = nutrition.TotalFat.tolist()
    dates = nutrition.Start.tolist()
    carbs = carbs[::-1]
    proteins = proteins[::-1]
    fats = fats[::-1]
    dates = dates[::-1]
    avgcarbs = np.average(carbs)
    avgproteins = np.average(proteins)
    avgfats = np.average(fats)

    #caloric
    data = pd.read_csv('data/Health Data.csv')
    calories = data[['Start','Finish','Active Calories (kcal)','Resting Calories (kcal)','Dietary Calories (cal)']]
    calories = calories[::-1].head(1)
    calories.columns = ['Start','Finish','ActiveCalories','RestingCalories','DietaryCalories']
    calories.DietaryCalories = calories.DietaryCalories * 0.001
    calories['Net'] = calories['DietaryCalories'] - (calories['ActiveCalories'] + calories['RestingCalories'] )
    active = calories.ActiveCalories[::-1].tolist()
    resting = calories.RestingCalories[::-1].tolist()
    dietary = calories.DietaryCalories[::-1].tolist()
    net = calories.Net[::-1].tolist()
    dates = calories.Start[::-1].tolist()

    avgactive = np.average(active)
    avgresting = np.average(resting)
    avgdietary = np.average(dietary)
    avgnet = np.average(net)

    #fitness
    data = pd.read_csv('data/Health Data.csv')
    fitness = data[['Start','Cycling Distance (mi)','Distance (mi)','Steps (count)']]
    fitness = fitness[::-1].head(1)
    fitness.columns = ['Start', 'Cycling','WalkingandRunning','Steps']
    avgcycling = np.average(fitness.Cycling)
    avgwalkingandrunning = np.average(fitness.WalkingandRunning)

    return render_template("today.html", sleepchart_json=sleepchart_json,foodchart_json=foodchart_json,caloricchart_json=caloricchart_json,fitnesschart_json=fitnesschart_json, avgsleep = avgsleep, avgcarbs = avgcarbs,avgproteins = avgcarbs, avgfats = avgfats, avgactive = avgactive, avgresting = avgresting, avgdietary = avgdietary, avgnet = avgnet, avgcycling = avgcycling, avgwalkingandrunning = avgwalkingandrunning)

@app.route("/yesterday")
def yesterday():

    sleepchart_json = get_yesterday_sleep_chart_json()
    foodchart_json = get_yesterday_food_chart_json()
    caloricchart_json = get_yesterday_caloric_chart_json()
    fitnesschart_json = get_yesterday_fitness_chart_json()

    #sleep
    sleepdata = pd.read_csv('data/Sleep Analysis.csv')
    sleep = sleepdata[['In bed start','In bed Finish','Minutes in bed','Minutes asleep']]
    sleep.columns = ['Inbedstart', 'InbedFinish','Minutesinbed','Minutesasleep']
    sleep = sleep[::-1][1:2]

    date = []
    for i in sleep.InbedFinish:
        date.append(i)

    minutesinbed = sleep.Minutesinbed
    sleep = []
    for i in minutesinbed:
        sleep.append(i / 60)

    avgsleep = np.average(sleep)

    #food
    data = pd.read_csv('data/Health Data.csv')
    nutrition = data[['Start','Finish','Carbohydrates (mg)','Protein (g)','Sugar (g)','Total Fat (g)','Caffeine (mg)','Dietary Calories (cal)','Resting Calories (kcal)','Dietary Water (L)']]
    nutrition = nutrition[::-1][1:2]
    nutrition.columns = ['Start', 'Finish','Carbohydrates','Proteins','Sugar','TotalFat','Caffeine','DietaryCalories','RestingCalories','DietaryWater']
    nutrition.Carbohydrates = nutrition.Carbohydrates * 0.001
    carbs = nutrition.Carbohydrates.tolist()
    proteins = nutrition.Proteins.tolist()
    fats = nutrition.TotalFat.tolist()
    dates = nutrition.Start.tolist()
    carbs = carbs[::-1]
    proteins = proteins[::-1]
    fats = fats[::-1]
    dates = dates[::-1]
    avgcarbs = np.average(carbs)
    avgproteins = np.average(proteins)
    avgfats = np.average(fats)

    #caloric
    data = pd.read_csv('data/Health Data.csv')
    calories = data[['Start','Finish','Active Calories (kcal)','Resting Calories (kcal)','Dietary Calories (cal)']]
    calories = calories[::-1][1:2]
    calories.columns = ['Start','Finish','ActiveCalories','RestingCalories','DietaryCalories']
    calories.DietaryCalories = calories.DietaryCalories * 0.001
    calories['Net'] = calories['DietaryCalories'] - (calories['ActiveCalories'] + calories['RestingCalories'] )
    active = calories.ActiveCalories[::-1].tolist()
    resting = calories.RestingCalories[::-1].tolist()
    dietary = calories.DietaryCalories[::-1].tolist()
    net = calories.Net[::-1].tolist()
    dates = calories.Start[::-1].tolist()

    avgactive = np.average(active)
    avgresting = np.average(resting)
    avgdietary = np.average(dietary)
    avgnet = np.average(net)

    #fitness
    data = pd.read_csv('data/Health Data.csv')
    fitness = data[['Start','Cycling Distance (mi)','Distance (mi)','Steps (count)']]
    fitness = fitness[::-1][1:2]
    fitness.columns = ['Start', 'Cycling','WalkingandRunning','Steps']
    avgcycling = np.average(fitness.Cycling)
    avgwalkingandrunning = np.average(fitness.WalkingandRunning)

    return render_template("yesterday.html", sleepchart_json=sleepchart_json,foodchart_json=foodchart_json,caloricchart_json=caloricchart_json,fitnesschart_json=fitnesschart_json, avgsleep = avgsleep, avgcarbs = avgcarbs,avgproteins = avgcarbs, avgfats = avgfats, avgactive = avgactive, avgresting = avgresting, avgdietary = avgdietary, avgnet = avgnet, avgcycling = avgcycling, avgwalkingandrunning = avgwalkingandrunning)

@app.route("/week")
def week():

    sleepchart_json = get_week_sleep_chart_json()
    foodchart_json = get_week_food_chart_json()
    caloricchart_json = get_week_caloric_chart_json()
    fitnesschart_json = get_week_fitness_chart_json()

    #sleep
    sleepdata = pd.read_csv('data/Sleep Analysis.csv')
    sleep = sleepdata[['In bed start','In bed Finish','Minutes in bed','Minutes asleep']]
    sleep.columns = ['Inbedstart', 'InbedFinish','Minutesinbed','Minutesasleep']
    sleep = sleep[::-1].head(7)

    date = []
    for i in sleep.InbedFinish:
        date.append(i)

    minutesinbed = sleep.Minutesinbed
    sleep = []
    for i in minutesinbed:
        sleep.append(i / 60)

    avgsleep = np.average(sleep)

    #food
    data = pd.read_csv('data/Health Data.csv')
    nutrition = data[['Start','Finish','Carbohydrates (mg)','Protein (g)','Sugar (g)','Total Fat (g)','Caffeine (mg)','Dietary Calories (cal)','Resting Calories (kcal)','Dietary Water (L)']]
    nutrition = nutrition[::-1].head(7)
    nutrition.columns = ['Start', 'Finish','Carbohydrates','Proteins','Sugar','TotalFat','Caffeine','DietaryCalories','RestingCalories','DietaryWater']
    nutrition.Carbohydrates = nutrition.Carbohydrates * 0.001
    carbs = nutrition.Carbohydrates.tolist()
    proteins = nutrition.Proteins.tolist()
    fats = nutrition.TotalFat.tolist()
    dates = nutrition.Start.tolist()
    carbs = carbs[::-1]
    proteins = proteins[::-1]
    fats = fats[::-1]
    dates = dates[::-1]
    avgcarbs = np.average(carbs)
    avgproteins = np.average(proteins)
    avgfats = np.average(fats)

    #caloric
    data = pd.read_csv('data/Health Data.csv')
    calories = data[['Start','Finish','Active Calories (kcal)','Resting Calories (kcal)','Dietary Calories (cal)']]
    calories = calories[::-1].head(7)
    calories.columns = ['Start','Finish','ActiveCalories','RestingCalories','DietaryCalories']
    calories.DietaryCalories = calories.DietaryCalories * 0.001
    calories['Net'] = calories['DietaryCalories'] - (calories['ActiveCalories'] + calories['RestingCalories'] )
    active = calories.ActiveCalories[::-1].tolist()
    resting = calories.RestingCalories[::-1].tolist()
    dietary = calories.DietaryCalories[::-1].tolist()
    net = calories.Net[::-1].tolist()
    dates = calories.Start[::-1].tolist()

    avgactive = np.average(active)
    avgresting = np.average(resting)
    avgdietary = np.average(dietary)
    avgnet = np.average(net)

    #fitness
    data = pd.read_csv('data/Health Data.csv')
    fitness = data[['Start','Cycling Distance (mi)','Distance (mi)','Steps (count)']]
    fitness = fitness[::-1].head(7)
    fitness.columns = ['Start', 'Cycling','WalkingandRunning','Steps']
    avgcycling = np.average(fitness.Cycling)
    avgwalkingandrunning = np.average(fitness.WalkingandRunning)

    return render_template("week.html", sleepchart_json=sleepchart_json,foodchart_json=foodchart_json,caloricchart_json=caloricchart_json,fitnesschart_json=fitnesschart_json, avgsleep = avgsleep, avgcarbs = avgcarbs,avgproteins = avgcarbs, avgfats = avgfats, avgactive = avgactive, avgresting = avgresting, avgdietary = avgdietary, avgnet = avgnet, avgcycling = avgcycling, avgwalkingandrunning = avgwalkingandrunning)

@app.route("/month")
def month():

    sleepchart_json = get_month_sleep_chart_json()
    foodchart_json = get_month_food_chart_json()
    caloricchart_json = get_month_caloric_chart_json()
    fitnesschart_json = get_month_fitness_chart_json()

    #sleep
    sleepdata = pd.read_csv('data/Sleep Analysis.csv')
    sleep = sleepdata[['In bed start','In bed Finish','Minutes in bed','Minutes asleep']]
    sleep.columns = ['Inbedstart', 'InbedFinish','Minutesinbed','Minutesasleep']
    sleep = sleep[::-1].head(30)

    date = []
    for i in sleep.InbedFinish:
        date.append(i)

    minutesinbed = sleep.Minutesinbed
    sleep = []
    for i in minutesinbed:
        sleep.append(i / 60)

    avgsleep = np.average(sleep)

    #food
    data = pd.read_csv('data/Health Data.csv')
    nutrition = data[['Start','Finish','Carbohydrates (mg)','Protein (g)','Sugar (g)','Total Fat (g)','Caffeine (mg)','Dietary Calories (cal)','Resting Calories (kcal)','Dietary Water (L)']]
    nutrition = nutrition[::-1].head(30)
    nutrition.columns = ['Start', 'Finish','Carbohydrates','Proteins','Sugar','TotalFat','Caffeine','DietaryCalories','RestingCalories','DietaryWater']
    nutrition.Carbohydrates = nutrition.Carbohydrates * 0.001
    carbs = nutrition.Carbohydrates.tolist()
    proteins = nutrition.Proteins.tolist()
    fats = nutrition.TotalFat.tolist()
    dates = nutrition.Start.tolist()
    carbs = carbs[::-1]
    proteins = proteins[::-1]
    fats = fats[::-1]
    dates = dates[::-1]
    avgcarbs = np.average(carbs)
    avgproteins = np.average(proteins)
    avgfats = np.average(fats)

    #caloric
    data = pd.read_csv('data/Health Data.csv')
    calories = data[['Start','Finish','Active Calories (kcal)','Resting Calories (kcal)','Dietary Calories (cal)']]
    calories = calories[::-1].head(30)
    calories.columns = ['Start','Finish','ActiveCalories','RestingCalories','DietaryCalories']
    calories.DietaryCalories = calories.DietaryCalories * 0.001
    calories['Net'] = calories['DietaryCalories'] - (calories['ActiveCalories'] + calories['RestingCalories'] )
    active = calories.ActiveCalories[::-1].tolist()
    resting = calories.RestingCalories[::-1].tolist()
    dietary = calories.DietaryCalories[::-1].tolist()
    net = calories.Net[::-1].tolist()
    dates = calories.Start[::-1].tolist()

    avgactive = np.average(active)
    avgresting = np.average(resting)
    avgdietary = np.average(dietary)
    avgnet = np.average(net)

    #fitness
    data = pd.read_csv('data/Health Data.csv')
    fitness = data[['Start','Cycling Distance (mi)','Distance (mi)','Steps (count)']]
    fitness = fitness[::-1].head(30)
    fitness.columns = ['Start', 'Cycling','WalkingandRunning','Steps']
    avgcycling = np.average(fitness.Cycling)
    avgwalkingandrunning = np.average(fitness.WalkingandRunning)

    return render_template("month.html", sleepchart_json=sleepchart_json,foodchart_json=foodchart_json,caloricchart_json=caloricchart_json,fitnesschart_json=fitnesschart_json, avgsleep = avgsleep, avgcarbs = avgcarbs,avgproteins = avgcarbs, avgfats = avgfats, avgactive = avgactive, avgresting = avgresting, avgdietary = avgdietary, avgnet = avgnet, avgcycling = avgcycling, avgwalkingandrunning = avgwalkingandrunning)

@app.route("/about")
def about():

    return render_template('about.html')


if __name__ == "__main__":
    app.run()
