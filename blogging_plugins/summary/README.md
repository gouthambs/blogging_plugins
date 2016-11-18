# Summary Plugin

This plugin adds a summary to each post in the index page. In order
to add to the view, you can add the summary by accessing the `post.summary`
attribute in the template view.

    {% if post.summary %}
        {{ post.summary }}
    {% endif %}
    
This plugin allows for some customization using the following 
configuration variables. 

- `BLOGGING_SUMMARY_LENGTH` (*int*): The number characters allowed in the summary. The default is 100 characters.
- `BLOGGING_SUMMARY_SUFFIX` (*str*): The suffix to use at the end of summary. The default is a trailing triple dot ` ...`.
