---
description:  
---
# Ip address

>  **Package : spaceone.api.inventory.v1**

## IPAddress

{% hint style="info" %}
**IPAddress Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [allocate](Ip-address.md#allocate)| [AllocateIPRequest](Ip-address.md#allocateiprequest) | [IPInfo](Ip-address.md#ipinfo) |  |
| 2 | [reserve](Ip-address.md#reserve)| [ReserveIPRequest](Ip-address.md#reserveiprequest) | [IPInfo](Ip-address.md#ipinfo) |  |
| 3 | [release](Ip-address.md#release)| [IPRequest](Ip-address.md#iprequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [update](Ip-address.md#update)| [UpdateIPRequest](Ip-address.md#updateiprequest) | [IPInfo](Ip-address.md#ipinfo) |  |
| 5 | [pin_data](Ip-address.md#pin_data)| [PinIPDataRequest](Ip-address.md#pinipdatarequest) | [IPInfo](Ip-address.md#ipinfo) |  |
| 6 | [get](Ip-address.md#get)| [GetIPRequest](Ip-address.md#getiprequest) | [IPInfo](Ip-address.md#ipinfo) |  |
| 7 | [list](Ip-address.md#list)| [IPQuery](Ip-address.md#ipquery) | [IPsInfo](Ip-address.md#ipsinfo) |  |
| 8 | [stat](Ip-address.md#stat)| [IPStatQuery](Ip-address.md#ipstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### allocate
> **POST** /inventory/v1/ip-addresses/allocate
>
> **POST** /inventory/v1/ip-address/{ip_address}/allocate




| Type | Message |
| :--- | :--- |
| Request | [AllocateIPRequest](Ip-address.md#allocateiprequest) |
| Response |  [IPInfo](Ip-address.md#ipinfo)  |



### reserve
> **PUT** /inventory/v1/ip-address/{ip_address}/reserve
>



| Type | Message |
| :--- | :--- |
| Request | [ReserveIPRequest](Ip-address.md#reserveiprequest) |
| Response |  [IPInfo](Ip-address.md#ipinfo)  |



### release
> **DELETE** /inventory/v1/ip-address/{ip_address}/release
>



| Type | Message |
| :--- | :--- |
| Request | [IPRequest](Ip-address.md#iprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### update
> **PUT** /inventory/v1/ip-address/{ip_address}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateIPRequest](Ip-address.md#updateiprequest) |
| Response |  [IPInfo](Ip-address.md#ipinfo)  |



### pin_data
> **PUT** /inventory/v1/ip-address/{ip_address}/pin-data
>



| Type | Message |
| :--- | :--- |
| Request | [PinIPDataRequest](Ip-address.md#pinipdatarequest) |
| Response |  [IPInfo](Ip-address.md#ipinfo)  |



### get
> **GET** /inventory/v1/ip-address/{ip_address}
>



| Type | Message |
| :--- | :--- |
| Request | [GetIPRequest](Ip-address.md#getiprequest) |
| Response |  [IPInfo](Ip-address.md#ipinfo)  |



### list
> **GET** /inventory/v1/ip-addresses
>
> **POST** /inventory/v1/ip-addresses/search




| Type | Message |
| :--- | :--- |
| Request | [IPQuery](Ip-address.md#ipquery) |
| Response |  [IPsInfo](Ip-address.md#ipsinfo)  |



### stat
> **POST** /inventory/v1/ip-addresses/stat
>



| Type | Message |
| :--- | :--- |
| Request | [IPStatQuery](Ip-address.md#ipstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### AllocateIPRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip_address |string |❌ ||
| 2 | resource |[Resource](Ip-address.md#resource) |❌ ||
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | reference |[IPReference](Ip-address.md#ipreference) |❌ ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | subnet_id |string |✅ ||
| 8 | domain_id |string |✅ ||

### GetIPRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip_address |string |✅ ||
| 2 | subnet_id |string |✅ ||
| 3 | domain_id |string |✅ ||
| 4 | only |string |❌ ||

### IPInfo
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
      <td style="text-align:left">ip_address</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>IPInfo.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ALLOCATED</li>
          	<li>RESERVED</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">resource</td>
      <td style="text-align:left">
<a href="Ip-address.md#resource">Resource</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">data</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">metadata</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">reference</td>
      <td style="text-align:left">
<a href="Ip-address.md#ipreference">IPReference</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">collection_info</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">network_info</td>
      <td style="text-align:left">
<a href="Ip-address.md#networkinfo">NetworkInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">subnet_info</td>
      <td style="text-align:left">
<a href="Ip-address.md#subnetinfo">SubnetInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">zone_info</td>
      <td style="text-align:left">
<a href="Ip-address.md#zoneinfo">ZoneInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### IPQuery
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
      <td style="text-align:left">
<a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a>
</td><td style="text-align:left"></td>
<td style="text-align:left">optional</td>
        <td style="text-align:left">optional</td>

    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">ip_address</td>
      <td style="text-align:left">

string

</td><td style="text-align:left"></td>
<td style="text-align:left">optional</td>
        <td style="text-align:left">optional</td>

    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>IPQuery.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ALLOCATED</li>
          	<li>RESERVED</li>
        </ul>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">subnet_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">network_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">zone_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">region_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
  </tbody>
</table>


### IPReference
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_id |string | ||
| 2 | external_link |string | ||

### IPRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip_address |string |✅ ||
| 2 | subnet_id |string |✅ ||
| 3 | domain_id |string |✅ ||

### IPStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### IPsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[IPInfo](Ip-address.md#ipinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### PinIPDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip_address |string |✅ ||
| 2 | keys |string |✅ ||
| 3 | subnet_id |string |✅ ||
| 4 | domain_id |string |✅ ||

### ReserveIPRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip_address |string |✅ ||
| 2 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 3 | subnet_id |string |✅ ||
| 4 | domain_id |string |✅ ||

### Resource
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | type |string | ||
| 2 | id |string | ||

### UpdateIPRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip_address |string |❌ ||
| 2 | resource |[Resource](Ip-address.md#resource) |❌ ||
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | reference |[IPReference](Ip-address.md#ipreference) |❌ ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | subnet_id |string |✅ ||
| 8 | domain_id |string |✅ ||
