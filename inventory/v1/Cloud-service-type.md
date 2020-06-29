---
description:  
---
# Cloud service type

>  **Package : spaceone.api.inventory.v1**

## CloudServiceType

{% hint style="info" %}
**CloudServiceType Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](Cloud-service-type.md#create)| [CreateServiceTypeRequest](Cloud-service-type.md#createservicetyperequest) | [CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo) |  |
| 2 | [update](Cloud-service-type.md#update)| [UpdateCloudServiceTypeRequest](Cloud-service-type.md#updatecloudservicetyperequest) | [CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo) |  |
| 3 | [pin_data](Cloud-service-type.md#pin_data)| [PinCloudServiceTypeDataRequest](Cloud-service-type.md#pincloudservicetypedatarequest) | [CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo) |  |
| 4 | [delete](Cloud-service-type.md#delete)| [CloudServiceTypeRequest](Cloud-service-type.md#cloudservicetyperequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [get](Cloud-service-type.md#get)| [GetCloudServiceTypeRequest](Cloud-service-type.md#getcloudservicetyperequest) | [CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo) |  |
| 6 | [list](Cloud-service-type.md#list)| [CloudServiceTypeQuery](Cloud-service-type.md#cloudservicetypequery) | [CloudServiceTypesInfo](Cloud-service-type.md#cloudservicetypesinfo) |  |
| 7 | [stat](Cloud-service-type.md#stat)| [CloudServiceTypeStatQuery](Cloud-service-type.md#cloudservicetypestatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/cloud-service-types
>



| Type | Message |
| :--- | :--- |
| Request | [CreateServiceTypeRequest](Cloud-service-type.md#createservicetyperequest) |
| Response |  [CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo)  |



### update
> **PUT** /inventory/v1/cloud-service-type/{cloud_service_type_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateCloudServiceTypeRequest](Cloud-service-type.md#updatecloudservicetyperequest) |
| Response |  [CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo)  |



### pin_data
> **PUT** /inventory/v1/cloud-service-type/{cloud_service_type_id}/pin-data
>



| Type | Message |
| :--- | :--- |
| Request | [PinCloudServiceTypeDataRequest](Cloud-service-type.md#pincloudservicetypedatarequest) |
| Response |  [CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo)  |



### delete
> **DELETE** /inventory/v1/cloud-service-type/{cloud_service_type_id}
>



| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeRequest](Cloud-service-type.md#cloudservicetyperequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/cloud-service-type/{cloud_service_type_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetCloudServiceTypeRequest](Cloud-service-type.md#getcloudservicetyperequest) |
| Response |  [CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo)  |



### list
> **GET** /inventory/v1/cloud-service-types
>
> **POST** /inventory/v1/cloud-service-types/search




| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeQuery](Cloud-service-type.md#cloudservicetypequery) |
| Response |  [CloudServiceTypesInfo](Cloud-service-type.md#cloudservicetypesinfo)  |



### stat
> **POST** /inventory/v1/cloud-service-types/stat
>



| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeStatQuery](Cloud-service-type.md#cloudservicetypestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CloudServiceTypeInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_type_id |string | ||
| 2 | name |string | ||
| 3 | provider |string | ||
| 4 | group |string | ||
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 7 | labels |string | ||
| 8 | collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 9 | cloud_service_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
| 10 | domain_id |string | ||
| 11 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 12 | updated_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### CloudServiceTypeQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | cloud_service_type_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | provider |string |❌ ||
| 5 | group |string |❌ ||
| 6 | include_cloud_service_count |bool |❌ ||
| 7 | domain_id |string |❌ ||

### CloudServiceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_type_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### CloudServiceTypeStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### CloudServiceTypesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[CloudServiceTypeInfo](Cloud-service-type.md#cloudservicetypeinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### CreateServiceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |❌ ||
| 2 | provider |string |❌ ||
| 3 | group |string |❌ ||
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) |❌ ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | domain_id |string |✅ ||

### GetCloudServiceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_type_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### PinCloudServiceTypeDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_type_id |string |✅ ||
| 2 | keys |string |✅ ||
| 3 | domain_id |string |✅ ||

### UpdateCloudServiceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_type_id |string |✅ ||
| 2 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 3 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) |❌ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | domain_id |string |✅ ||
