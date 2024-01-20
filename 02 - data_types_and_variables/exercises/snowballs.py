snowballs_made = int(input())

best_snowball = 0
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0


for snowball in range(snowballs_made):
    weight = int(input())
    time_for_making = int(input())
    quality = int(input())

    current_score = int((weight / time_for_making) ** quality)

    if current_score > best_snowball:
        best_snowball = current_score
        best_snowball_weight = weight
        best_snowball_time = time_for_making
        best_snowball_quality = quality

print(f"{best_snowball_weight} : {best_snowball_time} = {best_snowball} ({best_snowball_quality})")