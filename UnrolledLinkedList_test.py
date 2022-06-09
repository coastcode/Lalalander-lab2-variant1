import unittest
from typing import List, Any

from hypothesis import given
import hypothesis.strategies as st

from UnrolledLinkedList import UnrolledLinkedList, iterator
from UnrolledLinkedList import cons, length, remove
from UnrolledLinkedList import member, reverse, concat
from UnrolledLinkedList import to_list, from_list, find
from UnrolledLinkedList import filter, map, reduce, empty


class TestUnrolledLinkedList(unittest.TestCase):
    def test_api(self) -> None:
        empty = UnrolledLinkedList()
        l1 = cons(cons(empty, 1), None)
        l2 = cons(cons(empty, None), 1)
        self.assertEqual(str(empty), "[]")
        self.assertEqual(str(l1), "[1, None]")
        self.assertEqual(str(l2), "[None, 1]")
        self.assertNotEqual(empty, l1)
        self.assertNotEqual(empty, l2)
        self.assertNotEqual(l1, l2)
        self.assertEqual(l1, cons(cons(empty, 1), None))
        self.assertEqual(length(empty), 0)
        self.assertEqual(length(l1), 2)
        self.assertEqual(length(l2), 2)
        self.assertEqual(str(remove(l1, None)), "[1]")
        self.assertEqual(str(remove(l1, 1)), "[None]")
        self.assertFalse(member(empty, None))
        self.assertTrue(member(l1, None))
        self.assertTrue(member(l1, 1))
        self.assertFalse(member(l1, 2))
        self.assertEqual(str(l1), str(reverse(l2)))
        self.assertEqual(to_list(l1), [1, None])
        self.assertEqual(str(l1), str(from_list([1, None])))
        str1 = str(concat(l1, l2))
        str2 = str(from_list([1, None, None, 1]))
        self.assertEqual(str1, str2)
        buf = []
        for e in l1:
            buf.append(e)
        self.assertEqual(buf, [1, None])
        lst = to_list(l1) + to_list(l2)
        for e in l1:
            lst.remove(e)
        for e in l2:
            lst.remove(e)
        self.assertEqual(lst, [])

    @given(a=st.integers(), b=st.integers(),
           c=st.integers(), d=st.integers())
    def test_cons(self, a, b, c, d) -> None:
        empty_ull = UnrolledLinkedList()
        ull1 = UnrolledLinkedList()
        ull2 = UnrolledLinkedList()
        for i in range(3):
            ull1 = cons(ull1, i)
        for i in [a, b, c, d]:
            ull2 = cons(ull2, i)
        res1 = cons(empty_ull, 1)
        res2 = length(ull2)
        self.assertEqual(str(empty_ull), "[]")
        self.assertEqual("[0, 1, 2]", str(ull1))
        self.assertNotEqual(str(empty_ull), str(res1))
        self.assertEqual(res2, 4)

    def test_remove(self) -> None:
        ull1 = UnrolledLinkedList()
        ull2 = UnrolledLinkedList()
        empty_ull = UnrolledLinkedList()
        for i in range(1, 6):
            ull1 = cons(ull1, i)
            ull2 = cons(ull2, i)
        res1 = remove(ull1, 1)
        ull2 = remove(ull2, 6)
        ull3 = remove(empty_ull, 1)
        self.assertEqual(str(res1), "[2, 3, 4, 5]")
        self.assertEqual(str(ull2), "Element is not in the list.")
        self.assertEqual(str(ull3), "The unrolled linked list is empty.")

    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_length(self, a, b, c) -> None:
        empty_ull = UnrolledLinkedList()
        ull = UnrolledLinkedList()
        ull_ran = UnrolledLinkedList()
        for i in range(10):
            ull = cons(ull, i)
        for i in [a, b, c]:
            ull_ran = cons(ull_ran, i)
        ull1 = remove(ull, 2)
        self.assertEqual(length(empty_ull), 0)
        self.assertEqual(length(ull), 10)
        self.assertEqual(length(ull1), 9)
        self.assertEqual(length(ull_ran), 3)

    def test_member(self) -> None:
        empty_ull = UnrolledLinkedList()
        res1 = member(empty_ull, 1)
        ull = UnrolledLinkedList()
        for i in range(3):
            ull = cons(ull, i)
        res2 = member(ull, 0)
        res3 = member(ull, 3)
        self.assertEqual(res1, False)
        self.assertEqual(res2, True)
        self.assertEqual(res3, False)

    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_reverse(self, a, b, c) -> None:
        ull1 = UnrolledLinkedList()
        ull2 = UnrolledLinkedList()
        for i in range(5):
            ull1 = cons(ull1, i)
        for i in [a, b, c]:
            ull2 = cons(ull2, i)
        res1 = reverse(ull1)
        res2 = reverse(ull2)
        self.assertEqual(str(res1), "[4, 3, 2, 1, 0]")
        self.assertEqual(str(res2), str([c, b, a]))

    @given(a=st.integers(), b=st.integers(),
           c=st.integers(), d=st.integers())
    def test_tolist(self, a, b, c, d) -> None:
        ull1 = UnrolledLinkedList()
        ull2 = UnrolledLinkedList()
        for i in range(1, 5):
            ull1 = cons(ull1, i)
        for i in [a, b, c, d]:
            ull2 = cons(ull2, i)
        res1 = to_list(ull1)
        res2 = to_list(ull2)
        self.assertEqual(res1, [1, 2, 3, 4])
        self.assertEqual(res2, [a, b, c, d])

    @given(a=st.lists(st.integers()))
    def test_from_list(self, a: List[Any]) -> None:
        lst = [3, 4, 5]
        ull_list1 = from_list(lst)
        ull_list2 = from_list(a)
        self.assertEqual(str(ull_list1), "[3, 4, 5]")
        self.assertNotEqual(type(ull_list2), type(a))

    def test_find(self) -> None:
        empty_ull = UnrolledLinkedList()
        ull = UnrolledLinkedList()
        for i in range(10):
            ull = cons(ull, i)
        res1 = find(empty_ull, lambda x: x != 0)
        res2 = find(ull, lambda x: x >= 10)
        res3 = find(ull, lambda x: x <= 10)
        self.assertEqual(res1, "The unrolled linked list is empty.")
        self.assertEqual(res2, False)
        self.assertEqual(res3, True)

    def test_filter(self) -> None:
        ull = UnrolledLinkedList()
        for i in range(7):
            ull = cons(ull, i)
        res = filter(ull, lambda x: x % 3 == 0)
        dl = to_list(res)
        self.assertEqual(dl, [0, 3, 6])

    def test_map(self) -> None:
        ull = UnrolledLinkedList()
        for i in range(5):
            ull = cons(ull, i)
        ans = map(ull, lambda x: x - 2)
        dl = to_list(ans)
        self.assertEqual(dl, [-2, -1, 0, 1, 2])

    def test_reduce(self) -> None:
        ull = UnrolledLinkedList()
        for i in range(1, 6):
            ull = cons(ull, i)
        res = reduce(ull, lambda x, y: x + y, 0)
        self.assertEqual(res, 15)

    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_empty(self, a, b, c) -> None:
        empty_ull = UnrolledLinkedList()
        ull = UnrolledLinkedList()
        for i in [a, b, c]:
            ull = cons(ull, i)
        res1 = empty(ull)
        res2 = empty(empty_ull)
        res3 = to_list(empty_ull)
        self.assertEqual(res1, False)
        self.assertEqual(res2, True)
        self.assertEqual(res3, [])

    @given(a=st.integers(), b=st.integers())
    def test_concat(self, a, b) -> None:
        empty_ull = UnrolledLinkedList()
        ull1 = UnrolledLinkedList()
        ull1 = cons(ull1, a)
        ull2 = UnrolledLinkedList()
        ull2 = cons(ull2, b)
        res1 = concat(ull1, ull2)
        res2 = concat(empty_ull, ull1)
        self.assertEqual(str(res1), str([a, b]))
        self.assertEqual(str(res2), str([a]))

    @given(a=st.integers(), b=st.integers(), c=st.integers())
    def test_iterator(self, a, b, c) -> None:
        lst = [a, b, c]
        ull = from_list(lst)
        tmp = []
        for i in ull:
            tmp.append(i)
        self.assertEqual(to_list(ull), tmp)
        self.assertEqual(to_list(ull), lst)
        idx = iter(UnrolledLinkedList())
        self.assertRaises(StopIteration, lambda: next(idx))

    @given(lst=st.lists(st.integers()))
    def test_monoid(self, lst) -> None:
        a = from_list(lst)
        b = UnrolledLinkedList()
        for i in range(5):
            b = cons(b, i)
        c = [7, 8, 9]
        d = UnrolledLinkedList()
        ull_c = from_list(c)
        ull1 = UnrolledLinkedList()
        ull1 = cons(ull1, 7)
        ull2 = UnrolledLinkedList()
        ull2 = cons(ull2, 8)
        ull3 = UnrolledLinkedList()
        ull3 = cons(ull3, 9)
        concat1 = concat(a, d)
        concat2 = concat(d, a)
        concat3 = concat(ull2, ull3)
        concat4 = concat(ull1, ull2)
        self.assertEqual(str(a), str(concat1))
        self.assertEqual(str(a), str(concat2))
        self.assertEqual(str(ull_c), str(concat(ull1, concat3)))
        self.assertEqual(str(ull_c), str(concat(concat4, ull3)))
