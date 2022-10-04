---
description:  
---
# Data source

>  **Package : spaceone.api.cost_analysis.plugin**

## DataSource

{% hint style="info" %}
**DataSource Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](data-source.md#init)|   [InitRequest](data-source.md#initrequest) |   [PluginInfo](data-source.md#plugininfo) |
| [**verify**](data-source.md#verify)|   [PluginVerifyRequest](data-source.md#pluginverifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### init

> ''

| Type | Message |
| :--- | :--- |
| Request | [InitRequest](data-source.md#initrequest) |
| Response |  [PluginInfo](data-source.md#plugininfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### verify

> ''

| Type | Message |
| :--- | :--- |
| Request | [PluginVerifyRequest](data-source.md#pluginverifyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}


## 

## Message

### InitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| domain_id |string|✔| |

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
| domain_id |string|✔| |
