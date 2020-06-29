---
description:  
---
# Subnet

>  **Package : spaceone.api.inventory.v1**

## Subnet

{% hint style="info" %}
**Subnet Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Subnet.md#create)| [CreateSubnetRequest](Subnet.md#createsubnetrequest) | [SubnetInfo](Subnet.md#subnetinfo) |  |
| 2 | [update](Subnet.md#update)| [UpdateSubnetRequest](Subnet.md#updatesubnetrequest) | [SubnetInfo](Subnet.md#subnetinfo) |  |
| 3 | [pin_data](Subnet.md#pin_data)| [PinSubnetDataRequest](Subnet.md#pinsubnetdatarequest) | [SubnetInfo](Subnet.md#subnetinfo) |  |
| 4 | [delete](Subnet.md#delete)| [SubnetRequest](Subnet.md#subnetrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [get](Subnet.md#get)| [GetSubnetRequest](Subnet.md#getsubnetrequest) | [SubnetInfo](Subnet.md#subnetinfo) |  |
| 6 | [list](Subnet.md#list)| [SubnetQuery](Subnet.md#subnetquery) | [SubnetsInfo](Subnet.md#subnetsinfo) |  |
| 7 | [stat](Subnet.md#stat)| [SubnetStatQuery](Subnet.md#subnetstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/subnets
>



| Type | Message |
| :--- | :--- |
| Request | [CreateSubnetRequest](Subnet.md#createsubnetrequest) |
| Response |  [SubnetInfo](Subnet.md#subnetinfo)  |



### update
> **PUT** /inventory/v1/subnet/{subnet_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateSubnetRequest](Subnet.md#updatesubnetrequest) |
| Response |  [SubnetInfo](Subnet.md#subnetinfo)  |



### pin_data
> **PUT** /inventory/v1/subnet/{subnet_id}/pin-data
>



| Type | Message |
| :--- | :--- |
| Request | [PinSubnetDataRequest](Subnet.md#pinsubnetdatarequest) |
| Response |  [SubnetInfo](Subnet.md#subnetinfo)  |



### delete
> **DELETE** /inventory/v1/subnet/{subnet_id}
>



| Type | Message |
| :--- | :--- |
| Request | [SubnetRequest](Subnet.md#subnetrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/subnet/{subnet_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetSubnetRequest](Subnet.md#getsubnetrequest) |
| Response |  [SubnetInfo](Subnet.md#subnetinfo)  |



### list
> **GET** /inventory/v1/subnets
>
> **POST** /inventory/v1/subnets/search




| Type | Message |
| :--- | :--- |
| Request | [SubnetQuery](Subnet.md#subnetquery) |
| Response |  [SubnetsInfo](Subnet.md#subnetsinfo)  |



### stat
> **POST** /inventory/v1/subnets/stat
>



| Type | Message |
| :--- | :--- |
| Request | [SubnetStatQuery](Subnet.md#subnetstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreateSubnetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cidr |string |✅ ||
| 2 | name |string |❌ ||
| 3 | ip_ranges |[IPRange](Subnet.md#iprange) |❌ ||
| 4 | gateway |string |❌ ||
| 5 | vlan |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |❌ ||
| 6 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 8 | reference |[SubnetReference](Subnet.md#subnetreference) |❌ ||
| 9 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 10 | network_id |string |✅ ||
| 11 | network_type_id |string |✅ ||
| 12 | network_policy_id |string |❌ ||
| 13 | project_id |string |✅ ||
| 14 | domain_id |string |✅ ||

### GetSubnetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | subnet_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### IPRange
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | start |string | ||
| 2 | end |string | ||

### PinSubnetDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | subnet_id |string |✅ ||
| 2 | keys |string |✅ ||
| 3 | domain_id |string |✅ ||

### SubnetInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | subnet_id |string | ||
| 2 | name |string | ||
| 3 | cidr |string | ||
| 4 | ip_ranges |[IPRange](Subnet.md#iprange) | ||
| 5 | gateway |string | ||
| 6 | vlan |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
| 7 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 8 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 9 | reference |[SubnetReference](Subnet.md#subnetreference) | ||
| 10 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 11 | collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 12 | network_info |[NetworkInfo](Subnet.md#networkinfo) | ||
| 13 | network_type_info |[NetworkTypeInfo](Subnet.md#networktypeinfo) | ||
| 14 | network_policy_info |[NetworkPolicyInfo](Subnet.md#networkpolicyinfo) | ||
| 15 | region_info |[RegionInfo](Subnet.md#regioninfo) | ||
| 16 | zone_info |[ZoneInfo](Subnet.md#zoneinfo) | ||
| 17 | project_id |string | ||
| 18 | domain_id |string | ||
| 19 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### SubnetQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | subnet_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | cidr |string |❌ ||
| 5 | gateway |string |❌ ||
| 6 | vlan |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |❌ ||
| 7 | network_id |string |❌ ||
| 8 | network_type_id |string |❌ ||
| 9 | network_policy_id |string |❌ ||
| 10 | zone_id |string |❌ ||
| 11 | region_id |string |❌ ||
| 12 | project_id |string |❌ ||
| 13 | domain_id |string |✅ ||

### SubnetReference
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_id |string | ||
| 2 | external_link |string | ||

### SubnetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | subnet_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### SubnetStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### SubnetsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[SubnetInfo](Subnet.md#subnetinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### UpdateSubnetRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | subnet_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | ip_ranges |[IPRange](Subnet.md#iprange) |❌ ||
| 4 | gateway |string |❌ ||
| 5 | vlan |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |❌ ||
| 6 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 8 | reference |[SubnetReference](Subnet.md#subnetreference) |❌ ||
| 9 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 10 | network_type_id |string |❌ ||
| 11 | network_policy_id |string |❌ ||
| 12 | project_id |string |❌ ||
| 13 | domain_id |string |✅ ||
| 14 | release_project |bool |❌ ||
