with open("data.csv") as f:
    males =0
    survived_males =0
    females=0
    survived_females =0
    next(f)
    for line in f:
        data = line.split(",")
        sex = data[5]
        survived = data[1]
        if sex == "male":
            males+=1
            if survived == "1":
                survived_males+=1
        else:
            females+=1
            if survived == "1":
                survived_females+=1
    print(f"Доля выживших среди мужчин: {survived_males/males*100:.2f}%")
    print(f"Доля выживших среди женщин: {survived_females/females*100:.2f}%")

    
            

