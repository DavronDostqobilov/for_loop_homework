def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    list1=[]
    for i in range(k):
        list1.append(n)
        
    return list1
print(main(4,1))