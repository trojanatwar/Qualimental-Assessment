from sqlalchemy.sql.functions import user
from .model import DBSession, Page, User
from pyramid.view import view_config
from pyramid.response import Response

from pyramid.view import (
    view_config,
    forbidden_view_config,
    )

from pyramid.security import (
    remember,
    forget,
    )

from pyramid.httpexceptions import (
    HTTPFound,
    HTTPNotFound,
    )


@view_config(route_name='home', renderer="json")
def home(request):
    # Make a view that accepts user id and returns a list of all Page titles that are owned by the user
    return "Home Page"


@view_config(route_name='wiki_view', renderer='json')
def wiki_view(request):
    # Make a view that accepts user id and returns a list of all Page titles that are owned by the user
    li = []
    uid = request.matchdict['uid']
    
    data = DBSession.query(Page).\
           filter(Page.uid == int(uid)).\
           all()

    for r in data:
        li.append({"Id": r.uid, "Title": r.title})
    
    return li

@view_config(route_name='login', renderer='templates/login.pt')
@forbidden_view_config(renderer='templates/login.pt')
def login(request):
    headers = remember(request, 1)
    return HTTPFound(location = request.route_url('wiki_view'), headers = headers)

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    return HTTPFound(location = request.route_url('wiki_view'),
                     headers = headers)