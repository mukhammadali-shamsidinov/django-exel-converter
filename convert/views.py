from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from openpyxl import Workbook
import pandas as pd
from openpyxl.writer.excel import save_workbook

# Create your views here.

wb = Workbook()
ws = wb.active
from django.views import View

from .models import UserData


class UserView(View):
    def get(self,request):
        users = UserData.objects.all().values("fname","lname","phone_number","adress")
        df = pd.DataFrame(list(users))

        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=users.xlsx'

        with pd.ExcelWriter(response, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Users')


        return response





