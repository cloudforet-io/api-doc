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

> **POST** /repository/v1/plugin/register
>




 {{< tabs " register " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /repository/v1/plugin/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### deregister

> **POST** /repository/v1/plugin/deregister
>




 {{< tabs " deregister " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /repository/v1/plugin/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /repository/v1/plugin/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### get_versions

> **POST** /repository/v1/plugin/get-versions
>




 {{< tabs " get_versions " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /repository/v1/plugin/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /repository/v1/plugin/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /repository/v1/plugin/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


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
