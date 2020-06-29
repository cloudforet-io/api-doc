---
description:  
---
# Network type

>  **Package : spaceone.api.inventory.v1**

## NetworkType

{% hint style="info" %}
**NetworkType Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Network-type.md#create)| [CreateNetworkTypeRequest](Network-type.md#createnetworktyperequest) | [NetworkTypeInfo](Network-type.md#networktypeinfo) |  |
| 2 | [update](Network-type.md#update)| [UpdateNetworkTypeRequest](Network-type.md#updatenetworktyperequest) | [NetworkTypeInfo](Network-type.md#networktypeinfo) |  |
| 3 | [delete](Network-type.md#delete)| [NetworkTypeRequest](Network-type.md#networktyperequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [get](Network-type.md#get)| [GetNetworkTypeRequest](Network-type.md#getnetworktyperequest) | [NetworkTypeInfo](Network-type.md#networktypeinfo) |  |
| 5 | [list](Network-type.md#list)| [NetworkTypeQuery](Network-type.md#networktypequery) | [NetworkTypesInfo](Network-type.md#networktypesinfo) |  |
| 6 | [stat](Network-type.md#stat)| [NetworkTypeStatQuery](Network-type.md#networktypestatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/network-types
>



| Type | Message |
| :--- | :--- |
| Request | [CreateNetworkTypeRequest](Network-type.md#createnetworktyperequest) |
| Response |  [NetworkTypeInfo](Network-type.md#networktypeinfo)  |



### update
> **PUT** /inventory/v1/network-type/{network_type_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateNetworkTypeRequest](Network-type.md#updatenetworktyperequest) |
| Response |  [NetworkTypeInfo](Network-type.md#networktypeinfo)  |



### delete
> **DELETE** /inventory/v1/network-type/{network_type_id}
>



| Type | Message |
| :--- | :--- |
| Request | [NetworkTypeRequest](Network-type.md#networktyperequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/network-type/{network_type_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetNetworkTypeRequest](Network-type.md#getnetworktyperequest) |
| Response |  [NetworkTypeInfo](Network-type.md#networktypeinfo)  |



### list
> **GET** /inventory/v1/network-types
>
> **POST** /inventory/v1/network-types/search




| Type | Message |
| :--- | :--- |
| Request | [NetworkTypeQuery](Network-type.md#networktypequery) |
| Response |  [NetworkTypesInfo](Network-type.md#networktypesinfo)  |



### stat
> **POST** /inventory/v1/network-types/stat
>



| Type | Message |
| :--- | :--- |
| Request | [NetworkTypeStatQuery](Network-type.md#networktypestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateNetworkTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||

### GetNetworkTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_type_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### NetworkTypeInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_type_id |string | ||
| 2 | name |string | ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | domain_id |string | ||
| 5 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### NetworkTypeQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | network_type_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | domain_id |string |✅ ||

### NetworkTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_type_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### NetworkTypeStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### NetworkTypesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[NetworkTypeInfo](Network-type.md#networktypeinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateNetworkTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | network_type_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | domain_id |string |✅ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
