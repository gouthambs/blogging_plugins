from flask_blogging import signals

def get_prev_next_posts(all_posts, current_id):
    """
    :param dict all_posts: all posts with their id and slug
    :param int current_id: id of the currently processing post
    """
    posts = sorted(all_posts.keys())
    result = {}

    for idx, post_id in enumerate(posts):
        if post_id == current_id:
            before_idx, after_idx = idx - 1, idx + 1
            b_id = b_slug = a_id = a_slug = None
            
            if before_idx >= 0:  # current post is first post
                b_id, b_slug = posts[before_idx], all_posts[posts[before_idx]]
            
            if after_idx != len(posts):  # current post is last post
                a_id, a_slug = posts[after_idx], all_posts[posts[after_idx]]
            
            result['before'] = {'id': b_id, 'slug': b_slug}
            result['after'] = {'id': a_id, 'slug': a_slug}
            break

    return result

def get_posts_flow(app, engine, post, meta, post_id, slug):
    all_posts = {}

    for posts in engine.storage.get_posts(count=None):  # get all posts
        all_posts[posts['post_id']] = posts['title']

    post['post_flow'] = get_prev_next_posts(all_posts, post_id)


def register(app):
    signals.page_by_id_fetched.connect(get_posts_flow)
