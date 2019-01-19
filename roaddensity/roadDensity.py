

def calculate(locations,bins=100,times=[]):
    if times == []: times = [i for i in range(0,len(locations))]
    binWidth = max(max(locations)) / bins
    output = []
    for slice in locations: # each slice is a slice of time
        current = []
        for i in range(0,bins):
            current.append(sum([1 for j in slice if abs((i * binWidth) - j) < binWidth]))
        output.append(current)
    return [times, output]
