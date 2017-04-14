# PostsFlow Plugin

This plugin adds previous and next post entry to each blog entry. This **may** increase
in getting more page views. In order to add this to the view, you can check by accessing
`post.post_flow` attribute in page template.

    {% if post.post_flow and post.post_flow.before.id %}
        <a href="{{ url_for('blogging.page_by_id', page_id=post.post_flow.before.id) }}" title="See previous post...">
            {{ post.post_flow.before.slug }}
        </a> 
    {% endif %}
    {% if post.post_flow and post.post_flow.after.id %}
        <a href="{{ url_for('blogging.page_by_id', page_id=post.post_flow.after.id) }}" title="See next post...">
            {{ post.post_flow.after.slug }}
        </a> 
    {% endif %}

*If you are using bootstrap then please use proper classes to align these elements*
