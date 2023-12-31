# %%

import spacy

# %%

nlp = spacy.blank("en")

# %%

doc = nlp("Hello world!")

# %%

for token in doc:
    print(token.text)

# %%

token = doc[1]
print(token.text)

# %%

span = doc[1:3]
print(span.text)

# %%

doc2 = nlp("It costs $5.")

print("Index:   ", [token.i for token in doc2])
print("Text:    ", [token.text for token in doc2])

print("is_alpha:", [token.is_alpha for token in doc2])
print("is_punct:", [token.is_punct for token in doc2])
print("like_num:", [token.like_num for token in doc2])
