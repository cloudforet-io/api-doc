---
title: "Plugin"
linkTitle: "Plugin"
weight: 3
bookFlatSection: true
---
# [Plugin](#Plugin)
desc: A Plugin is a resource containing data of deployable plugins such as container image and registry URL.


>  **Package : spaceone.api.repository.v1**

<br>
<br>

## Plugin





**Plugin Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./Plugin#register) | [CreatePluginRequest](Plugin#createpluginrequest) | [PluginInfo](./Plugin#plugininfo) |
| [**update**](./Plugin#update) | [UpdatePluginRequest](Plugin#updatepluginrequest) | [PluginInfo](./Plugin#plugininfo) |
| [**deregister**](./Plugin#deregister) | [PluginRequest](Plugin#pluginrequest) | [Empty](./Plugin#empty) |
| [**enable**](./Plugin#enable) | [PluginRequest](Plugin#pluginrequest) | [PluginInfo](./Plugin#plugininfo) |
| [**disable**](./Plugin#disable) | [PluginRequest](Plugin#pluginrequest) | [PluginInfo](./Plugin#plugininfo) |
| [**get_versions**](./Plugin#get_versions) | [RepositoryPluginRequest](Plugin#repositorypluginrequest) | [VersionsInfo](./Plugin#versionsinfo) |
| [**get**](./Plugin#get) | [GetRepositoryPluginRequest](Plugin#getrepositorypluginrequest) | [PluginInfo](./Plugin#plugininfo) |
| [**list**](./Plugin#list) | [PluginQuery](Plugin#pluginquery) | [PluginsInfo](./Plugin#pluginsinfo) |
| [**stat**](./Plugin#stat) | [PluginStatQuery](Plugin#pluginstatquery) | [Struct](./Plugin#struct) |



    
<br>

### register

desc: Registers a Plugin. The parameter `registry_type`, meaning container registry type, can be either `DOCKER_HUB` or `AWS_PUBLIC_ECR`. The default value of the `registry_type` is `DOCKER_HUB`. The parameter `registry_url` is required if the `registry_type` is not `DOCKER_HUB`. The parameter `image` is limited to 40 characters.
request_example: >-
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
response_example: >-
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



> **POST** /repository/v1/plugin/register
>






    
<br>

### update

desc: Updates a specific Plugin registered. A Plugin can be updated only if its Repository's `repository_type` is `local`. You can make changes in Plugin settings, including `template` and its options, `schema`.
request_example: >-
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
response_example: >-
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



> **POST** /repository/v1/plugin/update
>






    
<br>

### deregister

desc: Deregisters and deletes a specific Plugin. You must specify the `plugin_id` of the Plugin to deregister.
request_example: >-
{
"plugin_id": "plugin-aws-sns-mon-webhook",
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/plugin/deregister
>






    
<br>

### enable

desc: Enables a specific Plugin. If the Plugin is enabled, the Plugin can be used as its parameter `state` becomes `ENABLED`.
request_example: >-
{
"plugin_id": "plugin-aws-sns-mon-webhook",
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/plugin/enable
>






    
<br>

### disable

desc: Disables a specific Plugin. If the Plugin is disabled, the Plugin cannot be used as its parameter `state` becomes `DISABLED`.
request_example: >-
{
"plugin_id": "plugin-aws-sns-mon-webhook",
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/plugin/disable
>






    
<br>

### get_versions

desc: Gets all version data of a specific Plugin from its Repository. The parameter `plugin_id` is used as an identifier of a Plugin to get version data.
request_example: >-
{
"plugin_id": "plugin-aws-sns-mon-webhook",
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/plugin/get-versions
>






    
<br>

### get

desc: Gets a specific Plugin. Prints detailed information about the Plugin, including  `image`, `registry_url`, and `state`.
request_example: >-
{
"plugin_id": "plugin-aws-sns-mon-webhook",
"domain_id": "domain-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/plugin/get
>






    
<br>

### list

desc: Gets a list of all Plugins registered in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Plugins. You can use a query to get a filtered list of Plugins.
request_example: >-
{
"query": {},
"repository_id": "repo-123456789012"
}
response_example: >-
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



> **POST** /repository/v1/plugin/list
>






    
<br>

### stat





> **POST** /repository/v1/plugin/stat
>






    


<br>
<br>

## Message



### CreatePluginRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **service_type** (string)  `Required` 

  *is_required: true*

    
* **image** (string)  `Required` 

  *is_required: true*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **registry_type** (PublicRegistryType)  `Required` 

  *is_required: false*

    
* **registry_config** (Struct)  `Required` 

  *is_required: false*

    
* **capability** (Struct)  `Required` 

  *is_required: false*

    
* **template** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **project_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetRepositoryPluginRequest
* **plugin_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **repository_id** (string)  `Required` 

  *is_required: false*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### PluginInfo
* **plugin_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **image** (string)  `Required` 

    
* **registry_url** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **service_type** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **registry_type** (PublicRegistryType)  `Required` 

    
* **registry_config** (Struct)  `Required` 

    
* **capability** (Struct)  `Required` 

    
* **template** (Struct)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **repository_info** (RepositoryInfo)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### PluginQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **plugin_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (State)  `Required` 

  *is_required: false*

    
* **service_type** (string)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **registry_type** (PublicRegistryType)  `Required` 

  *is_required: false*

    <br>

### PluginRequest
* **plugin_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### PluginStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **repository_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### PluginsInfo
* **results** (PluginInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### RepositoryPluginRequest
* **plugin_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **repository_id** (string)  `Required` 

  *is_required: false*

    <br>

### UpdatePluginRequest
* **plugin_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **capability** (Struct)  `Required` 

  *is_required: false*

    
* **template** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### VersionsInfo
* **version** (string)  `Required` 

  *desc: deprecated field*

    
* **total_count** (int32)  `Required` 

    
* **results** (string)  `Required` 

    <br>
