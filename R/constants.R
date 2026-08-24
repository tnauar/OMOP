FIRST_NAMES_MALE <- c(
  "Matti", "Pekka", "Kai", "Antti", "Seppo", "Juha", "Mikko", "Lari",
  "Timo", "Jari", "Emil", "Petri", "Hannu", "Aleksi", "Teppo", "Markku",
  "Ali", "Mohammed", "Sumit", "Veikko"
)

FIRST_NAMES_FEMALE <- c(
  "Maija", "Pirkko", "Kaisa", "Anna", "Sari", "Jaana", "Mervi", "Laura",
  "Tiina", "Joanna", "Emilia", "Pirjo", "Hanna", "Aleksandra", "Noora", "Maarit",
  "Aisha", "Fatima", "Johanna", "Vianna"
)

LAST_NAMES <- c(
  "Korhonen", "Virtanen", "Mäkinen", "Nieminen", "Mäkelä", "Hämäläinen",
  "Laine", "Heikkinen", "Koskinen", "Järvinen", "Lehtonen", "Salminen",
  "Eriksson", "Pandey", "Khan", "Hassan"
)

VISIT_TYPES <- list(
  list("Perusterveydenhuollon vastaanotto", 9202),
  list("Erikoissairaanhoidon poliklinikkakäynti", 9202),
  list("Päivystyskäynti", 9203),
  list("Sairaalan vuodeosastohoito", 9201),
  list("Puhelinkonsultaatio", 44818519),
  list("Uusintakäynti", 9202),
  list("Kotiutusarvio", 9201)
)

NATIONALITY <- c(
  "Suomi",
  "Viro",
  "Venäjä",
  "Ruotsi",
  "Irak",
  "Somalia",
  "Afganistan"
)

HEALTHCARE_PLAN <- c(
  "työterveys",
  "vakuutus",
  "yths",
  "julkinen"
)

EDUCATION <- c(
  "ylempi korkeakoulututkinto",
  "alempikorkeakoulututkinto",
  "ammattitutkinto",
  "opiskelijä",
  "kouluttamaton"
)

VACCINATION_KEYWORD <- c(
  "rokotettu",
  "rokotetaan"
)

VACCINATION_PLACE <- c(
  "ihoon",
  "lihakseen",
  "nenään",
  "suuhun",
  "ihon alle"
)

VACCINATION_TYPE <- c(
  "rotavirus",
  "MPR",
  "HPV",
  "pneumokokki",
  "influenssa",
  "korona",
  "viitos",
  "jäykkäkouristustehoste"
)

SYMPTOM_BANK <- c(
  "päänsärky",
  "pahoinvointi",
  "huimaus",
  "väsymys",
  "kuume",
  "yskä",
  "kurkkukipu",
  "hengenahdistus",
  "ripuli",
  "vatsakipu",
  "selkäkipu",
  "unettomuus",
  "nilkkaturvotus",
  "ihottuma",
  "rintakipu"
)

MEDICATIONS <- c(
  "parasetamoli", "ibuprofeeni", "omepratsoli", "amoksisilliini",
  "metformiini", "amlodipiini", "atorvastatiini", "setiritsiini",
  "salbutamoli", "furosemidi", "bisoprololi", "doksisykliini"
)

DURATIONS <- c(
  "2 päivää", "3 päivää", "viikon", "muutaman päivän", "noin viikon",
  "2 viikkoa", "kuukauden", "useita päiviä"
)

CONDITIONS <- c(
  "ylähengitystieinfektio",
  "niskajumi",
  "migreeni",
  "gastroenteriitti",
  "selkäkipu",
  "virtsatieinfektio",
  "astman pahenemisvaihe"
)

TEMPLATES <- c(
  "Potilas kertoo oireita: %s ja %s. Ei kuumetta. Kotihoitoon %sa tarvittaessa.",
  "Vastaanotolla kertoo, että %s jatkunut %s. Potilas on ottanut itse %sa.",
  "Potilaalla esiintyy %s ja yleinen %s. Ei viitettä akuuttiin infektioon.",
  "Päivystyksessä %s pahentunut viime yön aikana. Annettu %sa ja seurattu vointia.",
  "Puhelimitse kuvaa oireina: %s ja %s, jotka ovat jatkuneet %s. Ohjattu seuraamaan oiretta ja käyttämään %sa.",
  "Potilas saapuu kontrolliin. Aiempi %s selvästi helpottanut, mutta %s edelleen ajoittain.",
  "Sairaalahoidon aikana todettu %s ja %s. Lääkitys tarkistettu, %s aloitettu. Kotiutuu %s päästä",
  "Vapaa teksti: %s ei ole potilaan raportissa, mutta %s on. Käyttää %sa säännöllisesti.",
  "Oirekuva on todennäköisesti %s. Ei allergioita tiedossa. Kotiutuu tänään.",
  "Potilas kieltää, että %s olisi oire, mutta kertoo, että %s kestänyt %s. Ei kuumetta eikä yleistilan laskua.",
  "Ei viitettä, että kyseessä olisi %s tai %s. Potilas ei käytä %sa enää.",
  "Kieltää rintakivun. Hengenahdistusta ei esiinny levossa. Potilasta on auttanut %s.",
  "Ei pahoinvointia, ei oksentelua. %s on kuitenkin jatkunut lievänä %s.",
  "Potilas ei ole huomannut, että %s olisi pahentunut. Lopetettu %sa sivuvaikutusten vuoksi.",
  "Mahdollinen %s alkuvaiheessa. %s saattaa liittyä rasitukseen.",
  "Oirekuva on ehkä %s, mutta varmaa diagnoosia ei vielä ole.",
  "Voisi olla %s; %s on epäspesifi ja tilannetta seurataan.",
  "Syy oireeseen %s epäselvä, mahdollisesti lääkitykseen liittyvä. Tauotettu %s toistaiseksi.",
  "Epäilty %s, koska %s ja %s ovat lieviä ja vaihtelevia."
)

TEMPLATES_VACC <- c(
  "Potilas %s %s rokotteena %s-rokote. Ei allergista reaktiota.",
  "Potilas pelkäsi rokotusta. Annettu %s-rokote %s.",
  "Potilas saanut aikaisemmin allergisia oireita rokotteista. %s %s %s-rokote. Lievää ihottumaa rokotuksen jälkeen.",
  "Kieltäytyi rokotteesta %s-rokote. Piti tutkimusnäyttöjä riittämättöminä.",
  "Annettu %s-rokote nenäsuihkeena.",
  "Potilas %s %s sekä %s että %s-rokotteella.",
  "Potilaalle annettu pistos %s-rokotetta lihakseen. Lihas kipeytyi pistoksen jälkeen.",
  "Suihkutettu %s-rokote nenään."
)






