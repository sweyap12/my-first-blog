from django.db import models
from django.utils import timezone
from django.conf import settings

# from openpyxl import load_workbook
# import os
#
# # Create your models here.
#
# # Create relative path for Excel file
# file_name = 'rada_excel.xlsx'
# file_path = os.path.join(os.path.expanduser('~'), 'Desktop', file_name)
#
# # Working on Excel
# req = ['TEST-2', 'TEST-3', 'TEST-4']
# work_book = load_workbook(file_path, read_only=False, data_only=True)
# sheet = work_book.active  # Hope there is only one sheet in Excel
# func_names = [fn.value for ids, fn in zip(sheet['A:B'][0], sheet['A:B'][1]) if ids.value in req]
# print(func_names)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
