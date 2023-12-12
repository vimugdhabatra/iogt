# Generated by Django 3.2.23 on 2023-12-12 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("django_comments_xtd", "0008_auto_20200920_2037"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comments", "0004_auto_20230612_1218"),
    ]

    operations = [
        migrations.CreateModel(
            name="CommunityCommentModerationLogEntry",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("action", models.CharField(max_length=255)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="django_comments_xtd.xtdcomment",
                    ),
                ),
                (
                    "moderator",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
