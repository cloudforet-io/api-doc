---
description: A Plugin is a resource containing data of deployable plugins such as container image and registry URL.
---
# Plugin

>  **Package : spaceone.api.repository.v1**

## Plugin

{% hint style="info" %}
**Plugin Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](plugin.md#register)|   [CreatePluginRequest](plugin.md#createpluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**update**](plugin.md#update)|   [UpdatePluginRequest](plugin.md#updatepluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**deregister**](plugin.md#deregister)|   [PluginRequest](plugin.md#pluginrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**enable**](plugin.md#enable)|   [PluginRequest](plugin.md#pluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**disable**](plugin.md#disable)|   [PluginRequest](plugin.md#pluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**get_versions**](plugin.md#get_versions)|   [RepositoryPluginRequest](plugin.md#repositorypluginrequest) |   [VersionsInfo](plugin.md#versionsinfo) |
| [**get**](plugin.md#get)|   [GetRepositoryPluginRequest](plugin.md#getrepositorypluginrequest) |   [PluginInfo](plugin.md#plugininfo) |
| [**list**](plugin.md#list)|   [PluginQuery](plugin.md#pluginquery) |   [PluginsInfo](plugin.md#pluginsinfo) |
| [**stat**](plugin.md#stat)|   [PluginStatQuery](plugin.md#pluginstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### register
> **POST** /repository/v1/plugins
>

> Registers a Plugin. The parameter `registry_type`, meaning container registry type, can be either `DOCKER_HUB` or `AWS_PUBLIC_ECR`. The default value of the `registry_type` is `DOCKER_HUB`. The parameter `registry_url` is required if the `registry_type` is not `DOCKER_HUB`. The parameter `image` is limited to 40 characters.

| Type | Message |
| :--- | :--- |
| Request | [CreatePluginRequest](plugin.md#createpluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "JIRA Issue notification",
    "service_type": "notification.Procotol",
    "image": "pyengine/plugin-jira-noti-protocol",
    "registry_type": "DOCKER_HUB",
    "registry_config": {},
    "provider": "atlassian",
    "capability": {
        "supported_schema": [
            "atlassian_jira"
        ]
    },
    "template": {
        "options": {
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "project_id": {
                        "type": "string",
                        "title": "Project ID",
                        "minLength": 4.0
                    },
                    "sa_name": {
                        "title": "Service Account",
                        "type": "string",
                        "minLength": 4.0
                    }
                }
            }
        }
    },
    "labels": [
        "jira",
        "atlassian",
        "notification"
    ],
    "tags": {
        "description": "Atlassian JIRA Issue notification",
        "icon": "https://icon-path/jira-icon.png"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "plugin_id": "plugin-jira-noti-protocol",
    "name": "JIRA Issue notification",
    "image": "pyengine/plugin-jira-noti-protocol",
    "registry_url": "registry.hub.docker.com",
    "state": "ENABLED",
    "service_type": "notification.Procotol",
    "provider": "atlassian",
    "registry_type": "DOCKER_HUB",
    "registry_config": {},
    "capability": {
        "supported_schema": [
            "atlassian_jira"
        ]
    },
    "template": {
        "options": {
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "project_id": {
                        "type": "string",
                        "title": "Project ID",
                        "minLength": 4.0
                    },
                    "sa_name": {
                        "title": "Service Account",
                        "type": "string",
                        "minLength": 4.0
                    }
                }
            }
        }
    },
    "labels": [
        "jira",
        "atlassian",
        "notification"
    ],
    "tags": {
        "description": "Atlassian JIRA Issue notification",
        "icon": "https://icon-path/jira-icon.png"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Marketplace",
        "repository_type": "remote"
    },
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T08:02:38.094Z",
    "updated_at": "2022-01-01T08:02:38.094Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /repository/v1/plugin/{plugin_id}
>

> Updates a specific Plugin registered. A Plugin can be updated only if its Repository's `repository_type` is `local`. You can make changes in Plugin settings, including `template` and its options, `schema`.

| Type | Message |
| :--- | :--- |
| Request | [UpdatePluginRequest](plugin.md#updatepluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "JIRA Issue notification",
    "capability": {
        "supported_schema": [
            "atlassian_jira"
        ]
    },
    "template": {
        "options": {
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "project_id": {
                        "type": "string",
                        "title": "Project ID",
                        "minLength": 4.0
                    },
                    "sa_name": {
                        "title": "Service Account",
                        "type": "string",
                        "minLength": 4.0
                    }
                }
            }
        }
    },
    "labels": [
        "jira",
        "atlassian",
        "notification"
    ],
    "tags": {
        "description": "Atlassian JIRA Issue notification",
        "icon": "https://icon-path/jira-icon.png"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "plugin_id": "plugin-jira-noti-protocol",
    "name": "JIRA Issue notification",
    "image": "pyengine/plugin-jira-noti-protocol",
    "registry_url": "registry.hub.docker.com",
    "state": "ENABLED",
    "service_type": "notification.Procotol",
    "provider": "atlassian",
    "registry_type": "DOCKER_HUB",
    "registry_config": {},
    "capability": {
        "supported_schema": [
            "atlassian_jira"
        ]
    },
    "template": {
        "options": {
            "schema": {
                "type": "object",
                "required": [],
                "properties": {
                    "project_id": {
                        "type": "string",
                        "title": "Project ID",
                        "minLength": 4.0
                    },
                    "sa_name": {
                        "title": "Service Account",
                        "type": "string",
                        "minLength": 4.0
                    }
                }
            }
        }
    },
    "labels": [
        "jira",
        "atlassian",
        "notification"
    ],
    "tags": {
        "description": "Atlassian JIRA Issue notification",
        "spaceone:plugin_name": "plugin-jira-noti-protocol",
        "icon": "https://icon-path/jira-icon.png"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Marketplace",
        "repository_type": "remote"
    },
    "domain_id": "domain-123456789012",
    "created_at": "2022-01-01T08:02:38.094Z",
    "updated_at": "2022-01-01T08:02:38.094Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### deregister
> **DELETE** /repository/v1/plugin/{plugin_id}
>

> Deregisters and deletes a specific Plugin. You must specify the `plugin_id` of the Plugin to deregister.

| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](plugin.md#pluginrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "name": "AWS SNS Webhook",
    "image": "pyengine/plugin-aws-sns-mon-webhook",
    "registry_url": "registry.hub.docker.com",
    "state": "ENABLED",
    "service_type": "monitoring.Webhook",
    "registry_type": "DOCKER_HUB",
    "registry_config": {},
    "capability": {},
    "template": {},
    "labels": [],
    "tags": {
        "icon": "https://icon-path/Amazon-SNS.svg"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Marketplace",
        "repository_type": "remote"
    },
    "domain_id": "domain-987654321098",
    "created_at": "2022-01-01T08:14:23.175Z",
    "updated_at": "2022-01-01T08:14:23.175Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **PUT** /repository/v1/plugin/{plugin_id}/enable
>

> Enables a specific Plugin. If the Plugin is enabled, the Plugin can be used as its parameter `state` becomes `ENABLED`.

| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](plugin.md#pluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "name": "AWS SNS Webhook",
    "image": "pyengine/plugin-aws-sns-mon-webhook",
    "registry_url": "registry.hub.docker.com",
    "state": "ENABLED",
    "service_type": "monitoring.Webhook",
    "registry_type": "DOCKER_HUB",
    "registry_config": {},
    "capability": {},
    "template": {},
    "labels": [],
    "tags": {
        "icon": "https://icon-path/Amazon-SNS.svg"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Marketplace",
        "repository_type": "remote"
    },
    "domain_id": "domain-987654321098",
    "created_at": "2022-01-01T08:14:23.175Z",
    "updated_at": "2022-01-01T08:14:23.175Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **PUT** /repository/v1/plugin/{plugin_id}/disable
>

> Disables a specific Plugin. If the Plugin is disabled, the Plugin cannot be used as its parameter `state` becomes `DISABLED`.

| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](plugin.md#pluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "name": "AWS SNS Webhook",
    "image": "pyengine/plugin-aws-sns-mon-webhook",
    "registry_url": "registry.hub.docker.com",
    "state": "ENABLED",
    "service_type": "monitoring.Webhook",
    "registry_type": "DOCKER_HUB",
    "registry_config": {},
    "capability": {},
    "template": {},
    "labels": [],
    "tags": {
        "icon": "https://icon-path/Amazon-SNS.svg"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Marketplace",
        "repository_type": "remote"
    },
    "domain_id": "domain-987654321098",
    "created_at": "2022-01-01T08:14:23.175Z",
    "updated_at": "2022-01-01T08:14:23.175Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get_versions
> **GET** /repository/v1/plugins/{plugin_id}/versions
>

> Gets all version data of a specific Plugin from its Repository. The parameter `plugin_id` is used as an identifier of a Plugin to get version data.

| Type | Message |
| :--- | :--- |
| Request | [RepositoryPluginRequest](plugin.md#repositorypluginrequest) |
| Response |  [VersionsInfo](plugin.md#versionsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "total_count": 1,
    "results": [
        "1.2.2",
        "1.2.1.20220429.104002",
        "1.2.1.20220422.161421",
        "1.2.1.20220411.113807",
        "1.2.1"
    ]
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /repository/v1/plugins/{plugin_id}
>

> Gets a specific Plugin. Prints detailed information about the Plugin, including  `image`, `registry_url`, and `state`.

| Type | Message |
| :--- | :--- |
| Request | [GetRepositoryPluginRequest](plugin.md#getrepositorypluginrequest) |
| Response |  [PluginInfo](plugin.md#plugininfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "name": "AWS SNS Webhook",
    "image": "pyengine/plugin-aws-sns-mon-webhook",
    "registry_url": "registry.hub.docker.com",
    "state": "ENABLED",
    "service_type": "monitoring.Webhook",
    "registry_type": "DOCKER_HUB",
    "registry_config": {},
    "capability": {},
    "template": {},
    "labels": [],
    "tags": {
        "icon": "https://icon-url/Amazon-SNS.svg"
    },
    "repository_info": {
        "repository_id": "repo-123456789012",
        "name": "Marketplace",
        "repository_type": "remote"
    },
    "domain_id": "domain-987654321098",
    "created_at": "2021-06-14T08:14:23.175Z",
    "updated_at": "2021-06-14T08:14:23.175Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /repository/v1/plugins
>
> **POST** /repository/v1/plugins/search


> Gets a list of all Plugins registered in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Plugins. You can use a query to get a filtered list of Plugins.

| Type | Message |
| :--- | :--- |
| Request | [PluginQuery](plugin.md#pluginquery) |
| Response |  [PluginsInfo](plugin.md#pluginsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "repository_id": "repo-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "plugin_id": "plugin-api-direct-mon-webhook",
            "name": "API Direct Webhook",
            "image": "pyengine/plugin-api-direct-mon-webhook",
            "registry_url": "registry.hub.docker.com",
            "state": "ENABLED",
            "service_type": "monitoring.Webhook",
            "registry_type": "DOCKER_HUB",
            "registry_config": {},
            "capability": {},
            "template": {},
            "labels": [],
            "tags": {
                "icon": "https://icon-url/icon.svg"
            },
            "repository_info": {
                "repository_id": "repo-123456789012",
                "name": "Marketplace",
                "repository_type": "remote"
            },
            "domain_id": "domain-987654321098",
            "created_at": "2022-01-01T03:25:10.408Z",
            "updated_at": "2022-01-01T03:25:10.408Z"
        },
        {
            "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
            "name": "AWS HyperBilling Cost Analysis Data Source",
            "image": "pyengine/plugin-aws-hyperbilling-cost-datasource",
            "registry_url": "registry.hub.docker.com",
            "state": "ENABLED",
            "service_type": "cost_analysis.DataSoruce",
            "registry_type": "DOCKER_HUB",
            "registry_config": {},
            "capability": {},
            "template": {},
            "labels": [],
            "tags": {},
            "repository_info": {
                "repository_id": "repo-123456789012",
                "name": "Marketplace",
                "repository_type": "remote"
            },
            "domain_id": "domain-987654321098",
            "created_at": "2022-01-01T04:56:55.082Z",
            "updated_at": "2022-01-01T04:56:55.082Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /repository/v1/plugins/stat
>


| Type | Message |
| :--- | :--- |
| Request | [PluginStatQuery](plugin.md#pluginstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreatePluginRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">image</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_REGISTRY_TYPE</li>
          	<li>DOCKER_HUB</li>
          	<li>AWS_PUBLIC_ECR</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_config</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">template</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetRepositoryPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| plugin_id |string|✔| |
| domain_id |string|✔| |
| repository_id |string|✘| |
| only |list of string|✘| |

### PluginInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">image</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_url</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_REGISTRY_TYPE</li>
          	<li>DOCKER_HUB</li>
          	<li>AWS_PUBLIC_ECR</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_config</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">template</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repository_info</td>
      <td style="text-align:left"><a href="plugin.md#repositoryinfo">RepositoryInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PluginQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">repository_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">registry_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE_REGISTRY_TYPE</li>
          	<li>DOCKER_HUB</li>
          	<li>AWS_PUBLIC_ECR</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| plugin_id |string|✔| |
| domain_id |string|✔| |

### PluginStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| repository_id |string|✔| |
| domain_id |string|✔| |

### PluginsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PluginInfo](plugin.md#plugininfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### RepositoryPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| plugin_id |string|✔| |
| domain_id |string|✔| |
| repository_id |string|✘| |

### UpdatePluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| plugin_id |string|✔| |
| name |string|✘| |
| capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### VersionsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| version |list of string | deprecated field|
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| results |list of string | |
