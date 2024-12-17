animals = [
    {"id": 1, "name": "Leão"},
    {"id": 2, "name": "Macaco"},
    {"id": 3, "name": "Touro"},
    {"id": 4, "name": "Urso"},
    {"id": 5, "name": "Avestruz"},
    {"id": 6, "name": "Jacaré"},
    {"id": 7, "name": "Tigre"},
    {"id": 8, "name": "Cachorro"},
    {"id": 9, "name": "Elefante"},
    {"id": 10, "name": "Bode"},
    {"id": 11, "name": "Gato"},
    {"id": 12, "name": "Porto"}
]

award_types = [
    # Low awards (positions 1-3)
    {"position": 10, "type": "low", "multiplier": 3},
    {"position": 11, "type": "low", "multiplier": 4}, 
    {"position": 12, "type": "low", "multiplier": 5},

    # Medium awards (positions 4-6)
    {"position": 6, "type": "medium", "multiplier": 3},
    {"position": 7, "type": "medium", "multiplier": 4},
    {"position": 8, "type": "medium", "multiplier": 5},

    # Top awards (positions 7-9)
    {"position": 2, "type": "top", "multiplier": 3},
    {"position": 3, "type": "top", "multiplier": 4},
    {"position": 4, "type": "top", "multiplier": 5},

    # Medium with bonus awards (positions 10-12)
    {"position": 6, "type": "medium_bonus", "multiplier": 6},
    {"position": 7, "type": "medium_bonus", "multiplier": 8},
    {"position": 8, "type": "medium_bonus", "multiplier": 10}
]

award_order = [
    {"position": 1, "name": "low"},
    {"position": 2, "name": "medium_bonus"},
    {"position": 3, "name": "low"},
    {"position": 4, "name": "medium"},
    {"position": 5, "name": "top"},
    {"position": 6, "name": "medium_bonus"},
    {"position": 7, "name": "top"}
]

bets = [
    {"user_id": 1, "animal_id": 3, "value": 45},
    {"user_id": 2, "animal_id": 1, "value": 75},
    {"user_id": 3, "animal_id": 7, "value": 30},
    {"user_id": 4, "animal_id": 2, "value": 90},
    {"user_id": 5, "animal_id": 12, "value": 25},
    {"user_id": 6, "animal_id": 4, "value": 60},
    {"user_id": 7, "animal_id": 9, "value": 85},
    {"user_id": 8, "animal_id": 5, "value": 15},
    {"user_id": 9, "animal_id": 8, "value": 95},
    {"user_id": 10, "animal_id": 6, "value": 40},
    {"user_id": 11, "animal_id": 10, "value": 70},
    {"user_id": 12, "animal_id": 11, "value": 20},
    {"user_id": 13, "animal_id": 3, "value": 55},
    {"user_id": 14, "animal_id": 7, "value": 80},
    {"user_id": 15, "animal_id": 1, "value": 35},
    {"user_id": 16, "animal_id": 9, "value": 65},
    {"user_id": 17, "animal_id": 4, "value": 50},
    {"user_id": 18, "animal_id": 12, "value": 85},
    {"user_id": 19, "animal_id": 2, "value": 30},
    {"user_id": 20, "animal_id": 8, "value": 75},
    {"user_id": 21, "animal_id": 5, "value": 45},
    {"user_id": 22, "animal_id": 10, "value": 90},
    {"user_id": 23, "animal_id": 6, "value": 25},
    {"user_id": 24, "animal_id": 11, "value": 70},
    {"user_id": 25, "animal_id": 3, "value": 40},
    {"user_id": 26, "animal_id": 7, "value": 85},
    {"user_id": 27, "animal_id": 1, "value": 20},
    {"user_id": 28, "animal_id": 9, "value": 60},
    {"user_id": 29, "animal_id": 4, "value": 95},
    {"user_id": 30, "animal_id": 12, "value": 35},
    {"user_id": 31, "animal_id": 2, "value": 80},
    {"user_id": 32, "animal_id": 8, "value": 50},
    {"user_id": 33, "animal_id": 5, "value": 75},
    {"user_id": 34, "animal_id": 10, "value": 30},
    {"user_id": 35, "animal_id": 6, "value": 65},
    {"user_id": 36, "animal_id": 11, "value": 45},
    {"user_id": 37, "animal_id": 3, "value": 90},
    {"user_id": 38, "animal_id": 7, "value": 25},
    {"user_id": 39, "animal_id": 1, "value": 70},
    {"user_id": 40, "animal_id": 9, "value": 40},
    # Second bets for 10 users
    {"user_id": 1, "animal_id": 8, "value": 55},
    {"user_id": 5, "animal_id": 4, "value": 80},
    {"user_id": 10, "animal_id": 2, "value": 35},
    {"user_id": 15, "animal_id": 11, "value": 60},
    {"user_id": 20, "animal_id": 6, "value": 95},
    {"user_id": 25, "animal_id": 10, "value": 30},
    {"user_id": 30, "animal_id": 5, "value": 75},
    {"user_id": 35, "animal_id": 1, "value": 45},
    {"user_id": 38, "animal_id": 12, "value": 85},
    {"user_id": 40, "animal_id": 7, "value": 50}
]

def process_bets(bets):
    # Initialize dictionary to store animal stats
    animal_stats = {}
    
    # Process each bet
    for bet in bets:
        animal_id = bet["animal_id"]
        value = bet["value"]
        
        if animal_id not in animal_stats:
            animal_stats[animal_id] = {"users": set(), "total_amount": 0}
        
        animal_stats[animal_id]["users"].add(bet["user_id"])
        animal_stats[animal_id]["total_amount"] += value
    
    # Convert to list and add number of users
    results = []
    for animal_id, stats in animal_stats.items():
        results.append({
            "animal_id": animal_id,
            "num_users": len(stats["users"]),
            "total_amount": stats["total_amount"]
        })
    
    # Sort by total amount received
    results.sort(key=lambda x: x["total_amount"], reverse=True)
    
    return results

# Process and print results
results = process_bets(bets)
for animal in results:
    print(f"Animal {animal['animal_id']}: {animal['num_users']} users, total amount: {animal['total_amount']}")
