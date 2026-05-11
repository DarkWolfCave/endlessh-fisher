"""Initial migration for the notifications app."""

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notification",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("achievement", "Achievement Unlocked"),
                            ("challenge", "Daily Challenge Completed"),
                            ("rare_catch", "Rare Fish Caught"),
                        ],
                        db_index=True,
                        max_length=20,
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("title_de", models.CharField(max_length=200)),
                (
                    "message",
                    models.TextField(blank=True, default="", max_length=500),
                ),
                (
                    "message_de",
                    models.TextField(blank=True, default="", max_length=500),
                ),
                (
                    "emoji",
                    models.CharField(default="\U0001F514", max_length=10),
                ),
                (
                    "rarity",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("common", "Common"),
                            ("uncommon", "Uncommon"),
                            ("rare", "Rare"),
                            ("epic", "Epic"),
                            ("legendary", "Legendary"),
                            ("mythic", "Mythic"),
                            ("bronze", "Bronze"),
                            ("silver", "Silver"),
                            ("gold", "Gold"),
                            ("platinum", "Platinum"),
                            ("diamond", "Diamond"),
                            ("easy", "Easy"),
                            ("medium", "Medium"),
                            ("hard", "Hard"),
                        ],
                        default="",
                        max_length=20,
                    ),
                ),
                (
                    "rarity_color",
                    models.CharField(blank=True, default="", max_length=7),
                ),
                (
                    "achievement_slug",
                    models.SlugField(blank=True, default="", max_length=80),
                ),
                (
                    "challenge_id",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "caught_bot_id",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "is_read",
                    models.BooleanField(db_index=True, default=False),
                ),
                (
                    "toast_shown",
                    models.BooleanField(db_index=True, default=False),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.AddIndex(
            model_name="notification",
            index=models.Index(
                fields=["is_read", "-created_at"],
                name="idx_notif_unread",
            ),
        ),
        migrations.AddIndex(
            model_name="notification",
            index=models.Index(
                fields=["toast_shown", "-created_at"],
                name="idx_notif_toast",
            ),
        ),
        migrations.AddIndex(
            model_name="notification",
            index=models.Index(
                fields=["category", "-created_at"],
                name="idx_notif_category",
            ),
        ),
    ]
