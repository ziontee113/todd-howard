# %%

import spacy

# %%

nlp = spacy.load("en_core_web_sm")

# %%

doc = nlp("She ate the pizza")

# Iterate over the tokens
for token in doc:
    # Print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)
