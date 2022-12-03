from django.forms import forms
from rest_framework import permissions, viewsets, renderers
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book, Author, User
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, BookSerializer, AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
       Этот набор представлений автоматически обеспечивает `список`, `создать`, `получить`,
       действия «обновить» и «уничтожить».
       Кроме того, мы также предоставляем дополнительное действие «подсветить».
       """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class AuthorViewSet(viewsets.ModelViewSet):
    """
       Этот набор представлений автоматически обеспечивает `список`, `создать`, `получить`,
       действия «обновить» и «уничтожить».
       Кроме того, мы также предоставляем дополнительное действие «подсветить».
       """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
       Этот набор представлений автоматически предоставляет действия `список` и `получить`.
       """
    queryset = User.objects.all()
    serializer_class = UserSerializer
