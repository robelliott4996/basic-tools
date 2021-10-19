def codons(seq,frame): #requires a provided sequence and the frame of interest
    n = len(seq)
    print(n)
    for i in range(frame - 1, n - 2, 3):
        yield seq[i:i+3]
