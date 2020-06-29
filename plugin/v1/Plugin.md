---
description:  
---
# Plugin

>  **Package : spaceone.api.plugin.v1**

## Plugin

{% hint style="info" %}
**Plugin Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [get_plugin_endpoint](Plugin.md#get_plugin_endpoint)| [PluginEndpointRequest](Plugin.md#pluginendpointrequest) | [PluginEndpoint](Plugin.md#pluginendpoint) |  |
| 2 | [notify_failure](Plugin.md#notify_failure)| [PluginFailureRequest](Plugin.md#pluginfailurerequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |

### get_plugin_endpoint
> **POST** /plugin/v1/plugin/{plugin_id}/get-endpoint
>



| Type | Message |
| :--- | :--- |
| Request | [PluginEndpointRequest](Plugin.md#pluginendpointrequest) |
| Response |  [PluginEndpoint](Plugin.md#pluginendpoint)  |



### notify_failure
> **PUT** /plugin/v1/plugin/{plugin_id}/notify-failure
>



| Type | Message |
| :--- | :--- |
| Request | [PluginFailureRequest](Plugin.md#pluginfailurerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |





## Message

### PluginEndpoint
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | endpoint |string | ||
| 2 | access_token |string | ||

### PluginEndpointRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin_id |string |✅ ||
| 2 | version |string |✅ ||
| 3 | labels |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||

### PluginFailureRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string |✅ ||
| 2 | plugin_id |string |✅ ||
| 3 | version |string |✅ ||
| 4 | domain_id |string |✅ ||
