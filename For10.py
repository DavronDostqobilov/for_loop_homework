def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    s=' '.join(list1)
    x=s.title()
    d=x.split()
    return d
print(main(['davron','ilhom']))