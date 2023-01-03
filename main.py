


# How many combinations can be calculated from a set of 'n' elements, where each combination contains 'k' elements?
def combination_total(n:int, k:int) -> int:

    # The factorial of number 'a'
    def factorial(n:int):
        i = 1

        for a in range(1, n + 1):
            i *= a

        return i

    # Substituting into the formula: n! / (k! * (n - k)!)
    return factorial(n) // (factorial(k) * factorial(n - k))


# If each combination contains '1' element
def combination_var1(nums:list) -> list:
    var = []

    for a in nums:
        var.append([a])

    return var

# If each combination contains '2' elements
def combination_var2(nums:list) -> list:
    var = []

    for a in range(len(nums)):
        for b in nums[a + 1:]:
            var.append([nums[a], b])

    return var

# Combining the elements of 2 sets
def merge_combinations(comb1:list, comb2:list) -> list:
    var = []

    for a in comb1:
        for b in comb2:

            # Checking if the elements of set 'b' are included in the elements of set 'a'
            for n in b:
                if n in a:
                    break

            else:
                # Checking if the elements of sets '*a' and '*b' are already included in another set
                for c in var:
                    num = 0

                    for d in [*a, *b]:
                        if d in c:
                            num += 1

                    # If a set is found that contains all of these elements
                    if num == len(comb1[0]) + len(comb2[0]):
                        break

                else:
                    # If a set does not yet exist that contains these elements
                    var.append([*a, *b])

    return var

# If each combination does not contain '1' or '2' elements
def combination_var3(nums:list, length:int) -> list:
    var = []

    # If the number of elements in the combination is odd
    if length % 2 != 0:
        var.append(combination_var1(nums))

    # If the number of elements in the combination is even
    for a in range(length // 2):
        var.append(combination_var2(nums))

    # Combining multiple combinations
    while len(var) != combination_total(len(nums), length):
        var[0] = merge_combinations(var[0], var[1])

        var.pop(1)

        var = [var, var[0]][int(var == [var[0]])]

    return var


# Calculating combinations & returning the original numbers
def generate_combinations(numbers:list, length:int = 1) -> list:
    var = []

    # Handling exceptions
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

