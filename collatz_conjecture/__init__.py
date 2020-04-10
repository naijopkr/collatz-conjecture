def collatz_conjecture(num):
    try:
        current = int(num)
    except:
        raise TypeError('Input should be numeric')

    if current <= 1:
        raise ValueError('Number should be greater than one')

    counter = 0
    while current != 1:
        if current % 2 == 0:
            current = current/2
        else:
            current = 1 + current*3

        counter += 1

    return (current, counter)
