import time
class MiniTwitter:

    def __init__(self):
        # initialize your data structure here.
        self.followr = {}
        self.tweet = {}

    # @param {int} user_id
    # @param {str} tweet
    # @return {Tweet} a tweet
    def postTweet(self, user_id, tweet_text):
        # Write your code here
        #
        t = Tweet(user_id, tweet_text)
        #t = t.create()
        #t = tweet_text
        ts = time.time()
        if user_id not in self.tweet:
            self.tweet[user_id] = [(t,ts)]
        else:
            q = self.tweet[user_id]
            q.append((t,ts))
        return t

    # @param {int} user_id
    # return {Tweet[]} 10 new feeds recently
    # and sort by timeline
    def getNewsFeed(self, user_id):
        # Write your code here
        timeline = []
        res, rem = [], []
        if user_id in self.followr:
            for follower_id in self.followr[user_id]:
                if follower_id in self.tweet:
                    timeline += self.tweet[follower_id]
        if user_id in self.tweet:
            timeline += self.tweet[user_id]
        if timeline:
            timeline = sorted(timeline, key=lambda x:x[1], reverse=True)
            res, rem = zip(*timeline[:10]) 
        return res
        
        

        
    # @param {int} user_id
    # return {Tweet[]} 10 new posts recently
    # and sort by timeline
    def getTimeline(self, user_id):
        # Write your code here
        res, rem = [], []
        q = None
        if user_id in self.tweet:
            q = self.tweet[user_id]
        if q:
            q = sorted(q, key=lambda x:x[1], reverse=True)
            res, rem = zip(*q[:10]) 
        return res
            
            


    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id follows to_user_id
    def follow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id not in self.followr:
            self.followr[from_user_id] = [to_user_id]
        else:
            self.followr[from_user_id].append(to_user_id)
        return True

    # @param {int} from user_id
    # @param {int} to_user_id
    # from user_id unfollows to_user_id
    def unfollow(self, from_user_id, to_user_id):
        # Write your code here
        if from_user_id in self.followr:
            self.followr[from_user_id].remove(to_user_id)
        return True