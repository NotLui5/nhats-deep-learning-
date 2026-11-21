scores = [5, 4, 3, 4, 2]
for i in range(len(scores)):
    print(i, scores[i])


#  Δ s t = s t + 1 − s t 
scores = [5, 4, 4, 3, 2]
for i in range(len(scores) - 1):
    ## Why do we use len(scores) - 1?  
    ## For five observations, there are only four consecutive pairs.
    previous = scores[i]
    current = scores[i + 1]
    change = current - previous
    print(change)
 

# Reuse Week 2 Boolean logic
# None   
scores = [5, 4, None, 3, 2]
for i in range(len(scores) - 1):
    previous = scores[i]
    current = scores[i + 1]
    if previous is None or current is None:
        print("Change unavailable")
    else:
        change = current - previous
        print(change)
        

scores = [5, 4, 3]
total = 0
print("Start:           total = ", total)
for score in scores:
    total = total + score
    print("After ", score, ":         total =", total)


scores = [5, 4, None, 3, None]
total = 0
count = 0
for score in scores:
    if score is not None:
        total = total + score
        count = count + 1
mean = total / count
print(mean)


patients = [
    [5, 4, 4, 3, 3],
    [3, 3, None, 2, 1],
    [5, 5, 4, 4, None]
]

for patient_scores in patients:
    for score in patient_scores:
        print(score)
        
        
# Assignment part A: 
scores = [5, 4, None, 3, 2]
# Print every observation.
for score in scores:
    print(score)    
# Print the Python index of every observation.
for i in range(len(scores)):
    print(i, scores[i])    
# Count the number of valid observations.
val = 0
for i in range(len(scores)):
    if scores[i] is not None:
        val += 1 
print(val)
# Count the number of missing observations.
miss = 0
for i in range(len(scores)):
    if scores[i] is None:
        miss += 1 
print(miss)
# Calculate the sum of the valid observations.
sum_val = 0
for i in range(len(scores)):
    if scores[i] is not None:
        sum_val += scores[i] 
print(sum_val)
# Calculate the mean of the valid observations.
mean_val = sum_val / val
print(mean_val)
# Calculate every successive change for which both observations are available. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(len(scores) - 1):
    previous = scores[i]
    current = scores[i + 1]
    if current is None or previous is None:
        print(previous," -> ", current, "       change = unavailable")
    else:
        change = current - previous
        print(previous," -> ", current, "       change = ", change)
        

# Assignment part B:
# 5 fictional participants with 5 rounds each.
patients = [
    [5, 4, 4, None, 3],
    [3, 3, 2, 2, 1],
    [5, 5, 4, 4, None],
    [2, None, 2, 1, 1],
    [4, 4, 3, 3, 3]
]
# Print each participant's trajectory. !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Count valid observations for each participant.
# Count missing observations for each participant.
# Calculate valid successive changes for each participant.
pat_i = 1
val_obs = []
n_miss_obs = []
r = [[], [], [], [], []]
for patient in patients:
    all_obs = len(patients[pat_i-1])
    val = []
    succ = 0
    for _ in range(len(patient)):
        if patient[_] is not None:
            r[_].append(patient[_])
            val.append(patient[_])
    for i in range(len(patient)-1):        
        previous = patient[i]
        current = patient[i + 1]
        if current is None or previous is None:
            print(previous,"->", current, "       change = unavailable")
        else:
            succ += 1 # count succes sequential changes.
            change = current - previous
            if change == 0:
                print("Patient #",pat_i, "has equeal (", change,") score in round", i+1, "respect to round", i)
            elif change < 0:
                print("Patient #",pat_i, "has worst (", change,") score in round", i+1, "respect to round", i)
            elif change > 0:
                print("Patient #",pat_i, "has better (", change,") score in round", i+1, "respect to round", i)   
    val_obs.append(val)
    n_val_obs = len(val_obs[pat_i-1])
    print("Patient:", pat_i, "has", n_val_obs, "valid observations")
    
    miss_p = all_obs - n_val_obs #Compute missing according to all and valid
    n_miss_obs.append(miss_p)
    print("Patient", pat_i, "missing", miss_p, "obstervations")
    print("Patient", pat_i, "has valid successive changes :", succ)
    print("\n")            
    pat_i += 1 
    succ =0 
# Calculate the mean score for each round across participants.! 
for _ in range(len(patients[0])):
    # mean_r = sum(r[_]) / len(r[_])
    sum_round = 0
    for i in r[_]:
        sum_round += i
    mean_r = sum_round/len(r[_])
    val_r = len(r[_])
    miss_r = len(patients)
    r_i = _+1
    print(f"Round {r_i} valid = {val_r}, missing = {miss_r}, mean = {round(mean_r,2)}")
    # print("Round", _, "has mean", mean)



# Assigment part C
import random

random.seed(42)

patients = []

for participant in range(100):
    scores = []

    for round_number in range(5):
        if random.random() < 0.15:
            score = None
        else:
            score = random.randint(0, 5)
            if not not scores:
                if scores[round_number-1] is not None:
                    previouse = scores[round_number-1] 
                    current = score
                    change = abs(current-previous)
                    while change not in [0,1]:
                        score = random.randint(0, 5)
                        current = score
                        change = abs(current-previous)

                    
        scores.append(score)

    patients.append(scores)
    

# inspect
# patients[0:5]
for i in range(5):
    print(patients[i])
    
# Extension