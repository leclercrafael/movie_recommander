import math
import warnings
import pandas as pd

#IMPLEMENTATION OF COUNTVECTORIZER

# We first need to determine every unique words appearing in all of our strings

def create_index(a : list) -> list :
    '''
    Returns the list of each word constituting an index

    Args :
    a : the same list of strings 

    Returns : 
    The list of all words present in all of our strings
    '''

    concatenation = ''

    for indice, i in enumerate(a) :
        if indice != (len(a)-1) : 
            concatenation += (i + ' ')
        else:
            concatenation += i

    index = list(set(concatenation.split(' ')))

    return index


def myCountVectorizer (a : list) -> list :
    '''
    Returns the frequency of each word in each strings

    Args :
    a : a list of strings 

    Returns : 
    A list of list containing the frequency for each words
    '''

    out = [] #container of other lists

    all_words = create_index(a=a)

    for i in a :
        sub_out = [0] * len(all_words)
        words = i.split(' ')
        for j in words:
            sub_out[all_words.index(j)] +=1

        out.append(sub_out)

    
    return (out, all_words)


#IMPLEMENTATION OF COSINUS SIMILARITY

def produit_scalaire(x : list, y : list) -> float :
    
    '''
    Returns the scalar product of the two input vectors

    Args:
    x, y : two vectors
    '''

    if len(x) != len(y) :
        warnings.warn("The two inputs don't have the same dimensions.", UserWarning)
        return None
    else:
        sum = 0
        for i in range(len(x)):
            sum += (x[i]*y[i])

    return sum

def norm(x : list) -> float :

    '''
    Returns the norm of the input vector

    Args:
    x : vector
    '''
    out = 0
    for i in x:
        out += i**2

    return math.sqrt(out)

def get_cosinus(x : list, y : list) -> float :

    return produit_scalaire(x,y)/(norm(x)*norm(y))


def mycosinussimilarity(b : list) -> list :

    '''
    Returns the cosinus similarity between each vector under the form of a matrix

    Args : 
    b : list containing the CountVectorizer of our strings

    Returns :
    The matrix of similarity
    
    '''

    out = [[1.]*len(b) for i in range(len(b))]  # Creation of the matrix

    
    '''We can start to fill the output : matrix of cosinus similarity. 
    This matrix being symetrical we do not have to compute every element, including the diagonal and one side of the matrix'''

    for i in range(0, len(b)-1):
        for j in range(i+1, len(b)):
            out[i][j] = get_cosinus(b[i], b[j])
            out[j][i] = get_cosinus(b[i], b[j])

    return out

def get_title_from_index (df : pd.DataFrame, index) -> pd.Series: 
    mask = (df.index == index)
    return df[mask]['title'].values[0]

def get_index_from_title(df : pd.DataFrame, title) -> pd.Series:
    mask = (df.title == title)
    return df[mask]["index"].values[0]

