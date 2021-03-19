---
description:  
---
# History

>  **Package : spaceone.api.spot_automation.plugin**

## History

{% hint style="info" %}
**History Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**get**](history.md#get)|   [HistoryRequest](history.md#historyrequest) |   [HistoryInfo](history.md#historyinfo) |  | 
 

 
### get


| Type | Message |
| :--- | :--- |
| Request | [HistoryRequest](history.md#historyrequest) |
| Response |  [HistoryInfo](history.md#historyinfo)  |


## 

## Message

### HistoryInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | history_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### HistoryRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_id |string|✅| |
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
