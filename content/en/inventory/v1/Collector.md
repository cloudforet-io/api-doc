---
title: "Collector"
linkTitle: "Collector"
weight: 3
bookFlatSection: true
---
# [Collector](#Collector)
desc: A Collector is a plugin instance collecting cloud resources. A Collector can collect the resource data manually or by a pre-set schedule.


>  **Package : spaceone.api.inventory.v1**

<br>
<br>

## Collector





**Collector Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./Collector#create) | [CreateCollectorRequest](Collector#createcollectorrequest) | [CollectorInfo](./Collector#collectorinfo) |
| [**update**](./Collector#update) | [UpdateCollectorRequest](Collector#updatecollectorrequest) | [CollectorInfo](./Collector#collectorinfo) |
| [**update_plugin**](./Collector#update_plugin) | [UpdatePluginRequest](Collector#updatepluginrequest) | [CollectorInfo](./Collector#collectorinfo) |
| [**verify_plugin**](./Collector#verify_plugin) | [VerifyPluginRequest](Collector#verifypluginrequest) | [Empty](./Collector#empty) |
| [**delete**](./Collector#delete) | [CollectorRequest](Collector#collectorrequest) | [Empty](./Collector#empty) |
| [**get**](./Collector#get) | [GetCollectorRequest](Collector#getcollectorrequest) | [CollectorInfo](./Collector#collectorinfo) |
| [**enable**](./Collector#enable) | [CollectorRequest](Collector#collectorrequest) | [CollectorInfo](./Collector#collectorinfo) |
| [**disable**](./Collector#disable) | [CollectorRequest](Collector#collectorrequest) | [CollectorInfo](./Collector#collectorinfo) |
| [**list**](./Collector#list) | [CollectorQuery](Collector#collectorquery) | [CollectorsInfo](./Collector#collectorsinfo) |
| [**stat**](./Collector#stat) | [CollectorStatQuery](Collector#collectorstatquery) | [Struct](./Collector#struct) |
| [**collect**](./Collector#collect) | [CollectRequest](Collector#collectrequest) | [JobInfo](./Collector#jobinfo) |
| [**add_schedule**](./Collector#add_schedule) | [CreateScheduleRequest](Collector#createschedulerequest) | [ScheduleInfo](./Collector#scheduleinfo) |
| [**get_schedule**](./Collector#get_schedule) | [ScheduleRequest](Collector#schedulerequest) | [ScheduleInfo](./Collector#scheduleinfo) |
| [**update_schedule**](./Collector#update_schedule) | [UpdateScheduleRequest](Collector#updateschedulerequest) | [ScheduleInfo](./Collector#scheduleinfo) |
| [**delete_schedule**](./Collector#delete_schedule) | [DeleteScheduleRequest](Collector#deleteschedulerequest) | [Empty](./Collector#empty) |
| [**list_schedules**](./Collector#list_schedules) | [ScheduleQuery](Collector#schedulequery) | [SchedulesInfo](./Collector#schedulesinfo) |



    
<br>

### create

desc: Creates a new Collector with information of the plugin to use. Information of the plugin includes `version`, `provider`, and `upgrade_mode`.
request_example: >-
{
"name": "AWS Collector",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.13.13",
"options": {},
"provider": "aws",
"metadata": {
"filter_format": [],
"supported_schedules": [
"hours"
],
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
],
"supported_features": [
"garbage_collection"
]
},
"upgrade_mode": "AUTO"
},
"priority": 1,
"tags": {
"type": "test"
},
"is_public": true
}
response_example: >-
{
"collector_id": "collector-2c0847644f39",
"name": "AWS Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.13.13",
"options": {},
"provider": "aws",
"metadata": {
"supported_schedules": [
"hours"
],
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
],
"filter_format": [],
"supported_features": [
"garbage_collection"
]
},
"upgrade_mode": "AUTO"
},
"priority": 1,
"tags": {
"type": "test"
},
"created_at": "2022-06-17T06:33:27.195Z",
"domain_id": "domain-58010aa2e451",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true
}



> **POST** /inventory/v1/collector/create
>






    
<br>

### update

desc: Updates a specific Collector. You can make changes in Collector settings, including `name` and `tags`.
request_example: >-
{
"collector_id": "collector-2c0847644f39",
"name": "New AWS Collector",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.14.0",
"provider": "aws",
"upgrade_mode": "MANUAL"
},
"priority": 10,
"tags": {
"a": "b"
}
}
response_example: >-
{
"collector_id": "collector-2c0847644f39",
"name": "New AWS Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.14.0",
"options": {},
"provider": "aws",
"metadata": {
"supported_schedules": [
"hours"
],
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
],
"filter_format": [],
"supported_features": [
"garbage_collection"
]
},
"upgrade_mode": "MANUAL"
},
"priority": 10,
"tags": {
"a": "b"
},
"created_at": "2022-06-17T06:33:27.195Z",
"domain_id": "domain-58010aa2e451",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true
}



> **POST** /inventory/v1/collector/update
>






    
<br>

### update_plugin

desc: Updates the plugin of a specific Collector. This method resets the plugin data in the Collector to update the `metadata`.
request_example: >-
{

}
response_example: >-
{

}



> **POST** /inventory/v1/collector/update-plugin
>






    
<br>

### verify_plugin

desc: Verifies the plugin of a specific Collector. This method validates the plugin data, `version` and `endpoint`.
request_example: >-
{

}
response_example: >-
{

}



> **POST** /inventory/v1/collector/verify-plugin
>






    
<br>

### delete

desc: Deletes a specific Collector. You must specify the `collector_id` of the Collector to delete.
request_example: >-
{

}
response_example: >-
{

}



> **POST** /inventory/v1/collector/delete
>






    
<br>

### get

desc: Gets a specific Collector. Prints detailed information about the Collector, including its state, basic information, and the plugin information used for cloud resource collection.
request_example: >-
{
"collector_id": "collector-f2e4e9cc7f21"
}



> **POST** /inventory/v1/collector/get
>






    
<br>

### enable

desc: Enables a specific Collector. By enabling a Collector, you can communicate with a plugin used for collection.
request_example: >-
{
"collector_id": "collector-f2e4e9cc7f21"
}
response_example: >-
{
"collector_id": "collector-f2e4e9cc7f21",
"name": "AWS Cloud Service Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.14.10",
"options": {},
"provider": "aws",
"metadata": {
"supported_schedules": [
"hours"
],
"filter_format": [],
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
],
"supported_features": [
"garbage_collection"
]
},
"upgrade_mode": "AUTO"
},
"priority": 10,
"tags": {},
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true,
"created_at": "2021-03-08T06:49:27.876Z",
"last_collected_at": "2022-06-17T06:00:07.162Z",
"domain_id": "domain-58010aa2e451"
}



> **POST** /inventory/v1/collector/enable
>






    
<br>

### disable

desc: Disables a specific Collector. By disabling a Collector, you cannot communicate with a plugin used for collection.
request_example: >-
{
"collector_id": "collector-f2e4e9cc7f21"
}
response_example: >-
{
"collector_id": "collector-f2e4e9cc7f21",
"name": "AWS Cloud Service Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.14.10",
"options": {},
"provider": "aws",
"metadata": {
"supported_schedules": [
"hours"
],
"filter_format": [],
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
],
"supported_features": [
"garbage_collection"
]
},
"upgrade_mode": "AUTO"
},
"priority": 10,
"tags": {},
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true,
"created_at": "2021-03-08T06:49:27.876Z",
"last_collected_at": "2022-06-17T06:00:07.162Z",
"domain_id": "domain-58010aa2e451"
}



> **POST** /inventory/v1/collector/disable
>






    
<br>

### list

desc: Gets a list of all Collectors. You can use a query to get a filtered list of Collectors.
request_example: >-
{
"query": {}
}
response_example: >-
{
"results": [
{
"job_id": "job-3b124006c2d2",
"status": "SUCCESS",
"filter": {},
"total_tasks": 2,
"collector_info": {
"collector_id": "collector-accd02663b3d",
"name": "openstack-collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-openstack-inven-collector",
"version": "0.4.2.20220616.134758"
},
"provider": "openstack",
"capability": {
"supported_schema": [
"openstack_credentials"
]
},
"is_public": true
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-17T08:00:01.225Z",
"updated_at": "2022-06-17T08:00:01.225Z",
"finished_at": "2022-06-17T08:00:15.197Z"
},
{
"job_id": "job-587a3d3b4db3",
"status": "SUCCESS",
"filter": {},
"total_tasks": 3,
"collector_info": {
"collector_id": "collector-2c0847644f39",
"name": "AWS stat-kwon Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.13.13.20220610.143142"
},
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-17T08:00:00.407Z",
"updated_at": "2022-06-17T08:00:00.407Z",
"finished_at": "2022-06-17T08:07:32.023Z"
}
],
"total_count": 2
}



> **POST** /inventory/v1/collector/list
>






    
<br>

### stat





> **POST** /inventory/v1/collector/stat
>






    
<br>

### collect

desc: ''
request_example: >-
{

}
response_example: >-
{

}



> **POST** /inventory/v1/collector/collect
>






    
<br>

### add_schedule

desc: Adds a schedule to a specific Collector. When specifying the time to collect, the schedule is assigned in units of one hour.The specified schedule is applied every day.
request_example: >-
{
"collector_id": "collector-2c0847644f39",
"name": "regular collection",
"schedule": {
"hours": [16, 18, 20, 22, 0]
}
}
response_example: >-
{
"schedule_id": "sched-dfb2f6ef84bc",
"name": "regular collection",
"collect_mode": "ALL",
"schedule": {
"hours": [
16,
18,
20,
22,
0
]
},
"created_at": "2022-06-17T07:12:07.374Z",
"collector_info": {
"collector_id": "collector-2c0847644f39",
"name": "AWS stat-kwon Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.13.13.20220610.143142",
"options": {},
"provider": "aws",
"metadata": {
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
],
"supported_features": [
"garbage_collection"
],
"filter_format": [],
"supported_schedules": [
"hours"
]
},
"upgrade_mode": "MANUAL"
},
"priority": 10,
"tags": {
"a": "b"
},
"created_at": "2022-06-17T06:33:27.195Z",
"domain_id": "domain-58010aa2e451",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true
},
"filter": {}
}



> **POST** /inventory/v1/collector/add_schedule
>






    
<br>

### get_schedule

desc: Gets a specific schedule set in a specific Collector. You must specify the `collector_id` of the Collector and the `schedule_id` of the schedule.
request_example: >-
{
"collector_id": "collector-2c0847644f39",
"schedule_id": "sched-dfb2f6ef84bc"
}
response_example: >-
{
"schedule_id": "sched-dfb2f6ef84bc",
"name": "regular collection",
"collect_mode": "ALL",
"schedule": {
"hours": [
16,
18,
20,
22,
0
]
},
"created_at": "2022-06-17T07:12:07.374Z",
"collector_info": {
"collector_id": "collector-2c0847644f39",
"name": "AWS stat-kwon Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.13.13.20220610.143142",
"options": {},
"provider": "aws",
"metadata": {
"supported_features": [
"garbage_collection"
],
"filter_format": [],
"supported_schedules": [
"hours"
],
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
]
},
"upgrade_mode": "MANUAL"
},
"priority": 10,
"tags": {
"a": "b"
},
"created_at": "2022-06-17T06:33:27.195Z",
"domain_id": "domain-58010aa2e451",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true
},
"filter": {}
}



> **POST** /inventory/v1/collector/get-schedule
>






    
<br>

### update_schedule

desc: Updates a specific schedule of the Collector. You can make changes in schedule settings, including `name` and collection time.
request_example: >-
{
"schedule_id": "sched-dfb2f6ef84bc",
"collector_id": "collector-2c0847644f39",
"name": "regular collection",
"collect_mode": "ALL",
"schedule": {
"hours": [2, 4, 6, 8, 0]
},
"filter": {}
}
response_example: >-
{
"schedule_id": "sched-dfb2f6ef84bc",
"name": "regular collection",
"collect_mode": "ALL",
"schedule": {
"hours": [
2,
4,
6,
8,
0
]
},
"created_at": "2022-06-17T07:12:07.374Z",
"collector_info": {
"collector_id": "collector-2c0847644f39",
"name": "AWS stat-kwon Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.13.13.20220610.143142",
"options": {},
"provider": "aws",
"metadata": {
"supported_features": [
"garbage_collection"
],
"supported_schedules": [
"hours"
],
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
],
"filter_format": []
},
"upgrade_mode": "MANUAL"
},
"priority": 10,
"tags": {
"a": "b"
},
"created_at": "2022-06-17T06:33:27.195Z",
"last_collected_at": "2022-06-17T08:00:00.793Z",
"domain_id": "domain-58010aa2e451",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true
},
"filter": {}
}



> **POST** /inventory/v1/collector/update-schedule
>






    
<br>

### delete_schedule

desc: Deletes a specific schedule of the Collector. You must specify the `schedule_id` of the schedule to delete.
request_example: >-
{
"schedule_id": "sched-dfb2f6ef84bc",
"collector_id": "collector-2c0847644f39"
}



> **POST** /inventory/v1/collector/delete-schedule
>






    
<br>

### list_schedules

desc: Gets a list of all schedules set in a specific Collector. You must specify the `collector_id` of the Collector to get the schedule from.
request_example: >-
{
"collector_id": "collector-f2e4e9cc7f21"
}
response_example: >-
{
"results": [
{
"schedule_id": "sched-572819cabe90",
"name": "daily",
"collect_mode": "ALL",
"schedule": {
"hours": [
15,
16,
18,
21,
0,
3,
4,
6,
9,
12
]
},
"created_at": "2021-03-13T14:32:46.137Z",
"collector_info": {
"collector_id": "collector-f2e4e9cc7f21",
"name": "AWS Cloud Service Collector",
"state": "ENABLED",
"plugin_info": {
"plugin_id": "plugin-30d21ef75a5d",
"version": "1.13.13.20220610.143142",
"options": {},
"provider": "aws",
"metadata": {
"supported_features": [
"garbage_collection"
],
"supported_schedules": [
"hours"
],
"filter_format": [],
"supported_resource_type": [
"inventory.CloudService",
"inventory.CloudServiceType",
"inventory.Region"
]
},
"upgrade_mode": "AUTO"
},
"priority": 10,
"tags": {},
"created_at": "2021-03-08T06:49:27.876Z",
"last_collected_at": "2022-06-17T06:00:07.162Z",
"domain_id": "domain-58010aa2e451",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key"
]
},
"is_public": true
},
"filter": {}
}
],
"total_count": 1
}



> **POST** /inventory/v1/collector/list_schedules
>






    


<br>
<br>

## Message



### CollectRequest
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **filter** (Struct)  `Required` 

  *is_required: false*

    
* **secret_id** (string)  `Required` 

  *is_required: false*

    
* **collect_mode** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **use_cache** (bool)  `Required` 

  *is_required: false*

    <br>

### CollectorInfo
* **collector_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **plugin_info** (PluginInfo)  `Required` 

    
* **priority** (int32)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **last_collected_at** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **capability** (Struct)  `Required` 

    
* **is_public** (bool)  `Required` 

    
* **project_id** (string)  `Required` 

    <br>

### CollectorQuery
* **query** (Query)  `Required` 

    
* **collector_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **priority** (int32)  `Required` 

    
* **plugin_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### CollectorRequest
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CollectorStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CollectorsInfo
* **results** (CollectorInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateCollectorRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **plugin_info** (PluginInfo)  `Required` 

  *is_required: true*

    
* **priority** (int32)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **is_public** (bool)  `Required` 

  *is_required: false
desc: default is true*

    
* **project_id** (string)  `Required` 

  *is_required: false
desc: if is_public is false, project_id is require
remained as is_public | True | False*

    <br>

### CreateScheduleRequest
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **collect_mode** (string)  `Required` 

  *is_required: false*

    
* **schedule** (Scheduled)  `Required` 

  *is_required: true*

    
* **filter** (Struct)  `Required` 

  *is_required: false*

    <br>

### DeleteScheduleRequest
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **collector_id** (string)  `Required` 

  *is_required: true*

    <br>

### ErrorInfo
* **error_code** (string)  `Required` 

    
* **message** (string)  `Required` 

    
* **additional** (Struct)  `Required` 

    <br>

### GetCollectorRequest
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### JobInfo
* **job_id** (string)  `Required` 

    
* **status** (Status)  `Required` 

    
* **filter** (Struct)  `Required` 

    
* **total_tasks** (int32)  `Required` 

    
* **remained_tasks** (int32)  `Required` 

    
* **errors** (ErrorInfo)  `Required` 

    
* **collector_info** (CollectorInfo)  `Required` 

    
* **project_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    
* **finished_at** (string)  `Required` 

    <br>

### PluginInfo
* **plugin_id** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **secret_group_id** (string)  `Required` 

    
* **provider** (string)  `Required` 

    
* **service_account_id** (string)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **upgrade_mode** (UpgradeMode)  `Required` 

    <br>

### ScheduleInfo
* **domain_id** (string)  `Required` 

    
* **schedule_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **collect_mode** (string)  `Required` 

    
* **schedule** (Scheduled)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **last_scheduled_at** (string)  `Required` 

    
* **collector_info** (CollectorInfo)  `Required` 

    
* **filter** (Struct)  `Required` 

    <br>

### ScheduleQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **schedule_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ScheduleRequest
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **collector_id** (string)  `Required` 

  *is_required: true*

    <br>

### Scheduled
* **cron** (string)  `Required` 

    
* **interval** (int32)  `Required` 

    
* **minutes** (int32)  `Required` 

    
* **hours** (int32)  `Required` 

    <br>

### SchedulesInfo
* **results** (ScheduleInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdateCollectorRequest
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **plugin_info** (PluginInfo)  `Required` 

  *is_required: false
note: deprecated, use update_plugin*

    
* **priority** (int32)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdatePluginRequest
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **version** (string)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **upgrade_mode** (UpgradeMode)  `Required` 

  *is_required: false*

    <br>

### UpdateScheduleRequest
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **collect_mode** (string)  `Required` 

  *is_required: false*

    
* **schedule** (Scheduled)  `Required` 

  *is_required: false*

    
* **filter** (Struct)  `Required` 

  *is_required: false*

    <br>

### VerifyInfo
* **status** (bool)  `Required` 

    <br>

### VerifyPluginRequest
* **collector_id** (string)  `Required` 

  *is_required: true*

    
* **secret_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
