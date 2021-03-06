# Generated by Django 2.2.12 on 2020-06-15 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ablum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ablum_name', models.CharField(max_length=50)),
                ('release_year', models.IntegerField(choices=[(1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2020, verbose_name='year')),
                ('cover', models.ImageField(upload_to='cover')),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_name', models.CharField(max_length=30)),
                ('total_song', models.IntegerField(default=0)),
                ('singer_img', models.ImageField(upload_to='singerImg')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_order', models.IntegerField(default=0)),
                ('song_name', models.CharField(max_length=50)),
                ('song_singer', models.CharField(max_length=50)),
                ('song_source', models.FileField(upload_to='source')),
                ('song_type', models.CharField(choices=[('Pop', 'Pop'), ('J-Pop', 'J-Pop'), ('Jazz', 'Jazz'), ('Classic', 'Classic'), ('Blue', 'Blue'), ('EDM', 'EDM'), ('Other', 'Other')], default='Pop', max_length=7)),
                ('language_type', models.CharField(choices=[('CH', '中文'), ('JP', '日文'), ('EN', '英文'), ('OTH', '其他')], default='CH', max_length=2)),
                ('ablum_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ablum', to='main.Ablum')),
                ('release_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='year', to='main.Ablum')),
            ],
        ),
        migrations.CreateModel(
            name='LikeSong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_like', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ablum',
            name='ablum_singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='singer', to='main.Artist'),
        ),
        migrations.AddField(
            model_name='ablum',
            name='upLoad_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploadUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
