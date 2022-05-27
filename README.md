# Lalalannder - lab 2 - variant 1

This is an example project which demonstrates project structure and necessary
CI checks. It is not the best structure for real-world projects, but good
enough for educational purposes.

## Project structure

- `UnrolledLinkedList.py` -- Implementation of `UnrolledLinkedList` class
   with basic functions, such as adding and deleting elements,
   merging objects, etc. features. Stateless.
- `UnrolledLinkedList_test.py` -- unit and PBT tests for `UnrolledLinkedList`.

## Features

- A node class and an unrolled linked list class are defined.
- Add, delete and find elements in the unrolled linked list.
- Implements the iteration of the unrolled linked list object.
- Converts to and from list objects.
- Perform operations on unrolled linked list objects, such as Filter, Map,
  and Reduce based on a given condition or function.

## Contribution

- Wu Chenyun (1329846782@qq.com) -- UnrolledLinkedList, test and modify.
- Huang Yuting (hyut@hdu.edu.cn) -- Final modification and supplement.

## Changelog

- 27.05.2022 - 2
  - Modified errors in program and README.md file.
- 26.05.2022 - 1
  - Modified some errors and add type checks.
- 15.05.2022 - 0
  - Write programs and initial.

## Design notes

- According to definition of unrolled linked list, our goal is to design
  immutable data structures. In almost all methods, we used a copy of the
  original data to modify the data structure, so as to keep the original
  data structure unchanged and achieve the purpose of immutable operation object.
