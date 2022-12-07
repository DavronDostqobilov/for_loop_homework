def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    x=range(0,n)
    str1=''
    for i in x:
        str1+=str(i)
    return str1
print(main(9))