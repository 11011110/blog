def accept(threshold,strengthFilter=None,topicFilter=None):
    """Return percentage of accepted papers for threshold.
    A threshold of x means: always accept papers whose score
    is larger than x, always reject papers whose score is
    smaller than floor(x), and reject a (x-floor(x)) fraction
    of the papers whose score equals floor(x)."""
    submitted = accepted = 0.0
    for strength in range(5):
        for topic in range(3):
            for arbitrariness in range(3):
                if strengthFilter in (None,strength):
                    if topicFilter in (None,topic):
                        submitted += 1
                        if strength+topic+arbitrariness > threshold:
                            accepted += 1
                        elif strength+topic+arbitrariness == int(threshold):
                            accepted += 1 + int(threshold) - threshold
    return 100.0*accepted/submitted

strengths=["very weak","weak","mediocre","strong","very strong"]
topics=["speculative","conventionable","fashionable"]

def report(threshold):
    """Print report of what happens for the given threshold."""
    print "Threshold %0.2f, acceptance rate %0.1f%%" % \
        (threshold,accept(threshold))
    for strength in (4,3,2,1,0):
        for topic in (2,1,0):
            print "%0.1f%% of %s %s papers accepted" % \
                (accept(threshold,strength,topic),
                strengths[strength],topics[topic])
    total = 0.0
    speculative = 0.0
    for topic in (2,1,0):
        a = accept(threshold,None,topic)
        total += a
        if topic == 0:
            speculative += a
    print "Fraction of accepted papers that are speculative: %0.1f" % \
        (100.0 * speculative / total)
    print

def findthresh(acceptratio):
    lo,hi = 0.0,10.0
    for i in range(20):
        mid = (lo+hi)/2
        midacc = accept(mid)
        if midacc > acceptratio:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2

for percent in (10,25,35,45,50,65):
    report(findthresh(percent))
