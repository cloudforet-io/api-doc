---
description:  
---
# Server

>  **Package : spaceone.api.inventory.v1**

## Server

{% hint style="info" %}
**Server Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](server.md#create)|   [CreateServerRequest](server.md#createserverrequest) |   [ServerInfo](server.md#serverinfo) |  |
| 2 | [**update**](server.md#update)|   [UpdateServerRequest](server.md#updateserverrequest) |   [ServerInfo](server.md#serverinfo) |  |
| 3 | [**pin_data**](server.md#pin_data)|   [PinServerDataRequest](server.md#pinserverdatarequest) |   [ServerInfo](server.md#serverinfo) |  |
| 4 | [**delete**](server.md#delete)|   [ServerRequest](server.md#serverrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](server.md#get)|   [GetServerRequest](server.md#getserverrequest) |   [ServerInfo](server.md#serverinfo) |  |
| 6 | [**list**](server.md#list)|   [ServerQuery](server.md#serverquery) |   [ServersInfo](server.md#serversinfo) |  |
| 7 | [**stat**](server.md#stat)|   [ServerStatQuery](server.md#serverstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /inventory/v1/servers
>


| Type | Message |
| :--- | :--- |
| Request | [CreateServerRequest](server.md#createserverrequest) |
| Response |  [ServerInfo](server.md#serverinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/server/{server_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateServerRequest](server.md#updateserverrequest) |
| Response |  [ServerInfo](server.md#serverinfo)  |
 
 

 
### pin_data
> **PUT** /inventory/v1/server/{server_id}/pin-data
>


| Type | Message |
| :--- | :--- |
| Request | [PinServerDataRequest](server.md#pinserverdatarequest) |
| Response |  [ServerInfo](server.md#serverinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/server/{server_id}
>


| Type | Message |
| :--- | :--- |
| Request | [ServerRequest](server.md#serverrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/server/{server_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetServerRequest](server.md#getserverrequest) |
| Response |  [ServerInfo](server.md#serverinfo)  |
 
 

 
### list
> **GET** /inventory/v1/servers
>
> **POST** /inventory/v1/servers/search



| Type | Message |
| :--- | :--- |
| Request | [ServerQuery](server.md#serverquery) |
| Response |  [ServersInfo](server.md#serversinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/servers/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ServerStatQuery](server.md#serverstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateServerRequest
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
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>STATE_NONE</li>
          	<li>PENDING</li>
          	<li>INSERVICE</li>
          	<li>MAINTENANCE</li>
          	<li>CLOSED</li>
          	<li>DELETED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">primary_ip_address</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">server_type</td>
      <td style="text-align:left"><ul>
          	<li>SERVER_TYPE_NONE</li>
          	<li>BAREMETAL</li>
          	<li>VM</li>
          	<li>HYPERVISOR</li>
          	<li>UNKNOWN</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">os_type</td>
      <td style="text-align:left"><ul>
          	<li>OS_TYPE_NONE</li>
          	<li>LINUX</li>
          	<li>WINDOWS</li>
        </ul></td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">nics</td>
      <td style="text-align:left"><a href="server.md#servernic">ServerNIC</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">disks</td>
      <td style="text-align:left"><a href="server.md#serverdisk">ServerDisk</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">reference</td>
      <td style="text-align:left"><a href="server.md#serverreference">ServerReference</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">region_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">14</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">15</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### GetServerRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | server_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |string|❌| |

### PinServerDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | server_id |string|✅| |
| 2 | keys |string|✅| |
| 3 | domain_id |string|✅| |

### ServerDisk
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_index |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
| 2 | device |string|❌| |
| 3 | disk_type |string|❌| |
| 4 | size |float|❌| |
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### ServerInfo
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
      <td style="text-align:left">server_id</td>
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
          	<li>STATE_NONE</li>
          	<li>PENDING</li>
          	<li>INSERVICE</li>
          	<li>MAINTENANCE</li>
          	<li>CLOSED</li>
          	<li>DELETED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">primary_ip_address</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">ip_addresses</td>
      <td style="text-align:left"><a href="https://developers.google.com/protocol-buffers/docs/reference/overview">google.protobuf.ListValue</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">server_type</td>
      <td style="text-align:left"><ul>
          	<li>SERVER_TYPE_NONE</li>
          	<li>BAREMETAL</li>
          	<li>VM</li>
          	<li>HYPERVISOR</li>
          	<li>UNKNOWN</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">os_type</td>
      <td style="text-align:left"><ul>
          	<li>OS_TYPE_NONE</li>
          	<li>LINUX</li>
          	<li>WINDOWS</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">nics</td>
      <td style="text-align:left"><a href="server.md#servernic">ServerNIC</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">disks</td>
      <td style="text-align:left"><a href="server.md#serverdisk">ServerDisk</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">reference</td>
      <td style="text-align:left"><a href="server.md#serverreference">ServerReference</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">14</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">15</td>
      <td style="text-align:left">collection_info</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">16</td>
      <td style="text-align:left">region_info</td>
      <td style="text-align:left"><a href="server.md#regioninfo">RegionInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">17</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">18</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">19</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">20</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left">21</td>
      <td style="text-align:left">deleted_at</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a></td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ServerNIC
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | device_index |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✅| |
| 2 | device |string|❌| |
| 3 | nic_type |string|❌| |
| 4 | ip_addresses |string|✅| |
| 5 | cidr |string|❌| |
| 6 | mac_address |string|❌| |
| 7 | public_ip_address |string|❌| |
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |

### ServerQuery
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
      <td style="text-align:left">server_id</td>
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
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">primary_ip_address</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">ip_addresses</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">server_type</td>
      <td style="text-align:left"><ul>
          	<li>SERVER_TYPE_NONE</li>
          	<li>BAREMETAL</li>
          	<li>VM</li>
          	<li>HYPERVISOR</li>
          	<li>UNKNOWN</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">os_type</td>
      <td style="text-align:left"><ul>
          	<li>OS_TYPE_NONE</li>
          	<li>LINUX</li>
          	<li>WINDOWS</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">region_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### ServerReference
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_id |string| |
| 2 | external_link |string| |

### ServerRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | server_id |string|✅| |
| 2 | domain_id |string|✅| |

### ServerStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### ServersInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[ServerInfo](server.md#serverinfo)| |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)| |

### UpdateServerRequest
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
      <td style="text-align:left">server_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left">server unique id</td>
   </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left"><ul>
          	<li>STATE_NONE</li>
          	<li>PENDING</li>
          	<li>INSERVICE</li>
          	<li>MAINTENANCE</li>
          	<li>CLOSED</li>
          	<li>DELETED</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">primary_ip_address</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">server_type</td>
      <td style="text-align:left"><ul>
          	<li>SERVER_TYPE_NONE</li>
          	<li>BAREMETAL</li>
          	<li>VM</li>
          	<li>HYPERVISOR</li>
          	<li>UNKNOWN</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">os_type</td>
      <td style="text-align:left"><ul>
          	<li>OS_TYPE_NONE</li>
          	<li>LINUX</li>
          	<li>WINDOWS</li>
        </ul></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">nics</td>
      <td style="text-align:left"><a href="server.md#servernic">ServerNIC</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">disks</td>
      <td style="text-align:left"><a href="server.md#serverdisk">ServerDisk</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">reference</td>
      <td style="text-align:left"><a href="server.md#serverreference">ServerReference</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">14</td>
      <td style="text-align:left">region_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">15</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">16</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left">✅</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">17</td>
      <td style="text-align:left">release_region</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left">18</td>
      <td style="text-align:left">release_project</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left">❌</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>


