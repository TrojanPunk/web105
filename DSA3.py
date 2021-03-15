def TOH(n, source, destination, aux):
    if n == 1:
        print
        "Shift disk 1 from source", source, "to destination", destination
        return
    TOH(n - 1, source, aux, destination)
    print
    "Shift disk", n, "from source", source, "to destination", destination
    TOH(n - 1, aux, destination, source)

n = 4
TOH(n, 'X', 'Y', 'Z')