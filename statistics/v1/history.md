---
description: A History is a record of data collection based on a Schedule.
---
# History

>  **Package : spaceone.api.statistics.v1**

## History

{% hint style="info" %}
**History Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](history.md#create)|   [CreateHistoryRequest](history.md#createhistoryrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**list**](history.md#list)|   [QueryHistoryRequest](history.md#queryhistoryrequest) |   [HistoryInfo](history.md#historyinfo) |
| [**stat**](history.md#stat)|   [HistoryStatRequest](history.md#historystatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /statistics/v1/history
>


| Type | Message |
| :--- | :--- |
| Request | [CreateHistoryRequest](history.md#createhistoryrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### list
> **GET** /statistics/v1/history
>
> **POST** /statistics/v1/history/query


> Gets a list of all Histories. You can use a query to get a filtered list of Histories.

| Type | Message |
| :--- | :--- |
| Request | [QueryHistoryRequest](history.md#queryhistoryrequest) |
| Response |  [HistoryInfo](history.md#historyinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "topic": "daily_cloud_service_summary",
            "values": {
                "label": "Storage",
                "project_id": "project-f7111a9aa0c6",
                "provider": "azure",
                "value": 32213303296.0,
                "cloud_service_group": "Compute",
                "cloud_service_type": "Disk"
            },
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-07-18T01:01:57.579Z"
        },
        {
            "topic": "daily_cloud_service_summary",
            "values": {
                "cloud_service_type": "Bucket",
                "cloud_service_group": "CloudStorage",
                "label": "Storage",
                "provider": "google_cloud",
                "project_id": "project-4cd006b4993b",
                "value": 401399880.0
            },
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-07-18T01:01:57.579Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /statistics/v1/history/stat
>


| Type | Message |
| :--- | :--- |
| Request | [HistoryStatRequest](history.md#historystatrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateHistoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✔| |
| domain_id |string|✔| |

### HistoryInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of HistoryValueInfo](history.md#historyvalueinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### HistoryStatRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| topic |string|✘| |
| domain_id |string|✔| |

### HistoryValueInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| topic |string | |
| values |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| domain_id |string | |
| created_at |string | |

### QueryHistoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| topic |string|✘| |
| domain_id |string|✔| |
