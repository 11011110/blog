# Determine who has qualified from a partial climbing result
# Input is a set of lines with NAME SPEED BOULDER LEAD ranks,
# allowing the lead rank and some competitors to be missing.

maxscore = 20   # hardwire number of competitors

# =====================================
# Parse input
# =====================================

import sys
speed = {}
boulder = {}
lead = {}
order = {}
qualified = set()

for line in sys.stdin:
    words = line.split()
    name = words[0]
    speed[name] = int(words[1])
    boulder[name] = int(words[2])
    if len(words) > 3:
        lead[name] = int(words[3])

# =====================================
# Predict maximum possible ranks
# =====================================

def rank(competitor,scenario):
    """Ranking of competitor under the predicted lead outcomes"""
    if scenario == None:
        return 0    # Handle "stuck" case in makescenario
    threshold = speed[competitor]*boulder[competitor]*scenario[competitor]
    return len([x for x in speed
                if speed[x]*boulder[x]*scenario[x] <= threshold])

def makescenario(competitor,k,oldlead):
    """Build scenario in which k more competitors outrank competitor"""
    left = len(speed)-len(oldlead)
    newlead = {}
    for x in speed:
        if x not in oldlead:
            newlead[x] = maxscore
    newcomb = [(speed[x]*boulder[x],x) for x in newlead]
    newcomb.sort()
    newcomb = newcomb[:k]       # Top k competitors

    # Figure out how well they all need to do
    target = speed[competitor]*boulder[competitor]*(oldlead[competitor]+left)
    for c,x in newcomb:
        newlead[x] = min(newlead[x],target//c)

    # Resolve conflicts for who gets what rank
    leadnew = {}
    for x in newlead:
        y = newlead[x]
        while y > 0 and y in leadnew:
            y -= 1
        if y <= 0:
            return None # Unable to get k through
        leadnew[y] = x

    # Bump them up to slot in above n
    slot = oldlead[competitor] # where we think competitor will end up
    for i in range(maxscore+1):
        if i in leadnew:
            if i > slot:
                leadnew[slot] = leadnew[i]
                del leadnew[i]  # bump up
            slot += 1   # shift down
 
    # Merge with previous ordering
    sortednew = [(y,leadnew[y]) for y in leadnew]
    sortednew.sort()
    newlead = {x:y for y,x in sortednew}    # transpose
    for x in oldlead:
        nl = oldlead[x]
        for a,b in sortednew:
            if a <= nl:
                nl += 1
        newlead[x] = min(nl,maxscore)

    return newlead

def worstscenario(competitor):
    """Return lead ranking making competitor rank highest"""
    copylead = dict(lead)
    if competitor not in copylead:   # set up worst-possible rank
        copylead[competitor] = maxscore - len(speed) + len(lead) + 1    
    scenarios = (makescenario(competitor,k,copylead)
        for k in range(len(speed) - len(copylead) + 1))
    worst = max((rank(competitor,s),s) for s in scenarios)
    return worst[1]

# =====================================
# Process each competitor
# =====================================

for competitor in speed:
    worst = worstscenario(competitor)
    print("Worst rank for %s is %d" % (competitor,rank(competitor,worst)))
    print("Scenario: %s\n"%worst)
