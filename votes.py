"""http://telegra.ph/Anons-zadachi-48-Vybory-12-04"""
def votes(groups):
    groups.sort()
    return sum(map(lambda x: x // 2 + 1, groups[:len(groups)//2 + 1]))

if __name__ == "__main__":
    print(votes([2, 5, 6, 4]))
    print(votes([5, 5, 7]))
    print(votes([4, 2, 1, 3, 7]))
