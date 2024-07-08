from jinja2 import Template

#data ='''in HTML  <a href="#">smt</a>'''
#tm = Template('{{data|e}}')
#msg = tm.render()

Moon = [{'id': 1, 'name': "Moon1", 'prus':200},
        {'id': 4, 'name': "Moon2", 'prus':500},
        {'id': 7, 'name': "Moon3", 'prus':400}]

#aboba = '''{% for i in M-%}
#{% if i.id>=4-%}
#I love Moon number  {{i.id}} its name is {{i.name}}
#{%endif-%}
#{%endfor-%}'''

# aboba = '''
# Sum object = {{(M | max(attribute='prus')).name}}
# '''

# aboba = '''
# {% for i in M-%}
# {%filter upper%}i love {{i.name}}{%endfilter%}
# {%endfor-%}'''

aboba = '''
{% macro abo (name, value ='abor', size = 20)-%}
name ={{name}}, value ={{value}}, size = {{size}}
{%-endmacro%}
{{abo('pass', 'abo', 30)}}
{{abo('ed', 40, 50)}}
{{abo()}}
'''

tm = Template(aboba)
msg = tm.render()

print(msg)