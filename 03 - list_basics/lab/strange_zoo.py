body_arangement = []

for _ in range(3):
    body_part = input()
    body_arangement.append(body_part)

body_arangement[0],body_arangement[2] = body_arangement[2],body_arangement[0]

print(body_arangement)
