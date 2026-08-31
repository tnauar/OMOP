UPDATE omop.rokotustapataulukko
SET sourceConceptClass =  'VACCROUTEfi Level 0',
    sourceDomain = 'Route',
    sourceValidStartDate = TO_CHAR(sourceValidStartDate::date, 'DD.MM.YYYY')::date,
    sourceValidEndDate = TO_CHAR(sourceValidEndDate::date, 'DD.MM.YYYY')::date,
    LastModified = TO_CHAR(LastModified::date, 'DD.MM.YYYY')::date;

UPDATE omop.rokotustapataulukko
SET  sourceName = 'Intradermal',
     sourceConceptId =2023000101
WHERE  shortName = 'Ihoon';

UPDATE omop.rokotustapataulukko
SET  sourceName = 'Intramuscular',
     sourceConceptId =2023000102
WHERE  shortName = 'Lihakseen';

UPDATE omop.rokotustapataulukko
SET  sourceName = 'Intranasal',
     sourceConceptId =2023000103
WHERE  shortName = 'Nenään';

UPDATE omop.rokotustapataulukko
SET  sourceName = 'Other method of administration',
     sourceConceptId =2023000104
WHERE  sourceName_fi = 'Muu antotapa';

UPDATE omop.rokotustapataulukko
SET  sourceName = 'Oral',
     sourceConceptId =2023000105
WHERE  sourceName_fi = 'Suun kautta';

UPDATE omop.rokotustapataulukko
SET  sourceName = 'Subcutaneous',
     sourceConceptId =2023000106
WHERE  sourceName_fi = 'Ihonalaisesti'; 
