
from sklearn.decomposition import NMF
import pandas as pd


def feature_vectors(corpus, kwargs=None):
    """Multinomial and TF-IDF representations

    Paramaters
    ----------
    corpus : array-like
        A collection of documents
    kwargs : dict, default None
        Keyword arguments of variable length
        See sklearn.feature_extraction.text.CountVectorizer
        for accepted keyword arguments

    Returns
    -------
    count : scipy.sparse.csr.csr_matrix
        The multinomial representation shape (n_samples, n_features)
    tfidf : scipy.sparse.csr.csr_matrix
        The tf-idf representation
    vocab : list
        Vocabulary
    """
    assert isinstance(corpus, (list, pd.Series))
    count, vocab = _multinomial(corpus, kwargs)
    tfidf = _tfidf(count)
    return count, tfidf, vocab

def nmf_labels(tfidfmatrix, k):
    """For getting the labels (group assignment) associated with
    each sample (user, in this case)

    Parameters
    ----------
    tfidfmatrix : scipy.sparse.csr.csr_matrix
        The output from calling `TfidfVectorizer` on the users/features data

    k : int
        The number of groupings to create

    Returns
    -------
    labels : np.ndarray
        An array of group assignments of length tfidfmatrix.shape[0] (users)
    """
    from sklearn.decomposition import NMF
    H = NMF(n_components=k, random_state=42).fit_transform(tfidfmatrix)
    labels = np.argmax(H, axis=1)
    return labels


def nmf_inspect(tfidfmatrix, feature_names, k_vals=[3, 5, 7, 9], n_words=10):
    """For looping over various values of `k` and printing the
    top `n_words`

    Parameters
    ----------
    tfidfmatrix : scipy.sparse.csr.csr_matrix
        The output from calling `TfidfVectorizer` on the users/features data

    feature_names : list
        The output from calling the `.get_feature_names()` on
        the TfidfVectorizer object

    k_vals : list
        A list of values for `k`, the number of groupings

    n_words : int
        The top n words to print for each grouping

    Returns
    -------
    None
    """
    from sklearn.decomposition import NMF
    for k in k_vals:
        nmf = NMF(n_components=k, random_state=42).fit(tfidfmatrix)
        print(k, end='\n')
        _print_words(nmf, feature_names, n_words)