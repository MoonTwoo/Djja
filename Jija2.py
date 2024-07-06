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

aboba = '''
Sum object = {{(M | max(attribute='prus')).name}}
'''


tm = Template(aboba)
msg = tm.render(M=Moon)

print(msg)