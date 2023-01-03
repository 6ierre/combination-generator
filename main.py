


# hány darab kombinációt lehet kiszámolni 'n' darabszámú halmazból úgy, hogy 'k' elemet tartalmazhat 1 kombináció
def combination_total(n:int, k:int) -> int:

    # 'a' szám faktoriálisa
    def factorial(n:int):
        i = 1

        for a in range(1, n + 1):
            i *= a

        return i

    # behelyettesítés a képletbe: n! / (k! * (n - k)!)
    return factorial(n) // (factorial(k) * factorial(n - k))


# ha '1' elemet tartalmazhat 1 kombináció
def combination_var1(nums:list) -> list:
    var = []

    for a in nums:
        var.append([a])

    return var

# ha '2' elemet tartalmazhat 1 kombináció
def combination_var2(nums:list) -> list:
    var = []

    for a in range(len(nums)):
        for b in nums[a + 1:]:
            var.append([nums[a], b])

    return var

# 2 db halmaz elemeit összekombinálja
def merge_combinations(comb1:list, comb2:list) -> list:
    var = []

    for a in comb1:
        for b in comb2:

            # megnézi, hogy 'b' halmaz elemei benne vannak-e 'a' halmaz elemeibe
            for n in b:
                if n in a:
                    break

            else:
                # megnézi, hogy '*a' és '*b' halmazok elemei benne vannak-e már egy másik halmazban
                for c in var:
                    num = 0

                    for d in [*a, *b]:
                        if d in c:
                            num += 1

                    # ha talált egy olyan halmazt, amelyben benne van mindegyik elem
                    if num == len(comb1[0]) + len(comb2[0]):
                        break

                else:
                    # ha még nem létezik olyan halmaz, amely ezeket az elemek tartalmazzák
                    var.append([*a, *b])

    return var

# ha nem '1' vagy '2' elemet tartalmazhat 1 kombináció
def combination_var3(nums:list, length:int) -> list:
    var = []

    # ha a kombinációk elemszáma páratlan
    if length % 2 != 0:
        var.append(combination_var1(nums))

    # ha a kombinációk elemszáma páros
    for a in range(length // 2):
        var.append(combination_var2(nums))

    # több kombináció kombinálása
    while len(var) != combination_total(len(nums), length):
        var[0] = merge_combinations(var[0], var[1])

        var.pop(1)

        var = [var, var[0]][int(var == [var[0]])]

    return var


# kombinációk kiszámolása & visszaadja az eredeti számokat
def generate_combinations(numbers:list, length:int = 1) -> list:
    var = []

    # kivételek kezelése
    if length == 0: return []
    elif length == 1 or length == len(numbers): return numbers
    elif length == 2: return combination_var2(numbers)
    elif length > len(numbers): return f'1db kombináció maximum {len(numbers)}db elemet tartalmazhat!'

    for a in combination_var3(list(range(len(numbers))), length):
        nums = []

        for b in a:
            nums.append(numbers[b])

        var.append(nums)

    return var

