---
description: A Collector is a plugin instance collecting cloud resources. A Collector can collect the resource data manually or by a pre-set schedule.
---
# Collector

>  **Package : spaceone.api.inventory.v1**

## Collector

{% hint style="info" %}
**Collector Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](collector.md#create)|   [CreateCollectorRequest](collector.md#createcollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |
| [**update**](collector.md#update)|   [UpdateCollectorRequest](collector.md#updatecollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |
| [**update_plugin**](collector.md#update_plugin)|   [UpdatePluginRequest](collector.md#updatepluginrequest) |   [CollectorInfo](collector.md#collectorinfo) |
| [**verify_plugin**](collector.md#verify_plugin)|   [VerifyPluginRequest](collector.md#verifypluginrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**delete**](collector.md#delete)|   [CollectorRequest](collector.md#collectorrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](collector.md#get)|   [GetCollectorRequest](collector.md#getcollectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |
| [**enable**](collector.md#enable)|   [CollectorRequest](collector.md#collectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |
| [**disable**](collector.md#disable)|   [CollectorRequest](collector.md#collectorrequest) |   [CollectorInfo](collector.md#collectorinfo) |
| [**list**](collector.md#list)|   [CollectorQuery](collector.md#collectorquery) |   [CollectorsInfo](collector.md#collectorsinfo) |
| [**stat**](collector.md#stat)|   [CollectorStatQuery](collector.md#collectorstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**collect**](collector.md#collect)|   [CollectRequest](collector.md#collectrequest) |   [JobInfo](collector.md#jobinfo) |
| [**add_schedule**](collector.md#add_schedule)|   [CreateScheduleRequest](collector.md#createschedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |
| [**get_schedule**](collector.md#get_schedule)|   [ScheduleRequest](collector.md#schedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |
| [**update_schedule**](collector.md#update_schedule)|   [UpdateScheduleRequest](collector.md#updateschedulerequest) |   [ScheduleInfo](collector.md#scheduleinfo) |
| [**delete_schedule**](collector.md#delete_schedule)|   [DeleteScheduleRequest](collector.md#deleteschedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**list_schedules**](collector.md#list_schedules)|   [ScheduleQuery](collector.md#schedulequery) |   [SchedulesInfo](collector.md#schedulesinfo) | 
 

 
### create
> **POST** /inventory/v1/collector/create
>

> Creates a new Collector with information of the plugin to use. Information of the plugin includes `version`, `provider`, and `upgrade_mode`.

| Type | Message |
| :--- | :--- |
| Request | [CreateCollectorRequest](collector.md#createcollectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
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
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /inventory/v1/collector/update
>

> Updates a specific Collector. You can make changes in Collector settings, including `name` and `tags`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateCollectorRequest](collector.md#updatecollectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
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
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### update_plugin
> **POST** /inventory/v1/collector/update-plugin
>

> Updates the plugin of a specific Collector. This method resets the plugin data in the Collector to update the `metadata`.

| Type | Message |
| :--- | :--- |
| Request | [UpdatePluginRequest](collector.md#updatepluginrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### verify_plugin
> **POST** /inventory/v1/collector/verify-plugin
>

> Verifies the plugin of a specific Collector. This method validates the plugin data, `version` and `endpoint`.

| Type | Message |
| :--- | :--- |
| Request | [VerifyPluginRequest](collector.md#verifypluginrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /inventory/v1/collector/delete
>

> Deletes a specific Collector. You must specify the `collector_id` of the Collector to delete.

| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](collector.md#collectorrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /inventory/v1/collector/get
>

> Gets a specific Collector. Prints detailed information about the Collector, including its state, basic information, and the plugin information used for cloud resource collection.

| Type | Message |
| :--- | :--- |
| Request | [GetCollectorRequest](collector.md#getcollectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "collector_id": "collector-f2e4e9cc7f21"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **POST** /inventory/v1/collector/enable
>

> Enables a specific Collector. By enabling a Collector, you can communicate with a plugin used for collection.

| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](collector.md#collectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "collector_id": "collector-f2e4e9cc7f21"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **POST** /inventory/v1/collector/disable
>

> Disables a specific Collector. By disabling a Collector, you cannot communicate with a plugin used for collection.

| Type | Message |
| :--- | :--- |
| Request | [CollectorRequest](collector.md#collectorrequest) |
| Response |  [CollectorInfo](collector.md#collectorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "collector_id": "collector-f2e4e9cc7f21"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /inventory/v1/collector/list
>

> Gets a list of all Collectors. You can use a query to get a filtered list of Collectors.

| Type | Message |
| :--- | :--- |
| Request | [CollectorQuery](collector.md#collectorquery) |
| Response |  [CollectorsInfo](collector.md#collectorsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /inventory/v1/collector/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CollectorStatQuery](collector.md#collectorstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### collect
> **POST** /inventory/v1/collector/collect
>

> ''

| Type | Message |
| :--- | :--- |
| Request | [CollectRequest](collector.md#collectrequest) |
| Response |  [JobInfo](collector.md#jobinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### add_schedule
> **POST** /inventory/v1/collector/add_schedule
>

> Adds a schedule to a specific Collector. When specifying the time to collect, the schedule is assigned in units of one hour.The specified schedule is applied every day.

| Type | Message |
| :--- | :--- |
| Request | [CreateScheduleRequest](collector.md#createschedulerequest) |
| Response |  [ScheduleInfo](collector.md#scheduleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "collector_id": "collector-2c0847644f39",
    "name": "regular collection",
    "schedule": {
        "hours": [
            16,
            18,
            20,
            22,
            0
        ]
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### get_schedule
> **POST** /inventory/v1/collector/get-schedule
>

> Gets a specific schedule set in a specific Collector. You must specify the `collector_id` of the Collector and the `schedule_id` of the schedule.

| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](collector.md#schedulerequest) |
| Response |  [ScheduleInfo](collector.md#scheduleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "collector_id": "collector-2c0847644f39",
    "schedule_id": "sched-dfb2f6ef84bc"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### update_schedule
> **POST** /inventory/v1/collector/update-schedule
>

> Updates a specific schedule of the Collector. You can make changes in schedule settings, including `name` and collection time.

| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRequest](collector.md#updateschedulerequest) |
| Response |  [ScheduleInfo](collector.md#scheduleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "schedule_id": "sched-dfb2f6ef84bc",
    "collector_id": "collector-2c0847644f39",
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
    "filter": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### delete_schedule
> **POST** /inventory/v1/collector/delete-schedule
>

> Deletes a specific schedule of the Collector. You must specify the `schedule_id` of the schedule to delete.

| Type | Message |
| :--- | :--- |
| Request | [DeleteScheduleRequest](collector.md#deleteschedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "schedule_id": "sched-dfb2f6ef84bc",
    "collector_id": "collector-2c0847644f39"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list_schedules
> **POST** /inventory/v1/collector/list_schedules
>

> Gets a list of all schedules set in a specific Collector. You must specify the `collector_id` of the Collector to get the schedule from.

| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](collector.md#schedulequery) |
| Response |  [SchedulesInfo](collector.md#schedulesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "collector_id": "collector-f2e4e9cc7f21"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}


## 

## Message

### CollectRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✔| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| secret_id |string|✘| |
| collect_mode |string|✘| |
| domain_id |string|✔| |
| use_cache |bool|✘| |

### CollectorInfo
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
      <td style="text-align:left; width:100px;">collector_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
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
      <td style="text-align:left; width:100px;">plugin_info</td>
      <td style="text-align:left"><a href="collector.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">last_collected_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_public</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### CollectorQuery
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
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">collector_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
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
      <td style="text-align:left; width:100px;">priority</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### CollectorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✔| |
| domain_id |string|✔| |

### CollectorStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### CollectorsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CollectorInfo](collector.md#collectorinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCollectorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| plugin_info |[PluginInfo](collector.md#plugininfo)|✔| |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
| is_public |bool|✘| default is true|
| project_id |string|✔| if is_public is false, project_id is requireremained as is_public | True | False|

### CreateScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✔| |
| collector_id |string|✔| |
| name |string|✘| |
| collect_mode |string|✘| |
| schedule |[Scheduled](collector.md#scheduled)|✔| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |

### DeleteScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✔| |
| schedule_id |string|✔| |
| collector_id |string|✔| |

### ErrorInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| error_code |string | |
| message |string | |
| additional |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### GetCollectorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### JobInfo
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
      <td style="text-align:left; width:100px;">job_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">status</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREATED</li>
          	<li>CANCELED</li>
          	<li>IN_PROGRESS</li>
          	<li>SUCCESS</li>
          	<li>ERROR</li>
          	<li>TIMEOUT</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">filter</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">total_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">remained_tasks</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto">int32</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">errors</td>
      <td style="text-align:left"><a href="collector.md#errorinfo">list of ErrorInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">collector_info</td>
      <td style="text-align:left"><a href="collector.md#collectorinfo">CollectorInfo</a></td>
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
    <tr>
      <td style="text-align:left; width:100px;">finished_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



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
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_group_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">service_account_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ScheduleInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| domain_id |string | |
| schedule_id |string | |
| name |string | |
| collect_mode |string | |
| schedule |[Scheduled](collector.md#scheduled) | |
| created_at |string | |
| last_scheduled_at |string | |
| collector_info |[CollectorInfo](collector.md#collectorinfo) | |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### ScheduleQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| collector_id |string|✔| |
| schedule_id |string|✘| |
| domain_id |string|✔| |

### ScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✔| |
| schedule_id |string|✔| |
| collector_id |string|✔| |

### Scheduled
| Field | Type |  Description |
| :--- | :--- | :--- |
| cron |string | |
| interval |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| minutes |[list of int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| hours |[list of int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### SchedulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ScheduleInfo](collector.md#scheduleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateCollectorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✔| |
| name |string|✘| |
| plugin_info |[PluginInfo](collector.md#plugininfo)|✘| |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### UpdatePluginRequest
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
      <td style="text-align:left; width:100px;">collector_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UpdateScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| domain_id |string|✔| |
| schedule_id |string|✔| |
| collector_id |string|✔| |
| name |string|✘| |
| collect_mode |string|✘| |
| schedule |[Scheduled](collector.md#scheduled)|✘| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |

### VerifyInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| status |bool | |

### VerifyPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| collector_id |string|✔| |
| secret_id |string|✘| |
| domain_id |string|✔| |
