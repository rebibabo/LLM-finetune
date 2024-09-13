class Solution:
    def one_candy(self, idx):   
        if len(self.ratings) == 1:
            return True
        if idx==0:  
            return self.ratings[0] <= self.ratings[1]
        if idx==len(self.ratings)-1:    
            return self.ratings[-1] <= self.ratings[-2]
        a, b, c = self.ratings[idx-1], self.ratings[idx], self.ratings[idx+1]
        if a>b and c>b:     
            return True
        if a==b and b<c:    
            return True
        if a>b and b==c:    
            return True 
        if a==b==c:         
            return True 
        return False

    def candy(self, ratings: List[int]) -> int:
        self.ratings = ratings
        candies = [0] * len(ratings)
        for i in range(len(ratings)):   
            if self.one_candy(i):
                candies[i] = 1
        for i in range(1, len(ratings)):    
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        sum = candies[-1]
        for i in range(len(ratings)-2, -1, -1): 
            if ratings[i] > ratings[i+1]:                                                                          
                candies[i] = max(candies[i+1] + 1, candies[i])
            sum += candies[i]
        return sum