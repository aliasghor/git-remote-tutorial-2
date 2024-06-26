import student as sdt

def main() -> None:
    ali = sdt.Student("Ali", 21)
    gerry = sdt.Student("Gerry",20)

    print(ali)
    print(gerry)

    print(ali.acquaintance(gerry))

if __name__ == '__main__':
    main()