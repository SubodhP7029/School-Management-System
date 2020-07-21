from django.db import models

# Create your models here.

class Student(models.Model):

    classes = (
        (1, "1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
        (6,"6"),
        (7,"7"),
        (8,"8"),
        (9,"9"),
        (10,"10")
    )

    section = (
        ("A","A"),
        ("B", "B"),
        ("C", "C"),
        ("d", "D")
    )

    general_register_number = models.IntegerField(blank=False,null=False)
    student_name = models.CharField(blank=False, null=False, max_length=50)
    birthdate = models.DateField(null=True, blank=True)
    father_name = models.CharField(blank=True, null=True, max_length=50)
    mother_name = models.CharField(blank=True, null=True, max_length=50)
    caste = models.CharField(blank=True, null=True, max_length=50)
    birth_place = models.CharField(blank=True, null=True, max_length=50)
    admission_date = models.DateField(null=True, blank=True)
    standard = models.IntegerField(choices=classes,null=False,blank=False)
    division = models.CharField(choices=section, null=True, blank=True, max_length=50)

    def __str__(self):
        return self.student_name

