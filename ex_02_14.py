from nltk.corpus import wordnet as wn

def supergloss(syn):
    result = ""
    result = syn.name() + " : " + syn.definition() + "\n"
    for s in syn.hyponyms():
        result = result + s.name() + " : " + s.definition() + "\n"
    for d in syn.hypernyms():
        result = result + d.name() + " : " + d.definition() + "\n"
    return result

tes = supergloss(wn.synset('benthos.n.02'))
print(tes)