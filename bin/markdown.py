import os
import sys
import json
import glob
import yaml
import shutil
import re
from jinja2 import Environment, FileSystemLoader
from pydash import _

PROJECT = 'spaceone'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(BASE_DIR, 'artifact')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'template/markdown')
VERSION = os.path.join(BASE_DIR, 'VERSION')
TEMPLATE_NAMES = ['single_pb_page.jinja', 'summary.jinja', 'readme.jinja', 'version_records.jinja']
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(TEMPLATE_DIR),
    trim_blocks=False)

def _error(msg):
    print()
    print('[ERROR] %s' % (msg))
    print()
    sys.exit(1)

def _generate_md_file(output_file, template, context_input):
    with open(output_file, 'w') as f:
         markdown = render_template(template, context_input)
         f.write(markdown)

def create_reference_json():
    origin_json_files = _get_json_file_path(TARGET_DIR)
    return origin_json_files

def _get_json_data(file_path):
    with open(file_path) as json_file:
        json_data = json.load(json_file)
        return json_data

def _get_json_file_path(json_path):
    all_file_list = [proto_file for proto_file in glob.iglob(os.path.join(json_path, '**', '**', '*.json'), recursive=True)]
    all_file_list.sort()
    return all_file_list

def description_splitter(desc_json):
    returnable_value = ""
    context = ['desc:', 'note:', 'is_required:', 'request_example:', 'response_example:']
    try:
        splitted_json = re.split(r'(desc:|note:|is_required:|request_example:|response_example:|etc\s)\s*', desc_json)
        new_formatted_json = {}
        for idx, val in enumerate(splitted_json):
            if (val in context):
                key = val.replace(" ", "")
                key = val.replace(":", "")
                value = splitted_json[idx+1].replace('\n', '')
                if('>-' in value):
                    json_str = value.replace('>-', '')
                    try:
                        parsed_json = json.loads(json_str)
                        beautified = json.dumps(parsed_json, indent=4, sort_keys=False)
                        value = beautified
                    except Exception as e:
                        value = json.loads(json_str)

                new_formatted_json[key] = value

        print(new_formatted_json)
        returnable_value = new_formatted_json
    except Exception as ex:
        returnable_value = ""
    return returnable_value

def _modify_yaml_to_json(desc):
    parsing_str = None
    json_str = None
    flag = 0
    try:
        flag = 1
        parsing_str = yaml.safe_load(desc)
    except:
        flag = 2
        parsing_str = description_splitter(desc)

    if parsing_str == "":
        json_str = ""
    elif parsing_str is not None:
        loaded_json_str = json.dumps(parsing_str)
        json_str = json.loads(loaded_json_str)
    else:
        json_str = ""

    return json_str

def get_file_syntax(file_path):
    file_syntax = {}
    file_str = file_path.split('/')
    fname = file_str[len(file_str) - 1]
    file = fname.split('.')
    file_syntax['title'] = file[0].replace('_', ' ')
    file_syntax['header'] = file[0].replace('_', '-')
    file_syntax['full_name'] = file[0].replace('_', '-')+'.md'
    return file_syntax

def key_path_creator(path):
    divide_path = path.split('/')
    appendable = False
    key_to_append = ""
    for pieces in divide_path:
        if appendable:
            key_to_append += '/'+ pieces
        if pieces == 'artifact':
            appendable = True
    return key_to_append

def field_desc_wrapper(desc):
    fd_desc = _modify_yaml_to_json(desc)
    if ('is_required' in fd_desc):
        if (fd_desc['is_required'] == True):
            fd_desc['is_required'] = '✅'
        elif (fd_desc['is_required'] == False):
            fd_desc['is_required'] = '❌'
        else:
            fd_desc['is_required'] = ''
    if ('desc' in fd_desc):
        if (fd_desc['desc']) is None:
            fd_desc['desc'] = ''
    return fd_desc


def field_full_type_wrapper(fname, field, refer_link, package):
    if field["fullType"] in [*refer_link]:
        field["fullType_link"] = refer_link[field["fullType"]]

    elif field["fullType"].startswith(package, 0, len(package)):
        type_name_index = field["fullType"].rfind('.') + 1
        length = len(field["fullType"])
        field["fullType_link"] = fname['full_name']+'#'+field["fullType"][type_name_index:length].lower()

def field_long_type_wrapper(message, field, long_dict):
     if field['longType'] in long_dict:
         message['is_table'] = True
         field['enum_links'] = long_dict[field['longType']]

def is_exists_in_same_file(reference_context, method, fname):
    req = method['requestType']
    res = method['responseType']
    if (req in reference_context):
        method['req_link'] = fname['full_name']+'#'+method['requestLongType'].lower()
    if (res in reference_context):
        method['res_link'] = fname['full_name']+'#'+method['responseLongType'].lower()

# Get Enum values into dick forms
def get_enums_dict(enums):
    dict = {}
    for enum in enums:
        dict[enum['longName']] = enum['values']
    return dict

# Create a JSON2 from JSON1
def create_modified_json(reference_files):
    config = _get_json_data(os.path.join(BASE_DIR, 'config.json'))
    refer_link = _.get(config, 'refer_link')
    origin_json_files = _get_json_file_path(TARGET_DIR)

    if len(origin_json_files) == 0:
        _error(f"JSON not found at ({TARGET_DIR})")
    else:
        total_dictionary = {}
        for json_path in origin_json_files:
            fname = get_file_syntax(json_path)
            full_single_json = _get_json_data(json_path)
            single = _.get(full_single_json, 'files')
            total_dictionary[key_path_creator(json_path)] = full_single_json
            for obj in single:
                new_desc = _modify_yaml_to_json(obj['description'])
                _.set(obj, 'description', new_desc)
                package = obj['package']
                enums = get_enums_dict(obj['enums'])
                services = _.get(obj, 'services')
                messages = _.get(obj, 'messages')
                message_names = [a['name'] for a in messages]

                for service in services:
                     for method in service['methods']:
                         is_exists_in_same_file(message_names, method, fname)

                         svc_desc = _modify_yaml_to_json(method['description'])
                         method['description'] = svc_desc
                         google_api = _.get(method, 'options')

                         if(google_api is not None):
                            rest_apis = google_api['google.api.http']['rules']
                            method['restAPI'] = rest_apis

                         if method['responseFullType'] in [*refer_link]:
                             method['responseFullType_link'] = refer_link[method['responseFullType']]

                for message in messages:
                    for field in message["fields"]:
                        field_long_type_wrapper(message, field, enums)
                        field['description'] = field_desc_wrapper(field['description'])
                        field_full_type_wrapper(fname, field, refer_link, package)

            full_single_json['file_info'] = fname
        return total_dictionary


def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def _create_subdirectories(input_path):
    if not os.path.exists(input_path):
        os.makedirs(input_path)

def _generate_single_pb_mds(context_input):
    for key, value in context_input.items():
        ff_name = key.replace(".json", ".md")
        dic_name = ff_name[ff_name.find('api')+4:len(ff_name)].split('/')
        f_name = dic_name[len(dic_name)-1].replace('_','-')

        path_to_create = BASE_DIR
        print(value)
        for i in range(len(dic_name)):
            if(i == len(dic_name)-1):
                continue
            else:
                path_to_create = path_to_create + '/' + dic_name[i]
                _create_subdirectories(path_to_create)

        context_output = os.path.join(path_to_create, f_name)
        context_input = value
        _generate_md_file(context_output, TEMPLATE_NAMES[0], context_input)

def _generate_summary_mds(context_input, managed_link, history):
    table_of_contents = {}
    title_index = []
    for path in context_input:

        file_info = get_file_syntax(path)
        full_path = path[path.find('api/') + 4:len(path)].replace('.json', '.md')
        parsed_path = full_path.split('/')
        parsed_path[len(parsed_path) - 1] = parsed_path[len(parsed_path) - 1].replace('_', '-')
        full_file_name = '/'.join(parsed_path)
        parsed_path[len(parsed_path)-1] = file_info['title']
        base_bullet = '* '
        check_key = ""

        for i in range(len(parsed_path)):
            if(i != 0 ):
                check_key = check_key+'.'+parsed_path[i]
                base_bullet = '  ' + base_bullet
            else:
                check_key = parsed_path[i]

            updated_header = base_bullet + '[' + parsed_path[i] + ']'
            if(_.get(table_of_contents, check_key, None) == None ):
                if(i == (len(parsed_path)-1)):
                    _.set(table_of_contents, check_key, {})
                    title_index.append({'title': updated_header.title(), 'url': full_file_name})
                else:
                    mk_path = check_key.replace('.', '/')
                    readme_url = mk_path + '/'+ 'README.md'
                    readme_path = os.path.join(BASE_DIR, mk_path, 'README.md')

                    if not os.path.exists(readme_path):
                        _generate_md_file(readme_path, TEMPLATE_NAMES[2], '')

                    _.set(table_of_contents, check_key, {})
                    title_index.append({'title': updated_header.title(), 'url': readme_url})

    if ('version_record' in history and len(history['version_record']) > 0):
        vtable_of_contents = []
        previous_version_md = os.path.join(BASE_DIR, 'previous_version', 'README.md')

        for version in history['version_record']:
            line = f'* [{version}](previous_version/{version}/)'
            vtable_of_contents.append(line)

        _generate_md_file(previous_version_md, TEMPLATE_NAMES[3], {'list': vtable_of_contents})

    output_to_create = os.path.join(BASE_DIR, 'SUMMARY.md')
    context_input = {'toc': title_index}
    context_input['managed_link'] = _normalize_managed_link(managed_link)
    context_input['history'] = history
    _generate_md_file(output_to_create, TEMPLATE_NAMES[1], context_input)


def _normalize_managed_link(managed_link):
    n_normalized = {}
    for key, value in managed_link.items():
        n_key = key.replace('_',' ').title()
        n_value = value
        n_normalized[n_key] = n_value
    return n_normalized

def _delete_json1(json_path):
    if os.path.exists(json_path):
        shutil.rmtree(json_path, ignore_errors=True)

def _get_current_api_version():
    with open(VERSION, 'r') as f:
        version = f.read().strip()
        f.close()
        return version

def _get_artifact_version(f_path):
        begin_index = f_path.rfind('artifact/json/') + 14
        version = f_path[begin_index: len(f_path)].split('/')[0]
        return version

def _transfer_previous_doc(folders, pwd):
    version_readme = os.path.join(pwd, 'README.md')
    if not os.path.isfile(version_readme):
        _generate_md_file(version_readme, TEMPLATE_NAMES[2], '')

    for fd in folders:
        src_f = os.path.join(BASE_DIR, fd)
        tar_f = os.path.join(pwd, fd)
        if not os.path.exists(tar_f):
            shutil.move(src_f, pwd)

def _get_original_history():
    filepath = os.path.join(BASE_DIR, 'SUMMARY.md')
    all_previous_ref = []
    with open(filepath) as fp:
        is_previous_v = False
        for line in fp:
            if(line.find('Previous Versions') > 0):
                 is_previous_v = True

            if(is_previous_v):
                if (line.find('[Previous Versions]') > 0):
                    continue

                line = line.replace('\n', '')
                check_path = os.path.join(BASE_DIR, line[line.find('](') + 2: line.rfind(')')])
                if os.path.isfile(check_path):
                    all_previous_ref.append(line)

        # if(len(all_previous_ref) > 0):
        #     all_previous_ref.pop(0)
    return all_previous_ref

def _get_summary_info(version_info):
    filepath = os.path.join(BASE_DIR, 'SUMMARY.md')
    vinfo = version_info['current_version']
    previous_summary = {}
    mfolder_name = []
    line_contents = [f'* [Previous Versions](previous_version/README.md)', f'  * [v{vinfo}](previous_version/v{vinfo}/README.md)']

    with open(filepath) as fp:
        is_summary = False
        for line in fp:
            if(line.find('Table of contents') > 0):
                is_summary = True
            elif(line.find('Reference Link') > 0):
                is_summary = False

            if(is_summary):
                line = line.replace('\n', '')
                common_indent = '    '
                line_checker = line[0: line.find('](')]
                if(line_checker.startswith('*')):
                    mfolder_name.append(line[line.find('](')+2:line.find('/')])
                if(line.find('*') > -1):
                    pre = 'previous_version'
                    head = line[0:line.find('](')]
                    body = line[line.find('](') + 2: line.find('/')]
                    tail = line[line.find('/'): len(line)]
                    m_line = f'{common_indent}{head}]({pre}/v{vinfo}/{body}{tail}'
                    # check_path = os.path.join(BASE_DIR, m_line[m_line.find('](') + 2: m_line.rfind(')')])
                    # print(check_path)
                    # if os.path.isfile(check_path):
                    line_contents.append(m_line)

        previous_summary['title_lines'] = line_contents
        previous_summary['movable_fd'] = mfolder_name

    return previous_summary

def _diff_version(f_path):
    current_version = _get_current_api_version()
    artifact_version = _get_artifact_version(f_path)
    version = {}
    version['current_version'] = current_version
    version['artifact_version'] = artifact_version
    if(artifact_version > current_version):
        version['is_updated'] = True
    else:
        version['is_updated'] = False
    return version

def _get_version_records():
    path_to_check = os.path.join(BASE_DIR, 'previous_version')
    root, dirs, files = next(os.walk(path_to_check))
    return dirs

def _get_human_doc_links():
    config = _get_json_data(os.path.join(BASE_DIR, 'config.json'))
    human_doc_links = _.get(config, 'human_doc_links')
    return human_doc_links

def _update_current_version(file_path, version_info):
    with open(file_path, "r+") as f:
        f.seek(0)
        f.write(version_info)
        f.close()

def _update_summary_infos(version_info, ref_info):
    pre_v = 'previous_version'
    previous_summary = _get_summary_info(version_info)
    ref_info['added_history'] = previous_summary['title_lines']
    p_base_folder = os.path.join(BASE_DIR, pre_v)
    p_folder = os.path.join(BASE_DIR, pre_v, 'v' + version_info['current_version'])

    _create_subdirectories(p_base_folder)
    _create_subdirectories(p_folder)
    _transfer_previous_doc(previous_summary['movable_fd'], p_folder)


def main():
    file_reference = create_reference_json()
    if len(file_reference) == 0:
        _error("No artifact JSON")
    else:
        version_info = _diff_version(file_reference[0])
        ref_info = {}
        pre_v = 'previous_version'
        if(version_info['is_updated']):
            _update_summary_infos(version_info, ref_info)

        json2 = create_modified_json(file_reference)
        man_managed = _get_human_doc_links()
        _generate_single_pb_mds(json2)
        origin_history = _get_original_history()

        if os.path.exists(os.path.join(BASE_DIR, pre_v)):
            version_records = _get_version_records()
            if (len(version_records) > 0):
                ref_info['version_record'] = version_records
            if (len(origin_history) > 0):
                print(origin_history)
                ref_info['origin_history'] = origin_history

        _generate_summary_mds(file_reference, man_managed, ref_info)
        _update_current_version(VERSION, version_info['artifact_version'])
        _delete_json1(TARGET_DIR)

if __name__ == '__main__':
    main()