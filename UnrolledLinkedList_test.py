import unittest
from UnrolledLinkedList import UnrolledLinkedList
from UnrolledLinkedList import cons, length, remove
from UnrolledLinkedList import member, reverse, concat
from UnrolledLinkedList import to_list, from_list
from UnrolledLinkedList import filter, map, reduce, empty


class TestUnrolledLinkedList(unittest.TestCase):
    def test_api(self) -> None:    # 10
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

    def test_empty(self) -> None:
        ull = UnrolledLinkedList()
        for i in range(1, 4):
            ull = cons(ull, i)
        res = empty(ull)
        res = to_list(res)
        self.assertEqual(res, [])

    def test_member(self) -> None:
        ull = UnrolledLinkedList()
        for i in range(5):
            ull = cons(ull, i)
        res1 = member(ull, 2)
        self.assertEqual(res1, True)
        res2 = member(ull, 5)
        self.assertEqual(res2, False)