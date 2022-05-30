---
description:  
---
# Protocol

>  **Package : spaceone.api.notification.plugin**

## Protocol

{% hint style="info" %}
**Protocol Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](protocol.md#init)|   [InitRequest](protocol.md#initrequest) |   [PluginInfo](protocol.md#plugininfo) |
| [**verify**](protocol.md#verify)|   [PluginVerifyRequest](protocol.md#pluginverifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### init

> Initialized when protocol plugin is created first.When this method is executed, plugin return the metadata required when the plug-in is executed.

| Type | Message |
| :--- | :--- |
| Request | [InitRequest](protocol.md#initrequest) |
| Response |  [PluginInfo](protocol.md#plugininfo)  |
 
 

 
### verify

> A method that proves whether the plugin can be running.If there is no return value, it means that normal execution is possible.

| Type | Message |
| :--- | :--- |
| Request | [PluginVerifyRequest](protocol.md#pluginverifyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### InitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| Option value used when initializing the plugin.|

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | Metadata value required to input various values required for plugin to work.Metadata value required to input various values required for plugin to work.In the case of protocol plugins, when creating a channel, the plugin contains the definition of additional data (channel data) required for channel transmission.|

### PluginVerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| Option values required for the plugin to work.|
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| The secret value required for the plugin to work.The secret data usually includes the credential information required for the plugin to access the external system.|
