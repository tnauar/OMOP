# This program will write a 500 row rds data file that contains random
# imaginary health care data.

# This sources contains the constants from which the data is created.
source("./constants.R")

# Definition of functions start here.
generate_note <- function(
                          symptoms,
                          condition,
                          duration,
                          medication,
                          template
                          ){
    note <- sprintf(
                    template,
                    symptoms[[1]],
                    symptoms[[2]],
                    medication,
                    duration,
                    condition
                    )
}

generate_note_vacc <- function(
                          vacc_keyword,
                          vacc_place,
                          vacc_type,
                          template
){
  note <- sprintf(
                  template,
                  vacc_keyword,
                  vacc_place,
                  vacc_type
                  )
}
# Main program starts here.
# We will loop 500 times and for each round we will generate the random
# data and write it to memory.
random_data_results <- data.frame(
  gender = character(),
  firstname = character(),
  lastname = character(),
  condition = character(),
  duration = character(),
  education = character(),
  healthcare_plan = character(),
  medication = character(),
  nationality = character(),
  symptom_1 = character(),
  symptom_2 = character(),
  free_text = character(),
  visit_index = numeric(),
  person_id = numeric(),
  age = numeric(),
  visit_id = numeric(),
  visit_type = character(),
  visit_date = as.Date(character())
  
  
)

for (i in 1:500) {
  
  gender <- sample(
    c("M","N","T"),
    1,
    prob = c(0.5, 0.49, 0.01)
  )
  
  if (gender == "M") {
    firstname = sample(
      FIRST_NAMES_MALE,
      1
    )
  }  
  else if (gender == "N") {
    firstname = sample(
      FIRST_NAMES_FEMALE,
      1
    )
  }
  # For trans or no gender we choose randomly from both names.
  else {
    firstname = sample(
      c(FIRST_NAMES_MALE, FIRST_NAMES_FEMALE),
      1
    )
  }
  
  lastname <- sample(
    LAST_NAMES,
    1
  )
  
  visit_index <- sample(
    26000:32000, 
    1
  )
  
  person_id <- sample(
    10000:15000, 
    1
  )
  
  age <- sample(
    1:100,
    1
  )
  
  visit <- sample(
    VISIT_TYPES,
    1
  )
  
  visit_type <- visit[[1]][[1]]
  visit_id <- visit[[1]][[2]]
  
  today = Sys.Date()
  random_date <- sample(
    1:365,
    1
  )
  visit_date <- today-random_date
  
  condition = sample(
    CONDITIONS,
    1
  )
  
  duration = sample(
    DURATIONS,
    1
  )
  
  education = sample(
    EDUCATION,
    1
  )
  
  healthcare_plan = sample(
    HEALTHCARE_PLAN,
    1,
    prob = c(0.2, 0.2, 0.15, 0.45)
  )
  
  medication = sample(
    MEDICATIONS,
    1
  )
  
  nationality = sample(
    NATIONALITY,
    1,
    prob = c(0.90, 0.03, 0.02, 0.02, 0.01, 0.01, 0.01)
  )
  # Choosing two creates a symptom vector.
  symptoms = sample(
    SYMPTOM_BANK,
    2
  )
  
  # Vaccinations are separated from other templates.
  # They not as common.
  vaccination = sample(
    c("True", "False"),
    1,
    prob = c(0.2, 0.8)
  )
  
  if (vaccination == "True") {
    template = sample(
      TEMPLATES_VACC,
      1
    )
    vacc_keyword = sample(
      VACCINATION_KEYWORD,
      1
    )
    vacc_place = sample(
      VACCINATION_PLACE,
      1
    )
    vacc_type = sample(
      VACCINATION_TYPE,
      1
    )
    result_note <-generate_note_vacc(
                                vacc_keyword,
                                vacc_place,
                                vacc_type,
                                template)
  }
  else {
    template = sample(
      TEMPLATES,
      1
    )
    result_note <- generate_note(symptoms,
                                 condition,
                                 duration,
                                 medication,
                                 template)
  }
  
  row <-data.frame(  
                  gender,
                  firstname,
                  lastname,
                  condition,
                  duration,
                  education,
                  healthcare_plan,
                  medication,
                  nationality,
                  symptoms[[1]],
                  symptoms[[2]],
                  result_note,
                  visit_index,
                  person_id,
                  age,
                  visit_id,
                  visit_type,
                  visit_date
  )
  random_data_results <- rbind(random_data_results, row)
  
# End of for-loop  
}

# Finally we will write the data from the memory to an RDS file.

saveRDS(random_data_results, "results.rds")
csv_data <- readRDS("results.rds")
write.csv(random_data_results, "results.csv")


