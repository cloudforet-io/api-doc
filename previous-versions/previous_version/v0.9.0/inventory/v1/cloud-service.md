---
description: null
---

# Cloud Service

> **Package : spaceone.api.inventory.v1**

## CloudService

{% hint style="info" %}
**CloudService Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](cloud-service.md#create) | [CreateServiceRequest](cloud-service.md#createservicerequest) | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| 2 | [update](cloud-service.md#update) | [UpdateCloudServiceRequest](cloud-service.md#updatecloudservicerequest) | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| 3 | [pin\_data](cloud-service.md#pin_data) | [PinCloudServiceDataRequest](cloud-service.md#pincloudservicedatarequest) | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| 4 | [delete](cloud-service.md#delete) | [CloudServiceRequest](cloud-service.md#cloudservicerequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 5 | [get](cloud-service.md#get) | [GetCloudServiceRequest](cloud-service.md#getcloudservicerequest) | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |
| 6 | [list](cloud-service.md#list) | [CloudServiceQuery](cloud-service.md#cloudservicequery) | [CloudServicesInfo](cloud-service.md#cloudservicesinfo) |  |
| 7 | [stat](cloud-service.md#stat) | [CloudServiceStatQuery](cloud-service.md#cloudservicestatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /inventory/v1/cloud-services

| Type | Message |
| :--- | :--- |
| Request | [CreateServiceRequest](cloud-service.md#createservicerequest) |
| Response | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |

### update

> **PUT** /inventory/v1/cloud-service/{cloud\_service\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdateCloudServiceRequest](cloud-service.md#updatecloudservicerequest) |
| Response | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |

### pin\_data

> **PUT** /inventory/v1/cloud-service/{cloud\_service\_id}/pin-data

| Type | Message |
| :--- | :--- |
| Request | [PinCloudServiceDataRequest](cloud-service.md#pincloudservicedatarequest) |
| Response | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |

### delete

> **DELETE** /inventory/v1/cloud-service/{cloud\_service\_id}

| Type | Message |
| :--- | :--- |
| Request | [CloudServiceRequest](cloud-service.md#cloudservicerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /inventory/v1/cloud-service/{cloud\_service\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetCloudServiceRequest](cloud-service.md#getcloudservicerequest) |
| Response | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |

### list

> **GET** /inventory/v1/cloud-services
>
> **POST** /inventory/v1/cloud-services/search

| Type | Message |
| :--- | :--- |
| Request | [CloudServiceQuery](cloud-service.md#cloudservicequery) |
| Response | [CloudServicesInfo](cloud-service.md#cloudservicesinfo) |

### stat

> **POST** /inventory/v1/cloud-services/stat

| Type | Message |
| :--- | :--- |
| Request | [CloudServiceStatQuery](cloud-service.md#cloudservicestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CloudServiceInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud\_service\_id | string |  |  |
| 2 | cloud\_service\_type | string |  |  |
| 3 | provider | string |  |  |
| 4 | cloud\_service\_group | string |  |  |
| 5 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 6 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 7 | reference | [CloudServiceReference](cloud-service.md#cloudservicereference) |  |  |
| 8 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 9 | collection\_info | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 10 | region\_info | [RegionInfo](cloud-service.md#regioninfo) |  |  |
| 11 | project\_id | string |  |  |
| 12 | domain\_id | string |  |  |
| 13 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |
| 14 | updated\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### CloudServiceQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |  | optional |
| 2 | cloud\_service\_id | string |  | optional |
| 3 | cloud\_service\_type | string |  | optional |
| 4 | provider | string |  | optional |
| 5 | cloud\_service\_group | string |  | optional |
| 6 | region\_id | string |  | optional |
| 7 | project\_id | string |  | optional |
| 8 | domain\_id | string |  | optional |

### CloudServiceReference

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | resource\_id | string |  |  |
| 2 | external\_link | string |  |  |

### CloudServiceRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud\_service\_id | string |  | required |
| 2 | domain\_id | string |  | required |

### CloudServiceStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |  | required |
| 2 | domain\_id | string |  | required |

### CloudServicesInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [CloudServiceInfo](cloud-service.md#cloudserviceinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### CreateServiceRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud\_service\_type | string |  | required |
| 2 | provider | string |  | required |
| 3 | cloud\_service\_group | string |  | optional |
| 4 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | required |
| 5 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 6 | reference | [CloudServiceReference](cloud-service.md#cloudservicereference) |  | optional |
| 7 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 8 | region\_id | string |  | optional |
| 9 | project\_id | string |  | optional |
| 10 | domain\_id | string |  | required |

### GetCloudServiceRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud\_service\_id | string |  | required |
| 2 | domain\_id | string |  | required |
| 3 | only | string |  | optional |

### PinCloudServiceDataRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud\_service\_id | string |  | required |
| 2 | keys | string |  | required |
| 3 | domain\_id | string |  | required |

### UpdateCloudServiceRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | cloud\_service\_id | string |  | required |
| 2 | data | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 3 | metadata | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 4 | reference | [CloudServiceReference](cloud-service.md#cloudservicereference) |  | optional |
| 5 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  | optional |
| 6 | region\_id | string |  | optional |
| 7 | project\_id | string |  | optional |
| 8 | domain\_id | string |  | required |
| 9 | release\_project | bool |  | optional |
| 10 | release\_region | bool |  | optional |

