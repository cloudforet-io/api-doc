---
description:  
---
# Protocol

>  **Package : spaceone.api.notification.v1**

## Protocol

{% hint style="info" %}
**Protocol Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](protocol.md#create)|   [CreateProtocolRequest](protocol.md#createprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |  |
| 2 | [**update**](protocol.md#update)|   [UpdateProtocolRequest](protocol.md#updateprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |  |
| 3 | [**update_plugin**](protocol.md#update_plugin)|   [UpdateProtocolPluginRequest](protocol.md#updateprotocolpluginrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |  |
| 4 | [**enable**](protocol.md#enable)|   [ProtocolRequest](protocol.md#protocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |  |
| 5 | [**disable**](protocol.md#disable)|   [ProtocolRequest](protocol.md#protocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |  |
| 6 | [**delete**](protocol.md#delete)|   [ProtocolRequest](protocol.md#protocolrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 7 | [**get**](protocol.md#get)|   [GetProtocolRequest](protocol.md#getprotocolrequest) |   [ProtocolInfo](protocol.md#protocolinfo) |  |
| 8 | [**list**](protocol.md#list)|   [ProtocolQuery](protocol.md#protocolquery) |   [ProtocolsInfo](protocol.md#protocolsinfo) |  |
| 9 | [**stat**](protocol.md#stat)|   [ProtocolStatQuery](protocol.md#protocolstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /notification/v1/protocols
>


| Type | Message |
| :--- | :--- |
| Request | [CreateProtocolRequest](protocol.md#createprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### update
> **PUT** /notification/v1/protocol/{protocol_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProtocolRequest](protocol.md#updateprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### update_plugin
> **PUT** /notification/v1/protocol/{protocol_id}/plugin
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateProtocolPluginRequest](protocol.md#updateprotocolpluginrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### enable
> **PUT** /notification/v1/protocol/{protocol_id}/enable
>


| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### disable
> **PUT** /notification/v1/protocol/{protocol_id}/disable
>


| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### delete
> **DELETE** /notification/v1/protocol/{protocol_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ProtocolRequest](protocol.md#protocolrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /notification/v1/protocol/{protocol_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetProtocolRequest](protocol.md#getprotocolrequest) |
| Response |  [ProtocolInfo](protocol.md#protocolinfo)  |
 
 

 
### list
> **GET** /notification/v1/protocols
>
> **POST** /notification/v1/protocols/search



| Type | Message |
| :--- | :--- |
| Request | [ProtocolQuery](protocol.md#protocolquery) |
| Response |  [ProtocolsInfo](protocol.md#protocolsinfo)  |
 
 

 
### stat
> **POST** /notification/v1/protocols/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ProtocolStatQuery](protocol.md#protocolstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateProtocolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string|✅| |
| 2 | plugin_info |[PluginRequest](protocol.md#pluginrequest)|✅| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | project_id |string|✅| |
| 5 | domain_id |string|✅| |

### GetProtocolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | protocol_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### PluginInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | |
| 2 | version |string | |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | secret_id |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |

### PluginRequest
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | |
| 2 | version |string | |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 4 | secret_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 5 | schema |string | |

### ProtocolInfo
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
      <td style="text-align:left">protocol_id</td>
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
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">protocol_type</td>
      <td style="text-align:left"><ul>
          	<li>PROTOCOL_TYPE_NONE</li>
          	<li>INTERNAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left"><a href="protocol.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ProtocolQuery
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
      <td style="text-align:left">protocol_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">protocol_type</td>
      <td style="text-align:left"><ul>
          	<li>PROTOCOL_TYPE_NONE</li>
          	<li>INTERNAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### ProtocolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | protocol_id |string|✅| |
| 2 | domain_id |string|✅| |

### ProtocolStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### ProtocolsInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of ProtocolInfo](protocol.md#protocolinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateProtocolPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | protocol_id |string|✅| |
| 2 | version |string|❌| |
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |

### UpdateProtocolRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | protocol_id |string|✅| |
| 2 | name |string|❌| |
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | domain_id |string|✅| |
