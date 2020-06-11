import random

class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)
class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    # Create random friendsips
    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        for i in range(num_users):
            self.add_user(f'User {i + 1}')

        # Create friendships
        possible_friends = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                # add friendship in tuples
                possible_friends.append((user_id, friend_id))

        # create shuffled friends from list
        random.shuffle(possible_friends)
        # print('Possible friends: ', possible_friends)
        # number of total friendships is half of the product of number of users and the average number of friends
        total_friends = num_users * avg_friendships // 2
        # get only the number of total friends
        random_friends = possible_friends[:total_friends]
        # print('Random friends: ', random_friends)

        # counter = 0
        # 
        for friends in random_friends:
            # counter += 1
            # Invoke method to fill friendships
            self.add_friendship(friends[0], friends[1])



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        queue = Queue()
        queue.enqueue([user_id]) # add user id to queue

        while queue.size() > 0:
            path_to_current_user = queue.dequeue() # get the current id
            current_user = path_to_current_user[-1] # assign it to current user

            if current_user not in visited: # if user not in visited
                visited[current_user] = path_to_current_user # create id plus path
                # loop over friendships dict of sets to process friends of current friend
                for friend in self.friendships[current_user]:
                    path_to_friend = [*path_to_current_user, friend]
                    queue.enqueue(path_to_friend)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print('Random friendships: ', sg.friendships)
    connections = sg.get_all_social_paths(1)
    print('Degrees of seperation: ', connections)

    # sg.friends_info(1)
    # sg.average_degree_of_separation(1)

    random_social = {
        1: {9, 3, 5, 7},
        2: set(),
        3: {1, 4},
        4: {8, 10, 3},
        5: {8, 1, 10},
        6: set(),
        7: {1},
        8: {10, 4, 5},
        9: {1},
        10: {8, 4, 5}}

# every user in that user's extended network along with the shortest friendship path
Degrees_of_seperation = {
        1: [1],
        9: [1, 9],
        3: [1, 3],
        5: [1, 5],
        7: [1, 7],
        4: [1, 3, 4],
        8: [1, 5, 8],
        10: [1, 5, 10]}