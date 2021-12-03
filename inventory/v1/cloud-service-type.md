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
| 1 | [**create**](cloud-service-type.md#create)|   [CreateCloudServiceTypeRequest](cloud-service-type.md#createcloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |  |
| 2 | [**update**](cloud-service-type.md#update)|   [UpdateCloudServiceTypeRequest](cloud-service-type.md#updatecloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |  |
| 3 | [**delete**](cloud-service-type.md#delete)|   [CloudServiceTypeRequest](cloud-service-type.md#cloudservicetyperequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [**get**](cloud-service-type.md#get)|   [GetCloudServiceTypeRequest](cloud-service-type.md#getcloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |  |
| 5 | [**list**](cloud-service-type.md#list)|   [CloudServiceTypeQuery](cloud-service-type.md#cloudservicetypequery) |   [CloudServiceTypesInfo](cloud-service-type.md#cloudservicetypesinfo) |  |
| 6 | [**stat**](cloud-service-type.md#stat)|   [CloudServiceTypeStatQuery](cloud-service-type.md#cloudservicetypestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /inventory/v1/cloud-service-types
>


| Type | Message |
| :--- | :--- |
| Request | [CreateCloudServiceTypeRequest](cloud-service-type.md#createcloudservicetyperequest) |
| Response |  [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/cloud-service-type/{cloud_service_type_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCloudServiceTypeRequest](cloud-service-type.md#updatecloudservicetyperequest) |
| Response |  [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/cloud-service-type/{cloud_service_type_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeRequest](cloud-service-type.md#cloudservicetyperequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/cloud-service-type/{cloud_service_type_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCloudServiceTypeRequest](cloud-service-type.md#getcloudservicetyperequest) |
| Response |  [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  |
 
 

 
### list
> **GET** /inventory/v1/cloud-service-types
>
> **POST** /inventory/v1/cloud-service-types/search



| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeQuery](cloud-service-type.md#cloudservicetypequery) |
| Response |  [CloudServiceTypesInfo](cloud-service-type.md#cloudservicetypesinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/cloud-service-types/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CloudServiceTypeStatQuery](cloud-service-type.md#cloudservicetypestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CloudServiceTypeInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | cloud_service_type_id |string | |
| 2 | name |string | |
| 3 | provider |string | |
| 4 | group |string | |
| 5 | cloud_service_type_key |string | |
| 6 | service_code |string | |
| 7 | is_primary |bool | |
| 8 | is_major |bool | |
| 9 | resource_type |string | |
| 10 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 11 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 12 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| 13 | domain_id |string | |
| 14 | created_at |string | |
| 15 | updated_at |string | |

### CloudServiceTypeQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | cloud_service_type_id |string|❌| |
| 3 | name |string|❌| |
| 4 | provider |string|❌| |
| 5 | group |string|❌| |
| 6 | cloud_service_type_key |string|❌| |
| 7 | service_code |string|❌| |
| 8 | is_primary |bool|❌| |
| 9 | is_major |bool|❌| |
| 10 | resource_type |string|❌| |
| 11 | domain_id |string|✅| |

### CloudServiceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | cloud_service_type_id |string|✅| |
| 2 | domain_id |string|✅| |

### CloudServiceTypeStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |

### CloudServiceTypesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCloudServiceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | name |string|✅| |
| 2 | provider |string|✅| |
| 3 | group |string|✅| |
| 4 | service_code |string|❌| |
| 5 | is_primary |bool|❌| |
| 6 | is_major |bool|❌| |
| 7 | resource_type |string|❌| |
| 8 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 9 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| 10 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 11 | domain_id |string|✅| |

### GetCloudServiceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | cloud_service_type_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### UpdateCloudServiceTypeRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :---: | :--- |
| 1 | cloud_service_type_id |string|✅| |
| 2 | service_code |string|❌| |
| 3 | is_primary |bool|❌| |
| 4 | is_major |bool|❌| |
| 5 | resource_type |string|❌| |
| 6 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 9 | domain_id |string|✅| |
