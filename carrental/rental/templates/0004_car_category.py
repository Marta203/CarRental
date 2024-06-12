from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0003_alter_car_brand_alter_car_engine_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('suv', 'SUV'), ('miejski', 'miejski'), ('terenowy', 'terenowy'), ('van', 'VAN'), ('sportowy', 'sportowy')], default=None, max_length=20),
            preserve_default=False,
        ),
    ]
    