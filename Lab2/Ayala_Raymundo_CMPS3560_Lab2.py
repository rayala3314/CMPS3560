#Expert system implementing forward chaining

#A set of known facts mocking a database
DB = ["looks", "swims", "quacks"]
#A set of rules otherwise known as the knowledge base
KB = [(["looks", "swims", "quacks"], "duck"), (["barks"], "dog"), 
(["hoots", "flies"], "owl")]            

#counter variable used to denote cycle
#and variable to keep track of any changes in Database
count = 1                               
changes = True

while changes:
    changes = False

    print( "\nStarting Iteration: " + str(count) )
    print( "------------------------------------")

# Used to loop over the set of tuples in the knowledge base    
    for p in KB:
        # Grab values of first tuple                    
        antecedent, consequent = p       

        print( "Consider a rule where: " + str(antecedent))
        print("Implies: " + str(consequent))

        satisfied = True
        # Loop over different antecedents if more than one in tuple
        for q in antecedent:
        # check if the antecedent already exists in Database             
            if q not in DB:             
                satisfied = False
        # Check if consequent is not in the database given that the antecedent is
        if satisfied and consequent not in DB: 
            # If consequent not in the database add it to the database and keep track of change
            DB.append(consequent)
            changes = True
            print( "Antecedent is in DB, consquent is implied, DB is now: ")
            print(DB)
        elif satisfied and consequent in DB:
            print("Consequent is implied, but was already in DB")
        else:
            print("Consequent is not implied")
        print("\n")
    #Update count used to denote a cycle 
    #This means we went through all the rules once already and entering another cycle
    count = count + 1
print("No more changes. DB is: ")
print(DB)
