---
description:  
---
# Supervisor

>  **Package : spaceone.api.plugin.v1**

## Supervisor

{% hint style="info" %}
**Supervisor Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**publish**](supervisor.md#publish)|   [PublishSupervisorRequest](supervisor.md#publishsupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| 2 | [**register**](supervisor.md#register)|   [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| 3 | [**update**](supervisor.md#update)|   [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| 4 | [**deregister**](supervisor.md#deregister)|   [SupervisorRequest](supervisor.md#supervisorrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**enable**](supervisor.md#enable)|   [SupervisorRequest](supervisor.md#supervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| 6 | [**disable**](supervisor.md#disable)|   [SupervisorRequest](supervisor.md#supervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| 7 | [**recover_plugin**](supervisor.md#recover_plugin)|   [RecoverPluginRequest](supervisor.md#recoverpluginrequest) |   [PluginInfo](supervisor.md#plugininfo) |  |
| 8 | [**get**](supervisor.md#get)|   [GetSupervisorRequest](supervisor.md#getsupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |  |
| 9 | [**list**](supervisor.md#list)|   [SupervisorQuery](supervisor.md#supervisorquery) |   [SupervisorsInfo](supervisor.md#supervisorsinfo) |  |
| 10 | [**stat**](supervisor.md#stat)|   [SupervisorStatQuery](supervisor.md#supervisorstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 11 | [**list_plugins**](supervisor.md#list_plugins)|   [PluginQuery](supervisor.md#pluginquery) |   [PluginsInfo](supervisor.md#pluginsinfo) |  | 
 

 
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
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |string|❌| |

### PluginInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
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
      <td style="text-align:left">4</td>
      <td style="text-align:left">endpoint</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">supervisor_name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">managed</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">endpoints</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PluginQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">hostname</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PROVISIONING</li>
          	<li>ACTIVE</li>
          	<li>RE_PROVISIONING</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">endpoint</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### PluginsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[PluginInfo](supervisor.md#plugininfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |

### PublishSupervisorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | hostname |string|✅| |
| 3 | secret_key |string|❌| |
| 4 | plugin_info |[PluginInfo](supervisor.md#plugininfo)|❌| |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | is_public |bool|❌| |
| 7 | domain_id |string|✅| |

### RecoverPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string|✅| |
| 2 | plugin_id |string|✅| |
| 3 | version |string|✅| |
| 4 | domain_id |string|✅| |

### RegisterSupervisorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string|✅| |
| 2 | name |string|❌| |
| 3 | is_public |bool|❌| |
| 4 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|❌| |
| 5 | labels |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | domain_id |string|✅| |

### SupervisorInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">hostname</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
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
      <td style="text-align:left">5</td>
      <td style="text-align:left">is_public</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">labels</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### SupervisorQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | supervisor_id |string|❌| |
| 3 | name |string|❌| |
| 4 | is_public |bool|❌| |
| 5 | domain_id |string|✅| |

### SupervisorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string|✅| |
| 2 | domain_id |string|✅| |

### SupervisorStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### SupervisorsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[SupervisorInfo](supervisor.md#supervisorinfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |
