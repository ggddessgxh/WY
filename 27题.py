for i in range(ord('x'),ord('z')+1):
    for j in range(ord('x'),ord('z')+1):
        if i!=j:
            for k in range(ord('x'),ord('z')+1):
                if i!=k and j!=k:
                    if i!=ord("x") and k!=ord("x") and k!=ord("z"):
                        print("a --",chr(i))
                        print("b --",chr(j))
                        print("c --",chr(k))
