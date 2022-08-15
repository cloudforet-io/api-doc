---
description: A Collector is a plugin collecting data of external infrastructure resources.
---
# Collector

>  **Package : spaceone.api.inventory.plugin**

## Collector

{% hint style="info" %}
**Collector Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](collector.md#init)|   [InitRequest](collector.md#initrequest) |   [PluginInfo](collector.md#plugininfo) |
| [**verify**](collector.md#verify)|   [VerifyRequest](collector.md#verifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**collect**](collector.md#collect)|   [CollectRequest](collector.md#collectrequest) | **`stream`**   [ResourceInfo](collector.md#resourceinfo) | 
 

 
### init

> Initializes a specific Collector. During initialization, the Collector information to be passed to the Collector user is delivered as `metadata`. Collector information includes its name and version.

| Type | Message |
| :--- | :--- |
| Request | [InitRequest](collector.md#initrequest) |
| Response |  [PluginInfo](collector.md#plugininfo)  |
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

> Verifies a specific Collector. You must specify the parameter `secret_data`, encrypted account data of the Collector to validate.

| Type | Message |
| :--- | :--- |
| Request | [VerifyRequest](collector.md#verifyrequest) |
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
 
 

 
### collect

> Collects data of external infrastructure resources by a specific Collector.

| Type | Message |
| :--- | :--- |
| Request | [CollectRequest](collector.md#collectrequest) |
| Response |  [ResourceInfo](collector.md#resourceinfo)  |
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

### CollectRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| filter |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |

### CollectorVerifyInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### InitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### ResourceInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>CREATED</li>
          	<li>PENDING</li>
          	<li>INPROGRESS</li>
          	<li>SUCCESS</li>
          	<li>FAILURE</li>
          	<li>TIMEOUT</li>
          	<li>IDLE</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">message</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">match_rules</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">resource</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### VerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
