

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
    for k in k_vals:
        nmf = NMF(n_components=k, random_state=42).fit(tfidfmatrix)
        print(k, end='\n')
        _print_words(nmf, feature_names, n_words)