---
description:  
---
# Network

>  **Package : spaceone.api.inventory.v1**

## Network

{% hint style="info" %}
**Network Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Network.md#create)| [CreateNetworkRequest](Network.md#createnetworkrequest) | [NetworkInfo](Network.md#networkinfo) |  |
| 2 | [update](Network.md#update)| [UpdateNetworkRequest](Network.md#updatenetworkrequest) | [NetworkInfo](Network.md#networkinfo) |  |
| 3 | [pin_data](Network.md#pin_data)| [PinNetworkDataRequest](Network.md#pinnetworkdatarequest) | [NetworkInfo](Network.md#networkinfo) |  |
| 4 | [delete](Network.md#delete)| [NetworkRequest](Network.md#networkrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [get](Network.md#get)| [GetNetworkRequest](Network.md#getnetworkrequest) | [NetworkInfo](Network.md#networkinfo) |  |
| 6 | [list](Network.md#list)| [NetworkQuery](Network.md#networkquery) | [NetworksInfo](Network.md#networksinfo) |  |
| 7 | [stat](Network.md#stat)| [NetworkStatQuery](Network.md#networkstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/networks
>



| Type | Message |
| :--- | :--- |
| Request | [CreateNetworkRequest](Network.md#createnetworkrequest) |
| Response |  [NetworkInfo](Network.md#networkinfo)  |



### update
> **PUT** /inventory/v1/network/{network_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateNetworkRequest](Network.md#updatenetworkrequest) |
| Response |  [NetworkInfo](Network.md#networkinfo)  |



### pin_data
> **PUT** /inventory/v1/network/{network_id}/pin-data
>



| Type | Message |
| :--- | :--- |
| Request | [PinNetworkDataRequest](Network.md#pinnetworkdatarequest) |
| Response |  [NetworkInfo](Network.md#networkinfo)  |



### delete
> **DELETE** /inventory/v1/network/{network_id}
>



| Type | Message |
| :--- | :--- |
| Request | [NetworkRequest](Network.md#networkrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/network/{network_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetNetworkRequest](Network.md#getnetworkrequest) |
| Response |  [NetworkInfo](Network.md#networkinfo)  |



### list
> **GET** /inventory/v1/networks
>
> **POST** /inventory/v1/networks/search




| Type | Message |
| :--- | :--- |
| Request | [NetworkQuery](Network.md#networkquery) |
| Response |  [NetworksInfo](Network.md#networksinfo)  |



### stat
> **POST** /inventory/v1/networks/stat
>



| Type | Message |
| :--- | :--- |
| Request | [NetworkStatQuery](Network.md#networkstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateNetworkRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | cidr |string |✅ ||
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | reference |[NetworkReference](Network.md#networkreference) |❌ ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | zone_id |string |✅ ||
| 8 | domain_id |string |✅ ||

### GetNetworkRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### NetworkInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_id |string | ||
| 2 | name |string | ||
| 3 | cidr |string | ||
| 4 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 6 | reference |[NetworkReference](Network.md#networkreference) | ||
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 8 | collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 9 | region_info |[RegionInfo](Network.md#regioninfo) | ||
| 10 | zone_info |[ZoneInfo](Network.md#zoneinfo) | ||
| 11 | domain_id |string | ||
| 12 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### NetworkQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | network_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | cidr |string |❌ ||
| 5 | zone_id |string |❌ ||
| 6 | region_id |string |❌ ||
| 7 | domain_id |string |✅ ||

### NetworkReference
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_id |string | ||
| 2 | external_link |string | ||

### NetworkRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### NetworkStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### NetworksInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[NetworkInfo](Network.md#networkinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### PinNetworkDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_id |string |✅ ||
| 2 | keys |string |✅ ||
| 3 | domain_id |string |✅ ||

### UpdateNetworkRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | reference |[NetworkReference](Network.md#networkreference) |❌ ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | domain_id |string |✅ ||
