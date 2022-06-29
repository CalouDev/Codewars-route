# This kata is bugged and, with the randomized decks, there is an error from the patch script

def winner(deck_steve, deck_josh):
    steve_score, josh_score = 0, 0
    
    print(deck_steve, deck_josh)
    
    cards = {
        "A": "14",
        "K": "13",
        "Q": "12",
        "J": "11",
        "T": "10"
    }
    
    for i in range(len(deck_steve)):
        deck_steve[i] = cards.get(deck_steve[i], deck_steve[i])
        deck_josh[i] = cards.get(deck_josh[i], deck_josh[i])
        
        if int(deck_steve[i]) > int(deck_josh[i]):
            steve_score += 1
        elif int(deck_steve[i]) < int(deck_josh[i]):
            josh_score += 1
            
    if steve_score > josh_score:
        return "Steve wins {} to {}".format(steve_score, josh_score)
    elif steve_score < josh_score:
        return "Josh wins {} to {}".format(josh_score, steve_score)
    
    return "Tie"
