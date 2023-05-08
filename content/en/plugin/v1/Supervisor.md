---
title: "Supervisor"
linkTitle: "Supervisor"
weight: 3
bookFlatSection: true
---
# [Supervisor](#Supervisor)
desc: A Supervisor is a resource managing the lifecycle of the plugin instances to deploy. A Supervisor manages the deployment of plugin instances by deploying or deleting the `pod` of the plugin instances.


>  **Package : spaceone.api.plugin.v1**

<br>
<br>

## Supervisor


**Supervisor Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**publish**](./Supervisor#publish) | [PublishSupervisorRequest](Supervisor#publishsupervisorrequest) | [SupervisorInfo](./Supervisor#supervisorinfo) |
| [**register**](./Supervisor#register) | [RegisterSupervisorRequest](Supervisor#registersupervisorrequest) | [SupervisorInfo](./Supervisor#supervisorinfo) |
| [**update**](./Supervisor#update) | [RegisterSupervisorRequest](Supervisor#registersupervisorrequest) | [SupervisorInfo](./Supervisor#supervisorinfo) |
| [**deregister**](./Supervisor#deregister) | [SupervisorRequest](Supervisor#supervisorrequest) | [Empty](./Supervisor#empty) |
| [**enable**](./Supervisor#enable) | [SupervisorRequest](Supervisor#supervisorrequest) | [SupervisorInfo](./Supervisor#supervisorinfo) |
| [**disable**](./Supervisor#disable) | [SupervisorRequest](Supervisor#supervisorrequest) | [SupervisorInfo](./Supervisor#supervisorinfo) |
| [**recover_plugin**](./Supervisor#recover_plugin) | [RecoverPluginRequest](Supervisor#recoverpluginrequest) | [PluginInfo](./Supervisor#plugininfo) |
| [**get**](./Supervisor#get) | [GetSupervisorRequest](Supervisor#getsupervisorrequest) | [SupervisorInfo](./Supervisor#supervisorinfo) |
| [**list**](./Supervisor#list) | [SupervisorQuery](Supervisor#supervisorquery) | [SupervisorsInfo](./Supervisor#supervisorsinfo) |
| [**stat**](./Supervisor#stat) | [SupervisorStatQuery](Supervisor#supervisorstatquery) | [Struct](./Supervisor#struct) |
| [**list_plugins**](./Supervisor#list_plugins) | [PluginQuery](Supervisor#pluginquery) | [PluginsInfo](./Supervisor#pluginsinfo) |



    
<br>

### publish

> **POST** /plugin/v1/supervisor/publish
>




 {{< tabs " publish " >}}




{{< /tabs >}}

    
<br>

### register

> **POST** /plugin/v1/supervisor/register
>




 {{< tabs " register " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /plugin/v1/supervisor/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### deregister

> **POST** /plugin/v1/supervisor/deregister
>




 {{< tabs " deregister " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /plugin/v1/supervisor/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /plugin/v1/supervisor/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### recover_plugin

> **POST** /plugin/v1/supervisor/recover-plugin
>




 {{< tabs " recover_plugin " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /plugin/v1/supervisor/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /plugin/v1/supervisor/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /plugin/v1/supervisor/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    
<br>

### list_plugins

> **POST** /plugin/v1/supervisor/list-plugins
>




 {{< tabs " list_plugins " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### GetSupervisorRequest
* **supervisor_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### PluginInfo
* **plugin_id** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **endpoint** (string)  `Required` 

    
* **supervisor_id** (string)  `Required` 

    
* **supervisor_name** (string)  `Required` 

    
* **managed** (bool)  `Required` 

    
* **endpoints** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### PluginQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **supervisor_id** (string)  `Required` 

  *is_required: false*

    
* **hostname** (string)  `Required` 

  *is_required: false*

    
* **plugin_id** (string)  `Required` 

  *is_required: false*

    
* **version** (string)  `Required` 

  *is_required: false*

    
* **state** (State)  `Required` 

  *is_required: false*

    
* **endpoint** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### PluginsInfo
* **results** (PluginInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### PublishSupervisorRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **hostname** (string)  `Required` 

  *is_required: true*

    
* **secret_key** (string)  `Required` 

  *is_required: false*

    
* **plugin_info** (PluginInfo)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **is_public** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **labels** (Struct)  `Required` 

  *is_required: false*

    <br>

### RecoverPluginRequest
* **supervisor_id** (string)  `Required` 

  *is_required: true*

    
* **plugin_id** (string)  `Required` 

  *is_required: true*

    
* **version** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### RegisterSupervisorRequest
* **supervisor_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **is_public** (bool)  `Required` 

  *is_required: false*

    
* **priority** (int32)  `Required` 

  *is_required: false*

    
* **labels** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SupervisorInfo
* **supervisor_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **hostname** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **is_public** (bool)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **labels** (Struct)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### SupervisorQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **supervisor_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **is_public** (bool)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SupervisorRequest
* **supervisor_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SupervisorStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SupervisorsInfo
* **results** (SupervisorInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
