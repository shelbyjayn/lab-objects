class User:
    """An account with a follower count.

    >>> alice = User('alice')
    >>> alice.follow()
    >>> alice.follow()
    >>> alice.unfollow()
    >>> alice.followers
    1
    >>> print(alice)
    @alice
    >>> alice == User('alice')
    True
    """

    def __init__(self, username):
        self.username = username
        self.followers = 0

    def follow(self):
        self.followers += 1

    def unfollow(self):
        if self.followers > 0:
            self.followers -= 1

    def __str__(self):
        return '@' + self.username

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.username == other.username


class Tweet:
    """A post with an author, text, and like count.

    >>> Tweet('alice', 'Game night #Games #Games #BringSnacks!').hashtags()
    ['Games', 'Games', 'BringSnacks!']
    >>> Tweet('bob', 'word#inside is not a tag').hashtags()
    []
    >>> print(Tweet('alice', 'hello world'))
    @alice: hello world
    """

    def __init__(self, author, text):
        self.author = author
        self.text = text
        self.likes = 0

    def like(self):
        self.likes += 1

    def unlike(self):
        if self.likes > 0:
            self.likes -= 1

    def hashtags(self):
        tags = []
        for word in self.text.split():
            if word.startswith('#'):
                tags.append(word[1:])
        return tags

    def __str__(self):
        return '@' + self.author + ': ' + self.text