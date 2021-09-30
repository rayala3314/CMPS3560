#Expert System with improved forward chaining
#Modified by Raymundo Ayala 09/24/2021

#A set of propositional definite clauses
KB = [(["looks", "swims","quacks"], "duck"), (["barks"], "dog"), (["hoots","flies"], "owl")]

#Our set goal
q = "duck"

#Array indicating number of literals in premise 
#First tuple has 3 string literals, second tuple 1, so on..
count = [3, 1, 2]

#Array will hold literal that gets asserted
inferred = []

#List of known 'True' literals (facts)
agenda = ["barks", "hoots", "looks", "swims", "quacks"]

#Loop will pop from agenda and then check against our set goal
#if our set goal equals to whatever gets popped from the agenda 
#The goal is met
while agenda:
    p = agenda.pop(0)
    if p == q:
        print("Goal is entailed!")
        break

    #Literals from agenda get appended to our inferred array as long as they dont already exist there
    if p not in inferred:
        inferred.append(p)
    #Loop through out definite clauses(rules) and check our inferred literal against
    #our antecedents(can be multiple)
    #as long as we get a match we decrement our count array
        for c in range(0, len(KB)):
            premise, consequent = KB[c]
            if p in premise:
                count[c] -= 1
                #If we match all antecedents with literals from our inferred array
                #Rule fires so we append the consequent
                if count[c] == 0:
                    agenda.append( consequent )

