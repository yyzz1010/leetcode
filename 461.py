class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # len('{0:b}'.format(2 ** 31)) = 32
        binary_x = '{0:032b}'.format(x)
        binary_y = '{0:032b}'.format(y)
        count = 0
        for (x,y) in zip(binary_x, binary_y):
            if x != y:
                count += 1
        return count
