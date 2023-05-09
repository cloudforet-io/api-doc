---
title: "Schedule"
linkTitle: "Schedule"
weight: 3
bookFlatSection: true
---
# [Schedule](#Schedule)
desc: A Schedule is a time schedule of when a User will use a query.


>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## Schedule





**Schedule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./Schedule#add) | [AddScheduleRequest](Schedule#addschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**update**](./Schedule#update) | [UpdateScheduleRequest](Schedule#updateschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**enable**](./Schedule#enable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**disable**](./Schedule#disable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**delete**](./Schedule#delete) | [ScheduleRequest](Schedule#schedulerequest) | [Empty](./Schedule#empty) |
| [**get**](./Schedule#get) | [GetScheduleRequest](Schedule#getschedulerequest) | [ScheduleInfo](./Schedule#scheduleinfo) |
| [**list**](./Schedule#list) | [ScheduleQuery](Schedule#schedulequery) | [SchedulesInfo](./Schedule#schedulesinfo) |
| [**stat**](./Schedule#stat) | [ScheduleStatQuery](Schedule#schedulestatquery) | [Struct](./Schedule#struct) |



    
<br>

### add

desc: Adds a new Schedule. When creating, `topic` and queries to be used should be specified. The time interval of the Schedule should be also specified to run queries repeatedly. The run set by Schedule starts every hour on the hour.
request_example: >-
{
"topic": "daily_cloud_service_summary_test",
"options": {"aggregate": [{"query": {
"extend_data": {"label": "Server"}, "query": {
"filter": [{"key": "ref_cloud_service_type.is_primary", "value": true, "operator": "eq"},
{"value": "Server", "operator": "eq", "key": "ref_cloud_service_type.labels"}],
"aggregate": [{"group": {
"fields": [
{
"name": "value",
"operator": "count"}],
"keys": [
{
"name": "project_id",
"key": "project_id"},
{
"key": "cloud_service_type",
"name": "cloud_service_type"},
{
"key": "cloud_service_group",
"name": "cloud_service_group"},
{
"key": "provider",
"name": "provider"}]}}]},
"resource_type": "inventory.CloudService"}}, {"concat": {"resource_type": "inventory.CloudService", "query": {
"aggregate": [{"group": {"keys": [{"key": "project_id", "name": "project_id"},
{"name": "cloud_service_type", "key": "cloud_service_type"},
{"key": "cloud_service_group", "name": "cloud_service_group"},
{"key": "provider", "name": "provider"}],
"fields": [{"name": "value", "operator": "count"}]}}],
"filter": [{"value": true, "operator": "eq", "key": "ref_cloud_service_type.is_primary"},
{"value": "Database", "operator": "eq", "key": "ref_cloud_service_type.labels"}]},
"extend_data": {"label": "Database"}}}, {"concat": {
"resource_type": "inventory.CloudService", "extend_data": {"label": "Container"}, "query": {
"filter": [{"value": true, "key": "ref_cloud_service_type.is_primary", "operator": "eq"},
{"key": "ref_cloud_service_type.labels", "value": "Container", "operator": "eq"}],
"aggregate": [{
"group": {
"fields": [
{
"name": "value",
"operator": "count"}],
"keys": [
{
"key": "project_id",
"name": "project_id"},
{
"name": "cloud_service_type",
"key": "cloud_service_type"},
{
"name": "cloud_service_group",
"key": "cloud_service_group"},
{
"key": "provider",
"name": "provider"}]}}]}}},
{"concat": {
"extend_data": {"label": "Networking"},
"query": {"aggregate": [{"group": {
"keys": [{"name": "project_id",
"key": "project_id"}, {
"key": "cloud_service_type",
"name": "cloud_service_type"},
{
"key": "cloud_service_group",
"name": "cloud_service_group"},
{"key": "provider",
"name": "provider"}],
"fields": [{"name": "value",
"operator": "count"}]}}],
"filter": [{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true},
{
"key": "ref_cloud_service_type.labels",
"value": "Networking",
"operator": "eq"}]},
"resource_type": "inventory.CloudService"}},
{"concat": {
"resource_type": "inventory.CloudService",
"query": {"filter": [{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"},
{"operator": "eq",
"value": "Security",
"key": "ref_cloud_service_type.labels"}],
"aggregate": [{"group": {
"keys": [
{"key": "project_id",
"name": "project_id"},
{
"key": "cloud_service_type",
"name": "cloud_service_type"},
{
"name": "cloud_service_group",
"key": "cloud_service_group"},
{"key": "provider",
"name": "provider"}],
"fields": [
{"name": "value",
"operator": "count"}]}}]},
"extend_data": {"label": "Security"}}},
{"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {"label": "Analytics"},
"query": {"filter": [{"value": true,
"key": "ref_cloud_service_type.is_primary",
"operator": "eq"},
{"operator": "eq",
"value": "Analytics",
"key": "ref_cloud_service_type.labels"}],
"aggregate": [{"group": {
"fields": [
{"operator": "count",
"name": "value"}],
"keys": [
{"name": "project_id",
"key": "project_id"},
{
"key": "cloud_service_type",
"name": "cloud_service_type"},
{
"key": "cloud_service_group",
"name": "cloud_service_group"},
{"key": "provider",
"name": "provider"}]}}]}}},
{"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {"label": "All"},
"query": {"aggregate": [{"group": {
"keys": [{"name": "project_id",
"key": "project_id"}, {
"name": "cloud_service_type",
"key": "cloud_service_type"},
{
"name": "cloud_service_group",
"key": "cloud_service_group"},
{"key": "provider",
"name": "provider"}],
"fields": [{"operator": "count",
"name": "value"}]}}],
"filter": [{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true}]}}},
{"concat": {"query": {"filter": [
{"value": true, "operator": "eq",
"key": "ref_cloud_service_type.is_major"},
{"value": "Storage", "operator": "eq",
"key": "ref_cloud_service_type.labels"}],
"aggregate": [{
"group": {
"fields": [
{
"name": "value",
"key": "data.size",
"operator": "sum"}],
"keys": [
{
"name": "project_id",
"key": "project_id"},
{
"name": "cloud_service_type",
"key": "cloud_service_type"},
{
"key": "cloud_service_group",
"name": "cloud_service_group"},
{
"key": "provider",
"name": "provider"}]}}]},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Storage"}
}}]},
"schedule": {"hours": [1]},
"tags": {},
"domain_id": "domain-58010aa2e451"}

response_example: >-
{
"schedule_id": "sch-65bb6b55d162",
"topic": "daily_cloud_service_summary_test",
"state": "ENABLED",
"options": {
"aggregate": [
{
"query": {
"extend_data": {
"label": "Server"
},
"resource_type": "inventory.CloudService",
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"
},
{
"operator": "eq",
"key": "ref_cloud_service_type.labels",
"value": "Server"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
]
}
}
},
{
"concat": {
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
],
"filter": [
{
"operator": "eq",
"value": true,
"key": "ref_cloud_service_type.is_primary"
},
{
"operator": "eq",
"key": "ref_cloud_service_type.labels",
"value": "Database"
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Database"
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
],
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"
},
{
"operator": "eq",
"key": "ref_cloud_service_type.labels",
"value": "Container"
}
]
},
"extend_data": {
"label": "Container"
}
}
},
{
"concat": {
"query": {
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
],
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Networking"
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Networking"
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Security"
},
"query": {
"filter": [
{
"operator": "eq",
"key": "ref_cloud_service_type.is_primary",
"value": true
},
{
"operator": "eq",
"key": "ref_cloud_service_type.labels",
"value": "Security"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
]
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"
},
{
"key": "ref_cloud_service_type.labels",
"value": "Analytics",
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
]
},
"extend_data": {
"label": "Analytics"
}
}
},
{
"concat": {
"extend_data": {
"label": "All"
},
"resource_type": "inventory.CloudService",
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
]
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"operator": "sum",
"name": "value",
"key": "data.size"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
],
"filter": [
{
"operator": "eq",
"key": "ref_cloud_service_type.is_major",
"value": true
},
{
"value": "Storage",
"operator": "eq",
"key": "ref_cloud_service_type.labels"
}
]
},
"extend_data": {
"label": "Storage"
}
}
}
]
},
"schedule": {
"hours": [
1
]
},
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-26T02:08:48.233Z"
}



> **POST** /statistics/v1/schedule/add
>






    
<br>

### update

desc: Updates a specific Schedule. You can make changes in Schedule settings, including time intervals.
request_example: >-
{
"schedule_id": "sch-65bb6b55d162",
"schedule": {"hours": [2]},
"tags": {"a": "b"},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"schedule_id": "sch-65bb6b55d162",
"topic": "daily_cloud_service_summary_test",
"state": "ENABLED",
"options": {
"aggregate": [
{
"query": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Server"
},
"query": {
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"key": "ref_cloud_service_type.labels",
"value": "Server",
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
]
}
}
},
{
"concat": {
"extend_data": {
"label": "Database"
},
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
],
"filter": [
{
"operator": "eq",
"value": true,
"key": "ref_cloud_service_type.is_primary"
},
{
"value": "Database",
"key": "ref_cloud_service_type.labels",
"operator": "eq"
}
]
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"extend_data": {
"label": "Container"
},
"query": {
"filter": [
{
"value": true,
"key": "ref_cloud_service_type.is_primary",
"operator": "eq"
},
{
"operator": "eq",
"key": "ref_cloud_service_type.labels",
"value": "Container"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
]
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
],
"filter": [
{
"operator": "eq",
"value": true,
"key": "ref_cloud_service_type.is_primary"
},
{
"operator": "eq",
"value": "Networking",
"key": "ref_cloud_service_type.labels"
}
]
},
"extend_data": {
"label": "Networking"
}
}
},
{
"concat": {
"query": {
"filter": [
{
"value": true,
"key": "ref_cloud_service_type.is_primary",
"operator": "eq"
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Security"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
]
},
"extend_data": {
"label": "Security"
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Analytics"
},
"query": {
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Analytics"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
]
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "All"
},
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
]
}
}
},
{
"concat": {
"extend_data": {
"label": "Storage"
},
"resource_type": "inventory.CloudService",
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_major",
"operator": "eq",
"value": true
},
{
"value": "Storage",
"key": "ref_cloud_service_type.labels",
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"key": "data.size",
"name": "value",
"operator": "sum"
}
]
}
}
]
}
}
}
]
},
"schedule": {
"hours": [
2
]
},
"tags": {
"a": "b"
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-26T02:08:48.233Z"
}



> **POST** /statistics/schedule/update
>






    
<br>

### enable

desc: Enables a specific Schedule. If a Schedule is enabled, the query usage will be scheduled by the time interval specified.
request_example: >-
{
"schedule_id": "sch-65bb6b55d162",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"schedule_id": "sch-65bb6b55d162",
"topic": "daily_cloud_service_summary_test",
"state": "ENABLED",
"options": {
"aggregate": [
{
"query": {
"query": {
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
],
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"value": "Server",
"operator": "eq",
"key": "ref_cloud_service_type.labels"
}
]
},
"extend_data": {
"label": "Server"
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Database"
},
"query": {
"filter": [
{
"operator": "eq",
"key": "ref_cloud_service_type.is_primary",
"value": true
},
{
"value": "Database",
"operator": "eq",
"key": "ref_cloud_service_type.labels"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
]
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Container"
},
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
],
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true
},
{
"key": "ref_cloud_service_type.labels",
"value": "Container",
"operator": "eq"
}
]
}
}
},
{
"concat": {
"extend_data": {
"label": "Networking"
},
"resource_type": "inventory.CloudService",
"query": {
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
],
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Networking"
}
]
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Security"
},
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
],
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"value": "Security",
"operator": "eq",
"key": "ref_cloud_service_type.labels"
}
]
}
}
},
{
"concat": {
"extend_data": {
"label": "Analytics"
},
"resource_type": "inventory.CloudService",
"query": {
"filter": [
{
"operator": "eq",
"value": true,
"key": "ref_cloud_service_type.is_primary"
},
{
"operator": "eq",
"value": "Analytics",
"key": "ref_cloud_service_type.labels"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
]
}
}
},
{
"concat": {
"extend_data": {
"label": "All"
},
"query": {
"filter": [
{
"value": true,
"key": "ref_cloud_service_type.is_primary",
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
]
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"extend_data": {
"label": "Storage"
},
"resource_type": "inventory.CloudService",
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"key": "data.size",
"name": "value",
"operator": "sum"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
],
"filter": [
{
"value": true,
"key": "ref_cloud_service_type.is_major",
"operator": "eq"
},
{
"value": "Storage",
"key": "ref_cloud_service_type.labels",
"operator": "eq"
}
]
}
}
}
]
},
"schedule": {
"hours": [
2
]
},
"tags": {
"a": "b"
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-26T02:08:48.233Z"
}



> **POST** /statistics/v1/schedule/enable
>






    
<br>

### disable

desc: Disables a specific Schedule. If a Schedule is disabled, the query usage will not be scheduled.
request_example: >-
{
"schedule_id": "sch-65bb6b55d162",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"schedule_id": "sch-65bb6b55d162",
"topic": "daily_cloud_service_summary_test",
"state": "DISABLED",
"options": {
"aggregate": [
{
"query": {
"query": {
"filter": [
{
"operator": "eq",
"key": "ref_cloud_service_type.is_primary",
"value": true
},
{
"operator": "eq",
"value": "Server",
"key": "ref_cloud_service_type.labels"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
]
},
"extend_data": {
"label": "Server"
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"query": {
"filter": [
{
"operator": "eq",
"value": true,
"key": "ref_cloud_service_type.is_primary"
},
{
"operator": "eq",
"key": "ref_cloud_service_type.labels",
"value": "Database"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Database"
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Container"
},
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
],
"filter": [
{
"operator": "eq",
"value": true,
"key": "ref_cloud_service_type.is_primary"
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Container"
}
]
}
}
},
{
"concat": {
"extend_data": {
"label": "Networking"
},
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true
},
{
"operator": "eq",
"key": "ref_cloud_service_type.labels",
"value": "Networking"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
]
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Security"
},
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
],
"filter": [
{
"value": true,
"key": "ref_cloud_service_type.is_primary",
"operator": "eq"
},
{
"operator": "eq",
"value": "Security",
"key": "ref_cloud_service_type.labels"
}
]
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Analytics"
},
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
],
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"key": "ref_cloud_service_type.labels",
"value": "Analytics",
"operator": "eq"
}
]
}
}
},
{
"concat": {
"extend_data": {
"label": "All"
},
"query": {
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
],
"filter": [
{
"operator": "eq",
"key": "ref_cloud_service_type.is_primary",
"value": true
}
]
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"query": {
"filter": [
{
"value": true,
"key": "ref_cloud_service_type.is_major",
"operator": "eq"
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Storage"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"key": "data.size",
"operator": "sum",
"name": "value"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Storage"
}
}
}
]
},
"schedule": {
"hours": [
2
]
},
"tags": {
"a": "b"
},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-07-26T02:08:48.233Z"
}



> **POST** /statistics/v1/schedule/disable
>






    
<br>

### delete

desc: Deletes a specific Schedule. You must specify the `schedule_id` of the Schedule to delete.
request_example: >-
{
"schedule_id": "sch-3da9c9ed2ee2",
"domain_id": "domain-58010aa2e451"
}



> **POST** /statistics/v1/schedule/delete
>






    
<br>

### get

desc: Gets a specific Schedule. Prints detailed information about the Schedule, including the schedule interval and `state`.
request_example: >-
{
"schedule_id": "sch-3da9c9ed2ee2",
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"schedule_id": "sch-3da9c9ed2ee2",
"topic": "daily_cloud_service_summary",
"state": "ENABLED",
"options": {
"aggregate": [
{
"query": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Server"
},
"query": {
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"value": "Server",
"key": "ref_cloud_service_type.labels",
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
]
}
}
},
{
"concat": {
"extend_data": {
"label": "Database"
},
"resource_type": "inventory.CloudService",
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
],
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"value": "Database",
"operator": "eq",
"key": "ref_cloud_service_type.labels"
}
]
}
}
},
{
"concat": {
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true
},
{
"operator": "eq",
"key": "ref_cloud_service_type.labels",
"value": "Container"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Container"
}
}
},
{
"concat": {
"extend_data": {
"label": "Networking"
},
"resource_type": "inventory.CloudService",
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
],
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true
},
{
"operator": "eq",
"value": "Networking",
"key": "ref_cloud_service_type.labels"
}
]
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"query": {
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"operator": "eq",
"value": "Security",
"key": "ref_cloud_service_type.labels"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
]
},
"extend_data": {
"label": "Security"
}
}
},
{
"concat": {
"query": {
"filter": [
{
"operator": "eq",
"value": true,
"key": "ref_cloud_service_type.is_primary"
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Analytics"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
]
},
"extend_data": {
"label": "Analytics"
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"extend_data": {
"label": "All"
},
"resource_type": "inventory.CloudService",
"query": {
"filter": [
{
"value": true,
"key": "ref_cloud_service_type.is_primary",
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"fields": [
{
"operator": "count",
"name": "value"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
]
}
}
]
}
}
},
{
"concat": {
"query": {
"filter": [
{
"operator": "eq",
"key": "ref_cloud_service_type.is_major",
"value": true
},
{
"value": "Storage",
"key": "ref_cloud_service_type.labels",
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
],
"fields": [
{
"key": "data.size",
"operator": "sum",
"name": "value"
}
]
}
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Storage"
}
}
}
]
},
"schedule": {
"hours": [
1
]
},
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-13T11:41:35.811Z"
}



> **POST** /statistics/v1/schedule/get
>






    
<br>

### list

desc: Gets a list of all Schedules. You can use a query to get a filtered list of Schedules.
request_example: >-
{
"query": {},
"domain_id": "domain-58010aa2e451"
}
response_example: >-
{
"results": [
{
"schedule_id": "sch-3da9c9ed2ee2",
"topic": "daily_cloud_service_summary",
"state": "ENABLED",
"options": {
"aggregate": [
{
"query": {
"query": {
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
],
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true
},
{
"key": "ref_cloud_service_type.labels",
"value": "Server",
"operator": "eq"
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Server"
}
}
},
{
"concat": {
"query": {
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
],
"filter": [
{
"operator": "eq",
"key": "ref_cloud_service_type.is_primary",
"value": true
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Database"
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Database"
}
}
},
{
"concat": {
"query": {
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
],
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"operator": "eq",
"value": true
},
{
"operator": "eq",
"value": "Container",
"key": "ref_cloud_service_type.labels"
}
]
},
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Container"
}
}
},
{
"concat": {
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Networking"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"key": "project_id",
"name": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
]
},
"extend_data": {
"label": "Networking"
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"extend_data": {
"label": "Security"
},
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_primary",
"value": true,
"operator": "eq"
},
{
"key": "ref_cloud_service_type.labels",
"value": "Security",
"operator": "eq"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
],
"fields": [
{
"operator": "count",
"name": "value"
}
]
}
}
]
},
"resource_type": "inventory.CloudService"
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"query": {
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Analytics"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"name": "cloud_service_type",
"key": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "count"
}
]
}
}
]
},
"extend_data": {
"label": "Analytics"
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"query": {
"aggregate": [
{
"group": {
"fields": [
{
"name": "value",
"operator": "count"
}
],
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"key": "cloud_service_group",
"name": "cloud_service_group"
},
{
"name": "provider",
"key": "provider"
}
]
}
}
],
"filter": [
{
"value": true,
"operator": "eq",
"key": "ref_cloud_service_type.is_primary"
}
]
},
"extend_data": {
"label": "All"
}
}
},
{
"concat": {
"resource_type": "inventory.CloudService",
"extend_data": {
"label": "Storage"
},
"query": {
"filter": [
{
"key": "ref_cloud_service_type.is_major",
"operator": "eq",
"value": true
},
{
"key": "ref_cloud_service_type.labels",
"operator": "eq",
"value": "Storage"
}
],
"aggregate": [
{
"group": {
"keys": [
{
"name": "project_id",
"key": "project_id"
},
{
"key": "cloud_service_type",
"name": "cloud_service_type"
},
{
"name": "cloud_service_group",
"key": "cloud_service_group"
},
{
"key": "provider",
"name": "provider"
}
],
"fields": [
{
"name": "value",
"operator": "sum",
"key": "data.size"
}
]
}
}
]
}
}
}
]
},
"schedule": {
"hours": [
1
]
},
"tags": {},
"domain_id": "domain-58010aa2e451",
"created_at": "2022-06-13T11:41:35.811Z"
}
],
"total_count": 1
}



> **POST** /statistics/v1/schedule/list
>






    
<br>

### stat





> **POST** /statistics/v1/schedule/stat
>






    


<br>
<br>

## Message



### AddScheduleRequest
* **topic** (string)  `Required` 

  *is_required: true*

    
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **schedule** (Scheduled)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetScheduleRequest
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### QueryOption
* **aggregate** (StatAggregate)  `Required` 

  *is_required: true*

    
* **page** (StatPage)  `Required` 

  *is_required: false*

    <br>

### ScheduleInfo
* **schedule_id** (string)  `Required` 

    
* **topic** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **schedule** (Scheduled)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **last_scheduled_at** (string)  `Required` 

    <br>

### ScheduleQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **schedule_id** (string)  `Required` 

  *is_required: false*

    
* **topic** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **resource_type** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ScheduleRequest
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### ScheduleStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

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

### UpdateScheduleRequest
* **schedule_id** (string)  `Required` 

  *is_required: true*

    
* **schedule** (Scheduled)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **storage_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
