from django.shortcuts import render
from django.views.generic import View
from .models import Employee
from django.core.serializers import serialize
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from django.http import JsonResponse
from .forms import empform

@method_decorator(csrf_exempt,name='dispatch')
class home(View):
    def get(self,r,*args,**kwargs):
        id=r.body

        try:
            id=r.body
            id=json.loads(id)
        except:
            id=1
        o=Employee.venu.all()

        s_d=serialize('json',o)
        return JsonResponse(s_d,safe=False)

    def post(self,r,*args,**kwargs):
        id=r.body
        print(id)
        try:
            p_data=json.loads(id)
            print("babudui")
            print(p_data)

            form=empform(p_data)
            if form.is_valid():
                form.save(commit=True)
            print("venu")
            if form.errors:
                json_data=json.dumps(form.errors)



        except Exception as e:
            print(e)
            return JsonResponse("something went wrong ",safe=False)
        else:

            return JsonResponse("all good posted ",safe=False)
    def put(self,r,*args,**kwargs):
        j_data=r.body
        p_data=json.loads(j_data)
        #now we have python dict which we should modify with old how to get the old one
        id=p_data.get('id')
        #now we have the id we can get the data old
        obj=Employee.venu.get(id=id)
        #now this is in the object form we have to convert this to the dict form
        old_data={
        "eno":obj.eno,
        'ename':obj.ename,
        'esal':obj.esal,
        'eadd':obj.eadd
        }

        #since we have the old we can just update the data directly using update fucntion of the dict

        old_data.update(p_data)
        form = empform(old_data,instance=obj)
        if form.is_valid():
            form.save()
        else:
            return JsonResponse("something went wrong",safe=False)

        return JsonResponse("this is from put",safe=False)

    def delete(self,r,*args,**kwargs):
        data=r.body
        # now we have this in the format of json
        j_data=json.loads(data)
        id = j_data.get('id')
        #now we have the id we can get instance by this and then delete this
        obj = Employee.venu.get(id=id)
        obj.delete()
        return JsonResponse("this from delete method",safe=False)
