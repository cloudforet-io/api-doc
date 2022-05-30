---
description:  
---
# Controller

>  **Package : spaceone.api.power_scheduler.plugin**

## Controller

{% hint style="info" %}
**Controller Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**init**](controller.md#init)|   [InitRequest](controller.md#initrequest) |   [PluginInfo](controller.md#plugininfo) |
| [**verify**](controller.md#verify)|   [VerifyRequest](controller.md#verifyrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**start**](controller.md#start)|   [StartRequest](controller.md#startrequest) |   [UpdateInfo](controller.md#updateinfo) |
| [**stop**](controller.md#stop)|   [StopRequest](controller.md#stoprequest) |   [UpdateInfo](controller.md#updateinfo) |
| [**reboot**](controller.md#reboot)|   [RebootRequest](controller.md#rebootrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)| 
 

 
### init


| Type | Message |
| :--- | :--- |
| Request | [InitRequest](controller.md#initrequest) |
| Response |  [PluginInfo](controller.md#plugininfo)  |
 
 

 
### verify


| Type | Message |
| :--- | :--- |
| Request | [VerifyRequest](controller.md#verifyrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### start


| Type | Message |
| :--- | :--- |
| Request | [StartRequest](controller.md#startrequest) |
| Response |  [UpdateInfo](controller.md#updateinfo)  |
 
 

 
### stop


| Type | Message |
| :--- | :--- |
| Request | [StopRequest](controller.md#stoprequest) |
| Response |  [UpdateInfo](controller.md#updateinfo)  |
 
 

 
### reboot


| Type | Message |
| :--- | :--- |
| Request | [RebootRequest](controller.md#rebootrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |


## 

## Message

### InitRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### PluginInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### RebootRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| resource_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |

### Resource
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| resource_type |string | |

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
      <td style="text-align:left; width:100px;">resource</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ResourcesParams
| Field | Type |  Description |
| :--- | :--- | :--- |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| resources |[list of Resource](controller.md#resource) | |

### StartRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| resource_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |

### StopRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| resource_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| schema |string|❌| |

### UpdateInfo
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| action |string|✅| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |

### VerifyRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
