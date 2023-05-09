---
title: "Collector"
linkTitle: "Collector"
weight: 3
bookFlatSection: true
---
# [Collector](#Collector)
A Collector is a plugin instance collecting cloud resources. A Collector can collect the resource data manually or by a pre-set schedule.


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

Creates a new Collector with information of the plugin to use. Information of the plugin includes `version`, `provider`, and `upgrade_mode`.



> **POST** /inventory/v1/collector/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateCollectorRequest](./Collector#createcollectorrequest)

* **name** (string)  `Required` 


* **plugin_info** (PluginInfo)  `Required` 


* **domain_id** (string)  `Required` 


* **priority** (int32) 


* **tags** (Struct) 


* **is_public** (bool) 

  *default is true*


* **project_id** (string) 

  *if is_public is false, project_id is require
remained as is_public | True | False*





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Collector. You can make changes in Collector settings, including `name` and `tags`.



> **POST** /inventory/v1/collector/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateCollectorRequest](./Collector#updatecollectorrequest)

* **collector_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **name** (string) 


* **plugin_info** (PluginInfo) 


* **priority** (int32) 


* **tags** (Struct) 





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update_plugin

Updates the plugin of a specific Collector. This method resets the plugin data in the Collector to update the `metadata`.



> **POST** /inventory/v1/collector/update-plugin
>





 {{< tabs " update_plugin " >}}



 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### verify_plugin

Verifies the plugin of a specific Collector. This method validates the plugin data, `version` and `endpoint`.



> **POST** /inventory/v1/collector/verify-plugin
>






    
<br>

### delete

Deletes a specific Collector. You must specify the `collector_id` of the Collector to delete.



> **POST** /inventory/v1/collector/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[CollectorRequest](./Collector#collectorrequest)

* **collector_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "collector_id": "collector-f2e4e9cc7f21"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Collector. Prints detailed information about the Collector, including its state, basic information, and the plugin information used for cloud resource collection.



> **POST** /inventory/v1/collector/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetCollectorRequest](./Collector#getcollectorrequest)

* **collector_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **only** (string) 





{{< highlight json >}}
{
   "collector_id": "collector-f2e4e9cc7f21"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable

Enables a specific Collector. By enabling a Collector, you can communicate with a plugin used for collection.



> **POST** /inventory/v1/collector/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[CollectorRequest](./Collector#collectorrequest)

* **collector_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "collector_id": "collector-f2e4e9cc7f21"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable

Disables a specific Collector. By disabling a Collector, you cannot communicate with a plugin used for collection.



> **POST** /inventory/v1/collector/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[CollectorRequest](./Collector#collectorrequest)

* **collector_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "collector_id": "collector-f2e4e9cc7f21"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
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



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Collectors. You can use a query to get a filtered list of Collectors.



> **POST** /inventory/v1/collector/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[CollectorQuery](./Collector#collectorquery)

* **query** (Query)  `Required` 


* **collector_id** (string)  `Required` 


* **name** (string)  `Required` 


* **state** (State)  `Required` 


* **priority** (int32)  `Required` 


* **plugin_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorsInfo](#COLLECTORSINFO)
* **results** (CollectorInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /inventory/v1/collector/stat
>






    
<br>

### collect





> **POST** /inventory/v1/collector/collect
>





 {{< tabs " collect " >}}



 {{< tab "Response Example" >}}

[JobInfo](#JOBINFO)
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



{{< highlight json >}}
{
     "job_id": "job-123456789012",
     "status": "ERROR",
     "filter": {},
     "total_tasks": 2,
     "collector_info": {
         "collector_id": "collector-123456789012",
         "name": "Jenkins Collector",
         "state": "ENABLED",
         "plugin_info": {
             "plugin_id": "plugin-jenkins-inven-collector",
             "version": "0.1.1"
         },
         "provider": "jenkins",
         "capability": {},
         "is_public": true
     },
     "domain_id": "domain-123456789012",
     "created_at": "2022-01-01T10:00:01.389Z",
     "updated_at": "2022-01-01T10:00:01.389Z",
     "finished_at": "2022-01-01T10:02:11.270Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### add_schedule

Adds a schedule to a specific Collector. When specifying the time to collect, the schedule is assigned in units of one hour.The specified schedule is applied every day.



> **POST** /inventory/v1/collector/add_schedule
>





 {{< tabs " add_schedule " >}}

 {{< tab "Request Example" >}}



[CreateScheduleRequest](./Collector#createschedulerequest)

* **domain_id** (string)  `Required` 


* **collector_id** (string)  `Required` 


* **schedule** (Scheduled)  `Required` 


* **name** (string) 


* **collect_mode** (string) 


* **filter** (Struct) 





{{< highlight json >}}
{
   "collector_id": "collector-2c0847644f39",
   "name": "regular collection",
   "schedule": {
       "hours": [16, 18, 20, 22, 0]
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ScheduleInfo](#SCHEDULEINFO)
* **domain_id** (string)  `Required` 

* **schedule_id** (string)  `Required` 

* **name** (string)  `Required` 

* **collect_mode** (string)  `Required` 

* **schedule** (Scheduled)  `Required` 

* **created_at** (string)  `Required` 

* **last_scheduled_at** (string)  `Required` 

* **collector_info** (CollectorInfo)  `Required` 

* **filter** (Struct)  `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### get_schedule

Gets a specific schedule set in a specific Collector. You must specify the `collector_id` of the Collector and the `schedule_id` of the schedule.



> **POST** /inventory/v1/collector/get-schedule
>





 {{< tabs " get_schedule " >}}

 {{< tab "Request Example" >}}



[ScheduleRequest](./Collector#schedulerequest)

* **domain_id** (string)  `Required` 


* **schedule_id** (string)  `Required` 


* **collector_id** (string)  `Required` 





{{< highlight json >}}
{
   "collector_id": "collector-2c0847644f39",
   "schedule_id": "sched-dfb2f6ef84bc"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ScheduleInfo](#SCHEDULEINFO)
* **domain_id** (string)  `Required` 

* **schedule_id** (string)  `Required` 

* **name** (string)  `Required` 

* **collect_mode** (string)  `Required` 

* **schedule** (Scheduled)  `Required` 

* **created_at** (string)  `Required` 

* **last_scheduled_at** (string)  `Required` 

* **collector_info** (CollectorInfo)  `Required` 

* **filter** (Struct)  `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update_schedule

Updates a specific schedule of the Collector. You can make changes in schedule settings, including `name` and collection time.



> **POST** /inventory/v1/collector/update-schedule
>





 {{< tabs " update_schedule " >}}

 {{< tab "Request Example" >}}



[UpdateScheduleRequest](./Collector#updateschedulerequest)

* **domain_id** (string)  `Required` 


* **schedule_id** (string)  `Required` 


* **collector_id** (string)  `Required` 


* **name** (string) 


* **collect_mode** (string) 


* **schedule** (Scheduled) 


* **filter** (Struct) 





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ScheduleInfo](#SCHEDULEINFO)
* **domain_id** (string)  `Required` 

* **schedule_id** (string)  `Required` 

* **name** (string)  `Required` 

* **collect_mode** (string)  `Required` 

* **schedule** (Scheduled)  `Required` 

* **created_at** (string)  `Required` 

* **last_scheduled_at** (string)  `Required` 

* **collector_info** (CollectorInfo)  `Required` 

* **filter** (Struct)  `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete_schedule

Deletes a specific schedule of the Collector. You must specify the `schedule_id` of the schedule to delete.



> **POST** /inventory/v1/collector/delete-schedule
>





 {{< tabs " delete_schedule " >}}

 {{< tab "Request Example" >}}



[DeleteScheduleRequest](./Collector#deleteschedulerequest)

* **domain_id** (string)  `Required` 


* **schedule_id** (string)  `Required` 


* **collector_id** (string)  `Required` 





{{< highlight json >}}
{
   "schedule_id": "sched-dfb2f6ef84bc",
   "collector_id": "collector-2c0847644f39"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### list_schedules

Gets a list of all schedules set in a specific Collector. You must specify the `collector_id` of the Collector to get the schedule from.



> **POST** /inventory/v1/collector/list_schedules
>





 {{< tabs " list_schedules " >}}

 {{< tab "Request Example" >}}



[ScheduleQuery](./Collector#schedulequery)

* **collector_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **query** (Query) 


* **schedule_id** (string) 





{{< highlight json >}}
{
   "collector_id": "collector-f2e4e9cc7f21"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchedulesInfo](#SCHEDULESINFO)
* **results** (ScheduleInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    


<br>
<br>

## Message



### CollectRequest
* **collector_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **filter** (Struct) 

    
* **secret_id** (string) 

    
* **collect_mode** (string) 

    
* **use_cache** (bool) 

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

    
* **domain_id** (string)  `Required` 

    <br>

### CollectorStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### CollectorsInfo
* **results** (CollectorInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### CreateCollectorRequest
* **name** (string)  `Required` 

    
* **plugin_info** (PluginInfo)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **priority** (int32) 

    
* **tags** (Struct) 

    
* **is_public** (bool) 

  *default is true*

    
* **project_id** (string) 

  *if is_public is false, project_id is require
remained as is_public | True | False*

    <br>

### CreateScheduleRequest
* **domain_id** (string)  `Required` 

    
* **collector_id** (string)  `Required` 

    
* **schedule** (Scheduled)  `Required` 

    
* **name** (string) 

    
* **collect_mode** (string) 

    
* **filter** (Struct) 

    <br>

### DeleteScheduleRequest
* **domain_id** (string)  `Required` 

    
* **schedule_id** (string)  `Required` 

    
* **collector_id** (string)  `Required` 

    <br>

### ErrorInfo
* **error_code** (string)  `Required` 

    
* **message** (string)  `Required` 

    
* **additional** (Struct)  `Required` 

    <br>

### GetCollectorRequest
* **collector_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

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
* **collector_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **schedule_id** (string) 

    <br>

### ScheduleRequest
* **domain_id** (string)  `Required` 

    
* **schedule_id** (string)  `Required` 

    
* **collector_id** (string)  `Required` 

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

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **plugin_info** (PluginInfo) 

    
* **priority** (int32) 

    
* **tags** (Struct) 

    <br>

### UpdatePluginRequest
* **collector_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **version** (string) 

    
* **options** (Struct) 

    
* **upgrade_mode** (UpgradeMode) 

    <br>

### UpdateScheduleRequest
* **domain_id** (string)  `Required` 

    
* **schedule_id** (string)  `Required` 

    
* **collector_id** (string)  `Required` 

    
* **name** (string) 

    
* **collect_mode** (string) 

    
* **schedule** (Scheduled) 

    
* **filter** (Struct) 

    <br>

### VerifyInfo
* **status** (bool)  `Required` 

    <br>

### VerifyPluginRequest
* **collector_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **secret_id** (string) 

    <br>
