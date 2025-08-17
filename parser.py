def parse(s,n=5):
    if s is None:
        return None
    s = s.strip().lower()
    if s in("n","nie",""):
        return None
    tokens = s.replace(",","").replace(";","").split()
    idx = set()
    for t in tokens:
        if t.isdigit():
            k = int(t)
            if 1 <= k <= n:
                idx.add(k-1)
    return sorted(idx)