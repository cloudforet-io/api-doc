---
description:  
---
# History

>  **Package : spaceone.api.spot_automation.v1**

## History

{% hint style="info" %}
**History Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**list**](history.md#list)|   [QueryHistoryRequest](history.md#queryhistoryrequest) |   [HistoryInfo](history.md#historyinfo) |
| [**stat**](history.md#stat)|   [HistoryStatRequest](history.md#historystatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### list
> **GET** /spot-automation/v1/history
>
> **POST** /spot-automation/v1/history/search



| Type | Message |
| :--- | :--- |
| Request | [QueryHistoryRequest](history.md#queryhistoryrequest) |
| Response |  [HistoryInfo](history.md#historyinfo)  |
 
 

 
### stat
> **POST** /spot-automation/v1/history/stat
>


| Type | Message |
| :--- | :--- |
| Request | [HistoryStatRequest](history.md#historystatrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### HistoryInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of HistoryValueInfo](history.md#historyvalueinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### HistoryStatRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### HistoryValueInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| history_id |string | |
| spot_group_id |string | |
| ondemand_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| spot_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| project_id |string | |
| domain_id |string | |
| history_at |string | |
| created_at |string | |

### QueryHistoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| spot_group_id |string|✘| |
| domain_id |string|✔| |
