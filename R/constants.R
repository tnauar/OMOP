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
  "Potilas kertoo oireita: %1$s ja %2$s. Ei kuumetta. Kotihoitoon %3$sa tarvittaessa.",
  "Vastaanotolla kertoo, että %1$s jatkunut %4$s. Potilas on ottanut itse %3$sa.",
  "Potilaalla esiintyy %1$s ja yleinen %2$s. Ei viitettä akuuttiin infektioon.",
  "Päivystyksessä %1$s pahentunut viime yön aikana. Annettu %3$sa ja seurattu vointia.",
  "Puhelimitse kuvaa oireina: %1$s ja %2$s, jotka ovat jatkuneet %4$s. Ohjattu seuraamaan oiretta ja käyttämään %3$sa.",
  "Potilas saapuu kontrolliin. Aiempi %1$s selvästi helpottanut, mutta %2$s edelleen ajoittain.",
  "Sairaalahoidon aikana todettu %1$s ja %2$s. Lääkitys tarkistettu, %3$s aloitettu. Kotiutuu %4$s päästä",
  "Vapaa teksti: %1$s ei ole potilaan raportissa, mutta %2$s on. Käyttää %3$sa säännöllisesti.",
  "Oirekuva on todennäköisesti %5$s. Ei allergioita tiedossa. Kotiutuu tänään.",
  "Potilas kieltää, että %1$s olisi oire, mutta kertoo, että %2$s kestänyt %4$s. Ei kuumetta eikä yleistilan laskua.",
  "Ei viitettä, että kyseessä olisi %1$s tai %2$s. Potilas ei käytä %3$sa enää.",
  "Kieltää rintakivun. Hengenahdistusta ei esiinny levossa. Potilasta on auttanut %3$s.",
  "Ei pahoinvointia, ei oksentelua. %1$s on kuitenkin jatkunut lievänä %4$s.",
  "Potilas ei ole huomannut, että %1$s olisi pahentunut. Lopetettu %3$sa sivuvaikutusten vuoksi.",
  "Mahdollinen %5$s alkuvaiheessa. %1$s saattaa liittyä rasitukseen.",
  "Oirekuva on ehkä %5$s, mutta varmaa diagnoosia ei vielä ole.",
  "Voisi olla %5$s; %1$s on epäspesifi ja tilannetta seurataan.",
  "Syy oireeseen %1$s epäselvä, mahdollisesti lääkitykseen liittyvä. Tauotettu %3$s toistaiseksi.",
  "Epäilty %5$s, koska %1$s ja %2$s ovat lieviä ja vaihtelevia."
)

TEMPLATES_VACC <- c(
  "Potilas %1$s %2$s rokotteena %3$s-rokote. Ei allergista reaktiota.",
  "Potilas pelkäsi rokotusta. Annettu %3$s-rokote %2$s.",
  "Potilas saanut aikaisemmin allergisia oireita rokotteista. %1$s %2$s %3$s-rokote. Lievää ihottumaa rokotuksen jälkeen.",
  "Kieltäytyi rokotteesta %3$s-rokote. Piti tutkimusnäyttöjä riittämättöminä.",
  "Annettu %3$s-rokote nenäsuihkeena.",
  "Potilas %1$s %2$s %3$s-rokotteella.",
  "Potilaalle annettu pistos %3$s-rokotetta lihakseen. Lihas kipeytyi pistoksen jälkeen.",
  "Suihkutettu %3$s-rokote nenään."
)