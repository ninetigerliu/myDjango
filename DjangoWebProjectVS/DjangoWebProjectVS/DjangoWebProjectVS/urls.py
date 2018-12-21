"""
Definition of urls for DjangoWebProjectVS.
"""

from datetime import datetime
from django.conf.urls import url

from . import view,testdb,testdbDisplay,search,search2
 
urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^testdbDisplay$', testdbDisplay.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]