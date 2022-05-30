---
description:  
---
# History

>  **Package : spaceone.api.spot_automation.plugin**

## History

{% hint style="info" %}
**History Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**get**](history.md#get)|   [HistoryRequest](history.md#historyrequest) |   [HistoryInfo](history.md#historyinfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**get**](history.md#get) </div> | <div style="width:200px; text-align:center;">    [HistoryRequest](history.md#historyrequest)  </div> | <div style="width:200px; text-align:center;">   [HistoryInfo](history.md#historyinfo)  </div> | <div style="width:400px;">  </div> | 
 

 
### get


| Type | Message |
| :--- | :--- |
| Request | [HistoryRequest](history.md#historyrequest) |
| Response |  [HistoryInfo](history.md#historyinfo)  |


## 

## Message

### HistoryInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| history_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### HistoryRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_id |string|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
