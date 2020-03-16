def simulateGenderRatio(samplesize):
    child = 'G'
    population = [child, ]
    for i in range(1, samplesize):
        child = 'B'+child
        population.append(child)
    print(population)
    return population

def probability(population):
    prob = []
    for fam in population:
        prob.append((fam.count('G')*fam.count('B'))/len(fam)**2)
    print(prob)
    return prob
def estimateGenderRatio(prob , population):
    estimate = []
    populationprob = list(zip(population , prob))
    for fam,prob in populationprob:
        print(fam,prob)
        estimate.append(fam.count('B')*prob)
    print(estimate)
    res = (sum(estimate)/len(estimate))
    return res


pop = simulateGenderRatio(10)
est = probability(pop)
avg = estimateGenderRatio(est , pop )
print(avg)
#probability(['G', 'BG', 'BBG', 'BBBG', 'BBBBG', 'BBBBBG', 'BBBBBBG', 'BBBBBBBG', 'BBBBBBBBG', 'BBBBBBBBBG'])

# Conclusion : The odds of one being girl os 50% and boy is 50% . The 1 Girl Policy is ieffective, because on AVG every family contributes 1 girl and 1 boy. The Gender ratio is close to 0.56. Which means there are
# equal number of girls and boys.