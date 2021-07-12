import os
import sys
import json
import glob
import yaml
import shutil
import re
from jinja2 import Environment, FileSystemLoader
from pydash import _

"""
 
    BASE_DIR: base directory absolute path of api-doc when script runs by github action
    TARGET_DIR: target directory where artifact has copied through github action from api repository
    TEMPLATE_DIR: directory where templates are located in api-doc repository
    VERSION: path for where version file is located
    TEMPLATE_NAMES: all template file names in /api-doc/template/markdown
    TEMPLATE_ENVIRONMENT: environment for Jinja template to create a md files. 
    
"""

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
    """
        Generate output_file md file with given template, input_contents
           Args:
               output_file': 'str',
               template: 'str'
               context_input: dict
           Returns:
               markdown

    """
    with open(output_file, 'w') as f:
        markdown = _render_template(template, context_input)
        f.write(markdown)


def _create_reference_json():
    """
        get referenced json file list
           Args:

           Returns:
               list
    """
    origin_json_files = _get_json_file_path(TARGET_DIR)
    return origin_json_files


def _get_json_data(file_path):
    """
        get json_data from given json file path
           file_path: str

           Returns:
               dict
    """
    with open(file_path) as json_file:
        json_data = json.load(json_file)
        return json_data


def _get_json_file_path(json_path):
    all_file_list = [proto_file for proto_file in
                     glob.iglob(os.path.join(json_path, '**', '**', '*.json'), recursive=True)]
    all_file_list.sort()
    return all_file_list


def _description_splitter(desc_json):
    returnable_value = ""
    context = ['desc:', 'note:', 'is_required:', 'request_example:', 'response_example:']
    try:
        split_json = re.split(r'(desc:|note:|is_required:|request_example:|response_example:|etc\s)\s*', desc_json)
        new_formatted_json = {}
        for idx, val in enumerate(split_json):
            if val in context:
                key = val.replace(" ", "")
                key = key.replace(":", "")
                value = split_json[idx + 1].replace('\n', '')

                if '>-' in value:
                    json_str = value.replace('>-', '')
                    try:
                        parsed_json = json.loads(json_str)
                        beautified = json.dumps(parsed_json, indent=4, sort_keys=False)
                        value = beautified
                    except Exception as e:
                        print(e)
                        value = json.loads(json_str)

                new_formatted_json[key] = value
        returnable_value = new_formatted_json
    except Exception as e:
        print(e)

    return returnable_value


def _modify_yaml_to_json(desc):
    parsing_str = None
    json_str = None
    try:
        parsing_str = yaml.safe_load(desc)
    except Exception as e:
        parsing_str = _description_splitter(desc)

    if parsing_str == "":
        json_str = ""
    elif parsing_str is not None:
        loaded_json_str = json.dumps(parsing_str)
        json_str = json.loads(loaded_json_str)
    else:
        json_str = ""

    return json_str


def _get_file_name_syntax(file_path: str) -> dict:
    """
        get file's title, header, full_name, full_name_lower
           Args:
                file_path: str

           Returns:
               dict
    """
    file_str = file_path.split('/')
    file_name = file_str[len(file_str) - 1]
    file = file_name.split('.')

    return {
        'title': file[0].replace('_', ' '),
        'header': file[0].replace('_', '-'),
        'full_name': file[0].replace('_', '-') + '.md',
        'full_name_lower': file[0].replace('_', '-').lower() + '.md',
    }


def _key_path_creator(path):
    path_splits = path.split('/')
    appendable = False
    key_to_append = ""
    for pieces in path_splits:
        if appendable:
            key_to_append += '/' + pieces
        if pieces == 'artifact':
            appendable = True
    return key_to_append


def _desc_wrapper(desc):
    """
        Parsing JSON data into parsed proper dict
           Args:
                desc: dict

           Returns:
               dict
    """
    fd_desc = _modify_yaml_to_json(desc)
    if type(fd_desc) is dict and len(fd_desc) > 0:
        if 'is_required' in fd_desc:
            if fd_desc.get('is_required'):
                fd_desc['is_required'] = '✅'
            elif not fd_desc.get('is_required'):
                fd_desc['is_required'] = '❌'
            else:
                fd_desc['is_required'] = ''
        if 'desc' not in fd_desc:
            fd_desc['desc'] = ''

    return fd_desc


def _field_full_type_wrapper(file_name: dict, field: dict, refer_link: dict, package: str) -> None:
    """
        Parsing full_type into proper dict format
           Args:
                file_name: dict,
                field: dict,
                refer_link: dict,
                package: list

           Returns:

    """
    if field["fullType"] in [*refer_link]:
        field["fullType_link"] = refer_link[field["fullType"]]

    elif field["fullType"].startswith(package, 0, len(package)):
        type_name_index = field["fullType"].rfind('.') + 1
        length = len(field["fullType"])
        field["fullType_link"] = file_name['full_name'].lower() + '#' + field["fullType"][type_name_index:length].lower()


def _field_long_type_wrapper(message, field, long_dict):
    """
        Parsing long_type into proper dict format
           Args:
                message: dict,
                field: dict,
                long_dict: list

           Returns:
               dict
    """
    if field['longType'] in long_dict:
        message['is_table'] = True
        field['enum_links'] = long_dict[field['longType']]


def _is_exists_in_same_file(reference_context, method, file_name):
    """
        Parsing Enums into proper dict format
           Args:
                enums: list

           Returns:
               dict
    """
    req = method.get('requestType')
    res = method.get('responseType')

    if req in reference_context:
        method['req_link'] = file_name['full_name'].lower() + '#' + method['requestLongType'].lower()

    if res in reference_context:
        method['res_link'] = file_name['full_name'].lower() + '#' + method['responseLongType'].lower()

    return {
        'req_status': req in reference_context,
        'res_status': res in reference_context,
    }


def _get_enums_dict(enums):
    """
        Parsing Enums into proper dict format
           Args:
                enums: list

           Returns:
               dict
    """
    enums_dict = {}
    for enum in enums:
        long_name = enum.get('longName')
        enums_dict.update({long_name: enum.get('values')})
    return enums_dict


def _create_modified_json() -> dict:
    """
        Generate JSON2 that has mapping data according to Jinja templates
           Args:

           Returns:
               dict
    """
    config = _get_json_data(os.path.join(BASE_DIR, 'config.json'))
    refer_link = _.get(config, 'refer_link')
    origin_json_files = _get_json_file_path(TARGET_DIR)

    if len(origin_json_files) == 0:
        _error(f"JSON not found at ({TARGET_DIR})")
    else:
        total_dictionary = {}

        for json_path in origin_json_files:
            # Get file all file paths such as full path, file name, file name in lower case, etc
            file_name_syntax = _get_file_name_syntax(json_path)
            # Get full JSON data by its file path
            full_single_json = _get_json_data(json_path)
            # Get only proto buffer data from JSON file, No scalarValueTypes
            single = full_single_json.get('files')
            # Set full data json by its path and JSON file name
            total_dictionary[_key_path_creator(json_path)] = full_single_json

            # iterate over single dictionary file data
            for obj in single:

                obj['description'] = _modify_yaml_to_json(obj.get('description'))
                package = obj.get('package')
                enums = _get_enums_dict(obj.get('enums'))
                services = obj.get('services')
                messages = obj.get('messages')
                message_names = [msg['name'] for msg in messages]

                # processing services in JSON data
                for service in services:
                    for method in service.get('methods', []):
                        # find referred contents in the service to insert link in markdown
                        method_status = _is_exists_in_same_file(message_names, method, file_name_syntax)
                        # categorize and set description into managed key for markdown template
                        method['description'] = _desc_wrapper(method['description'])
                        # get rest API such as post, or get method
                        google_api = method.get('options')

                        # parsing all all service data into dict with appropriate key to mapping into Jinja template
                        if google_api is not None:
                            rest_apis = google_api.get('google.api.http', {}).get('rules', [])
                            method['restAPI'] = rest_apis

                        if method.get('requestFullType') in [*refer_link] and not method_status['req_status']:
                            method['requestFullType_link'] = refer_link[method['requestFullType']]

                        if method.get('responseFullType') in [*refer_link] and not method_status['res_status']:
                            method['responseFullType_link'] = refer_link[method['responseFullType']]

                # processing messages in JSON data
                for message in messages:
                    # Check is_required column may requires in markdown
                    is_require_exits = False
                    for idx, field in enumerate(message["fields"]):
                        # set fields referred to ENUM such as google.protobuf.Struct.
                        _field_long_type_wrapper(message, field, enums)
                        # categorize and set description into managed key for markdown template
                        field['description'] = _desc_wrapper(field['description'])
                        _field_full_type_wrapper(file_name_syntax, field, refer_link, package)
                        # set key is_required and its value for required column in markdown
                        if not is_require_exits and 'is_required' in field['description']:
                            is_require_exits = True

                    if not is_require_exits:
                        message['no_requires'] = 'true'

            full_single_json['file_info'] = file_name_syntax

        return total_dictionary


def _render_template(template_filename, contents):
    """
        Create a markdown by Jinja template and given contents
           Args:
                template_filename: str
                contents: dict
           Returns:
               directory
    """
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(contents)


def _create_subdirectories(input_path):
    """
        Generate sub-directories if input_path's directory is not created
           Args:
                input_path: str
           Returns:
               directory
    """
    if not os.path.exists(input_path):
        os.makedirs(input_path)


def _generate_single_pb_mds(context_input):
    for key, value in context_input.items():
        ff_name = key.replace(".json", ".md")
        dic_name = ff_name[ff_name.find('api') + 4:len(ff_name)].split('/')
        f_name = dic_name[len(dic_name) - 1].replace('_', '-')
        f_lower = f_name.lower()
        path_to_create = BASE_DIR

        value.update({'title_space': ' '})

        for i in range(len(dic_name)):
            if i == (len(dic_name) - 1):
                continue
            else:
                path_to_create = path_to_create + '/' + dic_name[i]
                _create_subdirectories(path_to_create)

        context_output = os.path.join(path_to_create, f_lower)
        _generate_md_file(context_output, TEMPLATE_NAMES[0], value)


def _generate_summary_mds(context_input, managed_link, history):
    table_of_contents = {}
    title_index = []
    config = _get_json_data(os.path.join(BASE_DIR, 'config.json'))

    for path in context_input:

        file_info = _get_file_name_syntax(path)
        full_path = path[path.find('api/') + 4:len(path)].replace('.json', '.md')
        parsed_path = full_path.split('/')
        parsed_path[len(parsed_path) - 1] = parsed_path[len(parsed_path) - 1].replace('_', '-')
        full_file_name = '/'.join(parsed_path)
        parsed_path[len(parsed_path) - 1] = file_info['title']
        base_bullet = '* '
        check_key = ""

        for i in range(len(parsed_path)):
            if i != 0:
                check_key = check_key + '.' + parsed_path[i]
                base_bullet = '  ' + base_bullet
            else:
                check_key = parsed_path[i]

            title_no_under_bar = parsed_path[i].replace('_', ' ')
            updated_header = base_bullet + '[' + title_no_under_bar + ']'

            if _.get(table_of_contents, check_key, None) is None:
                if i == (len(parsed_path) - 1):
                    _.set(table_of_contents, check_key, {})
                    title_index.append({'title': updated_header.title(), 'url': full_file_name.lower()})
                else:
                    mk_path = check_key.replace('.', '/')
                    readme_url = mk_path + '/' + 'README.md'
                    readme_path = os.path.join(BASE_DIR, mk_path, 'README.md')

                    if not os.path.exists(readme_path):
                        _generate_md_file(readme_path, TEMPLATE_NAMES[2], '')

                    _.set(table_of_contents, check_key, {})
                    title_index.append({'title': updated_header.title(), 'url': readme_url})

    output_to_create = os.path.join(BASE_DIR, 'SUMMARY.md')
    normalized_link = _normalize_managed_link(managed_link)
    context_input = {'toc': title_index,
                     'managed_link': normalized_link,
                     'history': {'cur_version': history}}

    # Updating All SUMMARY.md
    _generate_md_file(output_to_create, TEMPLATE_NAMES[1], context_input)

    # Updating All README.md
    output_to_create = os.path.join(BASE_DIR, 'README.md')
    readme_output = _.get(config, 'intro_comment')
    version_info = history if history.startswith('v') else 'v' + history
    _.set(readme_output, 'version', version_info)
    _generate_md_file(output_to_create, TEMPLATE_NAMES[2], readme_output)


def _normalize_managed_link(managed_link) -> dict:
    """
        Update Api-doc version
           Args:
               file_path': 'str',
               version_info: 'str'
           Returns:

    """
    n_normalized = {}
    for key, value in managed_link.items():
        n_key = key.replace('_', ' ')
        n_value = value
        n_normalized[n_key] = n_value
    return n_normalized


def _delete_json1_in_artifact(json_path: str) -> None:
    """
        Delete files that locates at given path
           Args:
               json_path:str
           Returns:

    """
    if os.path.exists(json_path):
        shutil.rmtree(json_path, ignore_errors=True)


def _get_current_api_version() -> str:
    """
        Retrieve version of api-doc
           Args:

           Returns:
               str
    """
    with open(VERSION, 'r') as f:
        version = f.read().strip()
        f.close()
        return version


def _get_artifact_version(f_path: str) -> str:
    """
        Retrieve version of artifact from given file path
           Args:
                f_path: str
           Returns:
               str
    """
    begin_idx = f_path.rfind('artifact/json/') + 14
    version = f_path[begin_idx: len(f_path)].split('/')[0]
    return version


def _diff_version(f_path: str) -> dict:
    """
        Get dict that includes artifact version, api-doc version, and flags whether update may requires
           Args:
                f_path: str
           Returns:
               dict
    """
    current_version = _get_current_api_version()
    artifact_version = _get_artifact_version(f_path)

    return {
        'current_version': current_version,
        'artifact_version': artifact_version,
        'is_updated': True if artifact_version > current_version else False
    }


def _get_human_managed_documents_links() -> dict:
    """
        Get human managed documents URL link from config.json
           Args:

           Returns:
               dict
    """
    config = _get_json_data(os.path.join(BASE_DIR, 'config.json'))
    human_doc_links = _.get(config, 'human_doc_links')
    return human_doc_links


def _update_current_version(file_path: str, version_info: str) -> None:
    """
        Update Api-doc version
           Args:
               file_path': 'str',
               version_info: 'str'
           Returns:

    """
    with open(file_path, "r+") as f:
        f.seek(0)
        f.write(version_info)
        f.close()


def main() -> None:

    """
    Main Desc: Create a markdown files according to artifact from API repository at


    script(markdown.py) is processing for following steps:

    [1]. Create a file name list with full path from artifact(JSON) from API repository
    [2]. Compare versions between artifacts and api-doc to check whether update may requires
    [3]. Create the new version of JSON files(JSON2) that parse in purpose of mapping to Jinja templates
    [4]. Create the new markdown files through Jinja templates from JSONs(JSON2)
    [5]. Create a new summary markdown page that includes all single API markdown's directory and reference links
    [6]. Update api-doc's version since it has created or updated in previous steps
    [7]. Delete artifact that was copied from api-repo

    """

    # [1]. Create a file name list with full path from artifact(JSON) from API repository
    referred_files = _create_reference_json()

    # Check whether Json files exists, to processing and throw error if there's no file to process
    if len(referred_files) == 0:
        _error("No JSON files in artifacts")
    else:
        # [2]. Compare artifacts and api-doc to check whether update might needs
        version_info = _diff_version(referred_files[0])
        artifact_version = version_info.get('artifact_version')
        api_doc_version = version_info.get('current_version')
        ref_info = artifact_version if version_info.get('is_updated') else api_doc_version

        # [3]. Create a new version of JSON files that parse in purpose of mapping to Jinja templates
        json2 = _create_modified_json()
        human_managed_doc_reference = _get_human_managed_documents_links()

        # [4]. Create the new markdown files through Jinja templates from JSONs(JSON2)
        _generate_single_pb_mds(json2)

        # [5]. Create a new summary markdown page that includes all single API markdown's directory and reference links
        _generate_summary_mds(referred_files, human_managed_doc_reference, ref_info)

        # [6]. Update api-doc's version since it has created or updated in previous steps
        _update_current_version(VERSION, artifact_version)

        # [7]. Delete artifact that was copied from api-repo
        _delete_json1_in_artifact(TARGET_DIR)

        print(f" Version: {artifact_version}, API Document is successfully processed")


if __name__ == '__main__':
    main()
