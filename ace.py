import pprint

def main(ranking):
    exchanges = {}
    processed = []
    aces = []
    ranking.sort(key = lambda x: x[1])
    for player in ranking:
        exchanges[player[0]] = []
        if not player[2]: # not spade ace
            if len(aces):
                exchanges[player[0]].extend(aces)
            processed.append(player[0])
        else: # spade ace
            exchanges[player[0]].extend(processed)
            #exchanges[player[0]].extend(aces)
            aces.append(player[0])

    return exchanges



ranking = []

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(main(ranking))
