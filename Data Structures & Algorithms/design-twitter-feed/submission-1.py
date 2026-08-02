class Twitter:
    #use a heap for the 10 most recent tweets part
    #we need a few dicts
    #one should be for everyone that a person follows
    #one should be for all of a person's followers
    #each time you post something you should also store the time at which the tweet was posted in a 
    #separate hashmap
    #why couldn't we just use a 
    #need a hashmap for O(1) lookup for follow, unfollow, and posttweet

    def __init__(self):
        self.count = 0 
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]: 
            if followeeId in self.tweetMap: 
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10: 
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0: 
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]: 
            self.followMap[followerId].remove(followeeId)
