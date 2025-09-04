
T = int(input())

for test_case in range(1, T + 1):
    word = list(input())
    result = ["#"]
    for i in word:
        result.append(".")
        result.append(i)
        result.append(".")
        result.append("#")
    print("."+(".#..")*len(word))
    print("."+("#.#.")*len(word))
    print("".join(result))
    print("."+("#.#.")*len(word))
    print("."+(".#..")*len(word))
