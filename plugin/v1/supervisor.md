---
description:  
---
# Supervisor

>  **Package : spaceone.api.plugin.v1**

## Supervisor

{% hint style="info" %}
**Supervisor Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**publish**](supervisor.md#publish)|   [PublishSupervisorRequest](supervisor.md#publishsupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| [**register**](supervisor.md#register)|   [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| [**update**](supervisor.md#update)|   [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| [**deregister**](supervisor.md#deregister)|   [SupervisorRequest](supervisor.md#supervisorrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**enable**](supervisor.md#enable)|   [SupervisorRequest](supervisor.md#supervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| [**disable**](supervisor.md#disable)|   [SupervisorRequest](supervisor.md#supervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| [**recover_plugin**](supervisor.md#recover_plugin)|   [RecoverPluginRequest](supervisor.md#recoverpluginrequest) |   [PluginInfo](supervisor.md#plugininfo) |  |
| [**get**](supervisor.md#get)|   [GetSupervisorRequest](supervisor.md#getsupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| [**list**](supervisor.md#list)|   [SupervisorQuery](supervisor.md#supervisorquery) |   [SupervisorsInfo](supervisor.md#supervisorsinfo) |  |
| [**stat**](supervisor.md#stat)|   [SupervisorStatQuery](supervisor.md#supervisorstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| [**list_plugins**](supervisor.md#list_plugins)|   [PluginQuery](supervisor.md#pluginquery) |   [PluginsInfo](supervisor.md#pluginsinfo) |  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**publish**](supervisor.md#publish) </div> | <div style="width:200px; text-align:center;">    [PublishSupervisorRequest](supervisor.md#publishsupervisorrequest)  </div> | <div style="width:200px; text-align:center;">   [SupervisorInfo](supervisor.md#supervisorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**register**](supervisor.md#register) </div> | <div style="width:200px; text-align:center;">    [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest)  </div> | <div style="width:200px; text-align:center;">   [SupervisorInfo](supervisor.md#supervisorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](supervisor.md#update) </div> | <div style="width:200px; text-align:center;">    [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest)  </div> | <div style="width:200px; text-align:center;">   [SupervisorInfo](supervisor.md#supervisorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**deregister**](supervisor.md#deregister) </div> | <div style="width:200px; text-align:center;">    [SupervisorRequest](supervisor.md#supervisorrequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**enable**](supervisor.md#enable) </div> | <div style="width:200px; text-align:center;">    [SupervisorRequest](supervisor.md#supervisorrequest)  </div> | <div style="width:200px; text-align:center;">   [SupervisorInfo](supervisor.md#supervisorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**disable**](supervisor.md#disable) </div> | <div style="width:200px; text-align:center;">    [SupervisorRequest](supervisor.md#supervisorrequest)  </div> | <div style="width:200px; text-align:center;">   [SupervisorInfo](supervisor.md#supervisorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**recover_plugin**](supervisor.md#recover_plugin) </div> | <div style="width:200px; text-align:center;">    [RecoverPluginRequest](supervisor.md#recoverpluginrequest)  </div> | <div style="width:200px; text-align:center;">   [PluginInfo](supervisor.md#plugininfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](supervisor.md#get) </div> | <div style="width:200px; text-align:center;">    [GetSupervisorRequest](supervisor.md#getsupervisorrequest)  </div> | <div style="width:200px; text-align:center;">   [SupervisorInfo](supervisor.md#supervisorinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](supervisor.md#list) </div> | <div style="width:200px; text-align:center;">    [SupervisorQuery](supervisor.md#supervisorquery)  </div> | <div style="width:200px; text-align:center;">   [SupervisorsInfo](supervisor.md#supervisorsinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](supervisor.md#stat) </div> | <div style="width:200px; text-align:center;">    [SupervisorStatQuery](supervisor.md#supervisorstatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list_plugins**](supervisor.md#list_plugins) </div> | <div style="width:200px; text-align:center;">    [PluginQuery](supervisor.md#pluginquery)  </div> | <div style="width:200px; text-align:center;">   [PluginsInfo](supervisor.md#pluginsinfo)  </div> | <div style="width:400px;">  </div> | 
 

 
### publish
> **POST** /plugin/v1/supervisors
>


| Type | Message |
| :--- | :--- |
| Request | [PublishSupervisorRequest](supervisor.md#publishsupervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
 
 

 
### register
> **POST** /plugin/v1/supervisor/{supervisor_id}/register
>


| Type | Message |
| :--- | :--- |
| Request | [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
 
 

 
### update
> **PUT** /plugin/v1/supervisor/{supervisor_id}
>


| Type | Message |
| :--- | :--- |
| Request | [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
 
 

 
### deregister
> **DELETE** /plugin/v1/supervisor/{supervisor_id}/register
>


| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](supervisor.md#supervisorrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### enable
> **PUT** /plugin/v1/supervisor/{supervisor_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](supervisor.md#supervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
 
 

 
### disable
> **PUT** /plugin/v1/supervisor/{supervisor_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](supervisor.md#supervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
 
 

 
### recover_plugin
> **POST** /plugin/v1/supervisor/{supervisor_id}/plugin/{plugin_id}/recover
>


| Type | Message |
| :--- | :--- |
| Request | [RecoverPluginRequest](supervisor.md#recoverpluginrequest) |
| Response |  [PluginInfo](supervisor.md#plugininfo)  |
 
 

 
### get
> **GET** /plugin/v1/supervisor/{supervisor_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetSupervisorRequest](supervisor.md#getsupervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
 
 

 
### list
> **GET** /plugin/v1/supervisors
>
> **POST** /plugin/v1/supervisors/search



| Type | Message |
| :--- | :--- |
| Request | [SupervisorQuery](supervisor.md#supervisorquery) |
| Response |  [SupervisorsInfo](supervisor.md#supervisorsinfo)  |
 
 

 
### stat
> **POST** /plugin/v1/supervisors/stat
>


| Type | Message |
| :--- | :--- |
| Request | [SupervisorStatQuery](supervisor.md#supervisorstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### list_plugins
> **GET** /plugin/v1/supervisor/{supervisor_id}/plugins
>
> **POST** /plugin/v1/supervisor/{supervisor_id}/plugins/search



| Type | Message |
| :--- | :--- |
| Request | [PluginQuery](supervisor.md#pluginquery) |
| Response |  [PluginsInfo](supervisor.md#pluginsinfo)  |


## 

## Message

### GetSupervisorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### PluginInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PROVISIONING</li>
          	<li>ACTIVE</li>
          	<li>RE_PROVISIONING</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">endpoint</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">supervisor_name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">managed</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">endpoints</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PluginQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">hostname</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PROVISIONING</li>
          	<li>ACTIVE</li>
          	<li>RE_PROVISIONING</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">endpoint</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PluginsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PluginInfo](supervisor.md#plugininfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### PublishSupervisorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| hostname |string|✅| |
| secret_key |string|❌| |
| plugin_info |[list of PluginInfo](supervisor.md#plugininfo)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| is_public |bool|❌| |
| domain_id |string|✅| |
| labels |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### RecoverPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✅| |
| plugin_id |string|✅| |
| version |string|✅| |
| domain_id |string|✅| |

### RegisterSupervisorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✅| |
| name |string|❌| |
| is_public |bool|❌| |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| labels |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### SupervisorInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">hostname</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
          	<li>PENDING</li>
          	<li>DISCONNECTED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">is_public</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">labels</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### SupervisorQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| supervisor_id |string|❌| |
| name |string|❌| |
| is_public |bool|❌| |
| domain_id |string|✅| |

### SupervisorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✅| |
| domain_id |string|✅| |

### SupervisorStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### SupervisorsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SupervisorInfo](supervisor.md#supervisorinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
