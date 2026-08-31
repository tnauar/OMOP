import pandas as pd
import re

def count_occurrence(text: str, pattern: str)-> int:
    """Counts the occurences of the pattern "rokot".
        
    Args:
        text: Contents of the free_text column. In this case a string.
        pattern: A string containing the pattern to search.  
            
    Returns: Length of the findings list.
    """
    findings = []
    findings = re.findall(pattern, str(text), flags=re.IGNORECASE)
    return len(findings)

def main():
    
    file = "./mining_data/omop_common.csv"
    df = pd.read_csv(file)

    """ Search pattern. We are looking for a raw string rokot.""" 
    pattern = r"rokot"

    """ We go through each row of the free_text column."""
    rokot_match = []
    for text in df["free_text"]:
        rokot_match.append(count_occurrence(text, pattern))

    df["rokot_match"] = rokot_match

    """ The total amount of hits for the whole file."""
    total_count = df["rokot_match"].sum()

    """ The row count of hits."""
    rows_with_match = (df["rokot_match"] > 0).sum()

    print(f"Total hits: {total_count}")
    print(f"Rows hit: {rows_with_match}")

if __name__ == "__main__":
    main()