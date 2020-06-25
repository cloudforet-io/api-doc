---
description: null
---

# Ip Address

> **Package : spaceone.api.inventory.v1**

## IPAddress

{% hint style="info" %}
**IPAddress Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [allocate](ip-address.md#allocate) | [AllocateIPRequest](ip-address.md#allocateiprequest) | [IPInfo](ip-address.md#ipinfo) |  |
| 2 | [reserve](ip-address.md#reserve) | [ReserveIPRequest](ip-address.md#reserveiprequest) | [IPInfo](ip-address.md#ipinfo) |  |
| 3 | [release](ip-address.md#release) | [IPRequest](ip-address.md#iprequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 4 | [update](ip-address.md#update) | [UpdateIPRequest](ip-address.md#updateiprequest) | [IPInfo](ip-address.md#ipinfo) |  |
| 5 | [pin\_data](ip-address.md#pin_data) | [PinIPDataRequest](ip-address.md#pinipdatarequest) | [IPInfo](ip-address.md#ipinfo) |  |
| 6 | [get](ip-address.md#get) | [GetIPRequest](ip-address.md#getiprequest) | [IPInfo](ip-address.md#ipinfo) |  |
| 7 | [list](ip-address.md#list) | [IPQuery](ip-address.md#ipquery) | [IPsInfo](ip-address.md#ipsinfo) |  |
| 8 | [stat](ip-address.md#stat) | [IPStatQuery](ip-address.md#ipstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### allocate

> **POST** /inventory/v1/ip-addresses/allocate
>
> **POST** /inventory/v1/ip-address/{ip\_address}/allocate

| Type | Message |
| :--- | :--- |
| Request | [AllocateIPRequest](ip-address.md#allocateiprequest) |
| Response | [IPInfo](ip-address.md#ipinfo) |

### reserve

> **PUT** /inventory/v1/ip-address/{ip\_address}/reserve

| Type | Message |
| :--- | :--- |
| Request | [ReserveIPRequest](ip-address.md#reserveiprequest) |
| Response | [IPInfo](ip-address.md#ipinfo) |

### release

> **DELETE** /inventory/v1/ip-address/{ip\_address}/release

| Type | Message |
| :--- | :--- |
| Request | [IPRequest](ip-address.md#iprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### update

> **PUT** /inventory/v1/ip-address/{ip\_address}

| Type | Message |
| :--- | :--- |
| Request | [UpdateIPRequest](ip-address.md#updateiprequest) |
| Response | [IPInfo](ip-address.md#ipinfo) |

### pin\_data

> **PUT** /inventory/v1/ip-address/{ip\_address}/pin-data

| Type | Message |
| :--- | :--- |
| Request | [PinIPDataRequest](ip-address.md#pinipdatarequest) |
| Response | [IPInfo](ip-address.md#ipinfo) |

### get

> **GET** /inventory/v1/ip-address/{ip\_address}

| Type | Message |
| :--- | :--- |
| Request | [GetIPRequest](ip-address.md#getiprequest) |
| Response | [IPInfo](ip-address.md#ipinfo) |

### list

> **GET** /inventory/v1/ip-addresses
>
> **POST** /inventory/v1/ip-addresses/search

| Type | Message |
| :--- | :--- |
| Request | [IPQuery](ip-address.md#ipquery) |
| Response | [IPsInfo](ip-address.md#ipsinfo) |

### stat

> **POST** /inventory/v1/ip-addresses/stat

| Type | Message |
| :--- | :--- |
| Request | [IPStatQuery](ip-address.md#ipstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### AllocateIPRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip\_address | string |  | optional |
| 2 | resource | [Resource](ip-address.md#resource) |  | optional |
| 3 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 5 | reference | [IPReference](ip-address.md#ipreference) |  | optional |
| 6 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 7 | subnet\_id | string |  | required |
| 8 | domain\_id | string |  | required |

### GetIPRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip\_address | string |  | required |
| 2 | subnet\_id | string |  | required |
| 3 | domain\_id | string |  | required |
| 4 | only | string |  | optional |

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
      <td style="text-align:left">string</td>
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
      <td style="text-align:left"> <a href="ip-address.md#resource">Resource</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">data</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">metadata</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">reference</td>
      <td style="text-align:left"> <a href="ip-address.md#ipreference">IPReference</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">collection_info</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">network_info</td>
      <td style="text-align:left"> <a href="ip-address.md#networkinfo">NetworkInfo</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">subnet_info</td>
      <td style="text-align:left"> <a href="ip-address.md#subnetinfo">SubnetInfo</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">zone_info</td>
      <td style="text-align:left"> <a href="ip-address.md#zoneinfo">ZoneInfo</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left"> <a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
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
      <td style="text-align:left"> <a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a>
      </td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">ip_address</td>
      <td style="text-align:left">string</td>
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
      </td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">subnet_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">network_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">zone_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">region_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left">optional</td>
      <td style="text-align:left">optional</td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">string</td>
      <td style="text-align:left">required</td>
      <td style="text-align:left">required</td>
    </tr>
  </tbody>
</table>

### IPReference

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource\_id | string |  |  |
| 2 | external\_link | string |  |  |

### IPRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip\_address | string |  | required |
| 2 | subnet\_id | string |  | required |
| 3 | domain\_id | string |  | required |

### IPStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### IPsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [IPInfo](ip-address.md#ipinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### PinIPDataRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip\_address | string |  | required |
| 2 | keys | string |  | required |
| 3 | subnet\_id | string |  | required |
| 4 | domain\_id | string |  | required |

### ReserveIPRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip\_address | string |  | required |
| 2 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 3 | subnet\_id | string |  | required |
| 4 | domain\_id | string |  | required |

### Resource

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | type | string |  |  |
| 2 | id | string |  |  |

### UpdateIPRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | ip\_address | string |  | optional |
| 2 | resource | [Resource](ip-address.md#resource) |  | optional |
| 3 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 5 | reference | [IPReference](ip-address.md#ipreference) |  | optional |
| 6 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 7 | subnet\_id | string |  | required |
| 8 | domain\_id | string |  | required |

