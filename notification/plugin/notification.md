---
description:  
---
# Notification

>  **Package : spaceone.api.notification.plugin**

## Notification

{% hint style="info" %}
**Notification Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**dispatch**](notification.md#dispatch)|   [PluginDispatchRequest](notification.md#plugindispatchrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### dispatch

> A method to propagate the Notification to external systems.

| Type | Message |
| :--- | :--- |
| Request | [PluginDispatchRequest](notification.md#plugindispatchrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### PluginDispatchRequest
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
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Option value required for notification delivery.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">message</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Message containing notification information</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">notification_type</td>
      <td style="text-align:left"><ul>
          	<li>NOTIFICATION_TYPE_NONE</li>
          	<li>INFO</li>
          	<li>ERROR</li>
          	<li>SUCCESS</li>
          	<li>WARNING</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">The type of Notification</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Secret value required for notification delivery.The secret data usually includes the credential information required for the plugin to access the external system.</td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">channel_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left">Channel data required for notification delivery.</td>
   </tr>
  </tbody>
</table>


