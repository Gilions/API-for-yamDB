from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.constraints import UniqueConstraint


class Roles(models.TextChoices):
    user = 'user'
    moderator = 'moderator'
    admin = 'admin'


class MyUser(AbstractUser):
    email = models.EmailField(
        max_length=50,
        help_text='Электронная почта пользователя',
        verbose_name='Электронная почта',
        unique=True,
    )
    bio = models.CharField(
        max_length=255,
        help_text='Информация о пользователе',
        verbose_name='Информация',
        blank=True,
    )
    role = models.CharField(
        choices=Roles.choices,
        default=Roles.user,
        max_length=50,
        help_text='Права пользователя',
        verbose_name='Права',
    )

    @property
    def is_moderator(self):
        return self.is_staff or self.role == Roles.moderator

    @property
    def is_admin(self):
        return self.is_superuser or self.role == Roles.admin

    class Meta:
        ordering = ['email']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Максимальная длина, 200 символов.'
    )
    slug = models.SlugField(
        verbose_name='Ссылка',
        unique=True,
        max_length=10,
        help_text='Содержание уникальное, длиной до 10 символов.'

    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Максимальная длина, 200 символов.'
    )
    slug = models.SlugField(
        verbose_name='Ссылка',
        unique=True,
        max_length=10,
        help_text='Содержание уникальное, длиной до 10 символов.'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Максимальная длина, 200 символов.'
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='Год',
        db_index=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        help_text='Необязательное к заполнению.'
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанр',
        related_name='titles',
        help_text='Необязательное к заполнению.'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Категория',
        related_name='titles',
        help_text='Необязательное к заполнению.'

    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(
        MyUser,
        help_text='Автор отзыва',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор отзыва',
    )
    title = models.ForeignKey(
        Title,
        help_text='Произведение, на которое сделан отзыв',
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение',
    )
    text = models.TextField(
        help_text='Отзыв пользователя',
        verbose_name='Отзыв',
    )
    score = models.PositiveSmallIntegerField(
        help_text='Оценка пользователя',
        validators=[
            MinValueValidator(1, 'Оценка не может быть меньше 1.'),
            MaxValueValidator(10, 'Оценка не может быть больше 10.')
        ],
        verbose_name='Оценка',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text='Дата добавления отзыва',
        verbose_name='Дата добавления',
    )

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review',
            )
        ]
        ordering = ['title']
        verbose_name = 'Отзыв пользователя'
        verbose_name_plural = 'Отзывы пользователей'

    def __str__(self):
        fragment = (
            self.text if len(self.text) <= 50 else self.text[:50] + '...'
        )
        date = self.pub_date.strftime('%d %m %Y')
        author = self.author
        return f'{author} - {date} - {fragment}'


class Comment(models.Model):
    author = models.ForeignKey(
        MyUser,
        help_text='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
    )
    text = models.TextField(
        help_text='Комментарий пользователя',
        verbose_name='Комментарий',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        help_text='Дата добавления комментария',
        verbose_name='Дата добавления',
    )
    review_id = models.ForeignKey(
        Review,
        help_text='Комментируемый отзыв',
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментируемый отзыв',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий пользователя'
        verbose_name_plural = 'Комментарии пользователей'

    def __str__(self):
        fragment = (
            self.text if len(self.text) <= 50 else self.text[:50] + '...'
        )
        date = self.pub_date.strftime('%d %m %Y')
        author = self.author
        return f'{author} - {date} - {fragment}'
