---
description:  
---
# History

>  **Package : spaceone.api.statistics.v1**

## History

{% hint style="info" %}
**History Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](History.md#create)| [CreateHistoryRequest](History.md#createhistoryrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 2 | [list](History.md#list)| [QueryHistoryRequest](History.md#queryhistoryrequest) | [HistoryInfo](History.md#historyinfo) |  |
| 3 | [stat](History.md#stat)| [HistoryStatRequest](History.md#historystatrequest) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 4 | [diff](History.md#diff)| [DiffHistoryRequest](History.md#diffhistoryrequest) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /statistics/v1/history
>



| Type | Message |
| :--- | :--- |
| Request | [CreateHistoryRequest](History.md#createhistoryrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### list
> **GET** /statistics/v1/history
>
> **POST** /statistics/v1/history/query




| Type | Message |
| :--- | :--- |
| Request | [QueryHistoryRequest](History.md#queryhistoryrequest) |
| Response |  [HistoryInfo](History.md#historyinfo)  |



### stat
> **POST** /statistics/v1/history/stat
>



| Type | Message |
| :--- | :--- |
| Request | [HistoryStatRequest](History.md#historystatrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |



### diff
> **POST** /statistics/v1/history/diff
>



| Type | Message |
| :--- | :--- |
| Request | [DiffHistoryRequest](History.md#diffhistoryrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateHistoryRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | schedule_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### DiffHistoryRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | topic |string |✅ ||
| 2 | filter |spaceone.api.core.v1.Filter |❌ ||
| 3 | filter_or |spaceone.api.core.v1.Filter |❌ ||
| 4 | from |string |✅ ||
| 5 | to |string |❌ ||
| 6 | default_fields |string |✅ ||
| 7 | diff_fields |string |✅ ||
| 8 | domain_id |string |✅ ||

### HistoryInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[HistoryValueInfo](History.md#historyvalueinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### HistoryStatRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | topic |string |✅ ||
| 3 | domain_id |string |✅ ||

### HistoryValueInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | topic |string | ||
| 2 | values |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 3 | domain_id |string | ||
| 4 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### QueryHistoryRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | topic |string |✅ ||
| 3 | domain_id |string |✅ ||
