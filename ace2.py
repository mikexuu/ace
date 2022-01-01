from collections import defaultdict
class Player:
    def __init__(self, name, position, is_ace):
        self.name = name
        self.position = position
        self.is_ace = is_ace

    
def calc_order(ranking):
    gives = defaultdict(list)
    processed = []
    aces = []
    ranking.sort(key = lambda x: x.position)

    print("RANKING:")
    for player in ranking:
        pos_str = "#" + str(player.position) + ": " + player.name
        if player.is_ace:
            pos_str += ", ACE"
        print(pos_str)

    for player in ranking:
        if not player.is_ace:
            if len(aces):
                gives[player].extend(aces)
            processed.append(player)
        else: # spade ace
            if len(processed):
                gives[player].extend(processed)
            aces.append(player)

    receives = defaultdict(list)
    for giver, receivers in gives.items():
        for receiver in receivers:
            receives[receiver].append(giver)
        if receives[receiver]:
            receives[receiver].sort(key = lambda x: x.position)
        
    print("\n\033[96mEXCHANGING LARGEST CARDS\033[0m\n")
    for player in ranking:
        if player in gives:
            card = 'card' if len(gives[player]) == 1 else 'cards'
            print(player.name + " starts pool of " + str(len(gives[player])) + " largest " + card + ":")
            verb = 'takes' if len(gives[player]) == 1 else 'take'
            print(', '.join(p.name for p in gives[player]) + " " + verb + " card from pool\n")
    
    print("\n\033[96mGIVING CARDS BACK\033[0m\n")
    for player in ranking:
        if player in receives:
            card = 'card' if len(gives[player]) == 1 else 'cards'
            print(player.name + " starts pool of any " + str(len(receives[player])) + card + ":")
            verb = 'takes' if len(gives[player]) == 1 else 'take'
            print(', '.join(p.name for p in receives[player]) + " " + verb + " card from pool\n")


    print("\n\033[92mSTART GAME!\033[0m\n")



ranking = [
    Player('XYZ', 1, False),
]

calc_order(ranking)

