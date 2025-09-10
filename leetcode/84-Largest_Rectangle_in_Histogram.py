def largestRectangleArea(heights):
    stack = []  
    max_area = 0
    heights.append(0) 
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            
            popped_index = stack.pop()
            popped_height = heights[popped_index]
            
            
            if not stack:
                width = i
            else:
                
                width = i - stack[-1] - 1
            
            max_area = max(max_area, popped_height * width)
        
        stack.append(i)
        
    return max_area
histogram1 = [2, 1, 5, 6, 2, 3]
print(f"Largest rectangle area in {histogram1}: {largestRectangleArea(histogram1)}") 

histogram2 = [6, 2, 5, 4, 5, 1, 6]
print(f"Largest rectangle area in {histogram2}: {largestRectangleArea(histogram2)}") 
