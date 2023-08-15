from django.db import models
from PIL import Image

RECIPE_IMAGE_SIZE = 500, 500

class Tag(models.Model):
    name = models.CharField(
        verbose_name="Тэг",
        max_length=24,
        unique=True,
    )
    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name

class Ingredient(models.Model):
    name = models.CharField(
        verbose_name="Ингридиент",
        max_length=24,
        unique=True
    )
    measurement_unit = models.CharField(
        verbose_name="Единицы измерения",
        max_length=24,
    )

    def __str__(self) -> str:
        return f"{self.name} {self.measurement_unit}"

    class Meta:
        verbose_name = "Ингридиент"
        verbose_name_plural = "Ингридиенты"
        ordering = ("name",)

class Recipe(models.Model):
    name = models.CharField(
        verbose_name="Название блюда",
        max_length=50,
    )
    tags = models.ManyToManyField(
        verbose_name="Тег",
        related_name="tag_recipes",
        to=Tag,
    )
    ingredients = models.ManyToManyField(
        verbose_name="Ингредиенты блюда",
        related_name="ingr_recipes",
        to=Ingredient,
        through="AmountIngredient",
    )
    amount = models.IntegerField(
        verbose_name='Количество'
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата публикации",
        auto_now_add=True,
        editable=False,
    )
    text = models.TextField(
        verbose_name="Описание блюда",
        max_length=1000,
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name="Время приготовления",
        default=0,
    )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"
        ordering = ("-pub_date",)

    def __str__(self) -> str:
        return self.name

