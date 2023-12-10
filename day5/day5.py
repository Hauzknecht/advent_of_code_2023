file = open("test_input.txt", "r")
segments = file.read().split("\n\n")
seeds = [ int(x) for x in segments[0].split(":")[1].strip().split(" ")]
mapping = []
for segment in segments[1:]:
    segment = segment.split("\n")
    tmp = []
    for line in segment[1:]:
        tmp1 = tuple(int(x) for x in line.split(" "))
        tmp.append(tmp1)
    mapping.append(tmp)

for map_ in mapping:
    print(map_)

def src_dest(seed):
    for _map in mapping:
        for _range in _map:
            if seed >= _range[1] and seed < _range[1]+_range[2]:
                seed = _range[0] + seed - _range[1]
                break
    return seed

destinations = []
for seed in seeds:
    destinations.append(src_dest(seed))
print("Minimal destination is", min(destinations))

r = []
for i in range(0,len(seeds),2):
    r.append((seeds[i],seeds[i]+seeds[i+1]-1))
print(r)
"""
def get_ranges(range_,map_):
    r = []
    for ran in map_:
        if range_[0] >= map_[1] and range_[1] < (map_[1]+map_[2]):
            r.append(map_[0]+range_[0]-map_[1],map_[0]+range_[1]-map_[1])
        if range_[0] < map_
"""
