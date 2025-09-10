def minimumLoss(price):
    
    indexed_prices = sorted(enumerate(price), key=lambda x: x[1])
    
    min_loss = float('inf')
   
    for i in range(len(indexed_prices) - 1):
        current_year, current_price = indexed_prices[i]
        next_year, next_price = indexed_prices[i + 1]
        
       
        if current_year > next_year:
            loss = next_price - current_price
            if loss < min_loss:
                min_loss = loss
    
    return min_loss


years = [20, 7, 8, 2, 5]
print(minimumLoss(years)) 
