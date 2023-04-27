import os
import shutil
import sys
import json
import glob
import re
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT = 'cloudforet'
TARGET_DIR = os.path.join(BASE_DIR, 'dist')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
DIST_JSON_DIR = os.path.join(BASE_DIR, 'dist', 'json')
DOCS_DIR = os.path.join(BASE_DIR, 'content', 'en')
VERSION = os.path.join(BASE_DIR, 'VERSION')
JINJA_ENV = Environment(
    autoescape=False,
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=False)


def _error(msg):
    print()
    print('[ERROR] %s' % (msg))
    print()
    sys.exit(1)


def _get_files_from_json_file(json_file):
    files = []
    for key, value in json_file.items():
        if key == 'files':
            files.extend(value)
    return files


def _get_messages_from_file(file):
    try:
        messages = {}
        for msg in file.get('messages'):
            messages.update({
                msg.get('name'): msg
            })
        return messages
    except Exception as e:
        _error(f'[ERROR]: {e}')


def _get_services_from_file(file):
    return file['services']


def _get_rpcs_from_services(services):
    rpcs = {}
    for service in services:
        rpcs.update({
            service.get('name'): service.get('methods')
        })
    return rpcs


def _get_service_name_from_file_path(file_path):
    return file_path.split('/')[-1].split('.')[0]


def _get_markdown_path_from_json_file_path(json_file_path):
    return os.path.join(BASE_DIR, DOCS_DIR, *json_file_path.split('/')[-3:-1]).lower()


def _modify_file_format_to_markdown(file):
    _pattern = r'\.json$'
    return re.sub(_pattern, '.md', file)


def _get_optional_and_description(description):
    description_lines = description.split('\n')
    for idx, line in enumerate(description_lines):
        if line.replace(' ', '').strip('+').lower() == 'optional':
            return 'Optional', '\n'.join(description_lines[:idx])
    return 'Required', description


def _make_output_path(output_dir, markdown_path):
    output_path = os.path.join(output_dir, markdown_path)

    if not os.path.exists(output_path):
        os.makedirs(output_path, exist_ok=True)


def _update_description_and_required_field(messages):
    for message_name, value in messages.items():
        for field in value.get('fields'):
            _description = field.get('description', None)
            _optional, _description = _get_optional_and_description(_description)
            field.update({
                'description': _description,
                'required': _optional
            })
        value['sorted_field'] = sorted(value.get('fields'), key=lambda x: x.get('required'), reverse=True)


def _make_markdown_file(json_file_path):
    try:
        with open(os.path.join(json_file_path), 'r') as _json_file:
            service_name = _get_service_name_from_file_path(json_file_path)
            _json_file_context = json.load(_json_file)
            _files_in_json_file_context = _get_files_from_json_file(_json_file_context)
            _markdown_path = _get_markdown_path_from_json_file_path(json_file_path)

            _make_output_path(BASE_DIR, _markdown_path)

            for _file in _files_in_json_file_context:
                _messages_in_proto = _get_messages_from_file(_file)
                _services_in_proto = _get_services_from_file(_file)
                _rpcs = _get_rpcs_from_services(_services_in_proto)

                _update_description_and_required_field(_messages_in_proto)

                template = JINJA_ENV.get_template('resource_page.jinja')
                content = template.render(
                    title=service_name,
                    file=_file,
                    messages=_messages_in_proto,
                    services=_services_in_proto,
                    rpcs=_rpcs,
                )

                with open(os.path.join(BASE_DIR, _markdown_path, f'{service_name}.md'), 'w') as f:
                    f.write(content)

                return content
    except Exception as e:
        _error(f"Failed to make markdown file from {json_file_path}\n{e}")


def _get_json_files_path(dist_json_dir):
    return [json_file for json_file in glob.iglob(os.path.join(dist_json_dir, '**', '*.json'), recursive=True)]


def _make_index_markdown_file(_index_path):
    try:
        for sub_dir in os.listdir(_index_path):
            if os.path.isdir(os.path.join(_index_path, sub_dir)):
                _folder_name = sub_dir.split('/')[-1]
                template = JINJA_ENV.get_template('_index_resource.jinja')
                content = template.render(folder_name=_folder_name)
                with open(os.path.join(_index_path, sub_dir, '_index.md'), 'w') as f:
                    f.write(content)

                    template = JINJA_ENV.get_template('_index_service.jinja')
                    content = template.render()
                    with open(os.path.join(_index_path, '_index.md'), 'w') as f:
                        f.write(content)
    except Exception as e:
        _error(f"Failed to make index markdown file from {_index_path}\n{e}")


def _make_intro_markdown_file(path):
    try:
        template = JINJA_ENV.get_template('_index_introduction.jinja')
        content = template.render()
        with open(os.path.join(path, '_index.md'), 'w') as f:
            f.write(content)
    except Exception as e:
        _error(f"Failed to make intro markdown file\n{e}")


def json_to_markdown():
    # Remove directory and files
    if os.path.exists(DOCS_DIR):
        shutil.rmtree(DOCS_DIR)

    os.makedirs(DOCS_DIR)

    json_files_path = _get_json_files_path(TARGET_DIR)

    for json_file_path in json_files_path:
        _make_markdown_file(json_file_path)

    for service in os.listdir(os.path.join(DIST_JSON_DIR, PROJECT, 'api')):
        _index_path = os.path.join(DOCS_DIR, service)
        _make_index_markdown_file(_index_path)

    _make_intro_markdown_file(DOCS_DIR)


if __name__ == '__main__':
    json_to_markdown()