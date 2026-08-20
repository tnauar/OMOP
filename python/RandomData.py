
class RandomData():

    """This class contains the data from which the random data is generated."""

    FIRST_NAMES_MALE = [
        "Matti", "Pekka", "Kai", "Antti", "Seppo", "Juha", "Mikko", "Lari",
        "Timo", "Jari", "Emil", "Petri", "Hannu", "Aleksi", "Teppo", "Markku",
        "Ali", "Mohammed", "Sumit", "Veikko"
    ]

    FIRST_NAMES_FEMALE = [
        "Maija", "Pirkko", "Kaisa", "Anna", "Sari", "Jaana", "Mervi", "Laura",
        "Tiina", "Joanna", "Emilia", "Pirjo", "Hanna", "Aleksandra", "Noora", "Maarit",
        "Aisha", "Fatima", "Johanna", "Vianna"
    ]

    LAST_NAMES = [
        "Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Mäkelä", "Hämäläinen",
        "Laine", "Heikkinen", "Koskinen", "Järvinen", "Lehtonen", "Salminen",
        "Eriksson", "Pandey", "Khan", "Hassan"
    ]

    VACCINATION_KEYWORD = [
        ("rokotus"),
        ("rokotettu"),
        ("rokotetaan"),
        ("piikitys"),
        ("piikitetty"),
        ("piikitetään"),
        ("sumutus"),
        ("sumuttettu"),
        ("sumutetaan"),
        ("suihkutus"),
        ("suihkutettu"),
        ("suihkutetaan"),
        ("tippa"),
        ("tippana")
    ]

    VACCINATION_PLACE = [
        ("ihoon", "ihonsisäisesti"),
        ("lihakseen", "lihaksensisäisesti"),
        ("nenään", "nenänsisäisesti"),
        ("suuhun", "suun kautta"),
        ("ihon alle"), ("ihon alaisesti")
    ]

    VACCINATION_TYPE = [
        ("rotavirus"),
        ("MPR"),
        ("HPV"),
        ("pneumokokki"),
        ("influenssa"),
        ("korona"),
        ("viitosrokote"),
        ("jäykkäkouristustehoste")
    ]

    SYMPTOM_BANK = [
        ("päänsärky", "päänsärkyä"),
        ("pahoinvointi", "pahoinvointia"),
        ("huimaus", "huimausta"),
        ("väsymys", "väsymystä"),
        ("kuume", "kuumetta"),
        ("yskä", "yskää"),
        ("kurkkukipu", "kurkkukipua"),
        ("hengenahdistus", "hengenahdistusta"),
        ("ripuli", "ripulia"),
        ("vatsakipu", "vatsakipua"),
        ("selkäkipu", "selkäkipua"),
        ("unettomuus", "unettomuutta"),
        ("nilkkaturvotus", "nilkkaturvotusta"),
        ("ihottuma", "ihottumaa"),
        ("rintakipu", "rintakipua"),
    ]

    MEDICATIONS = [
        "parasetamoli", "ibuprofeeni", "omepratsoli", "amoksisilliini",
        "metformiini", "amlodipiini", "atorvastatiini", "setiritsiini",
        "salbutamoli", "furosemidi", "bisoprololi", "doksisykliini"
    ]

    DURATIONS = [
        "2 päivää", "3 päivää", "viikon", "muutaman päivän", "noin viikon",
        "2 viikkoa", "kuukauden", "useita päiviä"
    ]

    CONDITIONS = [
        ("ylähengitystieinfektioo", "ylähengitystieinfektion"),
        ("niskajumii", "niskajumin"),
        ("migreenii", "migreenin"),
        ("gastroenteriittii", "gastroenteriitin"),
        ("selkäkipuu", "selkäkivun"),
        ("virtsatieinfektioo", "virtsatieinfektion"),
        ("astman pahenemisvaiheesee", "astman pahenemisvaiheen"),
    ]

    TEMPLATES = [
    "Potilas kertoo {sym1}sta ja {sym2}sta. Ei kuumetta. Kotihoitoon {med1} tarvittaessa.",
    "Vastaanotolla {sym1} jatkunut {duration}. Potilas aloittanut itse {med1}.",
    "Potilaalla esiintyy {sym1} ja yleistä {sym1}. Ei viitettä akuuttiin infektioon.",
    "Päivystyksessä {sym1} pahentunut viime yön aikana. Annettu {med1} ja seurattu vointia.",
    "Puhelimitse kuvaa {sym1} {duration}. Ohjattu seuraamaan oiretta ja käyttämään {med1}.",
    "Potilas saapuu kontrolliin. Aiempi {sym1} selvästi helpottanut, mutta {sym2} edelleen ajoittain.",
    "Sairaalahoidon aikana todettu {sym1} ja {sym2}. Lääkitys tarkistettu, {med1} aloitettu.",
    "Vapaa teksti: potilas ei raportoi {sym1}, mutta mainitsee {sym2}. Käyttää {med1} säännöllisesti.",
    "Oirekuva sopii todennäköisesti {condition}n. Ei allergioita tiedossa. Kotiutuu tänään.",

    # Negation
    "Potilas kieltää {sym1}n, mutta kertoo {sym2}sta. Ei kuumetta eikä yleistilan laskua.",
    "Ei viitettä {sym1}n tai {sym2}n. Potilas ei käytä {med1} enää.",
    "Kieltää rintakivun. Hengenahdistusta ei esiinny levossa. Parasetamoli on auttanut.",
    "Ei pahoinvointia, ei oksentelua. {sym1} on kuitenkin jatkunut lievänä.",
    "Potilas ei ole huomannut {sym1}n pahenemista. {med1} lopetettu sivuvaikutusten vuoksi.",

    # Uncertainty / speculation
    "Mahdollinen {condition}n alkuvaihe. {sym1} saattaa liittyä rasitukseen.",
    "Oirekuva viittaa ehkä {condition}n, mutta varmaa diagnoosia ei vielä ole.",
    "Voisi sopia {condition}n; {sym1} on epäspesifi ja tilannetta seurataan.",
    "Syy {sym1}n epäselvä, mahdollisesti lääkitykseen liittyvä. {med1} tauotettu toistaiseksi.",
    "Epäily {condition}sta, koska {sym2} ja {sym1} ovat lieviä ja vaihtelevia.",
]