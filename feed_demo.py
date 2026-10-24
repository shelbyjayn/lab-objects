from lab_classes import User, Tweet


def build_feed():
    ace = User('acehigh')
    river = User('riverrat')
    users = [ace, river]

    posts = [
        Tweet('acehigh', 'Poker night Friday at 8 #PokerNight #BringChips'),
        Tweet('riverrat', 'Hit a straight on the river. Sorry everyone #PokerNight'),
        Tweet('acehigh', 'Rematch next week? #Rematch!'),
    ]

    river.follow()
    river.follow()
    river.unfollow()
    ace.follow()

    posts[0].like()
    posts[1].like()
    posts[1].like()
    posts[1].unlike()

    return users, posts


def main():
    users, posts = build_feed()

    print('Accounts:')
    for user in users:
        print(user)

    print()
    print('Posts:')
    for post in posts:
        print(post)
        print(post.hashtags())


if __name__ == '__main__':
    main()