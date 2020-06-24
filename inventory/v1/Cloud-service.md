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
| 1 | [create](Cloud-service.md#create)| [CreateServiceRequest](Cloud-service.md#createservicerequest)| [CloudServiceInfo](Cloud-service.md#cloudserviceinfo) |  |
| 2 | [update](Cloud-service.md#update)| [UpdateCloudServiceRequest](Cloud-service.md#updatecloudservicerequest)| [CloudServiceInfo](Cloud-service.md#cloudserviceinfo) |  |
| 3 | [pin_data](Cloud-service.md#pin_data)| [PinCloudServiceDataRequest](Cloud-service.md#pincloudservicedatarequest)| [CloudServiceInfo](Cloud-service.md#cloudserviceinfo) |  |
| 4 | [delete](Cloud-service.md#delete)| [CloudServiceRequest](Cloud-service.md#cloudservicerequest)|[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [get](Cloud-service.md#get)| [GetCloudServiceRequest](Cloud-service.md#getcloudservicerequest)| [CloudServiceInfo](Cloud-service.md#cloudserviceinfo) |  |
| 6 | [list](Cloud-service.md#list)| [CloudServiceQuery](Cloud-service.md#cloudservicequery)| [CloudServicesInfo](Cloud-service.md#cloudservicesinfo) |  |
| 7 | [stat](Cloud-service.md#stat)| [CloudServiceStatQuery](Cloud-service.md#cloudservicestatquery)|[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### create
> **POST** /inventory/v1/cloud-services
>



| Type | Message |
| :--- | :--- |
| Request | [CreateServiceRequest](Cloud-service.md#createservicerequest) |
| Response |  [CloudServiceInfo](Cloud-service.md#cloudserviceinfo)  |



### update
> **PUT** /inventory/v1/cloud-service/{cloud_service_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateCloudServiceRequest](Cloud-service.md#updatecloudservicerequest) |
| Response |  [CloudServiceInfo](Cloud-service.md#cloudserviceinfo)  |



### pin_data
> **PUT** /inventory/v1/cloud-service/{cloud_service_id}/pin-data
>



| Type | Message |
| :--- | :--- |
| Request | [PinCloudServiceDataRequest](Cloud-service.md#pincloudservicedatarequest) |
| Response |  [CloudServiceInfo](Cloud-service.md#cloudserviceinfo)  |



### delete
> **DELETE** /inventory/v1/cloud-service/{cloud_service_id}
>



| Type | Message |
| :--- | :--- |
| Request | [CloudServiceRequest](Cloud-service.md#cloudservicerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### get
> **GET** /inventory/v1/cloud-service/{cloud_service_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetCloudServiceRequest](Cloud-service.md#getcloudservicerequest) |
| Response |  [CloudServiceInfo](Cloud-service.md#cloudserviceinfo)  |



### list
> **GET** /inventory/v1/cloud-services
>
> **POST** /inventory/v1/cloud-services/search




| Type | Message |
| :--- | :--- |
| Request | [CloudServiceQuery](Cloud-service.md#cloudservicequery) |
| Response |  [CloudServicesInfo](Cloud-service.md#cloudservicesinfo)  |



### stat
> **POST** /inventory/v1/cloud-services/stat
>



| Type | Message |
| :--- | :--- |
| Request | [CloudServiceStatQuery](Cloud-service.md#cloudservicestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CloudServiceInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string | ||
| 2 | cloud_service_type |string | ||
| 3 | provider |string | ||
| 4 | cloud_service_group |string | ||
| 5 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 6 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 7 | reference |[CloudServiceReference](Cloud-service.md#cloudservicereference) | ||
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 9 | collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 10 | region_info |[RegionInfo](Cloud-service.md#regioninfo) | ||
| 11 | project_id |string | ||
| 12 | domain_id |string | ||
| 13 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 14 | updated_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### CloudServiceQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | |optional|
| 2 | cloud_service_id |string | |optional|
| 3 | cloud_service_type |string | |optional|
| 4 | provider |string | |optional|
| 5 | cloud_service_group |string | |optional|
| 6 | region_id |string | |optional|
| 7 | project_id |string | |optional|
| 8 | domain_id |string | |optional|

### CloudServiceReference
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_id |string | ||
| 2 | external_link |string | ||

### CloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string | |required|
| 2 | domain_id |string | |required|

### CloudServiceStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) | |required|
| 2 | domain_id |string | |required|

### CloudServicesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[CloudServiceInfo](Cloud-service.md#cloudserviceinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### CreateServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_type |string | |required|
| 2 | provider |string | |required|
| 3 | cloud_service_group |string | |optional|
| 4 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |required|
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 6 | reference |[CloudServiceReference](Cloud-service.md#cloudservicereference) | |optional|
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 8 | region_id |string | |optional|
| 9 | project_id |string | |optional|
| 10 | domain_id |string | |required|

### GetCloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string | |required|
| 2 | domain_id |string | |required|
| 3 | only |string | |optional|

### PinCloudServiceDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string | |required|
| 2 | keys |string | |required|
| 3 | domain_id |string | |required|

### UpdateCloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string | |required|
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 3 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 4 | reference |[CloudServiceReference](Cloud-service.md#cloudservicereference) | |optional|
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 6 | region_id |string | |optional|
| 7 | project_id |string | |optional|
| 8 | domain_id |string | |required|
| 9 | release_project |bool | |optional|
| 10 | release_region |bool | |optional|
