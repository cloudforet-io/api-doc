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
| 1 | [**get_plugin_endpoint**](plugin.md#get_plugin_endpoint)|   [PluginEndpointRequest](plugin.md#pluginendpointrequest) |   [PluginEndpoint](plugin.md#pluginendpoint) | Retrieve plugins end points. |
| 2 | [**notify_failure**](plugin.md#notify_failure)|   [PluginFailureRequest](plugin.md#pluginfailurerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| send a notification if it has failed. | 
 

 
### get_plugin_endpoint
> **POST** /plugin/v1/plugin/{plugin_id}/get-endpoint
>

> Retrieve plugins end points.

| Type | Message |
| :--- | :--- |
| Request | [PluginEndpointRequest](plugin.md#pluginendpointrequest) |
| Response |  [PluginEndpoint](plugin.md#pluginendpoint)  |
 
 

 
### notify_failure
> **PUT** /plugin/v1/plugin/{plugin_id}/notify-failure
>

> send a notification if it has failed.

| Type | Message |
| :--- | :--- |
| Request | [PluginFailureRequest](plugin.md#pluginfailurerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### PluginEndpoint
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | endpoint |string | |
| 2 | access_token |string | |
| 3 | updated_version |string | |

### PluginEndpointRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">labels</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PluginFailureRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | supervisor_id |string|✅| |
| 2 | plugin_id |string|✅| |
| 3 | version |string|✅| |
| 4 | domain_id |string|✅| |
