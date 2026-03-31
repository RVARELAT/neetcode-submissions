class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use greg hoggs trick

        # make dict with frequencies (think we use counting)

        # then array with index from o to k

        # place corresponding nums in frequency array

        # loop through array backwards and return the first k elements
        
        
        # length of the input array
        n = len(nums)
        
        # count frequency of each number
        # example: [1,1,1,2,2,3] -> {1:3, 2:2, 3:1}
        counter = Counter(nums)
        
        frequencies = [0] * (n + 1)
        
        # place number into their freuqency bucket
        for num, freq in counter.items():
            
            # if bucket is empty, inialize list
            if frequencies[freq] == 0:
                frequencies[freq] = [num]
            # otherwise append the number
            else:
                frequencies[freq].append(num)
        
        result = []

        for i in range(len(frequencies) - 1, -1 , -1):
            
            if frequencies[i] != 0:
                result.extend(frequencies[i])
            
            if len(result) == k:
                break 
        
        return result