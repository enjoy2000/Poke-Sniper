# -*- coding: utf-8 -*-
import sys

from pokemongo_bot import inventory
from pokemongo_bot.human_behaviour import sleep
from pokemongo_bot.item_list import Item
from pokemongo_bot.base_task import BaseTask


class CalculateIv(BaseTask):

    SUPPORTED_TASK_API_VERSION = 1
    run = 1
    def initialize(self):
        self.api = self.bot.api

    def work(self):
        pokemons_max_cp = {"Mewtwo": 4144, "Dragonite": 3500, "Mew": 3299, "Moltres": 3240, "Zapdos": 3114, "Snorlax": 3112, "Arcanine": 2983, "Lapras": 2980, "Articuno": 2978, "Exeggutor": 2955, "Vaporeon": 2816, "Gyarados": 2688, "Flareon": 2643, "Charizard": 2602, "Muk": 2602, "Slowbro": 2597, "Machamp": 2594, "Venusaur": 2580, "Blastoise": 2542, "Victreebel": 2530, "Poliwrath": 2505, "Vileplume": 2492, "Nidoqueen": 2485, "Nidoking": 2475, "Clefable": 2397, "Golduck": 2386, "Golem": 2303, "Magmar": 2265, "Weezing": 2250, "Rhydon": 2243, "Omastar": 2233, "Tentacruel": 2220, "Rapidash": 2199, "Ninetales": 2188, "Hypno": 2184, "Starmie": 2182, "Wigglytuff": 2177, "Aerodactyl": 2165, "Dewgong": 2145, "Jolteon": 2140, "Kabutops": 2130, "Pinsir": 2121, "Electabuzz": 2119, "Pidgeot": 2091, "Gengar": 2078, "Scyther": 2073, "Cloyster": 2052, "Kangaskhan": 2043, "Seaking": 2043, "Raichu": 2028, "Golbat": 1921, "Venomoth": 1890, "Magneton": 1879, "Primeape": 1864, "Tauros": 1844, "Dodrio": 1836, "Kingler": 1823, "Alakazam": 1813, "Sandslash": 1810, "Arbok": 1767, "Machoke": 1760, "Parasect": 1747, "Dragonair": 1747, "Fearow": 1746, "Tangela": 1739, "Weepinbell": 1723, "Jynx": 1716, "Seadra": 1713, "Porygon": 1691, "Gloom": 1689, "Marowak": 1656, "Electrode": 1646, "Ivysaur": 1632, "Persian": 1631,
            "Lickitung": 1626, "Wartortle": 1582, "Charmeleon": 1557, "Ponyta": 1516, "Hitmonchan": 1516, "MrMime": 1494, "Hitmonlee": 1492, "Butterfree": 1454, "Raticate": 1444, "Beedrill": 1439, "Graveler": 1433, "Nidorina": 1404, "Haunter": 1380, "Nidorino": 1372, "Poliwhirl": 1340, "Growlithe": 1335, "Grimer": 1284, "Farfetchd": 1263, "Pidgeotto": 1223, "Slowpoke": 1218, "Clefairy": 1200, "Rhyhorn": 1182, "Dugtrio": 1168, "Koffing": 1151, "Oddish": 1148, "Kadabra": 1131, "Omanyte": 1119, "Bellsprout": 1117, "Psyduck": 1109, "Seel": 1107, "Kabuto": 1104, "Exeggcute": 1099, "Machop": 1089, "Eevee": 1077, "Drowzee": 1075, "Bulbasaur": 1071, "Venonat": 1029, "Squirtle": 1008, "Cubone": 1006, "Dratini": 983, "Goldeen": 965, "Charmander": 955, "Staryu": 937, "Ditto": 919, "Jigglypuff": 917, "Paras": 916, "Tentacool": 905, "Magnemite": 890, "Pikachu": 887, "Mankey": 878, "Nidoran♀": 876, "Onix": 857, "Doduo": 855, "Geodude": 849, "Nidoran♂": 843, "Voltorb": 839, "Vulpix": 831, "Ekans": 824, "Shellder": 822, "Gastly": 804, "Sandshrew": 798, "Poliwag": 795, "Horsea": 794, "Krabby": 792, "Meowth": 756, "Spearow": 686, "Pidgey": 679, "Chansey": 675, "Zubat": 642, "Abra": 600, "Rattata": 581, "Kakuna": 485, "Metapod": 477, "Diglett": 456, "Weedle": 449, "Caterpie": 443, "Magikarp": 262}

        if not self._should_run():
            return

        pokemons = []
        for pokemon in inventory.pokemons().all():
            pokemon.max_cp = pokemons_max_cp[pokemon.name.capitalize()] * pokemon.iv
            pokemons.append(pokemon)
 
        pokemons.sort(key=lambda x: (x.max_cp), reverse=True)

        for pokemon in pokemons:
            print('{} [iv: {}] [max_cp: {}]'.format(
                pokemon.name, pokemon.iv, pokemon.max_cp))

        self.run = 0


    def _should_run(self):
        return self.run
