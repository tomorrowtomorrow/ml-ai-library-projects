import random
def simulate_bayes(population, prevalence, sensitivity, specificity):
    """
    Simulates disease testing in a population.

    Parameters:
    population (int): Number of individuals to simulate.
    prevalence (float): Probability that a person has the disease (0–1).
    sensitivity (float): P(Test positive | Disease), accuracy of positive test.
    specificity (float): P(Test negative | No disease), accuracy of negative test.

    Returns:
    tuple:
        theory (float): Theoretical P(Disease | Positive).
        empirical (float): Empirical P(Disease | Positive) from simulation.
    """
    if population<=0 or (prevalence or sensitivity or specificity)>1 or (prevalence or sensitivity or specificity)<0:
        raise ValueError('invalid input for args!!!')
    Positive=0
    True_positive=0

    #our input informations 

    for i in range(population):
        has_disease=(random.randint() < prevalence) 
        if has_disease:
          test_pos=(random.randint() < sensitivity) 
        
        else:
          test_pos= random.random() < (1 - specificity)  #false negetive : patient is not sick but test is positive 
          
        if test_pos:
           positive+=1
           if has_disease:
              True_positive+=1

    #now we are findin chance of test is positive and is it actual ill or not P(D∣P)
    empirical_result=True_positive/positive
    #but we could find this by using theorms p(d|p)=(p(T|D)P(D))/P(T)   
    #CAUSE it is equal = (p(T|D)P(D))/(p(T|D)P(D))+(p(T|D^c)P(D^c))
    theory=(sensitivity*prevalence)/((sensitivity*prevalence)+(1-specificity)*(1-prevalence))
    return theory,empirical_result    

 
     

