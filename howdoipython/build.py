from os import path, makedirs, walk

from howdoipython.builder import renderer, parser


def build_topics(output_path, topics_path='topics'):
    output_path_template = path.join(output_path, 'topics', '{0}.html')

    output_dir = path.dirname(output_path_template)
    if not path.exists(output_dir):
        print "Making topic output dir at {0}".format(output_dir)
        makedirs(output_dir)

    full_path = path.join('data', topics_path)

    if not path.exists(full_path):
        print "Topics path {0} not found.".format(full_path)
        return

    try:
        _, _, files = next(walk(full_path))  # don't care about root / dirs
    except StopIteration:
        print "No topics found in path {0}".format(full_path)
        return

    topic_data = {}

    for topic_file in files:
        topic, extension = path.splitext(topic_file)
        if extension == '.yaml':
            topic_data[topic] = parser.get_topic_data(topic)
        else:
            print "Unknown type for topic file: {0}".format(topic_file)

    for topic, data in topic_data.items():
        file_path = output_path_template.format(topic)
        with open(file_path, "w") as output_file:
            output_file.write(renderer.build_topic_html(topic, data))
        print "Wrote to {0}".format(file_path)


def build_all(output_path='output'):
    build_topics(output_path)

if __name__ == '__main__':
    build_all()
