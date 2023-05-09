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

desc: Creates a new Supervisor. Only Users with the `MANAGED` permission can set the Supervisor `public`. The Supervisor manages the lifecycle of plugin instances by the Supervisor's state. When a Supervisor is created, the state of the resource is `PENDING`. If the state remains the same for 5 minutes, the state is changed to `DISCONNECTED`.
note: ''
request_example: >-
{
"name": "test",
"hostname": "dev-test2",
"secret_key": "xxxxx",
"tags": {
"a": "b"
}
}
response_example: >-
{
"supervisor_id": "supervisor-525982f2ae9a",
"name": "test",
"hostname": "dev-test2",
"state": "ENABLED",
"domain_id": "domain-1c5a6b8181ad",
"tags": {
"a": "b"
},
"labels": {},
"created_at": "2022-01-15T05:42:02.999Z"
}



> **POST** /plugin/v1/supervisor/publish
>






    
<br>

### register

desc: Registers a specific Supervisor. You must specify the `supervisor_id` of the Supervisor to register. The `state` of the Supervisor changes from `PENDING` to `ENABLED`.
note: ''
request_example: >-
{

}
response_example: >-
{

}



> **POST** /plugin/v1/supervisor/register
>






    
<br>

### update

desc: Updates a specific Supervisor. You can make changes in Supervisor settings, including `labels`, `tags`, and the `bool` type parameter `is_public`.
note: ''
request_example: >-
{
"supervisor_id": "supervisor-525982f2ae9a",
"is_public": true,
"priority": 10,
"labels": {
"a": "b"
},
"tags": {
"c": "d"
},
"domain_id": "domain-1c5a6b8181ad"
}
response_example: >-
{
"supervisor_id": "supervisor-525982f2ae9a",
"name": "test",
"hostname": "dev-test2",
"state": "ENABLED",
"is_public": true,
"domain_id": "domain-1c5a6b8181ad",
"tags": {
"a": "b"
},
"labels": {
"c": "d"
},
"created_at": "2022-06-15T05:42:02.999Z"
}



> **POST** /plugin/v1/supervisor/update
>






    
<br>

### deregister

desc: Deregisters and deletes a specific Supervisor. You must specify the `supervisor_id` of the Supervisor to deregister.
note: ''
request_example: >-
{
"supervisor_id": "supervisor-d73011256d55"
}



> **POST** /plugin/v1/supervisor/deregister
>






    
<br>

### enable

desc: Enables a specific Supervisor. By changing the `state` parameter to `ENABLED`, the Supervisor can deploy or delete the `pod` of the plugin instance.
note: ''
request_example: >-
{
"supervisor_id": "supervisor-d73011256d55"
}
response_example: >-
{
"supervisor_id": "supervisor-d73011256d55",
"name": "test-in-plugins",
"hostname": "dev-test3",
"state": "ENABLED",
"domain_id": "domain-1c5a6b8181ad",
"tags": {
"a": "b"
},
"labels": {},
"created_at": "2022-06-15T06:27:51.904Z"
}



> **POST** /plugin/v1/supervisor/enable
>






    
<br>

### disable

desc: Disables a specific Supervisor. By changing the `state` parameter to `DISABLED`, the Supervisor cannot deploy or delete the `pod` of the plugin instance.
note: ''
request_example: >-
{
"supervisor_id": "supervisor-d73011256d55"
}
response_example: >-
{
"supervisor_id": "supervisor-d73011256d55",
"name": "test-in-plugins",
"hostname": "dev-test3",
"state": "DISABLED",
"domain_id": "domain-1c5a6b8181ad",
"tags": {
"a": "b"
},
"labels": {},
"created_at": "2022-06-15T06:27:51.904Z"
}



> **POST** /plugin/v1/supervisor/disable
>






    
<br>

### recover_plugin

desc: Recovers a specific plugin instance in a specific Supervisor. Changes the `state` of the Supervisor to `RE-PROVISIONING`.
note: ''
request_example: >-
{
"supervisor_id": "supervisor-a4c287cba676",
"plugin_id": "plugin-api-direct-mon-webhook",
"version": "1.1.0"
}
response_example: >-
{

}



> **POST** /plugin/v1/supervisor/recover-plugin
>






    
<br>

### get





> **POST** /plugin/v1/supervisor/get
>






    
<br>

### list

desc: Gets a list of all Supervisors. You can use a query to get a filtered list of Supervisors.
note: ''
request_example: >-
{
"query": {}
}
response_example: >-
{
"results": [
{
"supervisor_id": "supervisor-3a091f899539",
"name": "root",
"hostname": "dev-supervisor.svc.cluster.local",
"state": "ENABLED",
"is_public": true,
"domain_id": "domain-1c5a6b8181ad",
"labels": {},
"created_at": "2020-05-12T00:24:48.250Z"
},
{
"supervisor_id": "supervisor-a4c287cba676",
"name": "test",
"hostname": "dev-test",
"state": "ENABLED",
"domain_id": "domain-1c5a6b8181ad",
"tags": {
"a": "b"
},
"labels": {},
"created_at": "2022-06-15T05:39:15.886Z"
}
],
"total_count": 2
}



> **POST** /plugin/v1/supervisor/list
>






    
<br>

### stat





> **POST** /plugin/v1/supervisor/stat
>






    
<br>

### list_plugins

desc: Gets a list of all plugin instances regardless of Supervisors. Prints detailed information about the plugin instances, including `version`, `state`, and the relevant Supervisor.
note: ''
request_example: >-
{
"query": {}
}
response_example: >-
{
"results": [
{
"plugin_id": "plugin-openstack-inven-collector",
"version": "0.4.1.20220609.122832",
"state": "ACTIVE",
"endpoint": "grpc://plugin-openstack-inven-collector-vbnnsoszfjsneiqz.dev-supervisor.svc.cluster.local:50051",
"supervisor_id": "supervisor-3a091f899539",
"supervisor_name": "root",
"managed": true,
"endpoints": [
"grpc://172.16.16.234:50051"
]
},
{
"plugin_id": "plugin-zabbix-mon-webhook",
"version": "1.0",
"state": "ACTIVE",
"endpoint": "grpc://plugin-zabbix-mon-webhook-dgqqfqsqidieeuk.dev-supervisor.svc.cluster.local:50051",
"supervisor_id": "supervisor-3a091f899539",
"supervisor_name": "root",
"managed": true,
"endpoints": [
"grpc://172.16.16.130:50051"
]
}
],
"total_count": 2
}



> **POST** /plugin/v1/supervisor/list-plugins
>






    


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
