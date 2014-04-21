from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('howdoipython', 'templates'))


def build_topic_html(topic, data):
    template = env.get_template('topic.html')
    return template.render(data)
