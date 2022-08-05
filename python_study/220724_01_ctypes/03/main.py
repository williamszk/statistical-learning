def main():
    import work

    print ("GCD : ", work.gcd(35, 42))

    print ("\ndivide : ", work.divide(42, 8))

    print ("\navg : ", work.avg([1, 2, 3]))

    # p1 = work.Point(1, 2)
    # p2 = work.Point(4, 5)
    p1 = work.Point(0, 1)
    p2 = work.Point(1, 0)
    print ("\ndistance : ", work.distance(p1, p2))




if __name__ == "__main__":
    main()