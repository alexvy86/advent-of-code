h = complex(0, 0)
t = complex(0, 0)

coords_visited_by_tail = set()

with open('day9.input') as f:
    for line in f.read().splitlines():
        (direction, how_much) = line.split(" ")
        how_much = int(how_much)
        delta_map = {
            "R": complex(1,0),
            "L": complex(-1,0),
            "U": complex(0,1),
            "D": complex(0,-1),
        }
        for i in range(how_much):
            h += delta_map[direction]
            if abs(h-t) >= 2:
                # Move tail
                if h.real == t.real:
                    if h.imag > t.imag:
                        t += delta_map["U"]
                    else:
                        t += delta_map["D"]
                elif h.real > t.real:
                    if h.imag == t.imag:
                        t += delta_map["R"]
                    elif h.imag > t.imag:
                        t += complex(1,1)
                    else:
                        t += complex(1,-1)
                else:
                    if h.imag == t.imag:
                        t += delta_map["L"]
                    elif h.imag > t.imag:
                        t += complex(-1,1)
                    else:
                        t += complex(-1,-1)
            coords_visited_by_tail.add(t)

print(len(coords_visited_by_tail))
