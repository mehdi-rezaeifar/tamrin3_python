import random
boys = {"ali", "reza", "yasin", "benyamin", "mehrdad", "sajjad", "aidin", "shahin"}
girls = {"sara", "zari", "neda", "homa", "eli", "goli", "mary", "mina"}
marriage = []

for i in range(len(boys)):
        random_boys = random.choice(tuple(boys))
        random_girls = random.choice(tuple(girls))
        marriage.append((random_boys,random_girls))
        
        print (marriage)
