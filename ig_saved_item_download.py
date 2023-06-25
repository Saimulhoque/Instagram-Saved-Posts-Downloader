import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to Instagram
loader.login('your username', 'password')

# Get your own profile
profile = instaloader.Profile.from_username(loader.context, 'your username')

# Iterate through saved posts
for post in profile.get_saved_posts():
    # Download the post
    loader.download_post(post, target='saved_posts')
    loader.download_feed_posts(post)


# # Logout
# loader.logout()
