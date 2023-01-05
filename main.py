


# If each combination contains '1' element
def comb_var1(nums:list) -> list:
    return [[a] for a in nums]

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
                comb = [*a, *b]
                comb.sort()

                if comb not in var:
                    var.append(comb)

    return var

# Calculating combinations
def generate_combinations(numbers:list, length:int = 1) -> list:
    ids = list(range(len(numbers)))

    # Handling exceptions
    if length == 0: return []
    elif length in [1, len(numbers)]: return numbers
    elif length > len(numbers): return 'len(numbers) > length'

    # Combining multiple combinations
    var = comb_var1(ids)

    for a in range(length - 1):
        var = merge_combinations(var, comb_var1(ids))

    # Original numbers replacement
    for a in range(len(var)):
        for b in range(length):
            var[a][b] = numbers[var[a][b]]

    return var
