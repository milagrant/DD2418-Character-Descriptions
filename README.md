# Generating Character Descriptions from Novels
Project in Language Engineering Course DD2418 at KTH

## Run Experiment
1. Install NLTK `pip install nltk`
1. Pull this repo
2. Download a plain text English language novel from [Project Gutenberg](https://www.gutenberg.org/).
3. Remove overhead `head -n -370 "file.txt" | tail -n +40`
4. Run `python FindCharacters.py "file.txt"`

Note: The parameters COMMON_ADJECTIVES and CHARACTERS need to be adjusted to reproduce the results in the report.
