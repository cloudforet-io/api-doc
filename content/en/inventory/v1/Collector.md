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
| [**create**](./Collector#create) | [CreateCollectorRequest](Collector#createcollectorrequest) | [CollectorInfo](Collector#collectorinfo) |
| [**update**](./Collector#update) | [UpdateCollectorRequest](Collector#updatecollectorrequest) | [CollectorInfo](Collector#collectorinfo) |
| [**update_plugin**](./Collector#update_plugin) | [UpdatePluginRequest](Collector#updatepluginrequest) | [CollectorInfo](Collector#collectorinfo) |
| [**verify_plugin**](./Collector#verify_plugin) | [VerifyPluginRequest](Collector#verifypluginrequest) | [Empty](Collector#empty) |
| [**delete**](./Collector#delete) | [CollectorRequest](Collector#collectorrequest) | [Empty](Collector#empty) |
| [**get**](./Collector#get) | [CollectorRequest](Collector#collectorrequest) | [CollectorInfo](Collector#collectorinfo) |
| [**list**](./Collector#list) | [CollectorQuery](Collector#collectorquery) | [CollectorsInfo](Collector#collectorsinfo) |
| [**stat**](./Collector#stat) | [CollectorStatQuery](Collector#collectorstatquery) | [Struct](Collector#struct) |
| [**collect**](./Collector#collect) | [CollectRequest](Collector#collectrequest) | [JobInfo](Collector#jobinfo) |



    
<br>

### create

Creates a new Collector with information of the plugin to use. Information of the plugin includes `version`, `provider`, and `upgrade_mode`.



> **POST** /inventory/v1/collector/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateCollectorRequest](./Collector#createcollectorrequest)

* **name** (string)   `Required` 


* **plugin_info** (PluginInfo)   `Required` 


* **resource_group** (ResourceGroup)   `Required` 


* **schedule** (Scheduled)  


* **provider** (string)  


* **secret_filter** (SecretFilter)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "name": "AWS Collector",
   "plugin_info": {
       "plugin_id": "plugin-30d21ef75a5d",
       "version": "1.13.13",
       "options": {},
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
   "schedule": {
       "state": "ENABLED",
       "hours": [0, 6, 12, 18]
   },
   "secret_filter": {
       "state": "ENABLED",
       "secrets": ["secret-xxx", "secret-yyy"],
       "service_accounts": ["sa-xxx", "sa-yyy"],
       "schemas": ["schema-xxx", "schema-yyy"]
   },
   "tags": {
       "type": "test"
   },
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
* **collector_id** (string)   `Required` 

* **name** (string)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **secret_filter** (SecretFilter)   `Required` 

* **plugin_info** (PluginInfo)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_collected_at** (string)   `Required` 



{{< highlight json >}}
{
   "collector_id": "collector-2c0847644f39",
   "name": "AWS Collector",
   "plugin_info": {
       "plugin_id": "plugin-30d21ef75a5d",
       "version": "1.13.13",
       "options": {},
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
   "schedule": {
       "state": "ENABLED",
       "hours": [0, 6, 12, 18]
   },
   "secret_filter": {
       "state": "ENABLED",
       "secrets": ["secret-xxx", "secret-yyy"],
       "service_accounts": ["sa-xxx", "sa-yyy"],
       "schemas": ["schema-xxx", "schema-yyy"]
   },
   "last_collected_at": "2022-06-17T06:33:27.195Z"
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

* **collector_id** (string)   `Required` 


* **name** (string)  


* **schedule** (Scheduled)  


* **secret_filter** (SecretFilter)  


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
   "schedule": {
       "state": "ENABLED",
       "hours": [0, 6, 12, 18]
   },
   "secret_filter": {
       "state": "ENABLED",
       "secrets": ["secret-xxx", "secret-yyy"],
       "service_accounts": ["sa-xxx", "sa-yyy"],
       "schemas": ["schema-xxx", "schema-yyy"]
   },
   "tags": {
       "a": "b"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
* **collector_id** (string)   `Required` 

* **name** (string)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **secret_filter** (SecretFilter)   `Required` 

* **plugin_info** (PluginInfo)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_collected_at** (string)   `Required` 



{{< highlight json >}}
{
   "collector_id": "collector-2c0847644f39",
   "name": "AWS Collector",
   "plugin_info": {
       "plugin_id": "plugin-30d21ef75a5d",
       "version": "1.13.13",
       "options": {},
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
   "schedule": {
       "state": "ENABLED",
       "hours": [0, 6, 12, 18]
   },
   "secret_filter": {
       "state": "ENABLED",
       "secrets": ["secret-xxx", "secret-yyy"],
       "service_accounts": ["sa-xxx", "sa-yyy"],
       "schemas": ["schema-xxx", "schema-yyy"]
   },
   "last_collected_at": "2022-06-17T06:33:27.195Z"
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
* **collector_id** (string)   `Required` 

* **name** (string)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **secret_filter** (SecretFilter)   `Required` 

* **plugin_info** (PluginInfo)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_collected_at** (string)   `Required` 



{{< highlight json >}}
{
   "collector_id": "collector-2c0847644f39",
   "name": "AWS Collector",
   "plugin_info": {
       "plugin_id": "plugin-30d21ef75a5d",
       "version": "1.13.13",
       "options": {},
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
   "schedule": {
       "state": "ENABLED",
       "hours": [0, 6, 12, 18]
   },
   "secret_filter": {
       "state": "ENABLED",
       "secrets": ["secret-xxx", "secret-yyy"],
       "service_accounts": ["sa-xxx", "sa-yyy"],
       "schemas": ["schema-xxx", "schema-yyy"]
   },
   "last_collected_at": "2022-06-17T06:33:27.195Z"
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

* **collector_id** (string)   `Required` 





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



[CollectorRequest](./Collector#collectorrequest)

* **collector_id** (string)   `Required` 





{{< highlight json >}}
{
   "collector_id": "collector-f2e4e9cc7f21"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorInfo](#COLLECTORINFO)
* **collector_id** (string)   `Required` 

* **name** (string)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **secret_filter** (SecretFilter)   `Required` 

* **plugin_info** (PluginInfo)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **resource_group** (ResourceGroup)   `Required` 

* **domain_id** (string)   `Required` 

* **workspace_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_collected_at** (string)   `Required` 



{{< highlight json >}}
{
   "collector_id": "collector-2c0847644f39",
   "name": "AWS Collector",
   "plugin_info": {
       "plugin_id": "plugin-30d21ef75a5d",
       "version": "1.13.13",
       "options": {},
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
   "schedule": {
       "state": "ENABLED",
       "hours": [0, 6, 12, 18]
   },
   "secret_filter": {
       "state": "ENABLED",
       "secrets": ["secret-xxx", "secret-yyy"],
       "service_accounts": ["sa-xxx", "sa-yyy"],
       "schemas": ["schema-xxx", "schema-yyy"]
   },
   "last_collected_at": "2022-06-17T06:33:27.195Z"
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

* **query** (Query)   `Required` 


* **collector_id** (string)   `Required` 


* **name** (string)   `Required` 


* **secret_filter_state** (State)   `Required` 


* **schedule_state** (State)   `Required` 


* **workspace_id** (string)   `Required` 


* **plugin_id** (string)   `Required` 





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CollectorsInfo](#COLLECTORSINFO)
* **results** (CollectorInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
    "results": [
       {
         "collector_id": "collector-2c0847644f39",
         "name": "AWS Collector",
         "plugin_info": {
             "plugin_id": "plugin-30d21ef75a5d",
             "version": "1.13.13",
             "options": {},
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
     "schedule": {
         "state": "ENABLED",
         "hours": [0, 6, 12, 18]
     },
     "secret_filter": {
         "state": "ENABLED",
         "secrets": ["secret-xxx", "secret-yyy"],
         "service_accounts": ["sa-xxx", "sa-yyy"],
         "schemas": ["schema-xxx", "schema-yyy"]
     },
     "last_collected_at": "2022-06-17T06:33:27.195Z"
   },
   {
     "collector_id": "collector-2c0847644f39",
     "name": "AWS Collector",
     "plugin_info": {
         "plugin_id": "plugin-30d21ef75a5d",
         "version": "1.13.13",
         "options": {},
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
     "schedule": {
         "state": "ENABLED",
         "hours": [0, 6, 12, 18]
     },
     "secret_filter": {
         "state": "ENABLED",
         "secrets": ["secret-xxx", "secret-yyy"],
         "service_accounts": ["sa-xxx", "sa-yyy"],
         "schemas": ["schema-xxx", "schema-yyy"]
     },
     "last_collected_at": "2022-06-17T06:33:27.195Z"
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






    


<br>
<br>

## Message



### CollectRequest
* **collector_id** (string)   `Required` 

    
* **secret_id** (string)  

    <br>

### CollectorInfo
* **collector_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **provider** (string)   `Required` 

    
* **capability** (Struct)   `Required` 

    
* **secret_filter** (SecretFilter)   `Required` 

    
* **plugin_info** (PluginInfo)   `Required` 

    
* **schedule** (Scheduled)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_collected_at** (string)   `Required` 

    <br>

### CollectorQuery
* **query** (Query)   `Required` 

    
* **collector_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **secret_filter_state** (State)   `Required` 

    
* **schedule_state** (State)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **plugin_id** (string)   `Required` 

    <br>

### CollectorRequest
* **collector_id** (string)   `Required` 

    <br>

### CollectorStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### CollectorsInfo
* **results** (CollectorInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### CreateCollectorRequest
* **name** (string)   `Required` 

    
* **plugin_info** (PluginInfo)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **schedule** (Scheduled)  

    
* **provider** (string)  

    
* **secret_filter** (SecretFilter)  

    
* **tags** (Struct)  

    <br>

### PluginInfo
* **plugin_id** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **metadata** (Struct)   `Required` 

    
* **upgrade_mode** (UpgradeMode)   `Required` 

    <br>

### Scheduled
* **state** (ScheduledState)   `Required` 

    
* **hours** (int32)  `Repeated`    `Required` 

    <br>

### SecretFilter
* **state** (SecretFilterState)   `Required` 

    
* **secrets** (string)  `Repeated`    `Required` 

    
* **service_accounts** (string)  `Repeated`    `Required` 

    
* **schemas** (string)  `Repeated`    `Required` 

    
* **exclude_secrets** (string)  `Repeated`    `Required` 

    
* **exclude_service_accounts** (string)  `Repeated`    `Required` 

    
* **exclude_schemas** (string)  `Repeated`    `Required` 

    <br>

### UpdateCollectorRequest
* **collector_id** (string)   `Required` 

    
* **name** (string)  

    
* **schedule** (Scheduled)  

    
* **secret_filter** (SecretFilter)  

    
* **tags** (Struct)  

    <br>

### UpdatePluginRequest
* **collector_id** (string)   `Required` 

    
* **version** (string)  

    
* **options** (Struct)  

    
* **upgrade_mode** (UpgradeMode)  

    <br>

### VerifyPluginRequest
* **collector_id** (string)   `Required` 

    
* **secret_id** (string)  

    <br>
