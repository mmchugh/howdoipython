from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('howdoipython', 'templates'))

from . import parser

DATA_PATH = 'data/{topic}.yaml'


def build_topic_html(topic):
    context = parser.get_topic_data(DATA_PATH.format(topic))
    template = env.get_template('topic.html')
    return template.render(context)
