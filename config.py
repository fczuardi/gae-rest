'''
Configuration File

Setup this file according to your application Models as to map their
attributes to the equivalent atom elements.
'''

'''
gae-rest needs to import the files containing your Models since it is
unable to dynamic infer what are all the available entity kinds
(content types) in your application
Example: models = ['my_models.py', 'my_expandos.py']
'''
models = []

'''
which attribute on each Entity can be used as atom <author> element
Example: author = {'Entry': 'author'}
'''
author = {}

'''
<title>
Example: title = {'Entry': 'title'}
'''
title = {}

'''
<content>
Example: content = {'Entry': 'body_html'}
'''
content = {}

'''
<summary>
Example: summary = {'Entry': 'excerpt'}
'''
summary = {}

'''
<published>
Example: published = {'Entry': 'published'}
'''
published = {}

'''
<updated>
Example: updated = {'Entry': 'updated'}
'''
updated = {}