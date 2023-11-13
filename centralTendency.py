

class centralTendancy:
    def describe(self, list1, roundVal = 0, class_interval = 0):
        print('Mean', self.mean(list1, roundVal))
        print('Median', self.median(list1))
        print('Mode', self.mode(list1, class_interval))
        print('Standard Deviation', self.stdDev(list1, roundVal))
        print('Variance', self.variance(list1, roundVal))
    
    
    # mean function
    def mean(self, list1, roundVal = 0): 
        meanVal = sum(list1)/len(list1)
        meanVal = round(meanVal, roundVal) if roundVal != 0 else meanVal
        return meanVal


    def median(self, list1):
        list1.sort()
        n = len(list1)
        
        if n % 2 == 0:
            return (list1[int((n/2))-1] + list1[int((n/2))])/2         
        return list1[int((n-1))/2]
    
    
    def mode(self, list1, class_interval = 0):
        maxData = max(list1)
        minData = min(list1)
        dicn={}
        class_interval = (maxData-minData)/10 if class_interval == 0 else class_interval
        
        while minData <= maxData:
            dicn[minData,minData + class_interval] = 0
            minData = minData + class_interval 
        dicnKey = list(dicn.keys()) 
         
        for i in list1:
            for j in dicnKey:
                
                if j[0] <= i and j[1] > i:
                    dicn[j] += 1
                    break
                
        modFreq, modalClass = 0, 0
        for i in dicnKey:
            if dicn[i] > modFreq:
                modFreq = dicn[i]
                modalClass = i
        return modalClass


    def variance(self, list1, roundVal = 0):
        list_mean = sum(list1)/len(list1)
        list_sum_mean_diff_sq = 0
        
        for i in list1:
            list_sum_mean_diff_sq += (list_mean - i) ** 2
            
        var = (list_sum_mean_diff_sq/len(list1)) 
        var = round(var, roundVal) if roundVal != 0 else var
        return var
    
    
    def stdDev(self, list1, roundVal = 0):  
        list_mean = sum(list1)/len(list1)
        list_sum_mean_diff_sq = 0
        
        for i in list1:
            list_sum_mean_diff_sq += (list_mean - i) ** 2
            
        stdDev = (list_sum_mean_diff_sq/len(list1)) ** 0.5
        stdDev = round(stdDev, roundVal) if roundVal != 0 else stdDev
        return stdDev
