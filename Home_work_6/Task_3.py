def main():

    fractions = []

    for denominator in range(2, 12):
        for numerator in range(1, denominator):
            if numerator == 1 or numerator == denominator - 1:
                fractions.append(str(numerator) + '/' + str(denominator))
            else:
                is_simple = True
                for i in range(2, min(numerator, denominator) + 1):
                    if numerator % i == 0 and denominator % i == 0:
                        is_simple = False
                        break
                if is_simple:
                    fractions.append(str(numerator) + '/' + str(denominator))

    print(', '.join(fractions))


main()
