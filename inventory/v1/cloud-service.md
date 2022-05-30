---
description:  
---
# Cloud service

>  **Package : spaceone.api.inventory.v1**

## CloudService

{% hint style="info" %}
**CloudService Methods:**

{%  endhint %}


| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
| [**create**](cloud-service.md#create)|   [CreateServiceRequest](cloud-service.md#createservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| [**update**](cloud-service.md#update)|   [UpdateCloudServiceRequest](cloud-service.md#updatecloudservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| [**pin_data**](cloud-service.md#pin_data)|   [PinCloudServiceDataRequest](cloud-service.md#pincloudservicedatarequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| [**delete**](cloud-service.md#delete)|   [CloudServiceRequest](cloud-service.md#cloudservicerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| [**get**](cloud-service.md#get)|   [GetCloudServiceRequest](cloud-service.md#getcloudservicerequest) |   [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| [**list**](cloud-service.md#list)|   [CloudServiceQuery](cloud-service.md#cloudservicequery) |   [CloudServicesInfo](cloud-service.md#cloudservicesinfo) |  |
| [**stat**](cloud-service.md#stat)|   [CloudServiceStatQuery](cloud-service.md#cloudservicestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |TEST

| Method | Request | Response | Description &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
| :-----: | :--------: | :--------: | :-------------------- |
|<div style="width:70px; text-align:center;">  [**create**](cloud-service.md#create) </div> | <div style="width:200px; text-align:center;">    [CreateServiceRequest](cloud-service.md#createservicerequest)  </div> | <div style="width:200px; text-align:center;">   [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**update**](cloud-service.md#update) </div> | <div style="width:200px; text-align:center;">    [UpdateCloudServiceRequest](cloud-service.md#updatecloudservicerequest)  </div> | <div style="width:200px; text-align:center;">   [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**pin_data**](cloud-service.md#pin_data) </div> | <div style="width:200px; text-align:center;">    [PinCloudServiceDataRequest](cloud-service.md#pincloudservicedatarequest)  </div> | <div style="width:200px; text-align:center;">   [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**delete**](cloud-service.md#delete) </div> | <div style="width:200px; text-align:center;">    [CloudServiceRequest](cloud-service.md#cloudservicerequest)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**get**](cloud-service.md#get) </div> | <div style="width:200px; text-align:center;">    [GetCloudServiceRequest](cloud-service.md#getcloudservicerequest)  </div> | <div style="width:200px; text-align:center;">   [CloudServiceInfo](cloud-service.md#cloudserviceinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**list**](cloud-service.md#list) </div> | <div style="width:200px; text-align:center;">    [CloudServiceQuery](cloud-service.md#cloudservicequery)  </div> | <div style="width:200px; text-align:center;">   [CloudServicesInfo](cloud-service.md#cloudservicesinfo)  </div> | <div style="width:400px;">  </div> |
|<div style="width:70px; text-align:center;">  [**stat**](cloud-service.md#stat) </div> | <div style="width:200px; text-align:center;">    [CloudServiceStatQuery](cloud-service.md#cloudservicestatquery)  </div> | <div style="width:200px; text-align:center;">  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) </div> | <div style="width:400px;">  </div> | 
 

 
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
| Field | Type |  Description |
| :--- | :--- | :--- |
| cloud_service_id |string | |
| name |string | |
| state |string | |
| account |string | |
| instance_type |string | |
| instance_size |float | |
| cloud_service_type |string | |
| cloud_service_group |string | |
| provider |string | |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| reference |[CloudServiceReference](cloud-service.md#cloudservicereference) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| region_code |string | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |
| updated_at |string | |
| deleted_at |string | |
| launched_at |string | |

### CloudServiceQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|❌| |
| cloud_service_id |string|❌| |
| name |string|❌| |
| state |string|❌| |
| account |string|❌| |
| instance_type |string|❌| |
| cloud_service_type |string|❌| |
| cloud_service_group |string|❌| |
| provider |string|❌| |
| region_code |string|❌| |
| resource_group_id |string|❌| |
| project_id |string|❌| |
| project_group_id |string|❌| |
| domain_id |string|✅| |

### CloudServiceReference
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_id |string | |
| external_link |string | |

### CloudServiceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_id |string|✅| |
| domain_id |string|✅| |

### CloudServiceStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✅| |
| domain_id |string|✅| |
| resource_group_id |string|❌| |

### CloudServicesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of CloudServiceInfo](cloud-service.md#cloudserviceinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### CreateServiceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_type |string|✅| |
| provider |string|✅| |
| cloud_service_group |string|✅| |
| name |string|❌| |
| account |string|❌| |
| instance_type |string|❌| |
| instance_size |float|❌| |
| launched_at |string|❌| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✅| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| reference |[CloudServiceReference](cloud-service.md#cloudservicereference)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| region_code |string|❌| |
| project_id |string|❌| |
| domain_id |string|✅| |

### GetCloudServiceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_id |string|✅| |
| domain_id |string|✅| |
| only |list of string|❌| |

### PinCloudServiceDataRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_id |string|✅| |
| keys |list of string|✅| |
| domain_id |string|✅| |

### UpdateCloudServiceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| cloud_service_id |string|✅| |
| name |string|❌| |
| account |string|❌| |
| instance_type |string|❌| |
| instance_size |float|❌| |
| launched_at |string|❌| |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| reference |[CloudServiceReference](cloud-service.md#cloudservicereference)|❌| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|❌| |
| region_code |string|❌| |
| project_id |string|❌| |
| domain_id |string|✅| |
| release_project |bool|❌| |
| release_region |bool|❌| |
