from rest_framework import permissions, viewsets
from .models import Book, Author, User
from .permissions import IsOwnerOrReadOnly
from .serializers import UserSerializer, BookSerializer, AuthorSerializer
from django_filters.rest_framework import DjangoFilterBackend


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'genre', 'author']


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
