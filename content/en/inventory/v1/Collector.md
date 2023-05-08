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

> **POST** /inventory/v1/collector/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /inventory/v1/collector/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### update_plugin

> **POST** /inventory/v1/collector/update-plugin
>




 {{< tabs " update_plugin " >}}




{{< /tabs >}}

    
<br>

### verify_plugin

> **POST** /inventory/v1/collector/verify-plugin
>




 {{< tabs " verify_plugin " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /inventory/v1/collector/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /inventory/v1/collector/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /inventory/v1/collector/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /inventory/v1/collector/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /inventory/v1/collector/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /inventory/v1/collector/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    
<br>

### collect

> **POST** /inventory/v1/collector/collect
>




 {{< tabs " collect " >}}




{{< /tabs >}}

    
<br>

### add_schedule

> **POST** /inventory/v1/collector/add_schedule
>




 {{< tabs " add_schedule " >}}




{{< /tabs >}}

    
<br>

### get_schedule

> **POST** /inventory/v1/collector/get-schedule
>




 {{< tabs " get_schedule " >}}




{{< /tabs >}}

    
<br>

### update_schedule

> **POST** /inventory/v1/collector/update-schedule
>




 {{< tabs " update_schedule " >}}




{{< /tabs >}}

    
<br>

### delete_schedule

> **POST** /inventory/v1/collector/delete-schedule
>




 {{< tabs " delete_schedule " >}}




{{< /tabs >}}

    
<br>

### list_schedules

> **POST** /inventory/v1/collector/list_schedules
>




 {{< tabs " list_schedules " >}}




{{< /tabs >}}

    


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
