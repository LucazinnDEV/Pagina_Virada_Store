import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_categoria_livro_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='imagem',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='livro',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='livros/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'jpeg'])]),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
