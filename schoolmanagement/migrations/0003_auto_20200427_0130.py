# Generated by Django 3.0 on 2020-04-27 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schoolmanagement', '0002_fourfiveresult_ninetenresult_onetwothreeresult_sixseveneightresult'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='fourfiveresult',
            new_name='Four_Five_Result',
        ),
        migrations.RenameModel(
            old_name='ninetenresult',
            new_name='Nine_Ten_Result',
        ),
        migrations.RenameModel(
            old_name='onetwothreeresult',
            new_name='One_Two_Three_Result',
        ),
        migrations.RenameModel(
            old_name='sixseveneightresult',
            new_name='Six_Seven_Eight_Result',
        ),
        migrations.AlterField(
            model_name='four_five_result',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolmanagement.Student_info'),
        ),
        migrations.AlterField(
            model_name='nine_ten_result',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolmanagement.Student_info'),
        ),
        migrations.AlterField(
            model_name='one_two_three_result',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolmanagement.Student_info'),
        ),
        migrations.AlterField(
            model_name='six_seven_eight_result',
            name='student_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schoolmanagement.Student_info'),
        ),
    ]