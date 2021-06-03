---
description:  
---
# Event

>  **Package : spaceone.api.monitoring.plugin**

## Event

{% hint style="info" %}
**Event Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**parse**](event.md#parse)|   [ParseRequest](event.md#parserequest) |   [EventInfo](event.md#eventinfo) |  | 
 

 
### parse


| Type | Message |
| :--- | :--- |
| Request | [ParseRequest](event.md#parserequest) |
| Response |  [EventInfo](event.md#eventinfo)  |


## 

## Message

### AffectedResource
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_id |string | |
| 2 | name |string | |
| 3 | ip_address |string | |

### EventInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | title |string | |
| 2 | description |string | |
| 3 | affected_resource |[AffectedResource](event.md#affectedresource) | |
| 4 | rule |string | |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### ParseRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | raw_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
