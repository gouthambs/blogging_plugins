from flask_blogging import signals


def smart_truncate(content, length=100, suffix=' ...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix


def add_index_page_summary(app, engine, posts, meta, count, page):
    length = app.config.get("BLOGGING_SUMMARY_LENGTH", 100)
    suffix = app.config.get("BLOGGING_SUMMARY_SUFFIX", " ...")
    for post in posts:
        post["summary"] = smart_truncate(post["text"], length, suffix)


def register(app):
    signals.index_posts_fetched.connect(add_index_page_summary)
