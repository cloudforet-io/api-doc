---
description:  
---
# History

>  **Package : spaceone.api.statistics.v1**

## History

{% hint style="info" %}
**History Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](history.md#create)|   [CreateHistoryRequest](history.md#createhistoryrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**list**](history.md#list)|   [QueryHistoryRequest](history.md#queryhistoryrequest) |   [HistoryInfo](history.md#historyinfo) |  |
| [**stat**](history.md#stat)|   [HistoryStatRequest](history.md#historystatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](history.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateHistoryRequest](history.md#createhistoryrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](history.md#list) </div> | <div style="width:200px; text-align:center;">    [QueryHistoryRequest](history.md#queryhistoryrequest)  </div> | <div style="width:200px; text-align:center;">   [HistoryInfo](history.md#historyinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](history.md#stat) </div> | <div style="width:200px; text-align:center;">    [HistoryStatRequest](history.md#historystatrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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



| Type | Message |
| :--- | :--- |
| Request | [QueryHistoryRequest](history.md#queryhistoryrequest) |
| Response |  [HistoryInfo](history.md#historyinfo)  |
 
 

 
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
| schedule_id |string|✅| |
| domain_id |string|✅| |

### HistoryInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of HistoryValueInfo](history.md#historyvalueinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### HistoryStatRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| topic |string|❌| |
| domain_id |string|✅| |

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
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| topic |string|❌| |
| domain_id |string|✅| |
