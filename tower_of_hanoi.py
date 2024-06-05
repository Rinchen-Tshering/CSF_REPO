class Solution:
    # This function solves the Tower of Hanoi problem for a given number of disks (N), starting rod (fromm), ending rod (to), and auxiliary rod (aux).
    def toh(self, N, fromm, to, aux):
        # Base case: if N is 1, print the move required to move the disk from the starting rod to the ending rod and return 1.
        if N == 1:
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
            print("\n")
            return 1

        # Calculate the total number of moves required to move all the disks from the starting rod to the ending rod.
        moves = 0
        moves += self.toh(N - 1, fromm, aux, to)
        moves += 1
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))
        moves += self.toh(N - 1, aux, to, fromm)
    
        # Return the total number of moves required.
        return moves

# Create an instance of the Solution class.
s = Solution()
# Call the toh function with 3 disks, starting rod 1, ending rod 3, and auxiliary rod 2.
print(s.toh(3, 1, 3, 2))