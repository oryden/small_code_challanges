"""
https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

side =101

max_number = side**2

if __name__ == '__main__':

    if side % 2 == 1:
        nr_add = 0
        add_number = 2
        sum = 1
        num_before = 1

        for i in range(2, max_number + 1):
            if i == num_before + add_number:
                sum += i
                nr_add +=1
                num_before = i

                if nr_add == 4:
                    nr_add = 0
                    add_number += 2
    else:
        nr_add = 0
        add_number = 1
        sum = 0
        num_before = 0
        for i in range(1, max_number + 1):
            if i == num_before + add_number:
                sum += i
                nr_add += 1
                num_before = i

                if nr_add == 4:
                    nr_add = 0
                    add_number += 2

    print(sum)