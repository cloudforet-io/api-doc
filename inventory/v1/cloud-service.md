---
description:  
---
# Cloud service

>  **Package : spaceone.api.inventory.v1**

## CloudService

{% hint style="info" %}
**CloudService Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [**create**](cloud-service.md#create)|   [CreateServiceRequest](cloud-service.md#createservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| 2 | [**update**](cloud-service.md#update)|   [UpdateCloudServiceRequest](cloud-service.md#updatecloudservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| 3 | [**pin_data**](cloud-service.md#pin_data)|   [PinCloudServiceDataRequest](cloud-service.md#pincloudservicedatarequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| 4 | [**delete**](cloud-service.md#delete)|   [CloudServiceRequest](cloud-service.md#cloudservicerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [**get**](cloud-service.md#get)|   [GetCloudServiceRequest](cloud-service.md#getcloudservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| 6 | [**list**](cloud-service.md#list)|   [CloudServiceQuery](cloud-service.md#cloudservicequery) |   [CloudServicesInfo](cloud-service.md#cloudservicesinfo) |  |
| 7 | [**stat**](cloud-service.md#stat)|   [CloudServiceStatQuery](cloud-service.md#cloudservicestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  | 
 

 
### create
> **POST** /inventory/v1/cloud-services
>


| Type | Message |
| :--- | :--- |
| Request | [CreateServiceRequest](cloud-service.md#createservicerequest) |
| Response |  [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  |
 
 

 
### update
> **PUT** /inventory/v1/cloud-service/{cloud_service_id}
>


| Type | Message |
| :--- | :--- |
| Request | [UpdateCloudServiceRequest](cloud-service.md#updatecloudservicerequest) |
| Response |  [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  |
 
 

 
### pin_data
> **PUT** /inventory/v1/cloud-service/{cloud_service_id}/pin-data
>


| Type | Message |
| :--- | :--- |
| Request | [PinCloudServiceDataRequest](cloud-service.md#pincloudservicedatarequest) |
| Response |  [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  |
 
 

 
### delete
> **DELETE** /inventory/v1/cloud-service/{cloud_service_id}
>


| Type | Message |
| :--- | :--- |
| Request | [CloudServiceRequest](cloud-service.md#cloudservicerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
 
 

 
### get
> **GET** /inventory/v1/cloud-service/{cloud_service_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetCloudServiceRequest](cloud-service.md#getcloudservicerequest) |
| Response |  [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  |
 
 

 
### list
> **GET** /inventory/v1/cloud-services
>
> **POST** /inventory/v1/cloud-services/search



| Type | Message |
| :--- | :--- |
| Request | [CloudServiceQuery](cloud-service.md#cloudservicequery) |
| Response |  [CloudServicesInfo](cloud-service.md#cloudservicesinfo)  |
 
 

 
### stat
> **POST** /inventory/v1/cloud-services/stat
>


| Type | Message |
| :--- | :--- |
| Request | [CloudServiceStatQuery](cloud-service.md#cloudservicestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CloudServiceInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string | |
| 2 | cloud_service_type |string | |
| 3 | provider |string | |
| 4 | cloud_service_group |string | |
| 5 | state |string | |
| 6 | name |string | |
| 7 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 8 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 9 | reference |[CloudServiceReference](cloud-service.md#cloudservicereference) | |
| 10 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 11 | collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| 12 | project_id |string | |
| 13 | domain_id |string | |
| 14 | region_code |string | |
| 15 | created_at |string | |
| 16 | updated_at |string | |
| 17 | deleted_at |string | |

### CloudServiceQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| 2 | cloud_service_id |string|❌| |
| 3 | cloud_service_type |string|❌| |
| 4 | cloud_service_group |string|❌| |
| 5 | provider |string|❌| |
| 6 | state |string|❌| |
| 7 | region_code |string|❌| |
| 8 | name |string|❌| |
| 9 | resource_group_id |string|❌| |
| 10 | project_id |string|❌| |
| 11 | domain_id |string|✅| |

### CloudServiceReference
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | resource_id |string | |
| 2 | external_link |string | |

### CloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string|✅| |
| 2 | domain_id |string|✅| |

### CloudServiceStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| 2 | domain_id |string|✅| |
| 3 | resource_group_id |string|❌| |

### CloudServicesInfo
| No | Field | Type |  Description |
| :--- | :--- | :--- | :--- |
| 1 | results |[list of CloudServiceInfo](cloud-service.md#cloudserviceinfo) | |
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_type |string|✅| |
| 2 | provider |string|✅| |
| 3 | cloud_service_group |string|✅| |
| 4 | name |string|❌| |
| 5 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| 6 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | reference |[CloudServiceReference](cloud-service.md#cloudservicereference)|❌| |
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 9 | project_id |string|❌| |
| 10 | domain_id |string|✅| |
| 11 | region_code |string|❌| |

### GetCloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string|✅| |
| 2 | domain_id |string|✅| |
| 3 | only |list of string|❌| |

### PinCloudServiceDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string|✅| |
| 2 | keys |list of string|✅| |
| 3 | domain_id |string|✅| |

### UpdateCloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string|✅| |
| 2 | name |string|❌| |
| 3 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 4 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 5 | reference |[CloudServiceReference](cloud-service.md#cloudservicereference)|❌| |
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| 7 | region_code |string|❌| |
| 8 | project_id |string|❌| |
| 9 | domain_id |string|✅| |
| 10 | release_project |bool|❌| |
| 11 | release_region |bool|❌| |
