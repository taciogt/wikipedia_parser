__author__ = 'tacio'


def wagner_fisher(word1, word2):
    size1 = len(word1)+1
    size2 = len(word2)+1

    matrix = [[None]*size1 for x in range(size2)]
    matrix[0][0] = 0

    for i in range(size1):
        matrix[0][i] = i
    for j in range(size2):
        matrix[j][0] = j

    for j in range(1, size2):
        for i in range(1, size1):
            index1 = i-1
            index2 = j-1
            if word1[index1] == word2[index2]:
                matrix[j][i] = matrix[j-1][i-1]
            else:
                matrix[j][i] = min(
                    matrix[j][i-1]+1,  # deletion
                    matrix[j-1][i]+1,  # insertion
                    matrix[j-1][i-1]+1  # substitution
                )
    return matrix


def damerau_levenshtein(word1, word2):
    size1 = len(word1)+1
    size2 = len(word2)+1

    matrix = [[None]*size1 for x in range(size2)]
    matrix[0][0] = 0

    for i in range(size1):
        matrix[0][i] = i
    for j in range(size2):
        matrix[j][0] = j

    for j in range(1, size2):
        for i in range(1, size1):
            index1 = i-1
            index2 = j-1

            cost = 1
            if word1[index1] == word2[index2]:
                cost = 0

            matrix[j][i] = min(
                matrix[j][i-1] + 1,  # deletion
                matrix[j-1][i] + 1,  # insertion
                matrix[j-1][i-1] + cost  # substitution
            )

            if index1 > 1 and index2 > 1 and word1[index1] == word2[index2-1] and word1[index1-1] == word2[index2]:
                matrix[j][i] = min(matrix[j][i],
                                   matrix[j-2][i-2] + cost)  # transposition

    return matrix


def show_matrix(word1, word2, matrix):
    word1_separated = '      '
    for letter in word1:
        word1_separated += letter + '  '

    print word1_separated
    for index, line in enumerate(matrix):
        if index == 0:
            print '  ' + str(line)
        else:
            print word2[index-1] + ' ' + str(line)



def run_algorithm(word1, word2):
    print '\nRunning algorthm for words: ' + word1 + ', ' + word2 + ''
    print 'Wagner-Fischer Algorithm (considers deletion, insertion and substitution)'
    matrix = wagner_fisher(word1, word2)
    show_matrix(word1, word2, matrix)
    print 'Levenshtein Distance: ' + str(matrix[len(word2)][len(word1)])

    print '\nDamerau-Levenshtein Algorithm (considers also transposition)'
    matrix = damerau_levenshtein(word1, word2)
    show_matrix(word1, word2, matrix)
    print 'Damerau-Levenshtein Distance: ' + str(matrix[len(word2)][len(word1)])


if __name__ == '__main__':

    run_algorithm('kitten', 'sitting')
    run_algorithm('bra', 'bar')




