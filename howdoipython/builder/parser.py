import pkg_resources
import yaml


def get_topic_data(topic_path):
    data_source = pkg_resources.resource_string('howdoipython', topic_path)
    data = yaml.safe_load(data_source)
    if 'further_topics' in data:
        topics = data.pop('further_topics')
        data['further_topics'] = []
        for topic in topics:
            data['further_topics'].append(
                {'title': topic, 'link': '/topics/{0}.html'.format(topic)}
            )
    return data
