# Generated by Django 5.1.6 on 2025-02-28 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("institution", models.CharField(max_length=200)),
                ("degree", models.CharField(max_length=200)),
                ("time_period", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "order",
                    models.IntegerField(
                        default=0,
                        help_text="Order to display (lower numbers shown first)",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Education",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company", models.CharField(max_length=200)),
                ("position", models.CharField(max_length=200)),
                ("time_period", models.CharField(max_length=100)),
                ("description", models.TextField()),
                (
                    "order",
                    models.IntegerField(
                        default=0,
                        help_text="Order to display (lower numbers shown first)",
                    ),
                ),
            ],
            options={
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=200)),
                ("message", models.TextField()),
                ("date_sent", models.DateTimeField(auto_now_add=True)),
                ("is_read", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=200)),
                (
                    "profile_image",
                    models.ImageField(blank=True, upload_to="profile_images/"),
                ),
                ("logo_image", models.ImageField(blank=True, upload_to="logo_images/")),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("location", models.CharField(max_length=100)),
                ("bio", models.TextField()),
                ("experience_years", models.IntegerField(default=0)),
                ("linkedin", models.URLField(blank=True)),
                ("github", models.URLField(blank=True)),
                ("twitter", models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "proficiency",
                    models.IntegerField(help_text="Proficiency percentage (0-100)"),
                ),
                (
                    "skill_type",
                    models.CharField(
                        choices=[
                            ("technical", "Technical Skill"),
                            ("professional", "Professional Skill"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Technology",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Technologies",
            },
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="project_images/")),
                ("demo_url", models.URLField(blank=True)),
                ("source_code_url", models.URLField(blank=True)),
                ("featured", models.BooleanField(default=False)),
                ("technologies", models.ManyToManyField(to="portfolio_app.technology")),
            ],
        ),
    ]
