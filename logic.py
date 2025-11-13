from collections import Counter
#vkmckyhmckyh
def get_majority(votes):
    """Return majority option among players"""
    if not votes:
        return None
    count = Counter(votes)
    return count.most_common(1)[0][0]

