username = input()
player_class = input()
xp = int(input())
wins = int(input())

is_veteran = xp >= 1000
has_enough_wins = wins >= 10

if is_veteran:
    badge = " *"
else:
    badge = ""

if has_enough_wins:
    ranked = "Eligible"
else:
    ranked = "Not yet"

if xp >= 5000:
    rank = "Legend"
elif xp >= 1500:
    rank = "Gold"
elif xp >= 500:
    rank = "Silver"
else:
    rank = "Bronze"

if player_class == "tank":
    perk = "+50 max health"
elif player_class == "healer":
    perk = "+20 percent healing"
elif player_class == "scout":
    perk = "+15% move speed"
else:
    perk = "no perk"

LINE = "============================"

print(LINE)
print("PLAYER CARD")
print(LINE)
print(f"User: {username}{badge}")
print(f"Class: {player_class}")
print(f"XP: {xp}")
print(f"Rank: {rank}")
print(f"Perk: {perk}")
print(f"Ranked: {ranked}")
print(LINE)