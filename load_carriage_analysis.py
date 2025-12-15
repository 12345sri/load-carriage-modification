# Load Carriage Modification - Simple Data Analysis
# Author: Sriporna Biswas
# Academic Project - Chandigarh University

data = [
    {"weight": 20, "force": 30, "energy": 120, "efficiency": 80},
    {"weight": 25, "force": 38, "energy": 150, "efficiency": 78},
    {"weight": 30, "force": 45, "energy": 180, "efficiency": 72},
    {"weight": 35, "force": 55, "energy": 210, "efficiency": 65},
    {"weight": 40, "force": 65, "energy": 250, "efficiency": 60},
]

for item in data:
    if item["weight"] <= 30:
        item["cluster"] = "Low Load"
    else:
        item["cluster"] = "High Load"

with open("clustered_output.csv", "w") as file:
    file.write("weight,force,energy,efficiency,cluster\n")
    for item in data:
        file.write(
            f'{item["weight"]},{item["force"]},{item["energy"]},'
            f'{item["efficiency"]},{item["cluster"]}\n'
        )

print("Load carriage analysis completed successfully.")
