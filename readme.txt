Django comes with inbuilt views and urls for login and logout

Django crispy forms are used to make django forms look pretty and good

For password changing, django has a default url where one can go to change their password provided they are logged in, the url is 127.0.0.1:8000/users/password_change, however this can be customized

To restrict view access to only logged in users, Django has a LoginRequired mixin that we can use. It’s powerful and extremely concise. In the articles/views.py file import it at the top and then add LoginRequiredMixin to our ArticleCreateView. Make sure that the mixin is to the left of ListView so it will be read first. We want the ListView to already know we intend to restrict access. And that’s it! We’re done.