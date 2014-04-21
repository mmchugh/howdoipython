from jinja2 import Environment, PackageLoader
env = Environment(loader=PackageLoader('howdoipython', 'templates'))


def build_topic_html(topic, data):
    template = env.get_template('topic.html')
    return template.render(data)


def build_index_html(data):
    topic_path = 'topics/{0}.html'
    topics = [
        {'topic': topic, 'link': topic_path.format(topic)} for topic in data
    ]
    template = env.get_template('index.html')
    return template.render({'topics': topics})
