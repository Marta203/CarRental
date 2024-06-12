from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_remove_user_address_address_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='Marka'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(choices=[('benzynowy', 'Benzynowy'), ('diesel', 'Diesel'), ('hybrydowy', 'Hybrydowy'), ('elektryczny', 'Elektryczny'), ('wodorowy', 'Wodorowy')], max_length=20, verbose_name='Typ silnika'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50, verbose_name='Model'),
        ),
    ]