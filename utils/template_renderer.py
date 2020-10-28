import os
import webbrowser

from jinja2 import Environment, PackageLoader, select_autoescape

"""
context_data = {
    'template_name': template_name,
    'data': data,
    'output': 'output.html' 
 } 

 """


class TemplateRender:
    def __init__(self, data: dict):
        self.template_file_name = data['template_name']  # just template file name
        self.template_dir_path = 'templates\\{}'.format(data['template_name'])

        # self.directory_path = os.path.dirname(os.path.abspath(__file__))
        self.directory_path = os.path.realpath('api')  # path i funksionit qe po e therret
        self.directory_name = os.path.basename(self.directory_path)
        self.template_file_path = os.path.join(self.directory_path, self.template_dir_path)
        # 'C:\Users\User\Desktop\kodi diploma\assistant\api' + 'templates/rofile-list.html'
        self.environment = self.run_environment()
        self.template = self.get_template()
        self.output = data['output']
        self.data = data['data']

        # self.run_environment()
        self.get_template()
        self.render_template()

    def run_environment(self):
        return Environment(
            loader=PackageLoader(self.directory_name, 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def get_template(self):
        return self.environment.get_template(self.template_file_name)

    def render_template(self):
        with open(os.path.join(self.directory_path + '\\templates_cache', self.output), "w", encoding='utf-8') as rendered_file:
            rendered_file.write(self.template.render({'data': self.data}))

        webbrowser.open('file://' + os.path.realpath('api\\templates_cache\\{}'.format(self.output)))
