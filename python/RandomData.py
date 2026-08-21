
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

    VISIT_TYPES = [
        ("Perusterveydenhuollon vastaanotto", 9202),
        ("Erikoissairaanhoidon poliklinikkakäynti", 9202),
        ("Päivystyskäynti", 9203),
        ("Sairaalan vuodeosastohoito", 9201),
        ("Puhelinkonsultaatio", 44818519),
        ("Uusintakäynti", 9202),
        ("Kotiutusarvio", 9201),
    ]


    VACCINATION_KEYWORD = [
        ("rokotettu"),
        ("rokotetaan")
    ]

    VACCINATION_PLACE = [
        ("ihoon"),
        ("lihakseen"),
        ("nenään"),
        ("suuhun"),
        ("ihon alle")
    ]

    VACCINATION_TYPE = [
        ("rotavirus"),
        ("MPR"),
        ("HPV"),
        ("pneumokokki"),
        ("influenssa"),
        ("korona"),
        ("viitos"),
        ("jäykkäkouristustehoste")
    ]

    SYMPTOM_BANK = [
        ("päänsärky"),
        ("pahoinvointi"),
        ("huimaus"),
        ("väsymys"),
        ("kuume"),
        ("yskä"),
        ("kurkkukipu"),
        ("hengenahdistus"),
        ("ripuli"),
        ("vatsakipu"),
        ("selkäkipu"),
        ("unettomuus"),
        ("nilkkaturvotus"),
        ("ihottuma"),
        ("rintakipu")
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
        ("ylähengitystieinfektio"),
        ("niskajumi"),
        ("migreeni"),
        ("gastroenteriitti"),
        ("selkäkipu"),
        ("virtsatieinfektio"),
        ("astman pahenemisvaihe")
    ]

    TEMPLATES = [
    "Potilas kertoo oireita: {sym1} ja {sym2}. Ei kuumetta. Kotihoitoon {med1}a tarvittaessa.",
    "Vastaanotolla kertoo, että {sym1} jatkunut {duration}. Potilas on ottanut itse {med1}a.",
    "Potilaalla esiintyy {sym1} ja yleinen {sym1}. Ei viitettä akuuttiin infektioon.",
    "Päivystyksessä {sym1} pahentunut viime yön aikana. Annettu {med1}a ja seurattu vointia.",
    "Puhelimitse kuvaa oireina: {sym1} ja {sym2}, jotka ovat jatkuneet {duration}. Ohjattu seuraamaan oiretta ja käyttämään {med1}a.",
    "Potilas saapuu kontrolliin. Aiempi {sym1} selvästi helpottanut, mutta {sym2} edelleen ajoittain.",
    "Sairaalahoidon aikana todettu {sym1} ja {sym2}. Lääkitys tarkistettu, {med1} aloitettu. Kotiutuu {duration} päästä",
    "Vapaa teksti: {sym1} ei ole potilaan raportissa, mutta {sym2} on. Käyttää {med1}a säännöllisesti.",
    "Oirekuva on todennäköisesti {condition}. Ei allergioita tiedossa. Kotiutuu tänään.",

    # Negation
    "Potilas kieltää, että {sym1} olisi oire, mutta kertoo, että {sym2} kestänyt {duration}. Ei kuumetta eikä yleistilan laskua.",
    "Ei viitettä, että kyseessä olisi {sym1} tai {sym2}. Potilas ei käytä {med1}a enää.",
    "Kieltää rintakivun. Hengenahdistusta ei esiinny levossa. Potilasta on auttanut {med1}.",
    "Ei pahoinvointia, ei oksentelua. {sym1} on kuitenkin jatkunut lievänä {duration}.",
    "Potilas ei ole huomannut, että {sym1} olisi pahentunut. Lopetettu {med1} sivuvaikutusten vuoksi.",

    # Uncertainty / speculation
    "Mahdollinen {condition} alkuvaiheessa. {sym1} saattaa liittyä rasitukseen.",
    "Oirekuva on ehkä {condition}, mutta varmaa diagnoosia ei vielä ole.",
    "Voisi olla {condition}; {sym1} on epäspesifi ja tilannetta seurataan.",
    "Syy oireeseen {sym1} epäselvä, mahdollisesti lääkitykseen liittyvä. Tauotettu {med1} toistaiseksi.",
    "Epäilty {condition}, koska {sym2} ja {sym1} ovat lieviä ja vaihtelevia.",
    ]

    TEMPLATES_VACC = [
    "Potilas {vacc_keyword} {vacc_place} rokotteena {vacc_type}-rokote. Ei allergista reaktiota.",
    "Potilas pelkäsi rokotusta. Annettu {vacc_type}-rokote {vacc_place}.",
    "Potilas saanut aikaisemmin allergisia oireita rokotteista. {vacc_keyword} {vacc_place} {vacc_type}-rokote. Lievää ihottumaa rokotuksen jälkeen.",
    "Kieltäytyi rokotteesta {vacc_type}-rokote. Piti tutkimusnäyttöjä riittämättöminä."
    "Annettu {vacc_type}-rokote nenäsuihkeena."
    "Potilas {vacc_keyword} {vacc_place} sekä {vacc_type} että {vacc_type}-rokotteella."
    "Potilaalle annettu pistos {vacc_type}-rokotetta lihakseen. Lihas kipeytyi pistoksen jälkeen."
    "Suihkutettu {vacc_type}-rokote nenään."
    ]