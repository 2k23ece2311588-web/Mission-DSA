def gridlandMetro(n, m, k, track):
    rows = {}
    for r, c1, c2 in track:
        if r not in rows:
            rows[r] = []
        rows[r].append((c1, c2))
    
    total_cells = n * m
    for r in rows:
        
        intervals = sorted(rows[r])
        merged = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                merged.append((start, end))
                start, end = intervals[i]
        merged.append((start, end))

       
        for start, end in merged:
            total_cells -= (end - start + 1)
    return total_cells


n = 4
m = 4
k = 3
track = [
    (2, 2, 3),
    (3, 1, 4),
    (4, 4, 4)
]
print(gridlandMetro(n, m, k, track)) 
