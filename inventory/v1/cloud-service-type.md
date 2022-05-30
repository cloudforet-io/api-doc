---
description:  
---
# Cloud service type

>  **Package : spaceone.api.inventory.v1**

## CloudServiceType

{% hint style="info" %}
**CloudServiceType Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](cloud-service-type.md#create)|   [CreateCloudServiceTypeRequest](cloud-service-type.md#createcloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |  |
| [**update**](cloud-service-type.md#update)|   [UpdateCloudServiceTypeRequest](cloud-service-type.md#updatecloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |  |
| [**delete**](cloud-service-type.md#delete)|   [CloudServiceTypeRequest](cloud-service-type.md#cloudservicetyperequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](cloud-service-type.md#get)|   [GetCloudServiceTypeRequest](cloud-service-type.md#getcloudservicetyperequest) |   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) |  |
| [**list**](cloud-service-type.md#list)|   [CloudServiceTypeQuery](cloud-service-type.md#cloudservicetypequery) |   [CloudServiceTypesInfo](cloud-service-type.md#cloudservicetypesinfo) |  |
| [**stat**](cloud-service-type.md#stat)|   [CloudServiceTypeStatQuery](cloud-service-type.md#cloudservicetypestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](cloud-service-type.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateCloudServiceTypeRequest](cloud-service-type.md#createcloudservicetyperequest)  </div> | <div style="width:200px; text-align:center;">   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](cloud-service-type.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateCloudServiceTypeRequest](cloud-service-type.md#updatecloudservicetyperequest)  </div> | <div style="width:200px; text-align:center;">   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](cloud-service-type.md#delete) </div> | <div style="width:200px; text-align:center;">    [CloudServiceTypeRequest](cloud-service-type.md#cloudservicetyperequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](cloud-service-type.md#get) </div> | <div style="width:200px; text-align:center;">    [GetCloudServiceTypeRequest](cloud-service-type.md#getcloudservicetyperequest)  </div> | <div style="width:200px; text-align:center;">   [CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](cloud-service-type.md#list) </div> | <div style="width:200px; text-align:center;">    [CloudServiceTypeQuery](cloud-service-type.md#cloudservicetypequery)  </div> | <div style="width:200px; text-align:center;">   [CloudServiceTypesInfo](cloud-service-type.md#cloudservicetypesinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](cloud-service-type.md#stat) </div> | <div style="width:200px; text-align:center;">    [CloudServiceTypeStatQuery](cloud-service-type.md#cloudservicetypestatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| cloud_service_type_id |string|❌| |
| name |string|❌| |
| provider |string|❌| |
| group |string|❌| |
| cloud_service_type_key |string|❌| |
| service_code |string|❌| |
| is_primary |bool|❌| |
| is_major |bool|❌| |
| resource_type |string|❌| |
| domain_id |string|✅| |

### CloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✅| |
| domain_id |string|✅| |

### CloudServiceTypeStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |

### CloudServiceTypesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CloudServiceTypeInfo](cloud-service-type.md#cloudservicetypeinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✅| |
| provider |string|✅| |
| group |string|✅| |
| service_code |string|❌| |
| is_primary |bool|❌| |
| is_major |bool|❌| |
| resource_type |string|❌| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |

### GetCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### UpdateCloudServiceTypeRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type_id |string|✅| |
| service_code |string|❌| |
| is_primary |bool|❌| |
| is_major |bool|❌| |
| resource_type |string|❌| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| labels |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| domain_id |string|✅| |
