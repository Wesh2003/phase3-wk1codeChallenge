# The function below links every letter of the alphabet with a number starting from 1 == 'a' in an ascending order
# It then returns highest number linked to a consonant in a word.
def find_high_value(word):
    sorteee = sorted(word)
    for j in range(1,26):
        const_val = [i == j for i in sorteee]
        j += 1
    return const_val[len(const_val) - 1]

print(find_high_value("zodiacs"))