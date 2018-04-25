import insertion

Ary = [4, 11, 0, 20, -10, 3, 67, -1]

sorted_Ary = Ary[:]
sorted_Ary.sort()


def test_insertion():
    A = Ary[:]
    insertion.insertion_sort(A)
    assert sorted_Ary == A
