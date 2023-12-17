---
title: "Plugin"
linkTitle: "Plugin"
weight: 3
bookFlatSection: true
---
# [Plugin](#Plugin)
A Plugin is a resource containing data of deployable plugins such as container image and registry URL.


>  **Package : spaceone.api.repository.v1**

<br>
<br>

## Plugin





**Plugin Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./Plugin#register) | [CreatePluginRequest](Plugin#createpluginrequest) | [PluginInfo](Plugin#plugininfo) |
| [**update**](./Plugin#update) | [UpdatePluginRequest](Plugin#updatepluginrequest) | [PluginInfo](Plugin#plugininfo) |
| [**deregister**](./Plugin#deregister) | [PluginRequest](Plugin#pluginrequest) | [Empty](Plugin#empty) |
| [**enable**](./Plugin#enable) | [PluginRequest](Plugin#pluginrequest) | [PluginInfo](Plugin#plugininfo) |
| [**disable**](./Plugin#disable) | [PluginRequest](Plugin#pluginrequest) | [PluginInfo](Plugin#plugininfo) |
| [**get_versions**](./Plugin#get_versions) | [RepositoryPluginRequest](Plugin#repositorypluginrequest) | [VersionsInfo](Plugin#versionsinfo) |
| [**get**](./Plugin#get) | [RepositoryPluginRequest](Plugin#repositorypluginrequest) | [PluginInfo](Plugin#plugininfo) |
| [**list**](./Plugin#list) | [PluginQuery](Plugin#pluginquery) | [PluginsInfo](Plugin#pluginsinfo) |
| [**stat**](./Plugin#stat) | [PluginStatQuery](Plugin#pluginstatquery) | [Struct](Plugin#struct) |



    
<br>

### register

Registers a Plugin. The parameter `registry_type`, meaning container registry type, can be either `DOCKER_HUB` or `AWS_PRIVATE_ECR`. The default value of the `registry_type` is `DOCKER_HUB`. The parameter `registry_url` is required if the `registry_type` is not `DOCKER_HUB`. The parameter `image` is limited to 40 characters.



> **POST** /repository/v1/plugin/register
>





 {{< tabs " register " >}}

 {{< tab "Request Example" >}}



[CreatePluginRequest](./Plugin#createpluginrequest)

* **name** (string)   `Required` 


* **resource_type** (string)   `Required` 


* **image** (string)   `Required` 


* **provider** (string)  


* **registry_type** (PublicRegistryType)  


* **registry_config** (Struct)  


* **capability** (Struct)  


* **labels** (ListValue)  


* **tags** (Struct)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginInfo](#PLUGININFO)
* **plugin_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **resource_type** (string)   `Required` 

* **image** (string)   `Required` 

* **provider** (string)   `Required` 

* **registry_type** (PublicRegistryType)   `Required` 

* **registry_url** (string)   `Required` 

* **registry_config** (Struct)   `Required` 

* **capability** (Struct)   `Required` 

* **labels** (ListValue)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **repository_info** (RepositoryInfo)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Plugin registered. A Plugin can be updated only if its Repository's `repository_type` is `local`. You can make changes in Plugin settings, including `template` and its options, `schema`.



> **POST** /repository/v1/plugin/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdatePluginRequest](./Plugin#updatepluginrequest)

* **plugin_id** (string)   `Required` 


* **name** (string)  


* **capability** (Struct)  


* **labels** (ListValue)  


* **tags** (Struct)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginInfo](#PLUGININFO)
* **plugin_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **resource_type** (string)   `Required` 

* **image** (string)   `Required` 

* **provider** (string)   `Required` 

* **registry_type** (PublicRegistryType)   `Required` 

* **registry_url** (string)   `Required` 

* **registry_config** (Struct)   `Required` 

* **capability** (Struct)   `Required` 

* **labels** (ListValue)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **repository_info** (RepositoryInfo)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### deregister

Deregisters and deletes a specific Plugin. You must specify the `plugin_id` of the Plugin to deregister.



> **POST** /repository/v1/plugin/deregister
>





 {{< tabs " deregister " >}}

 {{< tab "Request Example" >}}



[PluginRequest](./Plugin#pluginrequest)

* **plugin_id** (string)   `Required` 





{{< highlight json >}}
{
   "plugin_id": "plugin-aws-sns-mon-webhook",
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### enable

Enables a specific Plugin. If the Plugin is enabled, the Plugin can be used as its parameter `state` becomes `ENABLED`.



> **POST** /repository/v1/plugin/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[PluginRequest](./Plugin#pluginrequest)

* **plugin_id** (string)   `Required` 





{{< highlight json >}}
{
   "plugin_id": "plugin-aws-sns-mon-webhook",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginInfo](#PLUGININFO)
* **plugin_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **resource_type** (string)   `Required` 

* **image** (string)   `Required` 

* **provider** (string)   `Required` 

* **registry_type** (PublicRegistryType)   `Required` 

* **registry_url** (string)   `Required` 

* **registry_config** (Struct)   `Required` 

* **capability** (Struct)   `Required` 

* **labels** (ListValue)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **repository_info** (RepositoryInfo)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable

Disables a specific Plugin. If the Plugin is disabled, the Plugin cannot be used as its parameter `state` becomes `DISABLED`.



> **POST** /repository/v1/plugin/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[PluginRequest](./Plugin#pluginrequest)

* **plugin_id** (string)   `Required` 





{{< highlight json >}}
{
   "plugin_id": "plugin-aws-sns-mon-webhook",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginInfo](#PLUGININFO)
* **plugin_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **resource_type** (string)   `Required` 

* **image** (string)   `Required` 

* **provider** (string)   `Required` 

* **registry_type** (PublicRegistryType)   `Required` 

* **registry_url** (string)   `Required` 

* **registry_config** (Struct)   `Required` 

* **capability** (Struct)   `Required` 

* **labels** (ListValue)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **repository_info** (RepositoryInfo)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get_versions

Gets all version data of a specific Plugin from its Repository. The parameter `plugin_id` is used as an identifier of a Plugin to get version data.



> **POST** /repository/v1/plugin/get-versions
>





 {{< tabs " get_versions " >}}

 {{< tab "Request Example" >}}



[RepositoryPluginRequest](./Plugin#repositorypluginrequest)

* **plugin_id** (string)   `Required` 


* **repository_id** (string)  





{{< highlight json >}}
{
   "plugin_id": "plugin-aws-sns-mon-webhook",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[VersionsInfo](#VERSIONSINFO)
* **version** (string)  `Repeated`   `Required` 

  deprecated field

* **total_count** (int32)   `Required` 

* **results** (string)  `Repeated`   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get

Gets a specific Plugin. Prints detailed information about the Plugin, including  `image`, `registry_url`, and `state`.



> **POST** /repository/v1/plugin/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[RepositoryPluginRequest](./Plugin#repositorypluginrequest)

* **plugin_id** (string)   `Required` 


* **repository_id** (string)  





{{< highlight json >}}
{
   "plugin_id": "plugin-aws-sns-mon-webhook",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginInfo](#PLUGININFO)
* **plugin_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **resource_type** (string)   `Required` 

* **image** (string)   `Required` 

* **provider** (string)   `Required` 

* **registry_type** (PublicRegistryType)   `Required` 

* **registry_url** (string)   `Required` 

* **registry_config** (Struct)   `Required` 

* **capability** (Struct)   `Required` 

* **labels** (ListValue)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **repository_info** (RepositoryInfo)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Plugins registered in a specific Repository. The parameter `repository_id` is used as an identifier of a Repository to get its list of Plugins. You can use a query to get a filtered list of Plugins.



> **POST** /repository/v1/plugin/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[PluginQuery](./Plugin#pluginquery)

* **query** (Query)  


* **plugin_id** (string)  


* **name** (string)  


* **state** (State)  


* **resource_type** (string)  


* **provider** (string)  


* **registry_type** (PublicRegistryType)  


* **repository_id** (string)  





{{< highlight json >}}
{
   "query": {},
   "repository_id": "repo-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PluginsInfo](#PLUGINSINFO)
* **results** (PluginInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /repository/v1/plugin/stat
>






    


<br>
<br>

## Message



### CreatePluginRequest
* **name** (string)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **image** (string)   `Required` 

    
* **provider** (string)  

    
* **registry_type** (PublicRegistryType)  

    
* **registry_config** (Struct)  

    
* **capability** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### PluginInfo
* **plugin_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **resource_type** (string)   `Required` 

    
* **image** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **registry_type** (PublicRegistryType)   `Required` 

    
* **registry_url** (string)   `Required` 

    
* **registry_config** (Struct)   `Required` 

    
* **capability** (Struct)   `Required` 

    
* **labels** (ListValue)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **repository_info** (RepositoryInfo)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PluginQuery
* **query** (Query)  

    
* **plugin_id** (string)  

    
* **name** (string)  

    
* **state** (State)  

    
* **resource_type** (string)  

    
* **provider** (string)  

    
* **registry_type** (PublicRegistryType)  

    
* **repository_id** (string)  

    <br>

### PluginRequest
* **plugin_id** (string)   `Required` 

    <br>

### PluginStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **repository_id** (string)   `Required` 

    <br>

### PluginsInfo
* **results** (PluginInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### RepositoryPluginRequest
* **plugin_id** (string)   `Required` 

    
* **repository_id** (string)  

    <br>

### UpdatePluginRequest
* **plugin_id** (string)   `Required` 

    
* **name** (string)  

    
* **capability** (Struct)  

    
* **labels** (ListValue)  

    
* **tags** (Struct)  

    <br>

### VersionsInfo
* **version** (string)  `Repeated`    `Required` 

  *deprecated field*

    
* **total_count** (int32)   `Required` 

    
* **results** (string)  `Repeated`    `Required` 

    <br>
