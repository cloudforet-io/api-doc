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
| 1 | [create](Cloud-service.md#create)| [CreateServiceRequest](Cloud-service.md#createservicerequest) | [CloudServiceInfo](Cloud-service.md#cloudserviceinfo) |  |
| 2 | [update](Cloud-service.md#update)| [UpdateCloudServiceRequest](Cloud-service.md#updatecloudservicerequest) | [CloudServiceInfo](Cloud-service.md#cloudserviceinfo) |  |
| 3 | [pin_data](Cloud-service.md#pin_data)| [PinCloudServiceDataRequest](Cloud-service.md#pincloudservicedatarequest) | [CloudServiceInfo](Cloud-service.md#cloudserviceinfo) |  |
| 4 | [delete](Cloud-service.md#delete)| [CloudServiceRequest](Cloud-service.md#cloudservicerequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [get](Cloud-service.md#get)| [GetCloudServiceRequest](Cloud-service.md#getcloudservicerequest) | [CloudServiceInfo](Cloud-service.md#cloudserviceinfo) |  |
| 6 | [list](Cloud-service.md#list)| [CloudServiceQuery](Cloud-service.md#cloudservicequery) | [CloudServicesInfo](Cloud-service.md#cloudservicesinfo) |  |
| 7 | [stat](Cloud-service.md#stat)| [CloudServiceStatQuery](Cloud-service.md#cloudservicestatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

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
| 5 | state |string | ||
| 6 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 7 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 8 | reference |[CloudServiceReference](Cloud-service.md#cloudservicereference) | ||
| 9 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 10 | collection_info |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 11 | region_info |[RegionInfo](Cloud-service.md#regioninfo) | ||
| 12 | project_id |string | ||
| 13 | domain_id |string | ||
| 14 | created_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 15 | updated_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||
| 16 | deleted_at |[google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) | ||

### CloudServiceQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | cloud_service_id |string |❌ ||
| 3 | cloud_service_type |string |❌ ||
| 4 | provider |string |❌ ||
| 5 | cloud_service_group |string |❌ ||
| 6 | region_id |string |❌ ||
| 7 | project_id |string |❌ ||
| 8 | domain_id |string |❌ ||

### CloudServiceReference
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource_id |string | ||
| 2 | external_link |string | ||

### CloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### CloudServiceStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### CloudServicesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[CloudServiceInfo](Cloud-service.md#cloudserviceinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### CreateServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_type |string |✅ ||
| 2 | provider |string |✅ ||
| 3 | cloud_service_group |string |❌ ||
| 4 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |✅ ||
| 5 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | reference |[CloudServiceReference](Cloud-service.md#cloudservicereference) |❌ ||
| 7 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 8 | region_id |string |❌ ||
| 9 | project_id |string |❌ ||
| 10 | domain_id |string |✅ ||

### GetCloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### PinCloudServiceDataRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string |✅ ||
| 2 | keys |string |✅ ||
| 3 | domain_id |string |✅ ||

### UpdateCloudServiceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud_service_id |string |✅ ||
| 2 | data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 3 | metadata |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | reference |[CloudServiceReference](Cloud-service.md#cloudservicereference) |❌ ||
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | region_id |string |❌ ||
| 7 | project_id |string |❌ ||
| 8 | domain_id |string |✅ ||
| 9 | release_project |bool |❌ ||
| 10 | release_region |bool |❌ ||
