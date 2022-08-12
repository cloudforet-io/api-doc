---
description: A DataSource is a plugin instance receiving Metric and Log data from cloud services.
---
# Data source

>  **Package : spaceone.api.monitoring.plugin**

## DataSource

{% hint style="info" %}
**DataSource Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](data-source.md#init)|   [InitRequest](data-source.md#initrequest) |   [PluginInfo](data-source.md#plugininfo) |
| [**verify**](data-source.md#verify)|   [PluginVerifyRequest](data-source.md#pluginverifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### init

> Initializes a specific DataSource. During initialization, the DataSource information to be passed to the DataSource user is delivered as `metadata`. DataSource information includes its name and version.

| Type | Message |
| :--- | :--- |
| Request | [InitRequest](data-source.md#initrequest) |
| Response |  [PluginInfo](data-source.md#plugininfo)  |
 
 

 
### verify

> Verifies a specific DataSource. You must specify the parameter `secret_data`, encrypted account data of the DataSource to validate.

| Type | Message |
| :--- | :--- |
| Request | [PluginVerifyRequest](data-source.md#pluginverifyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### InitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### PluginVerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| schema |string|✘| |
