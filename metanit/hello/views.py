from django.shortcuts import HttpResponse
from jinja2 import Template

def index(request, msg):
   # host = request.META["HTTP_HOST"]
   # brows = request.META["HTTP_USER_AGENT"]
   # path = request.path
    data = '''in HTML  <a href="#">smt</a>'''
    tm = Template(data)
    msg = tm.render()
    return HttpResponse(f'''<h2>Приветики!</h2>
                        <p>yfyfy{msg}<p>
                        ''')
def enot(request,name, age):
    return HttpResponse(f"""<h2>О нас<h2>
                        <p>Имя: {name}<p>
                        <p>Возраст: {age}<p>
                        """)
def contact (request):
    return HttpResponse("<h2>Контакты<h2>")
