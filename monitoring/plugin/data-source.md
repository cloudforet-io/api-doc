---
description:  
---
# Data source

>  **Package : spaceone.api.monitoring.plugin**

## DataSource

{% hint style="info" %}
**DataSource Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**verify**](data-source.md#verify)|   [PluginVerifyRequest](data-source.md#pluginverifyrequest) | **`stream`**   [PluginVerifyResponse](data-source.md#pluginverifyresponse) |  | 
 

 
### verify


| Type | Message |
| :--- | :--- |
| Request | [PluginVerifyRequest](data-source.md#pluginverifyrequest) |
| Response |  [PluginVerifyResponse](data-source.md#pluginverifyresponse)  |


## 

## Message

### PluginVerifyInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| |

### PluginVerifyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### PluginVerifyResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_type |string|✅| |
| 2 | actions |[spaceone.api.core.v1.PluginAction](../../core/v1/plugin.md##pluginaction)|❌| |
| 3 | result |[PluginVerifyInfo](data-source.md#pluginverifyinfo)|✅| |
