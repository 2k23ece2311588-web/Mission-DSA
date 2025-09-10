class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        
        circular_pref = students.count(0)
        square_pref = students.count(1)

        
        for sandwich in sandwiches:
            if sandwich == 0:  
                if circular_pref > 0:
                    circular_pref -= 1  
                else:
                   
                    return square_pref  
            else:  
                if square_pref > 0:
                    square_pref -= 1  
                else:
                   
                    return circular_pref  
        
       
        return 0
