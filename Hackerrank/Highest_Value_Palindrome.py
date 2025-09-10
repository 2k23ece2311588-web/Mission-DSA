def highestValuePalindrome(s, n, k):
    s = list(s)
    changes_needed = [0] * n
    left, right = 0, n - 1

    
    while left < right:
        if s[left] != s[right]:
            higher = max(s[left], s[right])
            s[left] = s[right] = higher
            k -= 1
            changes_needed[left] = changes_needed[right] = 1
        left += 1
        right -= 1

    if k < 0:
        return '-1'

    
    left, right = 0, n - 1
    while left <= right and k > 0:
        if left == right:
           
            if s[left] != '9' and k > 0:
                s[left] = '9'
                k -= 1
        else:
            if s[left] != '9':
                
                if changes_needed[left] == 1 or changes_needed[right] == 1:
                    if k >= 1:
                        s[left] = s[right] = '9'
                        k -= 1
                else:
                    if k >= 2:
                        s[left] = s[right] = '9'
                        k -= 2
        left += 1
        right -= 1

    return ''.join(s)
