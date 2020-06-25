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
| 1 | [verify](Data-source.md#verify)| [PluginVerifyRequest](Data-source.md#pluginverifyrequest)| [PluginVerifyResponse](Data-source.md#pluginverifyresponse) |  |

### verify



| Type | Message |
| :--- | :--- |
| Request | [PluginVerifyRequest](Data-source.md#pluginverifyrequest) |
| Response |  [PluginVerifyResponse](Data-source.md#pluginverifyresponse)  |





## Message

### PluginVerifyInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||

### PluginVerifyRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |required|
| 2 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |required|

### PluginVerifyResponse
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_type |string | |required|
| 2 | actions |[spaceone.api.core.v1.PluginAction](../../core/v1/Plugin.md##pluginaction) | |optional|
| 3 | result |[PluginVerifyInfo](Data-source.md#pluginverifyinfo) | |required|
