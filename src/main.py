from fastapi import FastAPI

app = FastAPI()

# dicts {plant -> value}
count = {}
CO2_absorption = {}
O2_production = {}
rarity = {}


def compute_score(my_trees, my_flowers, my_bushes, my_houseplants):
    tree_scores = [
        count[x] * CO2_absorption[x] * O2_production[x] / rarity[x] for x in my_trees
    ]
    flower_scores = [
        count[x] * CO2_absorption[x] * O2_production[x] / rarity[x] for x in my_flowers
    ]
    bush_scores = [
        count[x] * CO2_absorption[x] * O2_production[x] / rarity[x] for x in my_bushes
    ]
    houseplant_scores = [
        count[x] * CO2_absorption[x] * O2_production[x] / rarity[x]
        for x in my_houseplants
    ]

    tree_scores_sum = sum(tree_scores)
    flower_scores_sum = sum(flower_scores)
    bush_scores_sum = sum(bush_scores)
    houseplant_scores_sum = sum(houseplant_scores)

    all_scores_sum = (
        tree_scores_sum + flower_scores_sum + bush_scores_sum + houseplant_scores_sum
    )

    coefficients = [1] * 4

    frequency = [0] * 4

    frequency[0] = tree_scores_sum * (1 - (tree_scores_sum / all_scores_sum))
    frequency[1] = flower_scores_sum * (1 - (flower_scores_sum / all_scores_sum))
    frequency[2] = bush_scores_sum * (1 - (bush_scores_sum / all_scores_sum))
    frequency[3] = houseplant_scores_sum * (
        1 - (houseplant_scores_sum / all_scores_sum)
    )

    total_score = 0

    for i in range(4):
        total_score += coefficients[i] * (1 - frequency[i])

    return total_score


@app.get("/")
def main():
    return {"success": True}


from .database.connector import connect_with_connector_auto_iam_authn


def create_app():
    app = FastAPI()
