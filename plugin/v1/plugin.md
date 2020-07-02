---
description: null
---

# Plugin

> **Package : spaceone.api.plugin.v1**

## Plugin

{% hint style="info" %}
**Plugin Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [get\_plugin\_endpoint](plugin.md#get_plugin_endpoint) | [PluginEndpointRequest](plugin.md#pluginendpointrequest) | [PluginEndpoint](plugin.md#pluginendpoint) |  |
| 2 | [notify\_failure](plugin.md#notify_failure) | [PluginFailureRequest](plugin.md#pluginfailurerequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |

### get\_plugin\_endpoint

> **POST** /plugin/v1/plugin/{plugin\_id}/get-endpoint

| Type | Message |
| :--- | :--- |
| Request | [PluginEndpointRequest](plugin.md#pluginendpointrequest) |
| Response | [PluginEndpoint](plugin.md#pluginendpoint) |

### notify\_failure

> **PUT** /plugin/v1/plugin/{plugin\_id}/notify-failure

| Type | Message |
| :--- | :--- |
| Request | [PluginFailureRequest](plugin.md#pluginfailurerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

## Message

### PluginEndpoint

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | endpoint | string |  |  |
| 2 | access\_token | string |  |  |

### PluginEndpointRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin\_id | string | ✅ |  |
| 2 | version | string | ✅ |  |
| 3 | labels | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 4 | domain\_id | string | ✅ |  |

### PluginFailureRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor\_id | string | ✅ |  |
| 2 | plugin\_id | string | ✅ |  |
| 3 | version | string | ✅ |  |
| 4 | domain\_id | string | ✅ |  |

