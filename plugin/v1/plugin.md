---
description: A Plugin is a resource managing endpoints of the plugin instances deployed. If there is a plugin instance that does not work properly, the Plugin requests the Supervisor to redeploy the instance.
---
# Plugin

>  **Package : spaceone.api.plugin.v1**

## Plugin

{% hint style="info" %}
**Plugin Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**get_plugin_endpoint**](plugin.md#get_plugin_endpoint)|   [PluginEndpointRequest](plugin.md#pluginendpointrequest) |   [PluginEndpoint](plugin.md#pluginendpoint) |
| [**notify_failure**](plugin.md#notify_failure)|   [PluginFailureRequest](plugin.md#pluginfailurerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### get_plugin_endpoint
> **POST** /plugin/v1/plugin/get-plugin-endpoint
>

> Gets the `endpoint` of a specific plugin instance. A Plugin returns only a single `endpoint` by determining `labels` and `priority`. If the requested plugin instance is already deployed, the `endpoint` is returned. If not, the `endpoint` is returned after deploying the plugin instance.

| Type | Message |
| :--- | :--- |
| Request | [PluginEndpointRequest](plugin.md#pluginendpointrequest) |
| Response |  [PluginEndpoint](plugin.md#pluginendpoint)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "plugin_id": "plugin-aws-sns-mon-webhook",
    "version": "1.2.2"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "endpoint": "grpc://endpoint-url:50051"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### notify_failure
> **POST** /plugin/v1/plugin/notify-failure
>


| Type | Message |
| :--- | :--- |
| Request | [PluginFailureRequest](plugin.md#pluginfailurerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### PluginEndpoint
| Field | Type |  Description |
| :--- | :--- | :--- |
| endpoint |string | |
| access_token |string | |
| updated_version |string | |

### PluginEndpointRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PluginFailureRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✔| |
| plugin_id |string|✔| |
| version |string|✔| |
| domain_id |string|✔| |
