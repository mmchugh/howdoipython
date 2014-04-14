from os import walk, path

from howdoipython.builder import renderer


def build_topics(output_path, topics_path='topics'):
    output_path_template = path.join(output_path, 'topics', '{0}.html')
    full_path = path.join('data', topics_path)

    print output_path, full_path

    if not path.exists(full_path):
        print "Topics path {0} not found.".format(full_path)
        return

    try:
        _, _, files = next(walk(full_path))  # don't care about root / dirs
    except StopIteration:
        print "No topics found in path {0}".format(full_path)
        return

    for topic_file in files:
        topic, extension = path.splitext(topic_file)
        if extension == '.yaml':
            with open(output_path_template.format(topic), "w") as output_file:
                output_file.write(renderer.build_topic_html(topic))
        else:
            print "Unknown type for topic file: {0}".format(topic_file)


def build_all(output_path='output'):
    build_topics(output_path)

if __name__ == '__main__':
    build_all()
