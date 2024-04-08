class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        r = 0
        while students:
            if sandwiches[0] not in students:
                return len(students)
            elif students[0] != sandwiches[0]:
                z = students.pop(0)
                students.append(z)
            elif students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
        return 0 


        