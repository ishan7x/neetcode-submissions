from datetime import datetime
import heapq
from typing import List, Dict, Set

# 1. High Cohesion: Tweet only cares about tweet data
class Tweet:
    def __init__(self, userId: int, tweetId: int):
        self.userId = userId
        self.tweetId = tweetId
        self.postTime = datetime.now()


# 2. High Cohesion: User handles its own internal collections and behaviors
class User:
    def __init__(self, userId: int):
        self.userId = userId
        self.following_ids: Set[int] = set()  # Loose coupling: Store IDs instead of raw objects
        self.tweets: List[Tweet] = [] 
    
    def post_tweet(self, tweetId: int) -> None:
        self.tweets.append(Tweet(self.userId, tweetId))

    def follow(self, followee_id: int) -> None:
        # Prevent self-following edge cases
        if followee_id != self.userId:
            self.following_ids.add(followee_id)

    def unfollow(self, followee_id: int) -> None:
        self.following_ids.discard(followee_id)  # .discard() won't crash if they weren't following


# 3. Low Coupling: Twitter orchestrates relationships via IDs
class Twitter:
    def __init__(self):
        # O(1) Lookups replace the inefficient self.getUser linear scan
        self.users: Dict[int, User] = {}

    def _ensure_user_exists(self, userId: int) -> User:
        """Helper method to encapsulate user provisioning."""
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self._ensure_user_exists(userId)
        user.post_tweet(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self._ensure_user_exists(userId)
        all_tweets = []
        
        # Gather author's own tweets
        for tweet in user.tweets:
            heapq.heappush(all_tweets, (-tweet.postTime.timestamp(), tweet.tweetId))
            
        # Gather followees' tweets via IDs (loosely coupled)
        for followee_id in user.following_ids:
            if followee_id in self.users:
                for tweet in self.users[followee_id].tweets:
                    heapq.heappush(all_tweets, (-tweet.postTime.timestamp(), tweet.tweetId))
        
        # Extract top 10
        top10 = []
        while all_tweets and len(top10) < 10:
            _, tweetId = heapq.heappop(all_tweets)
            top10.append(tweetId)
            
        return top10

    def follow(self, followerId: int, followeeId: int) -> None:
        # Provision both users cleanly
        follower = self._ensure_user_exists(followerId)
        self._ensure_user_exists(followeeId)
        
        # Delegate action directly to the entity
        follower.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].unfollow(followeeId)
