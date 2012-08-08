# -*- coding: UTF-8 -*-
class Card:
    def __init__(self, card):
        self.name = card['_id']
        self.mana = self.Mana(card['mana'])
        self.color = card['color']
        self.cmc = card['cmc']
        self.set = card['set'][0]['name']
        self.type = card['type']
        self.subtype = card['subtype']
        self.abilities = self.Abilities(card['abilities'])
        self.power = card['power']
        self.toughness = card['toughness']
        self.artist = card['set'][0]['artist']
        self.flavor = card['set'][0]['flavor']
        self.loyalty = card['loyalty']
        self.rarity = card['set'][0]['rarity']
        self.legality = None
        self.tags = None
        self.back = None
        self.pair = None
        self.test = None
    
    def Abilities(self, card):
        ability = []
        if card is not None:
            for ab in card:
                for a in ab.encode('utf-8', 'replace').split('£'):
                    temp = a.replace('#_#_', '<i>')
                    temp = temp.replace('_#_#', '</i>')
                    temp = temp.replace('#_', '<i>')
                    temp = temp.replace('_#', '</i>')
                    ability.append(temp.decode('utf-8', 'ignore'))
        else:
            ability.append("")

        return ability

    def Mana(self, card):
        mana = []
        if card is not None:
            for c in card:
                if c != "CL":
                    val = card[c]
                    while val != 0:
                        mana.append(c)
                        val -= 1
                else:
                    mana.append(card[c])
        #mana.reverse()
        return mana

    def assignPair(self, card):
        self.pair = card
        card.pair = self