import random

participant_id = "synthetic_001"
age = 78
score_2021 = 5
score_2022 = 4

change = score_2022 - score_2021

n_participants = 50

for i in range(n_participants):
    print(f"Participant {i + 1}:")
    print(f"ID: synthetic_00{i+1}")
    print(f"Age: {random.randint(60, 90)}")
    score_2021 = random.randint(1, 10)
    score_2022 = random.randint(1, 10)
    change = score_2022 - score_2021
    print(f"Clock score change: {change}")
    print("")





print(f"Number of participants: {n_participants}")
    
# print(f"Participant: {participant_id}")
# print(f"Age: {age}")
# print(f"Clock score change: {change}")
