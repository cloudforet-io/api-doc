---
description:  
---
# Cloud service type

>  **Package : spaceone.api.inventory.v1**

## CloudServiceType

{% hint style="info" %}
**CloudServiceType Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](cloud-service-type.md#create)|   [CreateCloudServiceTypeRequest](cloud-service-type.md#createcloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |
| [**update**](cloud-service-type.md#update)|   [UpdateCloudServiceTypeRequest](cloud-service-type.md#updatecloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |
| [**delete**](cloud-service-type.md#delete)|   [CloudServiceTypeRequest](cloud-service-type.md#cloudservicetyperequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](cloud-service-type.md#get)|   [GetCloudServiceTypeRequest](cloud-service-type.md#getcloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |
| [**list**](cloud-service-type.md#list)|   [CloudServiceTypeQuery](cloud-service-type.md#cloudservicetypequery) |   [CloudServiceTypesInfo](cloud-service-type.md#cloudservicetypesinfo) |
| [**stat**](cloud-service-type.md#stat)|   [CloudServiceTypeStatQuery](cloud-service-type.md#cloudservicetypestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
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
| Field | Type |  Description |
| :--- | :--- | :--- |
| cloud_service_type_id |string | |
| name |string | |
| provider |string | |
| group |string | |
| cloud_service_type_key |string | |
| service_code |string | |
| is_primary |bool | |
| is_major |bool | |
| resource_type |string | |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |

### CloudServiceTypeQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| cloud_service_type_id |string|✘| |
| name |string|✘| |
| provider |string|✘| |
| group |string|✘| |
| cloud_service_type_key |string|✘| |
| service_code |string|✘| |
| is_primary |bool|✘| |
| is_major |bool|✘| |
| resource_type |string|✘| |
| domain_id |string|✔| |

### CloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✔| |
| domain_id |string|✔| |

### CloudServiceTypeStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### CloudServiceTypesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| provider |string|✔| |
| group |string|✔| |
| service_code |string|✘| |
| is_primary |bool|✘| |
| is_major |bool|✘| |
| resource_type |string|✘| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### GetCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### UpdateCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✔| |
| service_code |string|✘| |
| is_primary |bool|✘| |
| is_major |bool|✘| |
| resource_type |string|✘| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
