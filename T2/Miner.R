df <- read.csv("./mining_data/omop_common.csv", stringsAsFactors = FALSE)

# Find occurrences in free_text fields.
count_occurrence <- function(text) {
  matches <- gregexpr("rokot", text, ignore.case = TRUE, perl = TRUE)[[1]]
  if (matches[1] == -1) return(0)
  length(matches)
}

df$rokot_match <- sapply(df$free_text, count_occurrence)

# Total amount of hits.
total_count <- sum(df$rokot_match)
# Rows with hits
rows_with_match <- sum(df$rokot_match > 0)

cat("Total hits:", total_count, "\n")
cat("Rows with hits:", rows_with_match, "\n")