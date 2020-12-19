from pprint import pprint


def solution_a(visits):
    m = {}
    for p in visits:
        if p[0] not in m:
            m[p[0]] = set()
        m[p[0]].add(p[1])
    print('m:')
    pprint(m)
    
    sites = list(m.keys())
    similarity = []
    for i in range(len(sites)):
        for j in range(i+1, len(sites)):
            a, b = sites[i], sites[j]
            ma, mb = m[a], m[b]
            similarity.append([len(ma&mb), -len(ma^mb), a, b])
    print('unordered similarity:')
    pprint(similarity)

    return sorted(similarity, reverse=True)

def main():
    visits = [
        ('a', 1), ('a', 3), ('a', 5),
        ('b', 2), ('b', 6),
        ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
        ('d', 4), ('d', 5), ('d', 6), ('d', 7),
        ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
    
    similarity = solution_a(visits)
    print('similarity:')
    pprint(similarity)


if __name__ == "__main__":
    main()
