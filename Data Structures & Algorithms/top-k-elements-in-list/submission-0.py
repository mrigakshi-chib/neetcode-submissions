class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_m = {} #empty hashmap to store frequencies
        for i in range(len(nums)): #putting values inside hashmap
            hash_m[nums[i]] = hash_m.get(nums[i],0) + 1

        buckets = [[] for _ in range(len(nums)+1)] #we create n+1 buckets 
        for num, freq in hash_m.items():
            buckets[freq].append(num) #storing values in frequency buckets

        result = [] #taking empty list

        for freq in range(len(buckets)-1, 0, -1): #traversing through buckets from right to left because max we have to take
            for num in buckets[freq]: 
                result.append(num) #appending num value in result
                if len(result) == k: #taking only k values
                    return result



