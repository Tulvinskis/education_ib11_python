def find_farthest_orbit(list_of_orbits):
    o = [(3.14 * a * b, orbit) for orbit in list_of_orbits for a, b in [orbit]]
    farthest_orbit = max(o, key=lambda x:x[0])[1]
    return farthest_orbit


orbits = [(1, 3), (2.5, 10), (7, 2)]
print(find_farthest_orbit(orbits))